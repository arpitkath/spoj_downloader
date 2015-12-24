import requests
import re
from bs4 import BeautifulSoup
import urllib.request
MYACCOUNT= "http://www.spoj.com/myaccount/"
HOME="https://www.spoj.com/"
def soln_id(user_name,password):
    ses=requests.Session()
    ses.post(HOME,data={'login_user':user_name,'password':password})
    data=ses.get(MYACCOUNT)
    soup=BeautifulSoup(data.text,'html.parser')
    anch=soup.find_all('a')
    solved=[]
    #print("1")
    for link in anch:
        k=link.get('href')
        if str(user_name) in str(k) and ',' in str(k):
            k=re.sub('[^A-Z0-9_]', '', k)
            if k!="":
                solved.append(k)
        if (len(solved))>1:
            break
    #print(solved)
    soln_ids=[]
    for id in solved:
        soln_page='http://www.spoj.com/status/'+str(id)+','+str(user_name)+'/'
        soln_data=ses.get(soln_page)
        soln_soup=BeautifulSoup(soln_data.text,'html.parser')
        inputTag = soln_soup.find(attrs={"id" : "max_id"})
        outputTag = inputTag['value']
        soln_ids.append(int(outputTag))
    #print(soln_ids)
    for i in range(len(soln_ids)):
        soln_download="http://www.spoj.com/files/src/save/"+str(soln_ids[i])
        file_name=str(solved[i])
        print(soln_download)
        urllib.request.urlretrieve(soln_download.strip(), file_name)
    print("done")
username = input("username: ")
password = input("password:").strip()
soln_id(username,password)
