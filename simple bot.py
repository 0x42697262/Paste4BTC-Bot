import urllib.request
import urllib.parse
import bs4 as bs


url = 'http://paste4btc.com/Wp1yPBAN'
removeWords = ['Syntax: text', 'Copy', 'Download', 'Print', 'Raw', 'Report']
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'


def visitPage():
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    soup = bs.BeautifulSoup(respData, 'lxml')

    olTag = str(soup.find('ol').text)

    for eachWords in removeWords:
        olTag = olTag.replace(eachWords + '\n', '')

    print(olTag)


if __name__ == "__main__":
    visitPage()
