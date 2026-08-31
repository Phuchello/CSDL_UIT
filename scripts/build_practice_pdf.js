const path = require('path');
const fs = require('fs');
const url = require('url');
const { chromium } = require('playwright');

async function main() {
  const repoRoot = path.resolve(__dirname, '..');
  const htmlPath = path.join(repoRoot, 'practice', 'index.html');
  const pdfPath = path.join(repoRoot, 'dist', 'IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf');
  fs.mkdirSync(path.dirname(pdfPath), { recursive: true });
  const browser = await chromium.launch({ headless: true, executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1240, height: 1754 } });
  const consoleErrors = [], pageErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(err.message || String(err)));
  await page.goto(url.pathToFileURL(htmlPath).href, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  const audit = await page.evaluate(() => {
    const text = document.body.innerText;
    const viewportRight = document.documentElement.clientWidth;
    const selectors = '.page, .cover-page, .info-page, .toc-page, table, pre, svg, img';
    const wide = [...document.querySelectorAll(selectors)].filter(el => el.scrollWidth > el.clientWidth + 2 || el.getBoundingClientRect().right > viewportRight + 2).map(el => ({ tag: el.tagName, className: String(el.className || '') }));
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
    return {
      title: document.title, bodyFont: getComputedStyle(document.body).fontFamily,
      bodyFontResolved: document.fonts.check('10pt Georgia') ? 'Georgia' : 'fallback',
      pages: document.querySelectorAll('.page, .cover-page, .info-page, .toc-page').length,
      duplicateIds: ids.filter((id, i, all) => all.indexOf(id) !== i),
      horizontalOverflow: wide,
      tofu: (text.match(/[□�]/g) || []).length,
      hasVietnamese: /THỰC HÀNH CƠ SỞ DỮ LIỆU|BIÊN SOẠN: VÕ TRỌNG PHÚC/.test(text),
      required: ['LAB 01', 'LAB 02', 'LAB 03', 'LAB 04', 'RANK', 'WITH TIES', 'Double NOT EXISTS', 'Msg 8120', 'A–H'].filter(x => !text.includes(x)),
    };
  });
  // Audit only the production manifest. Historical C1 proof chapters 06–08
  // remain in the source tree for provenance but are intentionally excluded
  // from the C2 production build.
  const chapters = [
    '00_cover_toc.html', '01_environment_workflow.html', '02_ddl_dml_foundations.html',
    '03_basic_queries_and_joins.html', '04_aggregation_and_subqueries.html',
    '05_integrity_and_triggers.html', '09_lab01_ddl.html', '10_lab02_dml.html',
    '11_lab03_advanced.html', '12_lab04_analytics.html', '13_debugging_expanded.html',
    '14_appendices_exam.html'
  ];
  const banned = ['🤔','🎯','🏃','✅','🔥','⭐','💡','🚨','☢','⚠','tuyệt kỹ','kỹ năng sống còn','thần chú','trọng điểm thi','exam mastery','mental model','fast pattern'];
  const sourceViolations = [];
  for (const ch of chapters) {
    const content = fs.readFileSync(path.join(repoRoot, 'practice', 'chapters', ch), 'utf8').toLowerCase();
    for (const phrase of banned) if (content.includes(phrase.toLowerCase())) sourceViolations.push(ch + ': ' + phrase);
  }
  audit.chapters = chapters; audit.sourceViolations = sourceViolations;
  await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: false, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
  const result = { htmlPath, pdfPath, pdfBytes: fs.statSync(pdfPath).size, consoleErrors, pageErrors, audit };
  console.log(JSON.stringify(result, null, 2));
  if (consoleErrors.length || pageErrors.length || audit.duplicateIds.length || audit.horizontalOverflow.length || audit.tofu || !audit.hasVietnamese || audit.bodyFontResolved === 'fallback' || audit.required.length || sourceViolations.length) process.exitCode = 2;
}
main().catch(err => { console.error(err.stack || String(err)); process.exit(1); });
