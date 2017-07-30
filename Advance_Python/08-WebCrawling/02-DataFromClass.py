# from bs4 import BeautifulSoup as bs
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("http://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2730173942&pf_rd_r=1CD8WSDN9WD675BFZ3NM&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1")

soup = bs.BeautifulSoup(sauce, 'lxml')

a = soup.find_all(class_='titleColumn')
# print(a)

for data in a:
    print(data.text)