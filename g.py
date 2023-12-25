import numpy
import requests
from bs4 import BeautifulSoup

gees = {'money':543,
        'power':4}
url='https://libraryofbabel.info/book.cgi?1-w4-s1-v20:1'
website = requests.get(url).text
doc=BeautifulSoup(website,'html.parser')
