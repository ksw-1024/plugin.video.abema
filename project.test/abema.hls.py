from selenium import webdriver
import chromedriver_binary
from time import sleep
import requests
import re
import os

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("https://abema.tv/now-on-air/abema-news")
    sleep(1)
    js = requests.get("https://abema.tv/xhrp.js").text
    mod_js = re.sub("(_0x31a687=.*?);", "\\1;window.key=_0x31a687;", js)
    browser.execute_script(mod_js)
    sleep(1)
    key = browser.execute_script('return window.key;')
    print(key)
    browser.close()

    f = open("key.bin", "wb")
    f.write(bytearray(key))
    f.close()

    pl = requests.get("https://linear-abematv.akamaized.net/channel/abema-news/1080/playlist.m3u8").text
    mod_pl = re.sub('URI=.*?\,', 'URI=\"key.bin\",', pl)

    f = open("playlist.m3u8", "w")
    f.write(mod_pl)
    f.close()

    os.system("ffplay playlist.m3u8 -protocol_whitelist file,http,https,tcp,tls,crypto")