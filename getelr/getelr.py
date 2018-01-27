# File grab education law reporter.
# https://educationlaw.org/member-services/members-pages/slr-back-issues

from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

browser = webdriver.Firefox(firefox_profile=fp)

browser.get('https://educationlaw.org/member-services/members-pages/slr-back-issues')

print('Visit browser, log in using your credentials, press enter here when ready to continue. ', end='')
discarded_wait = input()
print('\n\n\n')

elems = browser.find_elements_by_link_text('Read more ...')
for e in len(elems):
    elems[e].click()
    issues = browser.find_elements_by_css_selector('.article-content > p:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
    for i in len(issues):
        issues[i].click()
    browser.back()
