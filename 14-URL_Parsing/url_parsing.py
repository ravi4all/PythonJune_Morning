import urllib.request

with urllib.request.urlopen('http://www.google.co.in/?gws_rd=ssl') as response:
   html = response.read()

# print(html)

with open("goog.html",'w') as wr:
    wr.write(str(html))

