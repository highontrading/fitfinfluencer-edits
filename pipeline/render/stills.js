// node stills.js spec.json outDir t1 t2 ...  -> overlay PNG at given times
const { chromium } = require('playwright-core'); const fs = require('fs'), path = require('path');
(async () => {
  const [specPath, outDir, ...ts] = process.argv.slice(2); const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'overlay.html'));
  await page.evaluate(s => window.init(s), spec); await page.waitForFunction(() => window.READY === true);
  for (const t of ts) { await page.evaluate(t => window.render(t), +t); await page.screenshot({ path: path.join(outDir, `s_${(+t).toFixed(2)}.png`), omitBackground: true }); }
  await b.close();
})();
