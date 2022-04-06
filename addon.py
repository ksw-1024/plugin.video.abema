import sys
import xbmc
import xbmcgui
import xbmcplugin
from resources import streamlink

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = "rtsp://127.0.0.1:8554"

xbmc.Player().play(url)