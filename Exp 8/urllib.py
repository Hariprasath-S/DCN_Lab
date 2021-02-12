import urllib.request
url = 'http://gct.ac.in'
page = urllib.request.urlopen(url)
print(page.read())
