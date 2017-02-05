#import urllib2
from bs4 import BeautifulSoup
import urllib.request
from flask import Flask,request,render_template,flash,url_for,redirect
import pymysql
app=Flask(__name__)
db=pymysql.connect("localhost","root","","IPP", autocommit=True)
cursor=db.cursor()
app.secret_key='some_secret'

url="https://india.gov.in/sanctioned-nsap-beneficiaries-old-aged-disability-and-widows-scheme-nsap-mis"
request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page,"html.parser")
print(soup.title.text)
#for link in soup.findAll('a'):
 #   print(link.text)
#print(soup.find('div',{"class":"region region-three-33-third"},'a').find('href'))
#for link in soup.findAll('div',{"class":"region region-three-33-third"}):
   # print(link.find('a').text)
  #  q="""INSERT INTO news VALUES('%s')"""%(link.find('href'))
 #   cursor.execute(q)
#print(soup.find('div',{"class":"view view-metadata view-id-metadata view-display-id-block_4 accordion-container view-dom-id-88dcff5681d13b63b6707a690f658253"}).find('a'))
#for link in soup.findAll('div',{"class":"views-field views-field-php-4"}):
 #   for l in soup.findAll('link'): 
  #      if link.has_attr('href'):
   #         print(link.attrs['href'])
    #    print(link.find('a').text)
     #   q="""INSERT INTO news VALUES('%s')"""%(link.find('a'))
      #  cursor.execute(q)
pd=soup.findAll('div',attrs={'class':'views-field views-field-php-4'})
for d in pd:
    print(d.find('a').text)
    print('\t')
    print(d.find('a')['href'])
    print('\n')        
    q="""INSERT INTO news VALUES('%s','%s')"""%(d.find('a').text,d.find('a')['href'])
    cursor.execute(q)
  
            
#print(soup.prettify())
#print(soup.title.string)
#print(soup.findAll('a'))

