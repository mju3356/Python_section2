import io,sys
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


class Ncafe_Write_Att:
    def __init__(self):
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        #self.driver=webdriver.Chrome(chrome_options=chrome_options,executable_path='c:/MP/chromedriver')
        self.driver=webdriver.Chrome('c:/MP/chromedriver')
        self.driver.implicitly_wait(5)

    def Write_Attend_Check(self):
        self.driver.get('https://www.naver.com/')
        self.driver.find_element_by_xpath('//*[@id="account"]/a').click()
        self.driver.implicitly_wait(30)

        tag_id = self.driver.find_element_by_name('id')
        tag_pw = self.driver.find_element_by_name('pw')
        tag_id.clear()
        time.sleep(1)

        tag_id.click()
        pyperclip.copy('ok8562896')
        tag_id.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        tag_pw.click()
        pyperclip.copy('ok93932896')
        tag_pw.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        #self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        #self.driver.find_element_by_name('id').send_keys('ok8562896')
        #self.driver.find_element_by_name('pw').send_keys('ok93932896')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        #로그인완료
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=20156442&search.menuid=7')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다.')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)

    #소멸자
    def __del__(self):
        #self.driver.close() # 현재 포커스 종료
        self.driver.quit() #현재 프로그램 종료
        print('REMOVDE COMPLETE')

if __name__ == '__main__':
    a=Ncafe_Write_Att()
    start_time=time.time()
    a.Write_Attend_Check()
    print('--total %s Seconds--' % (time.time()-start_time))
    del a
