from pathlib import Path
from playwright.sync_api import sync_playwright

html = (Path(__file__).resolve().parents[1] / 'index.html').read_text(encoding='utf-8')
passed = 0
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
    for width, height in [(1440, 900), (428, 926), (390, 844), (360, 750), (320, 568), (780, 360)]:
        context = browser.new_context(viewport={'width': width, 'height': height})
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.set_content(html, wait_until='load')
        page.locator('#uDrawer-sanskrit').evaluate('element => element.open = true')
        page.locator('#kbPin').click()
        metrics = page.evaluate("""() => {
          const floating = document.querySelector('#kbFloat');
          const bounds = floating.getBoundingClientRect();
          const left = document.querySelector('#composerConsonants').getBoundingClientRect();
          const right = document.querySelector('#composerVowels').getBoundingClientRect();
          return [bounds.height <= innerHeight / 2 + 1,
                  floating.scrollHeight <= floating.clientHeight + 2,
                  Math.abs(left.y - right.y) < 4,
                  document.documentElement.scrollWidth <= innerWidth + 2];
        }""")
        for okay in metrics:
            assert okay, f'layout failure at {width} x {height}: {metrics}'
            passed += 1
        assert page.locator('#composerConsonants .compose-flick-key').first.locator('.kb-five span').count() == 5
        passed += 1
        assert page.locator('.kb-thumb-utility').count() == 8
        passed += 1
        page.locator('#composerInput').fill('राम ')
        page.locator('#kbBackThumb').click()
        assert page.locator('#composerInput').input_value() == 'राम'
        passed += 1
        page.locator('#kbUndoThumb').click()
        assert page.locator('#composerInput').input_value() == 'राम '
        passed += 1
        page.locator('#kbCollapse').click()
        assert not page.locator('#composerConsonants').is_visible()
        passed += 1
        assert page.locator('#kbPreviewText').is_visible()
        passed += 1
        assert not errors, errors
        passed += 1
        context.close()
    browser.close()
print(f'Compact keyboard smoke: {passed}/{passed} checks passed')
