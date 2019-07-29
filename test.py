import ssl
from urllib.request import urlopen
context = ssl._create_unverified_context()
html = urlopen("https://www.naver.com", context=context)
print(html.read())
