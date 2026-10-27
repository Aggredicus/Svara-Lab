#!/usr/bin/env python3
"""v1.4 synthetic touch input audit: 3-persona pilot or 12-context expansion.
Run: pip install playwright && playwright install chromium
     python qa/2026-10-26/consonant_matrix_test.py --n 12
Observations are automated, NEVER human participant feedback.
"""
import argparse, json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ap=argparse.ArgumentParser(); ap.add_argument("--n",type=int,choices=[3,12],default=3)
args=ap.parse_args()
html=Path(__file__).resolve().parents[2].joinpath("index.html").read_text()
views=[320,345,360,375,390,412,430,670,768,1280,1440,1920][:args.n]
report=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,args=["--no-sandbox"])
 for j,w in enumerate(views):
  page=b.new_page(viewport={"width":w,"height":844},has_touch=True,is_mobile=w<700)
  errors=[];page.on("pageerror",lambda e:errors.append(str(e)))
  page.set_content(html);page.locator("[data-view=compose]").click()
  tests=[]
  def check(label,ok): tests.append({"check":label,"pass":bool(ok)})
  check("34 unique consonants",page.evaluate("new Set(SvaraTest.C_GROUPS.flatMap(x=>x.parts.filter(Boolean).map(p=>p[0]))).size") ==34)
  check("phoneme self-test",page.evaluate("SvaraTest.runLetterAudit().passed"))
  groups=page.evaluate("SvaraTest.C_GROUPS")
  directions=[(0,0),(-45,0),(0,-45),(45,0),(0,45)]
  for k,g in enumerate(groups):
   for d,part in enumerate(g["parts"]):
    if part is None: continue
    page.evaluate('SvaraTest.composerEvent({kind:"clear"})')
    result=page.evaluate("""({k,d,dx,dy})=>{
      const el=document.querySelectorAll('#consonantFlick .flickkey')[k];
      const r=el.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,id=99+k*8+d;
      for(const [event,a,b] of [['pointerdown',x,y],['pointermove',x+dx,y+dy],['pointerup',x+dx,y+dy]])
       el.dispatchEvent(new PointerEvent(event,{bubbles:true,pointerType:'touch',pointerId:id,button:0,clientX:a,clientY:b}));
      return SvaraTest.getComposer().text}""",{"k":k,"d":d,"dx":directions[d][0],"dy":directions[d][1]})
    check(f'{g["name"]} direction {d}: {part[0]}',result==part[0])
  check("no horizontal overflow",page.evaluate("document.documentElement.scrollWidth<=innerWidth"))
  check("zero JS errors",not errors)
  report.append({"session_id":f"SIM-{j+1:02d}","viewport":[w,844],"observed_browser":True,"human_participant":False,"results":tests})
  page.close()
 b.close()
passed=sum(sum(x["pass"] for x in s["results"]) for s in report)
total=sum(len(s["results"]) for s in report)
print(json.dumps({"n":args.n,"passed":passed,"total":total,"human_participants":0},indent=2))
sys.exit(passed!=total)
