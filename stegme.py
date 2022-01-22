#   _______ _________ ______   _______    _______  ______
#  (  ____ \\__   __// ___  \ (  ____ \  (       )/ ___  \
#  | (    \/   ) (   \/   \  \| (    \/  | () () |\/   \  \
#  | (_____    | |      ___) /| |        | || || |   ___) /
#  (_____  )   | |     (___ ( | | ____   | |(_)| |  (___ (
#        ) |   | |         ) \| | \_  )  | |   | |      ) \
#  /\____) |   | |   /\___/  /| (___) |  | )   ( |/\___/  /
#  \_______)   )_(   \______/ (_______)  |/     \|\______/
#
#  Python 3
#  By Sh0vel4n6
#
# GUI - hide a file in an image
#
#
#
#
#
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from os import path
import os.path
import tkinter.font as tkFont

def creerFenetre(nomFenetre, titre):
    nomFenetre.title(titre)
    # centre la fenêtre horizontalement
    positionX = int(nomFenetre.winfo_screenwidth() / 2 - 300)
    # centre la fenêtre horizontalement
    positionY = int(nomFenetre.winfo_screenheight() / 2 - 250)
    nomFenetre.geometry("600x500")
    nomFenetre.geometry("+{}+{}".format(positionX, positionY))
    nomFenetre.configure(background='white')

def getsourcefile():
  #  folder_selected = filedialog.askdirectory()
    sourcefilepath.set(filedialog.askopenfilename())

def getimgpath():
    imgfilepath.set(filedialog.askopenfilename())

def getdirpath():
    destdirpath.set(filedialog.askdirectory())

def hide():
    testfile = sourcefilepath.get()
    testimg = imgfilepath.get()
    testdir = destdirpath.get()

    if testfile == '' or testdir == '' or testimg == "":
        print("missingfile")
    else:
        zip_dir = os.path.dirname(testfile)
        filename = os.path.basename(testfile)
        shutil.make_archive(zip_dir + "/archive", "zip", zip_dir, filename)

        destimgname = testdir + "/img_001.jpg"
        sourcezip = zip_dir + "/archive.zip"
        cmd = 'copy /b "'+testimg+'" + "'+sourcezip+'" "'+destimgname+'"'
        print(cmd)

        os.system(cmd)
        os.remove(sourcezip)
        fenetre1.destroy()



fenetre1 = Tk()
creerFenetre(fenetre1, "St3g M3")


sourcefilepath = StringVar()
imgfilepath = StringVar()
destdirpath = StringVar()

label_sourcepath = Label(fenetre1, text="Choisir le fichier à cacher")
label_sourcepath.configure(background ='white')
label_sourcepath['font']=tkFont.Font(family='Arial', size = 12)
label_sourcepath.pack(pady=20)
sourcefilepath.set("")

entree_src = Entry(fenetre1, textvariable=sourcefilepath, width=65).pack()
btn_chooseSource = Button(fenetre1, text="Choisir", command=getsourcefile, width=25).pack(pady=8)

label_imgpath = Label(fenetre1, text="Choisir l'image à montrer")
label_imgpath.configure(backgroun='white')
label_imgpath['font']=tkFont.Font(family='Arial', size = 12)
label_imgpath.pack(pady=20)
imgfilepath.set('')

entree_img = Entry(fenetre1, textvariable=imgfilepath, width=65).pack()
btn_chooseimg = Button(fenetre1, text="Choisir", command=getimgpath, width=25).pack(pady=8)

label_dirpath = Label(fenetre1, text="Choisir le dossier de destination")
label_dirpath.configure(backgroun='white')
label_dirpath['font']=tkFont.Font(family='Arial', size = 12)
label_dirpath.pack(pady=20)
destdirpath.set('')

entree_dir = Entry(fenetre1, textvariable=destdirpath, width=65).pack()
btn_choosedir = Button(fenetre1, text="Choisir", command=getdirpath, width=25).pack(pady=8)

btn_hide = Button(fenetre1, text="CACHE MOI", command=hide, width=25).pack(pady=15)

fenetre1.mainloop()
