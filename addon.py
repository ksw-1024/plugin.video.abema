import sys
import xbmc
import xbmcgui
import xbmcplugin
import streamlink

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

streams = streamlink.streams("https://abema.tv/now-on-air/abema-news")
url = "http://127.0.0.1:53422/base64/c3RyZWFtbGluayBodHRwczovL2FiZW1hLnR2L25vdy1vbi1haXIvc3BlY2lhbC1wbHVzIGJlc3QK"

xbmc.Player().play(url)