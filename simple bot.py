import urllib.request
import urllib.parse
import bs4 as bs
import random
import string
import threading
from urllib.request import urlopen
from random import choice

# ---- init ---- #
SSL_Proxies_URL = "https://sslproxies.org/"
bot_Header = {}
bot_Header['User-Agent'] = "curl/7.{curl_minor}.{curl_revision} (x86_64-pc-linux-gnu) libcurl/7.{curl_minor}.{curl_revision} OpenSSL/0.9.8{openssl_revision} zlib/1.2.{zlib_revision}".format(curl_minor=random.randint(8, 22), curl_revision=random.randint(1, 9), openssl_revision=random.choice(string.ascii_lowercase), zlib_revision=random.randint(2, 6)) # code copied from https://raw.githubusercontent.com/stamparm/fetch-some-proxies/master/fetch.py

removeWords = ['Syntax: text', 'Copy', 'Download', 'Print', 'Raw', 'Report']
# ---- acquire proxies ---- #

def get_proxy():
    prox_req = urllib.request.Request(SSL_Proxies_URL, headers=bot_Header)
    proxy_resp = urllib.request.urlopen(prox_req)
    proxy_data_resp = proxy_resp.read()
    soup = bs.BeautifulSoup(proxy_data_resp, 'html5lib')
    return {'https': choice(list(map(lambda x: 'https://'+x[0]+':'+x[1], list(zip(map(lambda x: x.text, soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8]))))))}


# ---- start botting ---- #

def start_bot(url):
    while 1:
        try:
            prx = get_proxy()
            print(prx)
            proxy = urllib.request.ProxyHandler(prx)
            proxy_opener = urllib.request.build_opener(proxy)
            proxy_installopener = urllib.request.install_opener(proxy_opener)

            req = urllib.request.Request(url, headers=bot_Header)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            soup = bs.BeautifulSoup(respData, 'lxml')

            olTag = str(soup.find('ol').text)

            for eachWords in removeWords:
                olTag = olTag.replace(eachWords + '\n', '')

            print(olTag)
            break
        except:
            pass


class threadBots(threading.Thread):
    def run(self):
        while 1:
            start_bot("[enter your paste4btc link here with https://]")


def run():
    #x = input("Paste4BTC Link: ")
    #y = input("Number of Threads: ")
    for b in range(100):
        bot = threadBots()
        bot.start()
        print(bot)


if __name__ == "__main__":
    run()
