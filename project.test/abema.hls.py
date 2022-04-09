from selenium import webdriver
import chromedriver_binary
from time import sleep
import requests
import re
import os

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("https://abema.tv/now-on-air/abema-news")
    sleep(2)

    pl = requests.get("https://linear-abematv.akamaized.net/channel/abema-news/1080/playlist.m3u8").text

    key_url = re.search(u'URI=\"(.*?)\"\,',pl).group(1)

    browser.execute_script('''
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200)
        window.key = new Uint8Array(xhr.response)
}
xhr.open("GET", "%s");
xhr.send();
'''%key_url)

    sleep(1)
    key = browser.execute_script("return window.key;")
    browser.close()

    f = open("key.bin", "wb")
    f.write(bytearray(key))
    f.close()

    mod_pl = re.sub('URI=.*?\,', 'URI=\"key.bin\",', pl)

    f = open("playlist.m3u8", "w")
    f.write(mod_pl)
    f.close()

    os.system("ffplay playlist.m3u8 -protocol_whitelist file,http,https,tcp,tls,crypto")