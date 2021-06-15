
import tkinter as tk, time, random
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

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

def quicksort(data, scores):
    if len(scores) <= 1:
        return scores
    else:
        pivot = int(scores.pop())

        items_higher = []
        items_lower = []

        for item in scores:
            if int(item) > pivot:
                items_higher.append(int(item))
            else:
                items_lower.append(int(item))
        

        return quicksort(data, items_lower) + [pivot] + quicksort(data, items_higher)

def solo10(data, scores):
    lista = quicksort(data, scores)
    length = len(lista)
    if length > 10:
        sobro = length - 10
        return lista[sobro:]
    else:
        return lista, length

def compare(data):
    ScoreFile = open("BEST SCORES.txt", "r") # genera la lista de datos leyendo cada palabra de cada línea
    lines = ScoreFile.readlines()
    for word in lines:
        data.append(word.strip("\n")) # se le quita el "cambio de línea" para hacer la lista
    return solo10(data, data[2::3])

def scores():
    mainWin.withdraw()
    scoresWin = tk.Toplevel()
    scoresWin.geometry("400x600")
    scoresWin.resizable(0,0)
    scoresWin.title("Records")
    scoresWin.config(bg="black")
    lenScores = compare([])[1]
    
    if lenScores >= 1:
        lblScore1 = tk.Label(scoresWin, text = "Puntaje #1: " + str(compare([])[0][-1:][0]))
        lblScore1.place(x = 160, y = 50)
    if lenScores >= 2:
        lblScore2 = tk.Label(scoresWin, text = "Puntaje #2: " + str(compare([])[0][-2:][0]))
        lblScore2.place(x = 160, y = 100)
    if lenScores >= 3:
        lblScore3 = tk.Label(scoresWin, text = "Puntaje #3: " + str(compare([])[0][-3:][0]))
        lblScore3.place(x = 160, y = 150)
    if lenScores >= 4:
        lblScore4 = tk.Label(scoresWin, text = "Puntaje #4: " + str(compare([])[0][-4:][0]))
        lblScore4.place(x = 160, y = 200)
    if lenScores >= 5:
        lblScore5 = tk.Label(scoresWin, text = "Puntaje #5: " + str(compare([])[0][-5:][0]))
        lblScore5.place(x = 160, y = 250)
    if lenScores >= 6:
        lblScore6 = tk.Label(scoresWin, text = "Puntaje #6: " + str(compare([])[0][-6:][0]))
        lblScore6.place(x = 160, y = 300)
    if lenScores >= 7:
        lblScore7 = tk.Label(scoresWin, text = "Puntaje #7: " + str(compare([])[0][-7:][0]))
        lblScore7.place(x = 160, y = 350)
    if lenScores >= 8:
        lblScore8 = tk.Label(scoresWin, text = "Puntaje #8: " + str(compare([])[0][-8:][0]))
        lblScore8.place(x = 160, y = 400)
    if lenScores >= 9:
        lblScore9 = tk.Label(scoresWin, text = "Puntaje #9: " + str(compare([])[0][-9:][0]))
        lblScore9.place(x = 160, y = 450)
    if lenScores >= 10:
        lblScore10 = tk.Label(scoresWin, text = "Puntaje #10: " + str(compare([])[0][-10:][0]))
        lblScore10.place(x = 160, y = 500)

    btnBack = tk.Button(scoresWin, command = lambda: (mainWin.deiconify(), scoresWin.destroy()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.place(x=170, y=560)

class Player:
    def __init__(self, canvas, window, life, lblLife, score, lblScore, tiempo, lblTime):
        self.canvas = canvas
        self.window = window
        
        self.life = life
        self.lblLife = lblLife
        
        self.score = score
        self.lblScore = lblScore
        
        self.tiempo = tiempo
        self.lblTime = lblTime
        
        self.img = tk.PhotoImage(file = "player.png").subsample(1,1)
        self.image = canvas.create_image(100, 100, image = self.img)

    def set_lblLife(self):
        self.life -= 1
        self.lblLife['text'] = f"VIDA: {self.life}"
        
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

    def coords_get(self):
        self.coords = self.canvas.bbox(self.image)
        self.px1 = self.coords[0]
        self.py1 = self.coords[1]
        self.px2 = self.coords[2]
        self.py2 = self.coords[3]
        return [self.px1, self.py1, self.px2, self.py2]
    
    def updateScore(self):
        while self.tiempo < 60 and self.life > 0:

            if optLevel.get() == "Nivel 1":
                self.score += 1
            if optLevel.get() == "Nivel 2":
                self.score += 3
            if optLevel.get() == "Nivel 3":
                self.score += 5
                
            self.lblScore['text'] = f"PUNTAJE: {self.score}"
            
            self.tiempo += 1
            self.lblTime['text'] = f"TIEMPO: {self.tiempo}"
            time.sleep(1)
            
        if self.tiempo >= 60:
            lblWon = tk.Label(self.canvas, text = "¡FELICIDADES! Has ganado el nivel").place(x = 250, y = 250)
        else:
            lblLost = tk.Label(self.canvas, text = "GAME OVER...").place(x = 250, y = 250)
            
        print(self.score)   
        self.bestScores()

    def bestScores(self):
        ScoreFile = open("BEST SCORES.txt", "a")
        ScoreFile.write(str(txtName.get()) + "\n")
        ScoreFile.write(str(optLevel.get()) + "\n")
        ScoreFile.write(str(self.score) + "\n")
        ScoreFile.close()
        
        """data = []
        ScoreFile = open("BEST SCORES.txt", "r") # genera la lista de datos leyendo cada palabra de cada línea
        lines = ScoreFile.readlines()
        for word in lines:
            data.append(word.strip("\n")) # se le quita el "cambio de línea" para hacer la lista
        print(solo10(data, data[2::3]))"""
            
class Ball:
    def __init__(self, canvas, level):
        self.existencia = True
        self.canvas = canvas
        self.level = level
        self.img = tk.PhotoImage(file = "player.png").subsample(2,2)
        spawnPoint = random.randint(1,4)
                
        # los proyectiles se moverán más rápido al avanzar de nivel
        if self.level == 1:
            self.speedX = random.randint(5, 10)
            self.speedY = random.randint(5,10)
        elif self.level == 2:
            self.speedX = random.randint(10, 15)
            self.speedY = random.randint(10,15)
        elif self.level == 3:
            self.speedX = random.randint(15, 20)
            self.speedY = random.randint(15,20)
        if spawnPoint == 1: # aparece arriba
            self.image = self.canvas.create_image(400, 0, image = self.img)
            self.coords = self.canvas.bbox(self.image)
            self.falling = True
            if self.speedX > 0:
                self.forward = True
            else: 
                self.forward = False
        if spawnPoint == 2: # aparece a la derecha
            self.image = self.canvas.create_image(800, 400, image = self.img)
            self.forward = False
            if self.speedY < 0:
                self.falling = True
            else:
                self.falling = False
        if spawnPoint == 3: # aparece abajo
            self.image = self.canvas.create_image(400, 800, image = self.img)
            self.falling = False
            if self.speedX > 0:
                self.forward = True
            else:
                self.forward = False
        if spawnPoint == 4: # aparece a la izquierda
            self.image = self.canvas.create_image(0, 400, image = self.img)
            self.forward = True
            if self.speedY > 0:
                self.falling = True
            else:
                self.falling = False
        
        self.bounce = 0 # rebotes
 
    def moveBall(self):
        while self.bounce < 3 and self.existencia:
            self.coords = self.canvas.bbox(self.image)
            self.x1 = self.coords[0]
            self.y1 = self.coords[1]
            self.x2 = self.coords[2]
            self.y2 = self.coords[3]

            if self.falling and self.forward: # Movimiento 1: derecha y abajo
                if self.x2 < 800:
                    self.canvas.move(self.image, self.speedX, 0)
                if self.y2 < 700:
                    self.canvas.move(self.image, 0, self.speedY)
                if self.x2 >= 800:
                    self.forward = False
                    self.bounce = self.bounce + 1
                if self.y2 >= 700:
                    self.falling = False
                    self.bounce = self.bounce + 1
            if self.falling and not self.forward: # Movimiento 2: izquierda y abajo
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y2 < 700:
                    self.canvas.move(self.image, 0, self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                    self.bounce = self.bounce + 1
                if self.y2 >= 700:
                    self.falling = False
                    self.bounce = self.bounce + 1
            if not self.falling and self.forward: # Movimiento 3: derecha y arriba
                if self.x2 < 800:
                    self.canvas.move(self.image, self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x2 >= 800:
                    self.forward = False
                    self.bounce = self.bounce + 1
                if self.y1 <= 0:
                    self.falling = True
                    self.bounce = self.bounce + 1
            if not self.falling and not self.forward: # Movimiento 4: izquierda y arriba
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                    self.bounce = self.bounce + 1
                if self.y1 <= 0:
                    self.falling = True
                    self.bounce = self.bounce + 1
            time.sleep(0.1)
            
        self.existencia = False
        self.canvas.delete(self.image)

    def impact(self): # evalúa colisiones
        global player
        while self.existencia and player.tiempo < 60 and player.life > 0:
            
            self.coords = self.canvas.bbox(self.image)
            self.bx1 = self.coords[0] 
            self.by1 = self.coords[1]
            self.bx2 = self.coords[2]
            self.by2 = self.coords[3]
            self.px1 = player.coords_get()[0]
            self.py1 = player.coords_get()[1]
            self.px2 = player.coords_get()[2]
            self.py2 = player.coords_get()[3]

            if self.px1<self.bx1<self.px2 and self.py1<self.by1<self.py2: # Choque 1: abajo derecha
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)                
                time.sleep(2)
                
            elif self.px1<self.bx2<self.px2 and self.py1<self.by1<self.py2: # Choque 2: abajo izquierda
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)                
                time.sleep(2)
                
            elif self.px1<self.bx1<self.px2 and self.py1<self.by2<self.py2: # Choque 3: arriba derecha
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)               
                time.sleep(2)
                
            elif self.px1<self.bx2<self.px2 and self.py1<self.by2<self.py2: # Choque 4: arriba izquierda
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)
                time.sleep(2)
                
        self.existencia = False        
        self.canvas.delete(self.image)
     
