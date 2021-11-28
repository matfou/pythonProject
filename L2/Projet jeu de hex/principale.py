from tkinter import *
import math

window = Tk()

window.title("Jeu de Hex")
window.geometry("1100x700")
window.configure(bg="wheat")

canvas = Canvas(window, width=900, height=500)
canvas.place(x=90, y=100)

taille = 20
class Hexagone:
    def __init__(self, canvas, x, y, taille, couleur):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.taille = taille
        self.couleur = couleur

    def createHexagone(self):
        xList = []
        yList = []
        for i in range(0, 6):
            angle = math.radians(i*360/6) + (math.pi/2)
            xList.append(int(self.x + self.taille*math.cos(angle)))
            yList.append(int(self.y + self.taille*math.sin(angle)))
        self.canvas.create_polygon(xList[0], yList[0], xList[1], yList[1], xList[2], yList[2], xList[3], yList[3], xList[4], yList[4], xList[5], yList[5], fill= self.couleur, outline="black")


class Plateau():
    def __init__(self):
        self.listPlateau = []

    def createPlateau(self, hexa):
        x1 = 0

        for col in range(0, 13):
            hexa.y = hexa.y + hexa.taille + hexa.taille / 2
            hexa.x += hexa.taille * (math.sqrt(3) / 2)
            for li in range(0, 13):
                if li == 0:
                    x1 = hexa.x + hexa.taille * (math.sqrt(3))
                    hexa1 = Hexagone(hexa.canvas, x1, hexa.y, hexa.taille, "red")
                    hexa1.createHexagone()
                elif li == 12:
                    x1 = x1 + hexa.taille * (math.sqrt(3))
                    hexa1 = Hexagone(hexa.canvas, x1, hexa.y, hexa.taille, "red")
                    hexa1.createHexagone()
                else:
                    if col == 0:
                        x1 = x1 + hexa.taille * (math.sqrt(3))
                        hexa1 = Hexagone(hexa.canvas, x1, hexa.y, hexa.taille, "blue")
                        hexa1.createHexagone()
                    elif col == 12:
                        x1 = x1 + hexa.taille * (math.sqrt(3))
                        hexa1 = Hexagone(hexa.canvas, x1, hexa.y, hexa.taille, "blue")
                        hexa1.createHexagone()
                    else:
                        x1 = x1 + hexa.taille * (math.sqrt(3))
                        hexa1 = Hexagone(hexa.canvas, x1, hexa.y, hexa.taille, "")
                        hexa1.createHexagone()
                self.listPlateau.append(hexa1)

compt = 0
def colorierHexa(event):
    global plat
    global compt
    compt += 1
    x, y = event.x, event.y
    for poly in plat.listPlateau:
        if poly.x - (poly.taille*math.cos(math.pi/6)) < x and poly.x + poly.taille*math.cos(math.pi/6) > x :
            if poly.y - (poly.taille*math.cos(math.pi/6)) < y and poly.y + poly.taille*math.cos(math.pi/6) > y :
                if compt%2 == 0:
                    newHexa = Hexagone(poly.canvas, poly.x, poly.y, poly.taille, "blue")
                else :
                    newHexa = Hexagone(poly.canvas, poly.x, poly.y, poly.taille, "red")

                newHexa.createHexagone()
                plat.listPlateau.remove(poly)
                plat.listPlateau.append(newHexa)

def motion():
    canvas.bind("<Button-1>",colorierHexa)



hexa = Hexagone(canvas,100,50,taille,"")
y = 50
x = 100
plat = Plateau()
plat.createPlateau(hexa)

canvas.bind('<Motion>', motion)

window.mainloop()