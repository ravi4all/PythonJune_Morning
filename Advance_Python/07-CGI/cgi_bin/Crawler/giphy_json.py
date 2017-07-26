import urllib.request,json
data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=bc56161131654faeb550630b83e0c977&limit=5").read())
print(json.dumps(data, sort_keys=True, indent=4))