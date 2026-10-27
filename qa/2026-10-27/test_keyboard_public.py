#!/usr/bin/env python3
"""Public Svara Lab keyboard regression. Requires Playwright (test-only dependency).
Run: python qa/2026-10-27/test_keyboard_public.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json, shutil, sys

APP=Path(__file__).resolve().parents[2]/"index.html"
SIZES=[(320,568),(390,844),(568,320),(768,1024),(1440,900)]
checks=[]
with sync_playwright() as p:
    exe=shutil.which("chromium")
    browser=p.chromium.launch(headless=True,args=["--no-sandbox"],**({"executable_path":exe} if exe else {}))
    for width,height in SIZES:
        mobile=width<600
        page=browser.new_page(viewport={"width":width,"height":height},is_mobile=mobile,has_touch=mobile)
        errors=[]
        page.on("pageerror",lambda error:errors.append(str(error)))
        page.set_content(APP.read_text(encoding="utf-8"))
        editor=page.locator("#compDisplay")
        toggle=page.locator("#allowDeviceKeys")
        def check(name,ok):
            checks.append({"viewport":[width,height],"check":name,"pass":bool(ok)})
        check("switch exists",toggle.count()==1)
        check("both Sanskrit pads visible",page.locator("#consonantFlick").is_visible() and page.locator("#vowelFlick").is_visible())
        check("device-aware default",toggle.is_checked()==(not mobile))
        check("contenteditable state",editor.get_attribute("contenteditable")==("false" if mobile else "true"))
        check("inputmode state",editor.get_attribute("inputmode")==("none" if mobile else "text"))
        check("no horizontal overflow",page.evaluate("document.documentElement.scrollWidth<=innerWidth"))
        page.locator("#consonantFlick .flickkey").first.click()
        check("custom pad inserts consonant",editor.inner_text().startswith("क"))
        toggle.check()
        check("switch enables editing",editor.get_attribute("contenteditable")=="true")
        editor.click()
        page.keyboard.press("ControlOrMeta+A")
        page.keyboard.insert_text("राम")
        check("hardware input accepted",editor.inner_text()=="राम")
        if mobile and height>=500:
            page.set_viewport_size({"width":width,"height":height-270})
            page.wait_for_timeout(80)
            check("keyboard viewport contraction recognized",page.locator("body").evaluate("e=>e.classList.contains('osk-visible')"))
            check("thumb pads remain visible",page.locator("#consonantFlick").is_visible() and page.locator("#vowelFlick").is_visible())
            # A regression once collapsed the layout on editor blur during pointerdown,
            # moving this control before pointerup. A real click must complete.
            toggle.uncheck()
            check("switch OFF clickable while keyboard viewport is reduced",not toggle.is_checked())
            check("contraction toggle retains text",editor.inner_text()=="राम")
        else:
            toggle.uncheck()
        check("switch locks editor",editor.get_attribute("contenteditable")=="false")
        check("toggle preserves text",editor.inner_text()=="राम")
        check("no uncaught script errors",not errors)
        page.close()
    browser.close()
passed=sum(row["pass"] for row in checks)
result={"passed":passed,"total":len(checks),"status":"PASS" if passed==len(checks) else "FAIL","human_participants":0,"checks":checks}
print(json.dumps({"status":result["status"],"passed":passed,"total":len(checks)},indent=2))
sys.exit(passed!=len(checks))
