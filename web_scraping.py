import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

res= requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

src=res.content
# print(src)

soup =BeautifulSoup(src,"lxml")
print(soup)