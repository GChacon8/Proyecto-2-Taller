import tkinter as tk, time, random, pygame, PIL.Image, PIL.ImageTk
from PIL import ImageTk, Image
from threading import Thread
from tkinter import *
from tkinter import ttk

pygame.mixer.init()  

"""class Nave():
    def __init__(self, vel, vida):
        self.vel = vel
        self.vida = vida
    def draw(self):#Lo que sea
        self.naveImg = tk.PhotoImage(file = "Nave.png").subsample(1, 1) 
        self.canvas.create_image(200, 450, image = self.naveImg)"""

"""class Proyectil():
    def __init__(self, harm, vel):
        self.harm = harm
        self.vel = vel
    def impact(self):"""
        
# objetos: juego, nave, proyectiles 
def about():
    mainWin.withdraw()
    aboutWin = tk.Tk()
    aboutWin.geometry("600x700")
    aboutWin.resizable(0,0)
    aboutWin.title("About")
    aboutWin.config(bg = "black")
    goBack = tk.Button(aboutWin, command = lambda: (mainWin.deiconify(), aboutWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    goBack.pack(padx = 10, pady = 50)
    pais = tk.Label(aboutWin,text = "Costa Rica", font = ("Times", 15), bg = "green", fg = "white")
    pais.pack(padx = 20, pady = 10)
    univ = tk.Label(aboutWin,text = "Instituto Tecnológico de Costa Rica", font = ("Times", 15), bg = "green", fg = "white")
    univ.pack(padx = 20, pady = 10)
    carrera = tk.Label(aboutWin,text = "Ingeniería en Computadores", font = ("Times", 15), bg = "green", fg = "white")
    carrera.pack(padx = 20, pady = 10)
    curso = tk.Label(aboutWin,text = "CE 1102 Taller de Programación", font = ("Times", 15), bg = "green", fg = "white")
    curso.pack(padx = 20, pady = 10)
    grupo = tk.Label(aboutWin,text = "Grupo 01 | I sem. 2021", font = ("Times", 15), bg = "green", fg = "white")
    grupo.pack(padx = 20, pady = 10)
    profe = tk.Label(aboutWin,text = "Prof. Jeff Schmidt Peralta", font = ("Times", 15), bg = "green", fg = "white")
    profe.pack(padx = 20, pady = 10)
    version = tk.Label(aboutWin,text = "Versión oficial/final\nVersión de Python: 3.8.10", font = ("Times", 15), bg = "green", fg = "white")
    version.pack(padx = 20, pady = 10)
    autor = tk.Label(aboutWin,text = "Autores: Jimena León Huertas | 2021016748 y Gabriel Chacón | 2021049454", font = ("Times", 15), bg = "green", fg = "white")
    autor.pack(padx = 20, pady = 10)
    autor2 = tk.Label(aboutWin,text = "Autores Módulos: Fredrik Lundh, Andrew Danner\nToby Dickenson, Guido van Rossum, Víctor Castrillo, entre otros", font = ("Times", 13), bg = "green", fg = "white")
    autor2.pack(padx = 20, pady = 10)
    instruc = tk.Label(aboutWin,text = "Instrucciones: utilice las teclas asdw para mover el cohete y\nespacio para lanzar proyectiles", font = ("Times", 13), bg = "green", fg = "white")
    instruc.pack(padx = 20, pady = 10)
    nota = tk.Label(aboutWin, text = "NOTA: ver documentación para más referencias", font = ("Times", 11), bg = "green", fg = "white")
    nota.place(x = 10, y = 600)

def game():
    pygame.mixer.stop() 
    mainWin.withdraw()
    gameWin = tk.Toplevel(mainWin)
    gameWin.geometry("400x600")
    gameWin.resizable(0,0)
    gameWin.title("GAME!")
    gameWin.config(bg="black")
    goBack = tk.Button(gameWin, command = lambda: (mainWin.deiconify(), gameWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    goBack.pack(padx = 10, pady = 50)
    cnv = tk.Canvas(gameWin,width=500, height= 40, borderwidth=0, highlightthickness=0, bg= "blue")
    cnv.place(x= 0, y= 0)
    if option.get() == 1:
        pygame.mixer.music.load("game.wav")
        pygame.mixer.music.play(loops = 0)
        mainWin.after(1000, pygame.mixer.stop())
    #nave1 = Nave()
    #nave1.draw()

def scores():
    mainWin.withdraw()
    scoresWin = tk.Toplevel()
    scoresWin.geometry("400x600")
    scoresWin.resizable(0,0)
    scoresWin.title("Records")
    scoresWin.config(bg="black")
    goBack = tk.Button(scoresWin, command = lambda: (mainWin.deiconify(), scoresWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    goBack.pack(padx = 10, pady = 50)

    

mainWin = tk.Tk()
mainWin.geometry("400x600")
mainWin.resizable(0,0)
mainWin.title("Star muars")
mainWin.config(bg="#041637")    

txtName = tk.Entry(mainWin)
txtName.place(x=150, y= 60)

lblName = tk.Label(mainWin, text="Nombre:", bg = "#424949")
lblName.place(x= 70, y=60)

levelValue = StringVar(mainWin)
levels = ['Nivel 1','Nivel 2','Nivel 3']
levelValue.set('1')

optLevel = ttk.Combobox(mainWin, values = levels, state = 'readonly')
optLevel.current(0)
optLevel.place(x=130, y = 120)

lblLevel = tk.Label(mainWin,text="Nivel:", bg = "#424949")
lblLevel.place(x= 70, y=120)

global option
option = IntVar()
#option.set(1)

def mainMusOn(option):
    if option == 1:        
        pygame.mixer.music.load("game.wav")
        pygame.mixer.music.play(loops = 0)
        mainWin.after(100, lambda: pygame.mixer.stop())

def mainMusOff(option):
    mainWin.update_idletasks()
    if option == 0:
        pygame.mixer.stop()

musicOn = tk.Radiobutton(mainWin, text = "MUSIC ON", value = 1, variable = option, command = mainMusOn(option.get())).place(x= 50, y= 550)
musicOff = tk.Radiobutton(mainWin, text = "MUSIC OFF", value = 0, variable = option, command = mainMusOff(option.get())).place(x= 150, y= 550)

btnPlay= tk.Button(mainWin, text = "Jugar", width = "20", height = "3", bg= "#86FF45", command = game)
btnPlay.place(x=130, y=210)

btnRecords= tk.Button(mainWin, text = "Mejores Puntajes", width = "20", height = "3", bg= "#86FF45", command = scores)
btnRecords.place(x=130, y=330)

btnAbout= tk.Button(mainWin, text = "About", width = "20", height = "3", bg= "#86FF45", command = about)
btnAbout.place(x=130, y=450)

mainWin.mainloop()