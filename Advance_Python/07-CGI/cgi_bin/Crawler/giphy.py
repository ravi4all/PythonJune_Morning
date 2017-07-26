#!C:/Python36-32/python.exe

import cgi
import bs4 as bs
import urllib.request, json

form = cgi.FieldStorage()
# to_search = form.getvalue("box_1")
to_search = 'wwe'

def print_html(data):

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
    """.format(data))


def main():
    # sauce = urllib.request.urlopen("https://giphy.com/search/wwe")
    #
    # soup = bs.BeautifulSoup(sauce, 'lxml')
    #
    # data = soup.find_all('img')
    data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=bc56161131654faeb550630b83e0c977&limit=5").read())
    print(data)

    # print_html(data)

main()