""" SEGUNDO PROYECTO | CE 1102 TALLER DE PROGRAMACIÓN | I sem. 2021 | I.T.C.R.
Realizado por: Gabriel Chacón Alfaro y Jimena Léon Huertas """

import tkinter as tk, time, random, winsound, pygame
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

#Funcion donde se crea la ventana de "about"
def about():
    #Creacion de ventana
    mainWin.withdraw()
    aboutWin = tk.Toplevel(mainWin)
    aboutWin.geometry("800x700")
    aboutWin.resizable(0,0)
    aboutWin.title("About")
    
    #Creacion de canvas
    cnvsData = tk.Canvas(aboutWin, width=800, height= 750)
    cnvsData.place(x = 0, y = 0)

    #Imagen de fondo
    Backimg = tk.PhotoImage(file = "about.png").subsample(1, 1)
    Backimage = cnvsData.create_image(0, 0, image = Backimg)
    
    #Boton de volver
    btnBack = tk.Button(aboutWin, command = lambda: (mainWin.deiconify(), aboutWin.destroy()), text = "VOLVER", font = "ErasITC 15 bold italic", bg = "black", fg = "white")
    btnBack.place(x = 50, y = 650)
    
    #Datos solicitados en las especificaciones
    pais = tk.Label(aboutWin,text = "Costa Rica", font = "ErasITC 13 bold italic", bg = "#e75719", fg = "white")  
    pais.pack(padx = 20, pady = 20)
    univ = tk.Label(aboutWin,text = "Instituto Tecnológico de Costa Rica", font = "ErasITC 12 bold italic", bg = "#e75719", fg = "white")
    univ.pack(padx = 20, pady = 20)
    carrera = tk.Label(aboutWin,text = "Ingeniería en Computadores", font = "ErasITC 12 bold italic", bg = "#e75719", fg = "white")
    carrera.pack(padx = 20, pady = 20)
    curso = tk.Label(aboutWin,text = "CE 1102 Taller de Programación", font = "ErasITC 12 bold italic", bg = "#e75719", fg = "white")
    curso.pack(padx = 20, pady = 20)
    grupo = tk.Label(aboutWin,text = "Grupo 01 | I sem. 2021", font = "ErasITC 12 bold italic", bg = "#e75719", fg = "white")
    grupo.pack(padx = 20, pady = 20)
    profe = tk.Label(aboutWin,text = "Prof. Jeff Schmidt Peralta", font = "ErasITC 12 bold italic", bg = "#e75719", fg = "white")
    profe.pack(padx = 20, pady = 20)
    version = tk.Label(aboutWin,text = "Versión final\nVersión de Python: 3.8/3.9", font = "ErasITC 10 bold italic", bg = "#e75719", fg = "white")
    version.pack(padx = 20, pady = 20)
    autor = tk.Label(aboutWin,text = "Autores: Jimena León Huertas | 2021016748 y Gabriel Chacón | 2021049454", font = "ErasITC 13 bold italic", bg = "#e75719", fg = "white")
    autor.pack(padx = 20, pady = 20)
    autor2 = tk.Label(aboutWin,text = "Autores Módulos: Fredrik Lundh, Andrew Danner\nToby Dickenson, Guido van Rossum, Víctor Castrillo, entre otros", font = "ErasITC 10 bold italic", bg = "#e75719", fg = "white")
    autor2.pack(padx = 20, pady = 20)
    instruc = tk.Label(aboutWin,text = "Utilice las flechas del teclado para mover el personaje", font = "ErasITC 13 bold italic", bg = "#e75719", fg = "white")
    instruc.pack(padx = 20, pady = 20)
    
    aboutWin.mainloop()

#Funcion con algoritmo de ordenamiento de la lista de puntajes
#E: Lista de puntajes
#S: Lista de puntajes ordenada de forma ascendente
#R: Lista no vacia
"""Ver la referencia en la documentacion"""
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

#Funcion para acotar la lista de puntajes a solamente los 10 mejores
#E: Lista de puntajes
#S: Lista de los 10 mejores puntajes ordenados de forma ascendente y el largo de la lista
def solo10(data, scores):
    lista = quicksort(data, scores)
    length = len(lista)
    if length > 10:
        sobro = length - 10
        return lista[sobro:] , length
    else:
        return lista, length

