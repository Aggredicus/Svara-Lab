#!/usr/bin/env python3
"""Synthetic persona browser QA for Svara Lab. Requires playwright + Chromium.
No real people are involved. Run: python qa/2026-10-26/run_cohort.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,time,shutil,sys
HERE=Path(__file__).resolve().parent
HTML=(HERE.parents[1]/"index.html").read_text()
ROLES=("novice","sanskrit_editor","music_producer")
SIZES=((320,700),(360,780),(390,844),(1440,900))
records=[];start=time.monotonic()
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--autoplay-policy=no-user-gesture-required"],**({"executable_path":shutil.which("chromium")} if shutil.which("chromium") else {}))
 for role in ROLES:
  for width,height in SIZES:
   errors=[]
   page=browser.new_page(viewport={"width":width,"height":height},has_touch=True,is_mobile=width<500)
   page.on("pageerror",lambda e:errors.append(str(e)))
   page.set_content(HTML)
   tests=[]
   def chk(task,observed,expected=True):
    tests.append({"task":task,"observed":observed,"expected":expected,"pass":observed==expected})
   chk("No horizontal overflow",page.evaluate("document.documentElement.scrollWidth<=innerWidth"))
   page.locator("[data-view=help]").click()
   chk("Help opens",page.locator("#helpPanel").is_visible())
   chk("Selected tab has semantic state",page.locator("[data-view=help]").get_attribute("aria-pressed"),"true")
   page.locator("[data-view=compose]").click()
   page.locator("#compDisplay").fill("राम")
   page.locator('[data-special="backspace"]').click()
   chk("Backspace after paste",page.locator("#compDisplay").inner_text(),"रा")
   page.locator("#compDisplay").fill("कृष्ण")
   chk("Krishna script is preserved",page.evaluate("SvaraTest.getComposer().text"),"कृष्ण")
   if role=="novice":
    page.locator("#compDisplay").fill("रामः")
    page.locator('[data-special="backspace"]').click()
    chk("Visarga removes independently",page.locator("#compDisplay").inner_text(),"राम")
   if role=="sanskrit_editor":
    chk("Krishna vowel nuclei",page.evaluate("SvaraTest.parseSanskritText('कृष्ण').segments.filter(x=>x.type==='v').length"),2)
    chk("Phoneme PCM bounded",page.evaluate("()=>{const r=SvaraTest.renderTextPCM('राम',{sr:16000});return r.nonzero>100&&r.data.every(x=>Number.isFinite(x)&&Math.abs(x)<=1)}"))
   if role=="music_producer":
    page.locator("[data-view=perform]").click()
    gate=page.locator("#gatePad");first=gate.bounding_box()
    for n in (13,14):gate.dispatch_event("pointerdown",{"pointerId":n,"pointerType":"touch","button":0,"clientX":50,"clientY":200})
    page.wait_for_timeout(160)
    after=gate.bounding_box()
    chk("Sustain gate geometry stable",all(abs(first[k]-after[k])<.3 for k in ("x","y","width","height")))
    chk("Gate starts",page.evaluate("SvaraTest.getActiveVoices().some(x=>x.id==='finger-gate')"))
    page.evaluate("SvaraTest.setExpression(5,40)")
    gate.dispatch_event("pointerup",{"pointerId":13,"pointerType":"touch","button":0,"clientX":50,"clientY":200})
    chk("One finger remains sustained",page.evaluate("SvaraTest.getActiveVoices().some(x=>x.id==='finger-gate')"))
    gate.dispatch_event("pointerup",{"pointerId":14,"pointerType":"touch","button":0,"clientX":50,"clientY":200})
    chk("All fingers released",page.evaluate("!SvaraTest.getActiveVoices().some(x=>x.id==='finger-gate')"))
   chk("JavaScript exceptions",len(errors),0)
   records.append({"id":f"SIM-{len(records)+1:02d}","persona":role,"viewport":[width,height],"source_type":"observed_automation_on_synthetic_persona","checks":tests})
   page.close()
 browser.close()
result={"participants_human":0,"sessions_simulated":len(records),"passed":sum(x["pass"] for r in records for x in r["checks"]),"total":sum(len(r["checks"]) for r in records),"elapsed_seconds":round(time.monotonic()-start,3),"sessions":records,"limitations":["Not human feedback","Real phone and audio quality not verified"]}
(HERE/"latest_runner_result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(f'Synthetic n={result["sessions_simulated"]}: {result["passed"]}/{result["total"]} browser checks passed')
sys.exit(result["total"]!=result["passed"])
