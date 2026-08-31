const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

async function main() {
  const here = __dirname;
  const htmlPath = path.join(here, 'proof', 'IT004_CSDL_UIT_v1.1_Theory_DesignProof.html');
  const pdfPath = path.resolve(here, '..', '..', 'dist', 'proofs', 'IT004_CSDL_UIT_v1.1_Theory_DesignProof.pdf');
  fs.mkdirSync(path.dirname(pdfPath), { recursive: true });
  const executablePath = process.env.CHROME_PATH || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const browser = await chromium.launch({ headless: true, executablePath, args: ['--allow-file-access-from-files', '--disable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(String(err)));
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(async () => { await document.fonts.ready; await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); });
  const audit = await page.evaluate(() => ({
    title: document.title,
    bodyFont: getComputedStyle(document.body).fontFamily,
    bodyFontResolved: document.fonts.check('10.5pt Georgia') ? 'Georgia' : (document.fonts.check('10.5pt Cambria') ? 'Cambria' : 'fallback'),
    pages: document.querySelectorAll('.page').length,
    duplicateIds: [...document.querySelectorAll('[id]')].map(x => x.id).filter((id, i, all) => all.indexOf(id) !== i),
    overflow: [...document.querySelectorAll('.page, table, pre, svg')].filter(el => el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1).map(el => ({ tag: el.tagName, className: el.className.baseVal || el.className })),
    tofu: (document.body.innerText.match(/[�□]/g) || []).length,
    vietnamese: /CƠ SỞ DỮ LIỆU|BIÊN SOẠN: VÕ TRỌNG PHÚC/.test(document.body.innerText),
    symbols: ['π', 'σ', '⋈', '÷', '→', 'X⁺'].every(s => document.body.innerText.includes(s)),
  }));
  await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: false, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
  console.log(JSON.stringify({ htmlPath, pdfPath, pdfBytes: fs.statSync(pdfPath).size, consoleErrors, pageErrors, audit }, null, 2));
  if (consoleErrors.length || pageErrors.length || audit.duplicateIds.length || audit.overflow.length || audit.tofu || !audit.vietnamese || !audit.symbols || !/Georgia|Cambria/.test(audit.bodyFont) || audit.bodyFontResolved === 'fallback') process.exitCode = 2;
}

main().catch(err => { console.error(err.stack || String(err)); process.exit(1); });