#Funcion para leer el archivo .txt y generar una lista, sino existe el .txt muestra un label indicandole
#E: Lista vacia y la ventana correspondiente
#S: Lista de los 10 mejores puntajes ordenados de forma ascendente y el largo de la lista
#R: Debe haber un archivo txt creado
def compare(data, win):
    try:
        ScoreFile = open("BEST SCORES.txt", "r") # genera la lista de datos leyendo cada palabra de cada línea
        lines = ScoreFile.readlines()
        for word in lines:
            data.append(word.strip("\n")) # se le quita el "cambio de línea" para hacer la lista
        return solo10(data, data[2::3])
    
    except: # no hay archivo creado
        lblNoScores = tk.Label(win, text = "No hay puntajes aún.\n¡Juega para ser el primero!", font = "Consolas 16 bold", bg = "#594c39", fg = "white")
        lblNoScores.place(x = 30, y = 160)
        return (["No hay puntajes"], 0)

#Funcion donde se crea la ventana de los mejores puntajes
def scores():
    #Creacion de la ventana
    mainWin.withdraw()
    scoresWin = tk.Toplevel()
    scoresWin.geometry("400x600")
    scoresWin.resizable(0,0)
    scoresWin.title("Records")
    
    #Creacion del canvas
    cnvsScores = tk.Canvas(scoresWin, width=400, height= 600, bg= "#e75719")           
    cnvsScores.place(x = 0, y = 0)

    #Imagen de fondo
    Scoresimg = tk.PhotoImage(file = "play.png").subsample(1, 1)
    Backimage = cnvsScores.create_image(200, 300, image = Scoresimg)
    
    #Boton de volver
    btnBack = tk.Button(scoresWin, command = lambda: (mainWin.deiconify(), scoresWin.destroy()), text = "Volver", font = ("Fixedsys", 15), bg = "black", fg = "white")
    btnBack.place(x=30, y=560)

    #Asignacion para no llamar varias veces a la funcion
    scores = compare([], scoresWin)
    lenScores = scores[1]
    
    #Labels para mostrar mejores puntajes
    if lenScores >= 1:
        lblScore1 = tk.Label(scoresWin, text = "1er lugar: " + str(scores[0][-1:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore1.pack(padx = 10, pady = 5)
    if lenScores >= 2:
        lblScore2 = tk.Label(scoresWin, text = "2do lugar: " + str(scores[0][-2:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore2.pack(padx = 10, pady = 5)
    if lenScores >= 3:
        lblScore3 = tk.Label(scoresWin, text = "3er lugar: " + str(scores[0][-3:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore3.pack(padx = 10, pady = 5)
    if lenScores >= 4:
        lblScore4 = tk.Label(scoresWin, text = "4to lugar: " + str(scores[0][-4:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore4.pack(padx = 10, pady = 5)
    if lenScores >= 5:
        lblScore5 = tk.Label(scoresWin, text = "5to lugar: " + str(scores[0][-5:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore5.pack(padx = 10, pady = 5)
    if lenScores >= 6:
        lblScore6 = tk.Label(scoresWin, text = "6to lugar: " + str(scores[0][-6:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore6.pack(padx = 10, pady = 5)
    if lenScores >= 7:
        lblScore7 = tk.Label(scoresWin, text = "7mo lugar: " + str(scores[0][-7:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore7.pack(padx = 10, pady = 5)
    if lenScores >= 8:
        lblScore8 = tk.Label(scoresWin, text = "8vo lugar: " + str(scores[0][-8:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore8.pack(padx = 10, pady = 5)
    if lenScores >= 9:
        lblScore9 = tk.Label(scoresWin, text = "9no lugar: " + str(scores[0][-9:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore9.pack(padx = 10, pady = 5)
    if lenScores >= 10:
        lblScore10 = tk.Label(scoresWin, text = "10mo lugar: " + str(scores[0][-10:][0]), font = "Fixedsys 17 bold", fg = "white", bg = "#594c39")
        lblScore10.pack(padx = 10, pady = 5)

    scoresWin.mainloop()

"""Clase: Player
Atributos: Canvas, Window, life, score, lblScore, tiempo y lblTime
Metodos: 
set_lblLife: Le baja un punto de vida al player y actualiza el label
killPlayer: Le baja la vida al jugador hasta 0
moveRight: Recibe el evento de la respectiva flecha para mover la imagen hacia la direccion correspondiente
moveLeft:Recibe el evento de la respectiva flecha para mover la imagen hacia la direccion correspondiente
moveUp: Recibe el evento de la respectiva flecha para mover la imagen hacia la direccion correspondiente
moveDown: Recibe el evento de la respectiva flecha para mover la imagen hacia la direccion correspondiente
coords_get: Saca las coordenas de el player y retorna la lista con las 2 coordenas de X y las 2 coordenadas de Y
updateScore: Actualiza el puntaje obtenido con su respetivo label y muestra un label si se supero a alguno de los mejores puntajes"""
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
        
        self.img = tk.PhotoImage(file = "player.png").subsample(9,9)
        self.image = canvas.create_image(400, 400, image = self.img)

    def set_lblLife(self):
        self.life -= 1
        self.lblLife['text'] = f"VIDA: {self.life}"
    
    def killPlayer(self):
        self.life = 0
        
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
            lblWon = tk.Label(self.canvas, text = "¡FELICIDADES! GANASTE EL NIVEL", font = "Fixedsys 18 bold italic").place(x = 250, y = 100)
        else:
            lblLost = tk.Label(self.canvas, text = "GAME OVER...", font = "Fixedsys 20 bold italic").place(x = 250, y = 100)
            
        ScoreFile = open("BEST SCORES.txt", "a")
        ScoreFile.write(str(txtName.get()) + "\n")
        ScoreFile.write(str(optLevel.get()) + "\n")
        ScoreFile.write(str(self.score) + "\n")
        ScoreFile.close()

        scores = compare([], self.canvas)
        lenScores = scores[1]
        
        #Casos para saber si se supero alguno de los mejores puntajes
        if self.score > int(scores[0][-1:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al primer lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 16 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-2:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al segundo lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-3:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al tercer lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-4:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al cuarto lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-5:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al quinto lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-6:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al sexto lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-7:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al séptimo lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-8:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al octavo lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-9:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al noveno lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
        elif self.score > int(scores[0][-10:][0]):
            lblScore = tk.Label(self.canvas, text = "¡Superaste al décimo lugar!\nTu puntaje es: " + str(self.score), font = "Fixedsys 20 bold", bg = "#7474a9", fg = "white")
            lblScore.place(x = 100, y = 200)
            
pygame.mixer.init()
ballSound = pygame.mixer.Sound("dodgeball.wav")

"""Clase: Ball
Atributos: canvas, level, existencia, img, speedX, speedY, imgage y coords
Metodos:
moveBall: En este metodo se programo la logica del movimiento de las bolitas, ademas sirvio para contar los rebotes y poner el sonido de rebote
impact: En este metodo se programo la logica para saber si una bolita chocaba con el player, ademas destruia la bolita si era el caso
"""
class Ball:
    def __init__(self, canvas, level):
        self.existencia = True
        self.canvas = canvas
        self.level = level
        self.img = tk.PhotoImage(file = "ball.png").subsample(5,5)
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
        global player
        while self.bounce < 3 and self.existencia and player.life>0:
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
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

                if self.y2 >= 700:
                    self.falling = False
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)                      

            if self.falling and not self.forward: # Movimiento 2: izquierda y abajo
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y2 < 700:
                    self.canvas.move(self.image, 0, self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

                if self.y2 >= 700:
                    self.falling = False
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

            if not self.falling and self.forward: # Movimiento 3: derecha y arriba
                if self.x2 < 800:
                    self.canvas.move(self.image, self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x2 >= 800:
                    self.forward = False
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

                if self.y1 <= 0:
                    self.falling = True
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

            if not self.falling and not self.forward: # Movimiento 4: izquierda y arriba
                if self.x1 > 0:
                    self.canvas.move(self.image, -self.speedX, 0)
                if self.y1 > 0:
                    self.canvas.move(self.image, 0, -self.speedY)
                if self.x1 <= 0:
                    self.forward = True
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

                if self.y1 <= 0:
                    self.falling = True
                    self.bounce = self.bounce + 1
                    if self.bounce < 3:
                        pygame.mixer.Sound.play(ballSound)

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
                pygame.mixer.Sound.play(ballSound)
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)                
                time.sleep(2)
                
            elif self.px1<self.bx2<self.px2 and self.py1<self.by1<self.py2: # Choque 2: abajo izquierda
                pygame.mixer.Sound.play(ballSound)
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)                
                time.sleep(2)
                
            elif self.px1<self.bx1<self.px2 and self.py1<self.by2<self.py2: # Choque 3: arriba derecha
                pygame.mixer.Sound.play(ballSound)
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)               
                time.sleep(2)
                
            elif self.px1<self.bx2<self.px2 and self.py1<self.by2<self.py2: # Choque 4: arriba izquierda
                pygame.mixer.Sound.play(ballSound)
                player.set_lblLife()
                self.existencia = False
                self.canvas.delete(self.image)
                time.sleep(2)

            time.sleep(0.1)
                
        self.existencia = False        
        self.canvas.delete(self.image)

#Funcion para crear el thread de la bola y el thread que verifica el impacto de la bola, ademas regula la frencuencia de aparicion de las bolas
def ballSet(canvas, level):
    global player

    while player.life > 0  and player.tiempo < 60:
        ball = Ball(canvas, level) # crea las instancias de proyectil (bola)       
        ballThread = Thread(target = ball.moveBall) # thread para el movimiento de cada bola
        ballThread.daemon = True
        ballThread.start()      

        ballThread1 = Thread(target = ball.impact) # thread para evaluar colisiones
        ballThread1.daemon = True
        ballThread1.start()

        # los proyectiles aparecerán más rápido en los niveles siguientes
        if level == 1:
            time.sleep(5)
        elif level == 2:
            time.sleep(3)
        elif level == 3:
            time.sleep(1)
    
#Funcion de la creacion de la ventana de juego  
def play():
    #Se detiene el sonido
    winsound.PlaySound(None, winsound.SND_FILENAME)
    mainWin.withdraw()

    #Segun el nivel se elige una cancion de fondo
    if optLevel.get() == "Nivel 1" and music.get() == "Con música":
        pygame.mixer.music.load("nivel1.wav")
        pygame.mixer.music.play()
        
    elif optLevel.get() == "Nivel 2" and music.get() == "Con música":
        pygame.mixer.music.load("nivel2.wav")
        pygame.mixer.music.play()
        
    elif optLevel.get() == "Nivel 3" and music.get() == "Con música":
        pygame.mixer.music.load("nivel3.wav")
        pygame.mixer.music.play()

    #Se crea la ventana
    gameWin = tk.Toplevel(mainWin)
    gameWin.geometry("800x760")
    gameWin.resizable(0,0)
    gameWin.title("GAME!")

    #Se crea el canvas
    cnvs = tk.Canvas(gameWin,width=800, height= 700, borderwidth=0, highlightthickness=0, bg= "green")
    cnvs.place(x= 0, y= 0)

    #Se pone la imagen de fondo
    Backimg = tk.PhotoImage(file = "play.png").subsample(1, 1)
    Backimage = cnvs.create_image(400, 350, image = Backimg)

    global player

    playerLife = 60
    lblLife = tk.Label(gameWin, text = "VIDA: " + str(playerLife), font = "Consolas 16 bold", bg = "#e75719", fg = "white")
    lblLife.place(x = 20, y = 720)

    playerScore = 0
    lblScore = tk.Label(gameWin, text = "SCORE: " + str(playerScore), font = "Consolas 16 bold", bg = "#e75719", fg = "white")
    lblScore.place(x = 150, y = 720)

    tiempo = 0
    lblTime = tk.Label(gameWin, text = "TIME: " + str(tiempo), font = "Consolas 16 bold", bg = "#e75719", fg = "white")
    lblTime.place(x = 300, y = 720)

    lblName = tk.Label(gameWin, text = "PLAYER: " + str(txtName.get()), font = "Consolas 16 bold", bg = "#7474a9", fg = "white")
    lblName.place(x = 450, y = 720)

    player = Player(cnvs, gameWin, playerLife, lblLife, playerScore, lblScore, tiempo, lblTime)
    player.coords_get()

    #Funcion para el boton de volver
    def varios():
        mainWin.deiconify()
        gameWin.withdraw()
        player.killPlayer()
        if music.get() == "Con música":
             pygame.mixer.music.stop()

    #Boton de volver
    btnBack = tk.Button(gameWin, command = varios, text = "Volver", font = ("Fixedsys", 17), bg = "black", fg = "white")
    btnBack.place(x = 650, y = 703)

    #Se crea el thread para llamar al ballset y poder crear mas threads
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

    #Se crea el thread para llamar al updateScore
    def threadScores():
        scoresThread = Thread(target = player.updateScore)
        scoresThread.daemon = True
        scoresThread.start()

    #Se establecen los eventos de movimiento para la nave, estos llaman a los metodos del jugador
    gameWin.bind('<Right>', player.moveRight)
    gameWin.bind('<Left>', player.moveLeft)
    gameWin.bind('<Up>', player.moveUp)
    gameWin.bind('<Down>',player.moveDown)

    #Se llaman a las funciones que hacen los threads
    threadScores()
    threadBall()

    gameWin.mainloop()

#Se crea la ventana principal
mainWin = tk.Tk()
mainWin.geometry("400x530")
mainWin.resizable(0,0)
mainWin.title("DODGEBALL / QUEMADOS")
mainWin.config(bg = "#c39c76")

#Label del titulo
lblTitle = tk.Label(mainWin, text="DODGEBALL", font = "Fixedsys 25 bold italic", bg = "#f29539")
lblTitle.pack(fill = tk.X)

#Entrada del nombre
txtName = tk.Entry(mainWin)
txtName.place(x=150, y= 60)

#Label del nombre
lblName = tk.Label(mainWin, text="NOMBRE:", font = "Fixedsys 13 bold", bg = "#f29539")
lblName.place(x= 70, y=60)

#Parte de la seleccion del nivel, se establecen valores de niveles posibles
levelValue = StringVar(mainWin)
levels = ['Nivel 1','Nivel 2','Nivel 3']
levelValue.set('1')

#Seleccion de nivel
optLevel = ttk.Combobox(mainWin, values = levels, state = 'readonly')
optLevel.current(0)
optLevel.place(x=130, y = 120)

#Label del nivel
lblLevel = tk.Label(mainWin,text="NIVEL:", font = "Fixedsys 13 bold", bg = "#f29539")
lblLevel.place(x= 70, y=120)

music = StringVar(mainWin)
music.set("Sin música")

#Seleccion de musica on
withMusic = Radiobutton(mainWin, text="Con música", value = "Con música", variable = music, command = lambda: winsound.PlaySound("inicio.wav", winsound.SND_ASYNC))
withMusic.place(x = 100, y = 190)

#Seleccion de musica off
noMusic = Radiobutton(mainWin, text="Sin música", value = "Sin música", variable = music, command = lambda: winsound.PlaySound(None, winsound.SND_FILENAME))
noMusic.place(x = 200, y = 190)

if music.get() == "Sin música":
    winsound.PlaySound(None, winsound.SND_FILENAME)

#Boton para jugar
btnPlay= tk.Button(mainWin, text = "JUGAR", width = "15", height = "2", command = play, font = "Fixedsys 12 bold", bg = "black", fg = "white")
btnPlay.place(x=130, y=250)

#Boton de los mejores puntajes
btnRecords= tk.Button(mainWin, text = "PUNTAJES", width = "15", height = "2",  font = "Fixedsys 12 bold", bg = "black", fg = "white", command = scores)
btnRecords.place(x=130, y=350)

#Boton del about
btnAbout= tk.Button(mainWin, text = "ABOUT", width = "15", height = "2", bg = "black",  font = "Fixedsys 12 bold", fg = "white", command = about)
btnAbout.place(x=130, y=450)

mainWin.mainloop()
