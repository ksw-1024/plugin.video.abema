import sys
import xbmc
import xbmcgui
import xbmcplugin
from resources import streamlink
import socket

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
addon_name = 'AbemaTV Player'

#リンクの設定
abema_news = "rtsp://127.0.0.1:8553"

#TCPポートテスト
host = '127.0.0.1'
port = 8553
timeout_seconds = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout_seconds)
result = sock.connect_ex((host,int(port)))
if result == 0:
    print("Host: {}, Port: {} - True".format(host, port))
    xbmc.Player().play(abema_news)
    
else:
    print("Host: {}, Port: {} - False".format(host, port))
    xbmcgui.Dialog().ok(addon_name, 'Streamlink is not running on a local machine.')
    already_play = False
