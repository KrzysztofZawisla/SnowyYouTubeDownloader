from winreg import *
from pytube import YouTube
import sys
import subprocess
import os
import shutil
import time

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    downloadsFolder = QueryValueEx(
        key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

def downloadFromYt():
    searchDone = False
    try:
        ytTitle = YouTube(str(sys.argv[1])).title
        yt = YouTube(str(sys.argv[1]))
        ytObjects = yt.streams.all()
        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"2160p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"1440p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(
                        filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"1080p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"720p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"480p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"360p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"240p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        if searchDone == False:
            for ytObjectVideoInt in range(len(ytObjects)):
                if ("res=\"144p\"" in str(ytObjects[ytObjectVideoInt])) and ("mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt])):
                    print(ytObjects[ytObjectVideoInt])
                    ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                    ytVideoName = "videoToProcess.mp4"
                    searchDone = True
                    break

        bandwitchI = 1000
        while bandwitchI > 0:
            for ytObjectAudioInt in range(len(ytObjects)):
                if ("abr=\""+str(bandwitchI)+"kbps\"" in str(ytObjects[ytObjectAudioInt])) and ("mime_type=\"audio/webm\"" in str(ytObjects[ytObjectAudioInt])):
                    print(ytObjects[ytObjectAudioInt])
                    ytObjects[ytObjectAudioInt].download(filename="audioToProcess")
                    ytAudioName = "audioToProcess.webm"
                    bandwitchI = 0
                    break
            bandwitchI -= 1

        cmdCommand = "ffmpeg.exe -i \""+ytVideoName+"\" -i \""+ytAudioName+"\" -y videoOutput.mp4"
        proc = subprocess.Popen(cmdCommand, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.wait()
    except:
        print("Wystąpił nieoczekiwany błąd. Powtórzymy całą operację jeszcze raz.")
        downloadFromYt()
    try:
        os.remove(ytVideoName)
    except:
        pass
    try:
        os.remove(ytAudioName)
    except:
        pass
    try:
        os.rename("videoOutput.mp4", str(ytTitle)+".mp4")
    except:
        print("Nie udało się zmienić nazwy pliku na nazwę utworu. Proszę zrobić to ręcznie.")
    try:
        shutil.move(str(ytTitle)+".mp4", downloadsFolder)
    except:
        try:
            shutil.move("videoOutput.mp4", downloadsFolder)
        except:
            print("Nie udało się przenieść pliku do folderu pobrane. Plik znajduje się w folderze: "+os.getcwd())

downloadFromYt()
