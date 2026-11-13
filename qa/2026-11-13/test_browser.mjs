#!/usr/bin/env node
// Headless Chromium smoke test. Test dependency is CI-only, not loaded by the app.
import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { resolve,dirname } from 'node:path';

const root=resolve(dirname(fileURLToPath(import.meta.url)),'../..');
const errors=[];
const browser=await chromium.launch({headless:true,channel:'chrome',args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
try{
 const page=await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+resolve(root,'index.html'),{waitUntil:'load'});
 await page.locator('#svaraVargas button').first().waitFor();
 assert.equal(await page.locator('#svaraVargas button').count(),25);
 assert.equal(await page.locator('[data-view="all"]').getAttribute('aria-label'),'Voice articulation studio');
 const dimensions=await page.evaluate(()=>({screenWidth:window.innerWidth,scrollWidth:document.documentElement.scrollWidth}));
 assert.ok(dimensions.scrollWidth<=dimensions.screenWidth+3,'No horizontal overflow on mobile: '+JSON.stringify(dimensions));
 const tongue=page.locator('#svaraTongue'),folds=page.locator('#svaraVocalFolds');
 const velar=await tongue.getAttribute('d');
 await page.evaluate(()=>{window.SvaraArticulation.stop();window.SvaraArticulation.select(window.SvaraArticulation.entries.find(e=>e.name==='ṭ'))});
 assert.notEqual(await tongue.getAttribute('d'),velar,'Retroflex tongue differs from velar');
 await page.evaluate(()=>{window.SvaraArticulation.stop();window.SvaraArticulation.select(window.SvaraArticulation.entries.find(e=>e.name==='m'))});
 assert.match(await page.locator('#svaraVelum').getAttribute('transform'),/rotate\(19 /,'Nasal lowers the velum');
 await page.evaluate(()=>{window.SvaraArticulation.stop();window.SvaraArticulation.select(window.SvaraArticulation.entries.find(e=>e.name==='p'))});
 assert.match(await page.locator('#svaraUpperLip').getAttribute('transform'),/6\.0/,'Labial closes lips');
 assert.ok(await folds.count());
 // Play a complete CV unit; the phase label and airflow follow the AudioContext clock.
 const started=await page.evaluate(()=>window.SvaraArticulation.speak('ख','letter'));
 assert.equal(started,true,'Web Audio started');
 await page.waitForFunction(()=>document.getElementById('svaraFigure').classList.contains('speaking'),{timeout:5000});
 await page.waitForTimeout(85);
 const phase=await page.locator('#svaraGestureReadout').textContent();
 assert.ok(['CLOSURE','RELEASE BURST','ASPIRATION','VOWEL ONSET','VOWEL'].includes(phase),'Recognized playback phase: '+phase);
 await page.locator('#svaraContrast').click();
 await page.waitForTimeout(100);
 assert.ok(errors.length===0,'Browser page exceptions: '+errors.join('; '));
 const desktop=await browser.newPage({viewport:{width:1440,height:900}});
 desktop.on('pageerror',e=>errors.push('desktop: '+e.message));
 await desktop.goto('file://'+resolve(root,'index.html'),{waitUntil:'load'});
 assert.equal(await desktop.locator('#svaraVargas button').count(),25);
 const fig=await desktop.locator('#svaraFigure svg').boundingBox();
 assert.ok(fig.width>300 && fig.height>150,'Desktop head illustration visible: '+JSON.stringify(fig));
 const wide=await desktop.evaluate(()=>({viewport:innerWidth,body:document.documentElement.scrollWidth}));
 assert.ok(wide.body<=wide.viewport+3,'Desktop horizontal overflow');
 await desktop.locator('#svaraType').click();
 await desktop.locator('#consonantFlick').waitFor();
 assert.ok(errors.length===0,'Page errors: '+errors.join('; '));
 console.log('PASS — mobile and desktop Chrome; 25 sounds, anatomical gestures, velum, lips, audio and comparison; widths '+dimensions.scrollWidth+'/'+wide.body);
}finally{await browser.close()}
