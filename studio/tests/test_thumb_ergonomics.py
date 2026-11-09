"""Svara Play v1.7 keyboard order, geometry, and editing smoke tests.

Run from repository root: python studio/tests/test_thumb_ergonomics.py
Requires: pip install playwright, plus a local Chromium installation.
No network requests or telemetry are made by the application.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

APP = (Path(__file__).resolve().parents[1] / 'index.html').read_text(encoding='utf-8')
LEFT = ['kbUndoThumb', 'kbJoinThumb', 'kbLeftThumb', 'kbRightThumb']
RIGHT = ['kbPasteThumb', 'kbCopyThumb', 'kbSpaceThumb', 'kbBackThumb']
checks = 0

def check(ok, message):
    global checks
    checks += 1
    assert ok, message

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    for width, height in [(1440, 900), (428, 926), (390, 844), (360, 750), (320, 568), (780, 360)]:
        ctx = browser.new_context(viewport={'width':width, 'height':height})
        page = ctx.new_page()
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.set_content(APP, wait_until='load')
        page.locator('#uDrawer-sanskrit').evaluate('(e) => e.open = true')
        page.locator('#kbPin').click()
        positions = page.evaluate("""() => {
            const rect=id=>document.getElementById(id).getBoundingClientRect();
            const left=[...document.querySelectorAll('#composerConsonants .kb-thumb-utility')].map(e=>e.id);
            const right=[...document.querySelectorAll('#composerVowels .kb-thumb-utility')].map(e=>e.id);
            const panel=document.getElementById('kbFloat');
            return {left,right,height:panel.getBoundingClientRect().height,
                    scrolling:panel.scrollHeight>panel.clientHeight+2,
                    overflow:document.documentElement.scrollWidth>innerWidth+2,
                    pasteY:rect('kbPasteThumb').y, copyY:rect('kbCopyThumb').y,
                    copyX:rect('kbCopyThumb').x, spaceX:rect('kbSpaceThumb').x,
                    backX:rect('kbBackThumb').x}
        }""")
        check(positions['left'] == LEFT, f'{width}: left order')
        check(positions['right'] == RIGHT, f'{width}: right order')
        check(positions['height'] <= height/2 + 2, f'{width}: <= half height')
        check(not positions['scrolling'], f'{width}: internal keyboard scroll')
        check(not positions['overflow'], f'{width}: horizontal overflow')
        check(positions['pasteY'] < positions['copyY'], f'{width}: paste in spare upper slot')
        check(positions['copyX'] < positions['spaceX'] < positions['backX'], f'{width}: high-use placement')
        check(not errors, f'{width}: JavaScript errors: {errors}')
        if width == 390:
            field=page.locator('#composerInput')
            field.fill('नम')
            field.evaluate('(e)=>{e.focus();e.setSelectionRange(e.value.length,e.value.length)}')
            page.locator('#kbJoinThumb').click()
            check(field.input_value() == 'नम्', 'virama insertion')
            page.locator('#kbSpaceThumb').click()
            check(field.input_value() == 'नम् ', 'space insertion')
            page.locator('#kbBackThumb').click()
            check(field.input_value() == 'नम्', 'backspace')
            page.locator('#kbUndoThumb').click()
            check(field.input_value() == 'नम् ', 'undo')
        ctx.close()
    browser.close()
print(f'Passed {checks}/{checks} thumb-ergonomics smoke checks')
