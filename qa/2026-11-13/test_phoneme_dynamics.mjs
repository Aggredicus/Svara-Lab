#!/usr/bin/env node
// Differential phoneme + timing tests for the single-file Svara Lab.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname,resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';

const root=resolve(dirname(fileURLToPath(import.meta.url)),'../..');
const html=readFileSync(resolve(root,'index.html'),'utf8');
const scripts=[...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
assert.ok(scripts.length>=4);
for(const src of scripts)new vm.Script(src);
const code=scripts[0], cut=code.lastIndexOf('window.SvaraTest=');
assert.ok(cut>=0);
const api=new Function('document','window',code.slice(0,cut)+
 'return {VOWELS,C_GROUPS,makeConsonantPCM,renderTextPCM,articulationGesture,vowelOnsetFromConsonant,segmentFeatures,PLACE_ACOUSTICS};')({},{});
const sr=24000,params={pitch:190,brightness:64,breath:12,depth:0,vibrato:0,tract:0,openness:60,attack:8,release:60};
const meanDiff=(a,b)=>a.reduce((sum,x,i)=>sum+Math.abs(x-(b[i]||0)),0)/Math.max(a.length,b.length);
const energy=a=>Math.sqrt(a.reduce((sum,x)=>sum+x*x,0)/a.length);
const names=api.C_GROUPS.slice(0,5).map(g=>g.parts.map(p=>p[1]));
const places=['velar','palatal','retroflex','dental','labial'];
assert.equal(names.flat().length,25);
for(let i=0;i<5;i++){
 assert.equal(api.segmentFeatures(names[i][0]).place,places[i]);
 for(let j=0;j<5;j++){
  const sym=names[i][j],gesture=api.articulationGesture(sym),clip=api.makeConsonantPCM(sym,sr,params,1);
  assert.ok(gesture.total>0 && Math.abs(clip.length/sr-gesture.total)<1/sr,'acoustic/visual length '+sym);
  assert.ok(clip.length>=sr*.08 && clip.every(Number.isFinite),'finite samples '+sym);
  assert.ok(clip.every(x=>Math.abs(x)<=1),'no clipping '+sym);
  assert.ok(energy(clip)>.003,'audible consonant '+sym);
 }
 const simple=api.articulationGesture(names[i][0]),asp=api.articulationGesture(names[i][1]);
 const voiced=api.articulationGesture(names[i][2]),breathy=api.articulationGesture(names[i][3]);
 assert.ok(asp.aspiration>simple.aspiration*3,'unvoiced VOT contrast '+places[i]);
 assert.ok(breathy.breathy && breathy.aspiration>voiced.aspiration*3,'murmured voicing '+places[i]);
 assert.ok(api.articulationGesture(names[i][4]).nasal,'homorganic nasal '+places[i]);
}
const k=api.makeConsonantPCM('k',sr,params,1);
for(const other of ['c','ṭ','t','p']){
 const clip=api.makeConsonantPCM(other,sr,params,1);
 assert.ok(meanDiff(k,clip)>.01,'place-coded burst distinguishes k from '+other);
}
const kk=api.makeConsonantPCM('k',sr,params,1);
const gg=api.makeConsonantPCM('g',sr,params,1);
const closure=Math.floor(sr*.04);
assert.ok(energy(gg.slice(0,closure))>energy(kk.slice(0,closure))*3,'voiced stop closure');
const nasal1=api.makeConsonantPCM('ṅ',sr,params,1);
const nasal2=api.makeConsonantPCM('m',sr,params,1);
assert.ok(meanDiff(nasal1,nasal2)>.01,'nasal places have different resonances');
const form=[700,1300,2700];
assert.notDeepEqual(api.vowelOnsetFromConsonant('t',form),api.vowelOnsetFromConsonant('ṭ',form));
const result=api.renderTextPCM('क ख ग घ ङ',{sr,params});
assert.equal(result.gestures.length,result.segments.length);
assert.equal(result.clipLengths.length,result.timeline.length);
assert.ok(result.data.every(Number.isFinite));
for(let i=1;i<result.timeline.length;i++)assert.ok(result.timeline[i]>result.timeline[i-1]);
assert.ok(result.timeline.at(-1)<result.duration);
for(const id of ['svaraHeadBone','svaraTongue','svaraTongueFibers','svaraVelum','svaraVocalFolds','svaraOralFlow','svaraNasalFlow','svaraContrast','svaraGestureReadout'])assert.ok(html.includes(id),'UI '+id);
for(const stage of ['CLOSURE','RELEASE BURST','ASPIRATION','BREATHY VOICING','NASAL AIRFLOW'])assert.ok(html.includes(stage),'stage '+stage);
assert.ok(!/<script[^>]+\bsrc=/.test(html),'offline script execution');
console.log('PASS — 25 Sanskrit consonants, five places, acoustic contrast, gesture timing, finite PCM and SVG controls');
