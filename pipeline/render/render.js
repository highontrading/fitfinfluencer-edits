// Render overlay frames (transparent PNG) for a spec: node render.js spec.json outDir [workers] [from] [to]
const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path');
(async () => {
  const [specPath, outDir, W = '3', F0, F1] = process.argv.slice(2);
  const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const fps = spec.fps[0] / spec.fps[1];
  const total = spec.frames;
  const from = F0 ? +F0 : 0, to = F1 ? +F1 : total;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--disable-gpu', '--font-render-hinting=none'] });
  const workers = +W;
  const t0 = Date.now();
  let done = 0;
  await Promise.all([...Array(workers)].map(async (_, k) => {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.resolve(__dirname, 'overlay.html'));
    await page.evaluate(s => window.init(s), spec);
    await page.waitForFunction(() => window.READY === true);
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('Emulation.setDefaultBackgroundColorOverride', { color: { r: 0, g: 0, b: 0, a: 0 } });
    for (let f = from + k; f < to; f += workers) {
      await page.evaluate(t => window.render(t), f / fps);
      const { data } = await cdp.send('Page.captureScreenshot', { format: 'png', optimizeForSpeed: true });
      fs.writeFileSync(path.join(outDir, String(f).padStart(5, '0') + '.png'), Buffer.from(data, 'base64'));
      if (++done % 300 === 0) console.log(`${done}/${to - from} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
  }));
  await browser.close();
  console.log('rendered', to - from, 'frames in', ((Date.now() - t0) / 1000).toFixed(0), 's');
})();
