const { chromium } = require('playwright-core'); const fs = require('fs'), path = require('path');
(async () => {
  const [specPath, outDir, frs] = process.argv.slice(2); const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  const fps = spec.fps[0] / spec.fps[1];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'overlay.html'));
  await page.evaluate(s => window.init(s), spec); await page.waitForFunction(() => window.READY === true);
  for (const f of frs.split(',')) { await page.evaluate(t => window.render(t), +f / fps); await page.screenshot({ path: path.join(outDir, String(f).padStart(5, '0') + '.png'), omitBackground: true }); }
  await b.close();
})();
