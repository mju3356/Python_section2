import io,sys
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#chrome_options=Options()
#chrome_options.add_argument('--headless')

#driver=webdriver.Chrome(chrome_options=chrome_options,executable_path='c:/MP/chromedriver')
driver=webdriver.Chrome('c:/MP/chromedriver')
driver.set_window_size(1920,1080)
driver.implicitly_wait(3)
driver.get('https://www.wishket.com/accounts/login/')
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_name('identification').send_keys('whddnr3356')
driver.implicitly_wait(1)
driver.find_element_by_name('password').send_keys('ok6542896')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()



print('완료')
