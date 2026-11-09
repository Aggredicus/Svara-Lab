"""Offline, local in-memory Chromium tests for Svara Play v1.6 mantra library.
No network, no account, no audio capture. Requires playwright and Chromium.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'index.html'
CATALOG=ROOT/'data/gayatri_catalog.json'
DATA=json.loads(CATALOG.read_text())
assert len(DATA)==38
assert sum(bool(i['hasAccents']) for i in DATA)==11
for rec in DATA:
    assert rec['id'] and rec['source'].startswith('https://') and rec['lines']
    assert len(set(rec['lines']))==len(rec['lines'])
    if rec['group']!='vedic': assert not rec['hasAccents']
    if rec['hasAccents']: assert any('॑' in x or '॒' in x for x in rec['lines'])

checks=0
failures=[]
def ok(condition, label):
    global checks
    checks+=1
    if not condition:
        failures.append(label)
        print('FAIL',label,flush=True)

src=APP.read_text()
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for width,height in ((1440,900),(428,926),(390,844),(360,750),(320,568)):
        context=browser.new_context(viewport={'width':width,'height':height},accept_downloads=True,is_mobile=width<500,has_touch=width<500)
        page=context.new_page(); errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
        page.set_content(src,wait_until='load')
        page.add_style_tag(content='*,html{scroll-behavior:auto!important;animation:none!important;transition:none!important}')
        page.set_default_timeout(5000)
        prefix=str(width)
        info=page.evaluate('SvaraGayatriInfo')
        ok(info['count']==38,prefix+' catalog has 38')
        ok(info['vedicAccented']==11,prefix+' 11 accented Vedic entries')
        ok(len(info['groups'])==3,prefix+' provenance groups')
        ok(page.locator('#gayatriLibrary').count()==1,prefix+' library attached to composer')
        ok(page.evaluate('document.documentElement.scrollWidth<=innerWidth+2'),prefix+' no page overflow closed')
        page.locator('#gayatriLibrary summary').click()
        ok(page.locator('#gayatriLibrary').evaluate('(e)=>e.open'),prefix+' open library')
        ok(page.locator('#gayatriList .gayatri-entry').count()==38,prefix+' full menu')
        ok(page.locator('#gayatriLines .gayatri-line').count()==3,prefix+' three Savitri padas')
        ok(page.locator('#gayatriAccents').is_checked(),prefix+' marks enabled')
        count=page.locator('#gayatriLines .tone-svarita').count()+page.locator('#gayatriLines .tone-low').count()
        ok(count>=8,prefix+' actual encoded marks visible')
        ok('॒' in page.locator('#gayatriLines').inner_text(),prefix+' low mark text')
        ok('॑' in page.locator('#gayatriLines').inner_text(),prefix+' svarita mark text')
        ok('Nicṛd' in page.locator('#gayatriMeter').inner_text(),prefix+' irregular first pada explanation')
        page.locator('#gayatriAccents').uncheck()
        ok('॑' not in page.locator('#gayatriLines').inner_text() and '॒' not in page.locator('#gayatriLines').inner_text(),prefix+' plain mode removes only accents')
        page.locator('#gayatriAccents').check()
        page.locator('#gayatriPreface').check()
        page.evaluate('Object.defineProperty(navigator,"clipboard",{configurable:true,value:{writeText:async text=>window.__copy=text}})')
        page.locator('#gayatriCopyPlain').click()
        page.wait_for_timeout(40)
        value=page.evaluate('window.__copy')
        ok(value.startswith('ॐ भूर्भुवः स्वः'),prefix+' optional invocation preface')
        ok('॑' not in value and '॒' not in value,prefix+' plain copy strips marks')
        page.locator('#gayatriCopyAccented').click()
        page.wait_for_timeout(30)
        value=page.evaluate('window.__copy')
        ok('॑' in value and '॒' in value,prefix+' accent copy preserved')
        page.locator('#gayatriPreface').uncheck()
        page.locator('#gayatriGroup').select_option('upanishad')
        ok(page.locator('#gayatriList .gayatri-entry').count()==18,prefix+' Upanishad 18')
        page.locator('#gayatriList button[data-id="mnu-16"]').click()
        ok(page.locator('#gayatriEditor').input_value().startswith('नारायणाय'),prefix+' Narayana inserted')
        ok(page.locator('#gayatriAccents').is_disabled(),prefix+' unverified marks disabled')
        ok(page.locator('#gayatriCopyAccented').is_disabled(),prefix+' no fabricated Vedic copy')
        page.locator('#gayatriList .gayatri-entry').filter(has=page.locator('button[data-id="mnu-16"]')).locator('.gayatri-direct-copy').click()
        page.wait_for_timeout(30)
        ok(page.evaluate('window.__copy').startswith('नारायणाय'),prefix+' direct-copy on list selection')
        page.locator('#gayatriGroup').select_option('devotional')
        ok(page.locator('#gayatriList .gayatri-entry').count()==9,prefix+' devotional 9')
        page.locator('#gayatriList button[data-id="dev-hanuman"]').click()
        ok('अञ्जनासुताय' in page.locator('#gayatriEditor').input_value(),prefix+' Hanuman variant')
        ok('No accent transcription' in page.locator('#gayatriLegend').inner_text(),prefix+' no deceptive accents')
        page.locator('#gayatriSearch').fill('lakṣmī')
        ok(page.locator('#gayatriList .gayatri-entry').count()==1,prefix+' dynamic search IAST name')
        page.locator('#gayatriSearch').fill('')
        page.locator('#gayatriList button[data-id="dev-lakshmi"]').click()
        page.locator('#gayatriEditor').fill('अ॒ग्निः\nस्व॑रितम्')
        page.locator('#gayatriPreviewEdited').check()
        ok(page.locator('#gayatriLines .tone-svarita').count()>=1,prefix+' live accent update above')
        ok(page.locator('#gayatriLines .tone-low').count()>=1,prefix+' live accent update below')
        page.locator('#gayatriTarget').select_option('composerInput')
        page.locator('#gayatriInsert').click()
        ok(page.locator('#composerInput').input_value()=='अ॒ग्निः\nस्व॑रितम्',prefix+' handoff to seven sounds')
        page.locator('#gayatriEditor').focus()
        page.locator('#uDrawer-sanskrit').evaluate('(e)=>e.open=true')
        page.locator('#kbPin').click()
        ok(page.evaluate('SvaraKeyboardInfo.getState().pinned'),prefix+' pinned keyboard opens while mantra editor active')
        page.locator('#gayatriEditor').focus()
        ok(page.evaluate('SvaraKeyboardInfo.getState().target')=='gayatriEditor',prefix+' keyboard recognizes mantra editor')
        ok(page.locator('#kbFloat').evaluate('(e)=>e.getBoundingClientRect().height<=innerHeight/2+2'),prefix+' compact pinned height retained')
        page.locator('#kbSpaceThumb').click()
        ok(page.locator('#gayatriEditor').input_value().endswith(' '),prefix+' key inserts into mantra editor')
        ok(not errors,prefix+' no Javascript errors: '+str(errors))
        ok(page.evaluate('document.documentElement.scrollWidth<=innerWidth+2'),prefix+' no page overflow open')
        context.close()
    browser.close()
print(f'Gayatri suite: {checks} checks, {len(failures)} failures')
if failures: raise SystemExit(1)