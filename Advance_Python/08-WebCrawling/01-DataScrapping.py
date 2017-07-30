# from bs4 import BeautifulSoup as bs
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://www.flipkart.com/")

soup = bs.BeautifulSoup(sauce, 'lxml')

a = soup.find_all('a')
# print(a)

for data in a:
    print(data.text)