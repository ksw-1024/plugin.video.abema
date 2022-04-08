from resources import streamlink
import vlc
import socket
import time

#リンクの設定
abema_news = "rtsp://127.0.0.1:8554"

#VLCの設定
player = vlc.MediaPlayer()
player.set_mrl(abema_news)
already_play = False
loop = True

#TCPポートテスト
host = '127.0.0.1'
port = 8553
timeout_seconds = 1

while loop == 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout_seconds)
    result = sock.connect_ex((host,int(port)))
    if result == 0:
        print("Host: {}, Port: {} - True".format(host, port))
        if already_play == False:
            player.play()
            already_play == True
    else:
        print("Host: {}, Port: {} - False".format(host, port))
        if already_play == True:
            player.stop()
            already_play == False
    
    time.sleep(timeout_seconds)
