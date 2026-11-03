// Render overlay2 frames: node render2.js spec.json outDir [workers] [frameList]
// Writes NNNNN.png (front layer) and, for frames where text sits behind the speaker, b_NNNNN.png (behind layer).
const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path');
(async () => {
  const [specPath, outDir, W = '3', LIST] = process.argv.slice(2);
  const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const fps = spec.fps[0] / spec.fps[1];
  const frames = LIST ? LIST.split(',').map(Number) : [...Array(spec.frames).keys()];
  const behind = (spec.events || []).filter(e => e.layer === 'behind').map(e => [e.t0 - 0.05, e.t1 + 0.05]);
  const isBehind = t => behind.some(([a, b]) => t >= a && t <= b);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--disable-gpu', '--font-render-hinting=none', '--allow-file-access-from-files'] });
  const workers = +W, t0 = Date.now(); let done = 0;
  await Promise.all([...Array(workers)].map(async (_, k) => {
    const [VW, VH] = spec.size || [1080, 1920];
    const page = await browser.newPage({ viewport: { width: VW, height: VH }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.resolve(__dirname, 'overlay2.html'));
    await page.evaluate(s => window.init(s), spec);
    await page.waitForFunction(() => window.READY === true);
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('Emulation.setDefaultBackgroundColorOverride', { color: { r: 0, g: 0, b: 0, a: 0 } });
    const shot = async p => { const { data } = await cdp.send('Page.captureScreenshot', { format: 'png', optimizeForSpeed: true }); fs.writeFileSync(p + '.tmp', Buffer.from(data, 'base64')); fs.renameSync(p + '.tmp', p); };
    for (let i = k; i < frames.length; i += workers) {
      const f = frames[i], t = f / fps, nm = String(f).padStart(5, '0') + '.png';
      if (process.env.STREAM) {   // stay at most AHEAD frames in front of the compositor, which deletes frames it has used
        const AHEAD = 900; const pf = path.join(outDir, '_pos');
        for (;;) { let pos = 0; try { pos = +fs.readFileSync(pf, 'utf8') || 0; } catch (e) {} if (f <= pos + AHEAD) break; await new Promise(r => setTimeout(r, 250)); }
      }
      await page.evaluate(t => window.render(t), t);
      if (isBehind(t)) {
        await page.evaluate(() => window.setLayer('behind')); await shot(path.join(outDir, 'b_' + nm));
        await page.evaluate(() => window.setLayer('front'));
      }
      await shot(path.join(outDir, nm));
      if (++done % 300 === 0) console.log(`${done}/${frames.length} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
  }));
  await browser.close();
  fs.writeFileSync(path.join(outDir, '_done'), 'ok');
  console.log('rendered', frames.length, 'frames in', ((Date.now() - t0) / 1000).toFixed(0), 's');
})();
