import sys
import json
import subprocess
import xbmc
import xbmcgui
import xbmcplugin
import streamlink

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

streams = streamlink.streams("https://abema.tv/now-on-air/abema-news")
url = streams['best'].to_url()

xbmc.Player().play(url)