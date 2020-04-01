#importing the module 
import os
import pafy 
from .constant import BASEDIR,SAVE_PATH_VIDEO,SAVE_PATH_SOUND
import shutil
from pydub import AudioSegment
#where to save 
def findExtension(data):
    i=len(data)-1
    char=""
    while(data[i]!='.' and i>0):
        char=data[i]+char
        i-=1
    char="."+char
    return char

def videoDownload(link,choice): 
    try:
        video = pafy.new(link)
        best = video.getbest()
        best = video.getbest(preftype="mp4")
        fname=link[len(link)-11::]
        if choice=="video":
            loc=SAVE_PATH_VIDEO+fname+".mp4"
        # else:
        #     loc=SAVE_PATH_SOUND+fname+".mp3"
        if os.path.isfile(loc):
            return loc
        filename = best.download(filepath=loc)
        return loc
    except:
        return 0

def soundDownloader(link):
    try:
        video = pafy.new(link)
        best = video.getbestaudio()
        print(best.title)
        fname=link[len(link)-11::]
        loc=best.title+"."+best.extension
        if os.path.isfile(SAVE_PATH_SOUND+fname+".mp3"):
            return SAVE_PATH_SOUND+fname+".mp3"
        filename = best.download()
        extention=best.extension
        os.rename(loc,fname+".mp3")
        # loc=loc[:len(loc)-len(extention):]+".mp3"
        shutil.move(fname+".mp3", SAVE_PATH_SOUND+fname+".mp3")
        return  SAVE_PATH_SOUND+fname+".mp3"
    except:
        return 0

def findName(data):
    data=str(data)
    i=len(data)-1
    char=""
    while(data[i]!='/' and i>0):
        char=data[i]+char
        i-=1
    # char="."+char
    return char