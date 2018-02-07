from os import *

newpath = r'%s/Desktop/MASPpics'%(home)
os.makedirs(newpath)
MASPpre = '%s/MASP/MASP.sh'
MASPpost = '%s/Desktop/MASP.sh'
os.rename(MASPpre, MASPpost)
os.system("cd Desktop")
os.system("#!/usr/local/bin/python")
os.system("chmod +x MASP.sh")
os.system("python3 MASP.py")