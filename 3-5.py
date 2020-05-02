import io,sys
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

URL='https://www.wishket.com/accounts/login/'
ua=UserAgent()
#print(ua.ie)
#print(ua.chrome)
#print(ua.random)

with requests.session() as s:
    s.get(URL)
    Login_Info={
        'identification' : 'whddnr3356',
        'password' : 'ok6542896',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }

    response=s.post(URL,data=Login_Info,headers={'User-Agent':str(ua.chrome), 'Referer' : 'https://www.wishket.com/accounts/login/'})
    if response.status_code==200 and response.ok:
        soup=BeautifulSoup(response.text,'html.parser')
        Project_List=soup.select('div.partners-history > div')
        print(Project_List)
        for i in Project_List:
            print(i)
            #print(i.find('th').string,i.find('td').text)
