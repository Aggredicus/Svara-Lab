#!/usr/bin/env node
// Offline checks for the single-file Sanskrit phonetic renderer.
// Run: node qa/2026-11-13/test_articulation.mjs
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import vm from 'node:vm';

const here=dirname(fileURLToPath(import.meta.url));
const html=readFileSync(resolve(here,'../../index.html'),'utf8');
const scripts=[...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
assert.ok(scripts.length>=4,'Main studio + support scripts are present');
for(const src of scripts)new vm.Script(src); // parse every script, without requiring a browser
assert.match(html,/svaraVargas/); // The studio UI is a JSON-encoded template within the final script.
assert.match(html,/svara-artic-script/);
assert.match(html,/SvaraCockpit\.activate\('all'\)/);
assert.ok(!/<script[^>]+\bsrc=/.test(html),'No fetched script dependency');

const main=scripts[0],entry=main.lastIndexOf('window.SvaraTest=');
assert.ok(entry>0,'Main renderer test entrypoint exists');
const api=new Function('document','window',main.slice(0,entry)+
 'return {VOWELS,C_GROUPS,parseSanskritText,renderTextPCM,makeConsonantPCM,segmentFeatures};')({},{});
const names=t=>api.parseSanskritText(t).segments.map(x=>x.id||x.name||x.type);
assert.deepEqual(names('राम'),names('rāma'),'Devanagari and IAST share a pronunciation');
assert.deepEqual(names('राम'),['r','aa','m','a']);
assert.deepEqual(names('कृष्ण'),['k','r','ṣ','ṇ','a'],'Virama and conjuncts suppress schwa');
assert.deepEqual(names('śānti'),['ś','aa','n','t','i']);

const base=api.C_GROUPS.slice(0,5).flatMap(g=>g.parts.map(p=>p[1]));
assert.equal(base.length,25);
for(const symbol of base){
 const traits=api.segmentFeatures(symbol);
 assert.ok(traits.place && traits.place!=='other','Phonetic place: '+symbol);
 const pcm=api.renderTextPCM(api.C_GROUPS.flatMap(g=>g.parts).find(p=>p[1]===symbol)[0],{sr:12000});
 assert.ok(pcm.nonzero>100,'Audible consonant '+symbol);
 assert.equal(pcm.timeline.length,pcm.segments.length,'Timeline aligned '+symbol);
 assert.ok(pcm.data.every(Number.isFinite),'Finite audio '+symbol);
 assert.ok(pcm.data.every(x=>Math.abs(x)<=1),'Bounded audio '+symbol);
}
for(const [plain,asp] of [['k','kh'],['c','ch'],['ṭ','ṭh'],['t','th'],['p','ph'],['g','gh'],['d','dh']]){
 const a=api.makeConsonantPCM(plain,12000,{pitch:196},1);
 const b=api.makeConsonantPCM(asp,12000,{pitch:196},1);
 assert.ok(b.length>a.length,'Aspirated stop release length '+asp);
}
assert.equal(api.renderTextPCM('अंक',{sr:12000}).segments.find(x=>x.original==='ṃ')?.name,'ṅ');
assert.equal(api.renderTextPCM('अंप',{sr:12000}).segments.find(x=>x.original==='ṃ')?.name,'m');
assert.equal(api.VOWELS.length,14);
for(const v of api.VOWELS){
 const pcm=api.renderTextPCM(v.dev,{sr:12000});
 assert.ok(pcm.nonzero>100 && Number.isFinite(pcm.duration),'Synthesis '+v.dev);
}
console.log('PASS — syntax, 25 varga consonants, 14 vowels, script parity, conjuncts, nasal place and stop-aspiration timing');
