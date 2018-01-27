# File grab education law reporter.
# https://educationlaw.org/member-services/members-pages/slr-back-issues

from time import sleep
from selenium import webdriver
import os
import requests

browser = webdriver.Firefox()

# Get webpage. Send user to browser to enter credentials.
browser.get('https://educationlaw.org/member-services/members-pages/slr-back-issues')
print('\n\n\n Visit browser, log in using your credentials, press enter here when ready to continue. ', end='')
discarded_wait = input()
print('\n\n\n')

# Declare year index. Will count backwards from 2017.
year = 2017
elems = browser.find_elements_by_link_text('Read more ...')
# Would prefer e in elems suntax...
# Needs to use range(len(elems)) syntax because after returning at end of loop
# list of elems needs a refresh. Otherwise stale error occurs.
for e in range(len(elems)):
    elems = browser.find_elements_by_link_text('Read more ...')
    print('STARTING ' + str(year))
    elems[e].click()
    sleep(.5)
    # CSS Selector would be preferred but did not reliably identify desired links.
    for m in [r'January & February','January','February','March','April','May','June','July','August','September','October','November','December']:
        # Try/Except flow control; Some years some months not available.
        try:
            issue = browser.find_element_by_link_text(m)
            filelink = issue.get_attribute('href')
            r = requests.get(filelink)
            sleep(2)
            m1 = m.replace(r' &','')
            m2 = m1 + str(year) + '.pdf'
            print('Proceeding with ' + m2 + '.')
            open(m2, 'wb').write(r.content)
            sleep(1)
        except:
            print('No issue with link ' + m + ' name. Proceeding to next.')
            sleep(1)
    # Send browser back to original url.
    browser.back()
    # Wait to ensure browswer loads.
    sleep(1)
    # Increment year index.
    year = year - 1
    # Give user feedback.
    print('FINISHED ' + str(year))
    print('  ')
    print('  ')

