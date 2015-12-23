import requests
import re
from bs4 import BeautifulSoup

MYACCOUNT= "http://www.spoj.com/myaccount/"
HOME="https://www.spoj.com/"

def login(user_name,password):
    ses=requests.Session()
    ses.post(HOME,data={'login_user':user_name,'password':password})
'''def soln_id(data,user_name):
    data=requests.get(MYACCOUNT)
    soup=BeautifulSoup(data.text,'html.parser')
    anch=soup.find_all('a')
    l=[]
    for link in anch:
        k=link.get('href')
        if str(user_name) in str(k) and ',' in str(k):
            k=re.sub('[^A-Z]', '', k)#BUG:does not get numbers of solution id's
            if k!="":
                l.append(k)'''
'''First tried to apply here.
data = open('C:\\Users\\arpit\\Desktop\\spoj_home.htm', 'r')
soup = BeautifulSoup(data,'html.parser')
anch=soup.find_all('a')
    l=[]
    for link in anch:
        k=link.get('href')
        if str(user_name) in str(k) and ',' in str(k):
            k=re.sub('[^A-Z]', '', k)#BUG:does not get numbers of solution id's
            if k!="":
                l.append(k)print(tag)
'''