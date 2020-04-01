from django.shortcuts import render
from .utils import videoDownload,soundDownloader,findName

# Create your views here.
def index(request):
    return render(request,"index.html")

def download(request):
    link=request.GET['fname']
    choice=request.GET['downloader']
    if choice=="video":
        result=videoDownload(link,choice)
    else:
        result=soundDownloader(link)
    print(result)
    filename=findName(result)
    return render(request,"download.html",{"cat":choice,"link":result,"fname":filename})