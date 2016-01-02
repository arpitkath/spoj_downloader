import requests
import re
from bs4 import BeautifulSoup
from os import mkdir,path
from getpass import getpass
MYACCOUNT = "http://www.spoj.com/myaccount/"
HOME = "https://www.spoj.com/"


def soln_id(user_name, password):
    ses = requests.Session()
    ses.post(HOME, data={'login_user': user_name, 'password':password})
    data = ses.get(MYACCOUNT)
    soup = BeautifulSoup(data.text, 'html.parser')
    anch = soup.find_all('a')
    solved = []
    for link in anch:
        k = link.get('href')
        if str(user_name) in str(k) and ',' in str(k):
            k=re.sub('[^A-Z0-9_]', '', k)
            if k != "":
                solved.append(k)
    soln_ids = []
    print("Fetching solution id's(be patient..)")
    for id in solved:
        soln_page = 'http://www.spoj.com/status/'+str(id)+','+str(user_name)+'/'
        soln_data = ses.get(soln_page)
        soln_soup = BeautifulSoup(soln_data.text,'html.parser')
        inputTag = soln_soup.find(attrs={"id": "max_id"})
        outputTag = inputTag['value']
        soln_ids.append(int(outputTag))
    file_path = 'SPOJ_'+user_name
    print("Files will be saved in directory "+file_path)
    if not path.exists(file_path):
        mkdir(file_path)
    for i in range(len(soln_ids)):
        soln_download = "http://www.spoj.com/files/src/save/"+str(soln_ids[i])
        r = ses.get(soln_download)
        d = r.headers['content-disposition']
        file_ext = re.findall("filename=(.+)", d)[0][12:]
        file_name = str(solved[i])+file_ext
        f = open("SPOJ_"+user_name+"/"+file_name,'w')
        f.write(r.text)
        f.close()
    print("done")
username = input("Username: ")
password = getpass()
soln_id(username, password)
