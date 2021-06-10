import tkinter as tk, time, random
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
    
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.img = tk.PhotoImage(file = "player.png").subsample(1,1)
        self.image = canvas.create_image(100, 100, image = self.img)
        
    def moveRight(self, event):
        self.coords = self.canvas.bbox(self.image)
        self.x2 = self.coords[2]
        if  self.x2 < 800:
            self.canvas.move(self.image, 10, 0)

    def moveLeft(self, event):
        self.coords = self.canvas.bbox(self.image)
        self.x1 = self.coords[0]
        if self.x1 > 0:
            self.canvas.move(self.image, -10, 0)

    def moveUp(self, event):
        self.coords = self.canvas.bbox(self.image)
        self.y1 = self.coords[1]
        if self.y1 > 0:
            self.canvas.move(self.image, 0, -10)

    def moveDown(self, event):
        self.coords = self.canvas.bbox(self.image)
        self.y2 = self.coords[3]
        if self.y2 < 700:
            self.canvas.move(self.image, 0, 10)
       
class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.img = tk.PhotoImage(file = "player.png").subsample(2,2)
        spawnPoint = random.randint(1,4)
        if spawnPoint == 1: # arriba
            self.image = self.canvas.create_image(400, 0, image = self.img)
            self.speedX = random.randint(5, 10)
            self.speedY = random.randint(5,10)
            self.coords = self.canvas.bbox(self.image)
            self.falling = True
            if self.speedX > 0:
                self.forward = True
            else: 
                self.forward = False
        if spawnPoint == 2: # derecha
            self.image = self.canvas.create_image(800, 400, image = self.img)
            self.speedX = random.randint(5, 10)
            self.speedY = random.randint(5, 10)
            self.forward = False
            if self.speedY < 0:
                self.falling = True
            else:
                self.falling = False
        if spawnPoint == 3: # abajo
            self.image = self.canvas.create_image(400, 800, image = self.img)
            self.speedX = random.randint(5, 10)
            self.speedY = random.randint(5,10)
            self.falling = False
            if self.speedX > 0:
                self.forward = True
            else:
                self.forward = False
        if spawnPoint == 4: # izquierda
            self.image = self.canvas.create_image(0, 400, image = self.img)
            self.speedX = random.randint(5, 10)
            self.speedY = random.randint(5, 10)
            self.forward = True
            if self.speedY > 0:
                self.falling = True
            else:
                self.falling = False

        self.bounce = 0

        
    def moveBall(self):
        while self.bounce < 3:
            self.coords = self.canvas.bbox(self.image)
            self.x1 = self.coords[0]
            self.y1 = self.coords[1]
            self.x2 = self.coords[2]
            self.y2 = self.coords[3]
            if self.falling and self.forward: # CASO 1: derecha y abajo
                if self.x2 < 800:
                    self.canvas.move(self.image, self.speedX, 0)
                if self.y2 < 700:
                    self.canvas.move(self.image, 0, self.speedY)
                if self.x2 >= 800:
                    self.forward = False
                if self.y2 >= 700:
                    self.falling = False
            if self.falling and not self.forward: # CASO 2: izquierda y abajo
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y2 < 700:
                    self.canvas.move(self.image, 0, self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                if self.y2 >= 700:
                    self.falling = False
            if not self.falling and self.forward: # CASO 3: derecha y arriba
                if self.x2 < 800:
                    self.canvas.move(self.image, self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x2 >= 800:
                    self.forward = False
                if self.y1 <= 0:
                    self.falling = True
            if not self.falling and not self.forward: # CASO 4: izquierda y arriba
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                if self.y1 <= 0:
                    self.falling = True
            time.sleep(0.1)                    
        self.canvas.delete(self.img)
           
def play():
    gameWin = tk.Toplevel(mainWin)
    gameWin.geometry("800x800")
    gameWin.resizable(0,0)
    gameWin.title("GAME!")
    gameWin.config(bg="black")
    btnBack = tk.Button(gameWin, command = lambda: (mainWin.deiconify(), gameWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.place(x= 40, y = 740)
    cnvs = tk.Canvas(gameWin,width=800, height= 700, borderwidth=0, highlightthickness=0, bg= "green")
    cnvs.place(x= 0, y= 0)

    player = Player(cnvs)
    ball = Ball(cnvs) 
    
    ballThread = Thread(target = ball.moveBall)
    ballThread.start()

    gameWin.bind('<Right>', player.moveRight)
    gameWin.bind('<Left>', player.moveLeft)
    gameWin.bind('<Up>', player.moveUp)
    gameWin.bind('<Down>',player.moveDown)

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

btnPlay= tk.Button(mainWin, text = "Jugar", width = "20", height = "3", bg= "#86FF45", command = play)
btnPlay.place(x=130, y=210)

btnRecords= tk.Button(mainWin, text = "Mejores Puntajes", width = "20", height = "3", bg= "#86FF45", command = scores)
btnRecords.place(x=130, y=330)

btnAbout= tk.Button(mainWin, text = "About", width = "20", height = "3", bg= "#86FF45", command = about)
btnAbout.place(x=130, y=450)

mainWin.mainloop()
