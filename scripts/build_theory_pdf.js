const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

async function main() {
  const repoRoot = path.resolve(__dirname, '..');
  const htmlPath = path.join(repoRoot, 'book', 'index.html');
  const pdfPath = path.join(repoRoot, 'dist', 'IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf');
  fs.mkdirSync(path.dirname(pdfPath), { recursive: true });

  const executablePath = process.env.CHROME_PATH || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const browser = await chromium.launch({
    headless: true,
    executablePath,
    args: ['--allow-file-access-from-files', '--disable-gpu'],
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(String(err)));

  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(async () => {
    await document.fonts.ready;
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  });

  const audit = await page.evaluate(() => {
    const bodyText = document.body.innerText;
    const viewportRight = document.documentElement.clientWidth;
    const wide = [...document.querySelectorAll('.page, table, pre, svg, img')]
      .filter(el => el.scrollWidth > el.clientWidth + 2 || el.getBoundingClientRect().right > viewportRight + 2)
      .map(el => ({ tag: el.tagName, id: el.id || '', className: typeof el.className === 'string' ? el.className : '' }));
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
    return {
      title: document.title,
      bodyFont: getComputedStyle(document.body).fontFamily,
      bodyFontResolved: document.fonts.check('10.5pt Georgia') ? 'Georgia' : (document.fonts.check('10.5pt Cambria') ? 'Cambria' : 'fallback'),
      sourceSections: [...document.querySelectorAll('section[id], #ch02')].map(el => el.id),
      practicalHidden: (() => { const el = document.querySelector('#ch07'); return !!el && getComputedStyle(el).display === 'none'; })(),
      duplicateIds: ids.filter((id, i, all) => all.indexOf(id) !== i),
      horizontalOverflow: wide,
      tofu: (bodyText.match(/[�□]/g) || []).length,
      coverText: bodyText.slice(0, 300),
      hasVietnamese: /CƠ SỞ DỮ LIỆU|BIÊN SOẠN: VÕ TRỌNG PHÚC/.test(bodyText),
      symbols: Object.fromEntries(['π', 'σ', 'ρ', '⋈', '÷', '∪', '∩', '→', 'X⁺'].map(s => [s, bodyText.includes(s)])),
      exerciseCount: (bodyText.match(/Câu\s+\d+:/g) || []).length,
    };
  });

  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: false,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });
  await browser.close();

  const result = { htmlPath, pdfPath, pdfBytes: fs.statSync(pdfPath).size, consoleErrors, pageErrors, audit };
  console.log(JSON.stringify(result, null, 2));
  if (
    consoleErrors.length || pageErrors.length || audit.duplicateIds.length || audit.horizontalOverflow.length ||
    audit.tofu || !audit.hasVietnamese || Object.values(audit.symbols).some(v => !v) ||
    !/Georgia|Cambria/.test(audit.bodyFont) || audit.bodyFontResolved === 'fallback' ||
    !audit.practicalHidden || audit.exerciseCount < 30
  ) process.exitCode = 2;
}

main().catch(err => { console.error(err.stack || String(err)); process.exit(1); });
