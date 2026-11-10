"""Standalone browser regression for Svara Play v1.8 mobile flow.
Run: python studio/tests/test_mobile_flow.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

APP = (Path(__file__).resolve().parents[1] / 'index.html').read_text(encoding='utf-8')
checks=0

def ok(value, note):
 global checks
 checks+=1
 assert value, f'CHECK {checks}: {note}'

with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(320,568),(360,750),(390,844),(428,926),(760,700),(1440,900)]:
  context=browser.new_context(viewport={'width':width,'height':height},has_touch=width<=760,is_mobile=width<=760,accept_downloads=True)
  page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(APP,wait_until='load');page.add_style_tag(content='*,html{transition:none!important;animation:none!important;scroll-behavior:auto!important}')
  ok(page.evaluate('window.__svaraFlowV18?.version')=='1.8.0',f'{width}: adapter initialized')
  ok(page.evaluate('document.documentElement.scrollWidth<=innerWidth+2'),f'{width}: no horizontal overflow')
  ok(page.locator('#uKeyStrip .u-key').count()==12,f'{width}: chromatic options retained')
  ok(page.locator('#composerSlots .compose-slot').count()==7,f'{width}: composer retained')
  ok(page.locator('#piano .piano-key').count()==37,f'{width}: piano retained')
  ok(page.locator('#uDrawers .u-disclosure').count()==14,f'{width}: all advanced drawers retained')
  ok(page.locator('#gayatriLibrary').locator('xpath=..').get_attribute('id')=='uDrawers',f'{width}: mantra library reachable in tools')
  ok(page.locator('#v18ScalesMore').get_attribute('open') is None,f'{width}: supplemental scale options initially closed')
  if width<=760:
   ok(page.locator('#v18BottomNav').is_visible(),f'{width}: navigation visible')
   ok(page.locator('#v18BottomNav button').count()==5,f'{width}: five quick actions')
   ok(page.locator('.u-switchbar').evaluate('(e)=>e.getBoundingClientRect().height')<180,f'{width}: compact selector')
   page.locator('#v18BottomNav button[data-go="play"]').click()
   ok(page.locator('#v18BottomNav button[data-go="play"]').get_attribute('aria-current')=='page',f'{width}: play nav')
   page.locator('#v18BottomNav button[data-go="beat"]').click()
   ok(page.locator('#v18BottomNav button[data-go="beat"]').get_attribute('aria-current')=='page',f'{width}: beat nav')
   page.locator('#v18BottomNav button[data-go="mantras"]').click()
   ok(page.locator('#gayatriLibrary').evaluate('(e)=>e.open'),f'{width}: mantra library opened')
   page.locator('#v18BottomNav button[data-go="explore"]').click()
   ok(page.locator('#v18BottomNav button[data-go="explore"]').get_attribute('aria-current')=='page',f'{width}: explore nav')
   page.locator('#v18BottomNav button[data-go="write"]').click()
   ok(page.locator('#v18BottomNav button[data-go="write"]').get_attribute('aria-current')=='page',f'{width}: write nav')
  else:ok(not page.locator('#v18BottomNav').is_visible(),f'{width}: desktop navigation unobtrusive')
  old=page.locator('#uScaleName').inner_text()
  page.locator('#uNextRaga').click()
  ok(page.locator('#uScaleName').inner_text()!=old,f'{width}: instant scale change')
  page.locator('#uDockKeyUp').click()
  ok(page.locator('#uDockKeyName').inner_text()=='Sa C♯',f'{width}: instant tonic change')
  page.locator('#v18ScalesMore').evaluate('(e)=>e.open=true')
  ok(page.locator('#uFamily').is_visible(),f'{width}: family filter accessible')
  ok(page.locator('#uAutoPreview').is_visible(),f'{width}: auto-preview toggle accessible')
  page.locator('#v18PhraseMore').evaluate('(e)=>e.open=true')
  ok(page.locator('#composerTala').is_visible(),f'{width}: phrase and tala sync accessible')
  page.locator('#v18PianoTips').evaluate('(e)=>e.open=true')
  ok(page.locator('#toggleTuning').is_visible(),f'{width}: just intonation option accessible')
  page.locator('#v18Meaning').evaluate('(e)=>e.open=true')
  ok(page.locator('#composerArt').is_visible(),f'{width}: original artistic guide accessible')
  page.locator('#uDrawer-sanskrit').evaluate('(e)=>e.open=true')
  page.locator('#kbPin').click()
  ok(page.locator('#kbFloat').is_visible(),f'{width}: original keyboard pin works')
  height_ratio=page.locator('#kbFloat').evaluate('(e)=>e.getBoundingClientRect().height/innerHeight')
  ok(height_ratio<=.5+0.002,f'{width}: keyboard <= half viewport')
  if width<=760:ok(page.locator('#v18BottomNav').is_visible(),f'{width}: nav stays in reserved space beneath pinned keyboard')
  ok(not errors,f'{width}: no runtime JS errors: {errors}')
  context.close()
 browser.close()
print(f'v1.8 mobile flow: {checks}/{checks} PASS')
