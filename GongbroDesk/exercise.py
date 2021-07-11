from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com') as resopnse:
    soup = BeautifulSoup(resopnse, 'html.parser')
    for anchor in soup.select("span.ah_k"):
        print(anchor.get_text())