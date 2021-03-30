import os
from time import sleep
from datetime import datetime as dt
import pyautogui as gui

os.system("color 2f")
os.system("mode 40,25")

now = dt.now()
date = str(now.strftime("%d")) + str(now.strftime("%m"))
formattedDate = now.strftime("%b") + now.strftime("%d")
folder = "./" + formattedDate


filePaths = {
    "Ahmet " : "./files/ahmet.png",
    "Arda " : "./files/arda.png",
    "Öykü " : "./files/oyku.png",
    "Bersu " : "./files/bersu.png",
    "Beyza " : "./files/beyza.png",
    "Canan " : "./files/canan.png",
    "Duru " : "./files/duru.png",
    "Eda " :  "./files/eda.png",
    "Efe " : "./files/efe.png",
    "Efekan " : "./files/efekan.png",
    "Elif " : "./files/elif.png",
    "Cavit " : "./files/cavit.png",
    "Feyza " : "./files/feyza.png",
    "Haktan " : "./files/haktan.png",
    "Selam şef!" : "./files/sef.png",
    "Mahmut " : "./files/mahmut.png",
    "Mehmet " : "./files/mehmet.png",
    "Münevver " : "./files/munevver.png",
    "Gülsu " : "./files/gulsu.png",
    "Rüya " : "./files/ruya.png",
    "Samet " : "./files/samet.png",
    "Ülkü " : "./files/ulku.png",
    "Yalın " : "./files/yalin.png",
    "Yiğit " : "./files/yigit.png",
    "Demiryapan " : "./files/demiryapan.png",
    "Sert " : "./files/sert.png",
    "Yusuf " : "./files/yusuf.png",
    "Eylül " : "./files/eylul.png",
    "Sare " : "./files/sare.png",
    "Zeynep T " : "./files/zeynep.png",
}

notInClass = list(filePaths.keys())
confirm = False
skipOutput = False

def setup():
    global outputPath
    global confirm
    global skipOutput
    if os.path.exists(folder) != True:
        os.mkdir(folder)
    className = gui.prompt(text="Ders Adı", title="Otonom Yoklama Alıcı v1")
    if className == None:
        confirm = True 
        skipOutput = True
        pass
    else:
        outputPath = folder + "/" + className + date + ".txt"

def nameDetection():
    global notInClass
    copy = notInClass.copy()
    for person in copy:
        print(person, end=" ")
        personPath = filePaths[person]
        position = gui.locateOnScreen(personPath, grayscale=True)
        gui.moveTo(position)
        if position != None:
            notInClass.remove(person)
        else:
            print("YOK", end="")
        notInClass = notInClass
        print()

def confirmation():
    global confirm
    answer = gui.confirm(text="Yoklamayı bu haliyle onaylıyor musun, şef?", title='Otonom Yoklama Alıcı v1', buttons=['Tekrar Al', 'Onaylıyorum'])
    if answer == "Onaylıyorum":
        confirm = True
    elif answer == "Tekrar Al":
        confirm = False
        print("\nTekrar Alıyorum", end="")
        for i in range(3):
            print(".", end="")
        print("\n")

def output():
    if len(notInClass) != 0:
        with open(outputPath, "a") as outputFile:
            for person in notInClass:
                outputFile.write(person + "\n")
            outputFile.write("----\n")
    else:
        gui.alert(text="Yoklama Tam :)", title="Otonom Yoklama Alıcı v1", button="oley :)")

setup()
while confirm == False:
    nameDetection()
    print("~", len(notInClass))
    confirmation()
else:
    if skipOutput != True:
        output()
        print("Yoklamayı kaydettim şef, iyi günler!")
        sleep(10)
    else:
        exit()
