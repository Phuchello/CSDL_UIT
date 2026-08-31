const path = require('path');
const fs = require('fs');
const url = require('url');
const { chromium } = require('playwright');

async function main() {
  const repoRoot = path.resolve(__dirname, '..');
  const htmlPath = path.join(repoRoot, 'practice', 'index.html');
  const pdfPath = path.join(repoRoot, 'dist', 'proofs', 'IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf');

  fs.mkdirSync(path.dirname(pdfPath), { recursive: true });

  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  });
  const page = await browser.newPage({ viewport: { width: 1240, height: 1754 } });

  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(err.message || String(err)));

  await page.goto(url.pathToFileURL(htmlPath).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  const audit = await page.evaluate(() => {
    const bodyText = document.body.innerText;
    const viewportRight = document.documentElement.clientWidth;
    const wide = [...document.querySelectorAll('.page, .cover-page, .info-page, .toc-page, table, pre, svg, img')]
      .filter(el => el.scrollWidth > el.clientWidth + 2 || el.getBoundingClientRect().right > viewportRight + 2)
      .map(el => ({
        tag: el.tagName,
        id: el.id || '',
        className: typeof el.className === 'string' ? el.className : '',
      }));
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
    return {
      title: document.title,
      bodyFont: getComputedStyle(document.body).fontFamily,
      bodyFontResolved: document.fonts.check('10pt Georgia') ? 'Georgia' : (document.fonts.check('10pt Cambria') ? 'Cambria' : 'fallback'),
      duplicateIds: ids.filter((id, i, all) => all.indexOf(id) !== i),
      horizontalOverflow: wide,
      tofu: (bodyText.match(/[□]/g) || []).length,
      hasVietnamese: /THỰC HÀNH CƠ SỞ DỮ LIỆU|BIÊN SOẠN: VÕ TRỌNG PHÚC/.test(bodyText),
    };
  });

  const practiceChapters = [
    '00_cover_toc.html',
    '01_environment_workflow.html',
    '02_ddl_dml_foundations.html',
    '03_basic_queries_and_joins.html',
    '04_aggregation_and_subqueries.html',
    '05_integrity_and_triggers.html',
    '06_debugging_system.html',
    '07_lab_progression.html',
    '08_exam_workflow_references.html',
  ];
  const forbiddenEmojis = ['🤔', '🎯', '🏃', '✅', '🔥', '⭐', '💡', '🚨', '☢', '⚠'];
  const forbiddenHypePhrases = [
    'tuyệt kỹ',
    'kỹ năng sống còn',
    'thần chú',
    'trọng điểm thi',
    'giảng viên thường khuyến khích',
    'exam mastery',
    'mental model',
    'fast pattern',
  ];
  const forbiddenColors = [
    '#dbeafe', '#2563eb', '#dcfce7', '#059669', '#fef9c3', '#d97706',
    '#fee2e2', '#991b1b', '#f3e8ff', '#6b21a8', '#fdf4ff', '#a855f7'
  ];
  const legacyViolations = [];
  for (const ch of practiceChapters) {
    const filePath = path.join(repoRoot, 'practice', 'chapters', ch);
    if (!fs.existsSync(filePath)) {
      legacyViolations.push(`Missing chapter: ${ch}`);
      continue;
    }
    const content = fs.readFileSync(filePath, 'utf-8');
    for (const emoji of forbiddenEmojis) {
      if (content.includes(emoji)) {
        legacyViolations.push(`Forbidden emoji "${emoji}" in ${ch}`);
      }
    }
    for (const phrase of forbiddenHypePhrases) {
      if (content.toLowerCase().includes(phrase.toLowerCase())) {
        legacyViolations.push(`Forbidden hype phrase "${phrase}" in ${ch}`);
      }
    }
    for (const color of forbiddenColors) {
      if (content.toLowerCase().includes(color.toLowerCase())) {
        legacyViolations.push(`Forbidden color "${color}" in ${ch}`);
      }
    }
  }
  audit.legacyViolations = legacyViolations;

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
    audit.tofu || !audit.hasVietnamese ||
    !/Georgia|Cambria/.test(audit.bodyFont) || audit.bodyFontResolved === 'fallback' ||
    legacyViolations.length
  ) process.exitCode = 2;
}

main().catch(err => { console.error(err.stack || String(err)); process.exit(1); });
