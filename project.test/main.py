from resources import streamlink
import vlc
import socket
import time
import rtsp

#リンクの設定
abema_news = "rtsp://127.0.0.1:8553"

#VLCの設定
player = vlc.MediaPlayer()
player.set_mrl(abema_news)
already_play = False
loop = True

#TCPポートテスト
host = '127.0.0.1'
port = 8553
timeout_seconds = 1

count = 0

#RTSPの設定
RTSP_URL = f"rtsp://127.0.0.1:8553"
client = rtsp.Client(rtsp_server_uri=RTSP_URL, verbose=True)
# client.read()

while loop == True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout_seconds)
    result = sock.connect_ex((host,int(port)))
    
    count +=1
    if result == 0:
        print("Host: {}, Port: {} - True".format(host, port))
    else:
        print("Host: {}, Port: {} - False".format(host, port))
        loop = False
    print(str(count))
    time.sleep(timeout_seconds)
