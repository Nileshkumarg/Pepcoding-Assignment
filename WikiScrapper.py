from bs4 import BeautifulSoup
import requests


def whatisname():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Please use only letters, try again")

inp = whatisname()
page = requests.get("https://en.wikipedia.org/wiki/"+inp[0])


wiki=requests.get("https://en.m.wikipedia.org/wiki/"+inp[0])
soup=BeautifulSoup(wiki.text,'html')

print("History")

ww2_contents=soup.find_all(class_='mf-section-1')
for i in ww2_contents:
    print(i.text)

print("Use in writing systems")

ww2_contents=soup.find_all(class_='mf-section-2')
for i in ww2_contents:
    print(i.text)
    
print("Other uses")

ww2_contents=soup.find_all(class_='mf-section-3')
for i in ww2_contents:
    print(i.text)