def ballSet(canvas, level):
    global player
    x = 0
    while x < 60:
        ball = Ball(canvas, level) # crea las instancias de proyectil (bola)       
        ballThread = Thread(target = ball.moveBall) # thread para el movimiento de cada bola
        ballThread.daemon = True
        ballThread.start()      

        ballThread1 = Thread(target = ball.impact) # thread para evaluar colisiones
        ballThread1.daemon = True
        ballThread1.start()

        x += 1
        
        # los proyectiles aparecerán más rápido en los niveles siguientes
        if level == 1:
            time.sleep(5)
        elif level == 2:
            time.sleep(3)
        elif level == 3:
            time.sleep(1)
        
def play():
    
    mainWin.withdraw()

    gameWin = tk.Toplevel(mainWin)
    gameWin.geometry("800x800")
    gameWin.resizable(0,0)
    gameWin.title("GAME!")
    gameWin.config(bg="black")
    cnvs = tk.Canvas(gameWin,width=800, height= 700, borderwidth=0, highlightthickness=0, bg= "green")
    cnvs.place(x= 0, y= 0)
    btnBack = tk.Button(gameWin, command = lambda: (mainWin.deiconify(), gameWin.withdraw()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.place(x = 600, y = 700)

    global player
    
    playerLife = 3
    lblLife = tk.Label(gameWin, text = "VIDA: " + str(playerLife))
    lblLife.place(x = 50, y = 700)

    playerScore = 0
    lblScore = tk.Label(gameWin, text = "PUNTAJE: " + str(playerScore))
    lblScore.place(x = 150, y = 700)

    tiempo = 0
    lblTime = tk.Label(gameWin, text = "TIEMPO: " + str(tiempo))
    lblTime.place(x = 250, y = 700)

    lblName = tk.Label(gameWin, text = "JUGADOR: " + str(txtName.get()))
    lblName.place(x = 450, y = 700)

    player = Player(cnvs, gameWin, playerLife, lblLife, playerScore, lblScore, tiempo, lblTime)
    player.coords_get()

    def threadBall():
        if optLevel.get() == "Nivel 1":
            lvl = 1
        elif optLevel.get() == "Nivel 2":
            lvl = 2
        elif optLevel.get() == "Nivel 3":
            lvl = 3
        ballThread = Thread(target = ballSet, args = [cnvs, lvl]) # crea un thread en el main
        ballThread.daemon = True
        ballThread.start()

    def threadScores():
        scoresThread = Thread(target = player.updateScore)
        scoresThread.daemon = True
        scoresThread.start()

    gameWin.bind('<Right>', player.moveRight)
    gameWin.bind('<Left>', player.moveLeft)
    gameWin.bind('<Up>', player.moveUp)
    gameWin.bind('<Down>',player.moveDown)

    threadScores()
    threadBall()

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
