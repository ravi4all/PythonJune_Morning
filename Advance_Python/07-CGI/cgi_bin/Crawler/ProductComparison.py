#!C:/Python36-32/python.exe

import bs4 as bs
import urllib.request
import cgi

form = cgi.FieldStorage()

item_name = form.getvalue('item')
# item_name = 'iphone 7'

def print_html(name):

    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
    Data {}
    </body>
    </html>
    """.format(name))


def main():
    d = []
    # sauce = urllib.request.urlopen("https://www.flipkart.com/")
    sauce = urllib.request.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1/257-5609592-0603442?url=search-alias%3Daps&field-keywords="+item_name)
    soup = bs.BeautifulSoup(sauce, 'lxml')

    data = soup.find_all('li', class_="s-result-item")

    for i in data:
        d.append(i)
        # print(d)

    print_html(d)

main()