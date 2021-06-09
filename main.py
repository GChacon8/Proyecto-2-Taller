import tkinter as tk, time, random, pygame
from threading import Thread
from tkinter import *
from tkinter import ttk

def about():
    mainWin.withdraw()
    aboutWin = tk.Tk()
    aboutWin.geometry("600x700")
    aboutWin.resizable(0,0)
    aboutWin.title("About")
    aboutWin.config(bg = "black")
    btnBack = tk.Button(aboutWin, command = lambda: (mainWin.deiconify(), aboutWin.destroy()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.pack(padx = 10, pady = 50)
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

def scores():
    mainWin.withdraw()
    scoresWin = tk.Toplevel()
    scoresWin.geometry("400x600")
    scoresWin.resizable(0,0)
    scoresWin.title("Records")
    scoresWin.config(bg="black")
    btnBack = tk.Button(scoresWin, command = lambda: (mainWin.deiconify(), scoresWin.destroy()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.pack(padx = 10, pady = 50)

#Clase: Juego
#Atributos: Nivel
class Game():
    def __init__(self, nivel):
        self.nivel = nivel
    
    def startGame(self):
        gameWin = tk.Toplevel(mainWin)
        gameWin.geometry("800x800")
        gameWin.resizable(0,0)
        gameWin.title("GAME!")
        gameWin.config(bg="black")
        btnBack = tk.Button(gameWin, command = lambda: (mainWin.deiconify(), gameWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
        btnBack.place(x= 40, y = 740)
        cnvs = tk.Canvas(gameWin,width=800, height= 700, borderwidth=0, highlightthickness=0, bg= "green")
        cnvs.place(x= 0, y= 0)
        playerPhoto = tk.PhotoImage(file ="player.png")
        playerImage = cnvs.create_image(350,350,image = playerPhoto)
        def moveRight(event):
            if cnvs.bbox(playerImage)[2]<800:
                cnvs.move(playerImage, 10, 0)
        def moveLeft(event):
             if cnvs.bbox(playerImage)[0]>0:
                cnvs.move(playerImage, -10, 0)
        def moveUp(event):
             if cnvs.bbox(playerImage)[1]>0:
                cnvs.move(playerImage, 0, -10)
        def moveDown(event):
             if cnvs.bbox(playerImage)[3]<700:
                cnvs.move(playerImage, 0, 10)
        if optLevel.get() == "Nivel 1":
            print("a")
        if optLevel.get() == "Nivel 2":
            print("a")
        if optLevel.get() == "Nivel 3":
            print("a")
        gameWin.bind('<Right>', moveRight)
        gameWin.bind('<Left>', moveLeft)
        gameWin.bind('<Up>', moveUp)
        gameWin.bind('<Down>', moveDown)
        gameWin.mainloop()


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

game = Game(levelValue.get())

btnPlay= tk.Button(mainWin, text = "Jugar", width = "20", height = "3", bg= "#86FF45", command = game.startGame)
btnPlay.place(x=130, y=210)

btnRecords= tk.Button(mainWin, text = "Mejores Puntajes", width = "20", height = "3", bg= "#86FF45", command = scores)
btnRecords.place(x=130, y=330)

btnAbout= tk.Button(mainWin, text = "About", width = "20", height = "3", bg= "#86FF45", command = about)
btnAbout.place(x=130, y=450)

mainWin.mainloop()