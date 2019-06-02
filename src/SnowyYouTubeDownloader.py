from winreg import *
from pytube import YouTube
import sys
import subprocess
import os
import shutil

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    downloadsFolder = QueryValueEx(
        key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

def downloadFromYt():
    searchDone = False
    try:
        ytTitle = YouTube(str(sys.argv[1])).title
        yt = YouTube(str(sys.argv[1]))
        ytObjects = yt.streams.all()
        resolutionI = 10000
        while resolutionI > 0:
            for ytObjectVideoInt in range(len(ytObjects)):
                try:
                    if "res=\""+str(resolutionI)+"p\"" in str(ytObjects[ytObjectVideoInt]):
                        print(ytObjects[ytObjectVideoInt])
                        ytObjects[ytObjectVideoInt].download(filename="videoToProcess")
                        if "mime_type=\"video/mp4\"" in str(ytObjects[ytObjectVideoInt]):
                            ytVideoName = "videoToProcess.mp4"
                        elif "mime_type=\"video/webm\"" in str(ytObjects[ytObjectVideoInt]):
                            ytVideoName = "videoToProcess.webm"
                        resolutionI = 0
                        break
                except:
                    continue
            resolutionI -= 1

        bandwitchI = 1000
        while bandwitchI > 0:
            for ytObjectAudioInt in range(len(ytObjects)):
                try:
                    if ("abr=\""+str(bandwitchI)+"kbps\"" in str(ytObjects[ytObjectAudioInt])) and ("mime_type=\"audio/webm\"" in str(ytObjects[ytObjectAudioInt])):
                        print(ytObjects[ytObjectAudioInt])
                        ytObjects[ytObjectAudioInt].download(filename="audioToProcess")
                        ytAudioName = "audioToProcess.webm"
                        bandwitchI = 0
                        break
                except:
                    continue
            bandwitchI -= 1

        print(ytVideoName+" . "+ytAudioName)
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
