import urllib.request
from urllib.request import urlopen
import urllib.parse
import bs4 as bs
import threading

url = 'http://paste4btc.com/Wp1yPBAN'

removeWords = ['Syntax: text', 'Copy', 'Download', 'Print', 'Raw', 'Report']
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'


class startBotting(threading.Thread):
    def run(self):
        while True:
            visitPage()


def showHits():
    global respData
    soup = bs.BeautifulSoup(respData, 'lxml')

    olTag = str(soup.find('ol').text)

    for eachWords in removeWords:
        olTag = olTag.replace(eachWords + '\n', '')

    print(olTag)


def visitPage():
    global respData
    proxy = urllib.request.ProxyHandler({"https": "https://68.183.47.61:3128"})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    
def runit():
    for y in range(100):
        x = startBotting()
        #x.daemon = True
        x.start()
        print(x)

if __name__ == "__main__":
    runit()
