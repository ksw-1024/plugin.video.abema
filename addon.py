import sys
import json
import subprocess
import xbmc
import xbmcgui
import xbmcplugin
from resources.streamlink import Streamlink

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

streams = Streamlink.streams("https://abema.tv/now-on-air/abema-news")
url = streams['best'].to_url()

xbmc.Player().play(url)