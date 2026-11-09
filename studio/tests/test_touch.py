"""Chromium CDP mobile touch smoke tests for Svara Play keyboard v1.4."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'index.html').read_text(encoding='utf-8')

def tp(*points):
    return [{'x':x,'y':y,'radiusX':6,'radiusY':6,'force':0.8,'id':pid} for pid,x,y in points]

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    context=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True)
    page=context.new_page()
    page.set_content(HTML,wait_until='load')
    page.locator('#composerInput').fill('')
    page.evaluate('document.querySelector("#uDrawer-sanskrit").open=true')
    first=page.locator('#composerConsonants button').first
    first.scroll_into_view_if_needed()
    box=first.bounding_box()
    x,y=box['x']+box['width']/2,box['y']+box['height']/2
    cdp=context.new_cdp_session(page)
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':tp((0,x,y))})
    for k in range(1,6):
        cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':tp((0,x+k*9,y))})
        page.wait_for_timeout(24)
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    assert page.locator('#composerInput').input_value()=='ग','Touch swipe right failed'

    page.locator('#composerInput').fill('')
    box=first.bounding_box()
    x,y=box['x']+box['width']/2,box['y']+box['height']/2
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':tp((0,x,y))})
    page.wait_for_timeout(450)
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    assert page.locator('#kbChoiceMenu').is_visible(),'Hold popup did not persist'
    page.locator('#kbChoiceMenu [data-direction="left"]').tap()
    assert page.locator('#composerInput').input_value()=='ङ','Hold popup variant failed'

    # Simultaneous chords: releasing second thumb first does not reverse input.
    page.locator('#composerInput').fill('')
    consonant=page.locator('#composerConsonants button').first
    vowel=page.locator('#composerVowels button').nth(1)  # इ
    consonant.scroll_into_view_if_needed();vowel.scroll_into_view_if_needed()
    a,b=consonant.bounding_box(),vowel.bounding_box()
    x1,y1=a['x']+a['width']/2,a['y']+a['height']/2
    x2,y2=b['x']+b['width']/2,b['y']+b['height']/2
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':tp((0,x1,y1))})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':tp((0,x1,y1),(1,x2,y2))})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':tp((0,x1,y1))})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    assert page.locator('#composerInput').input_value()=='कि','Two-touch order not preserved'
    context.close();browser.close()
print('CDP TOUCH CHECKS: 3 PASSED')