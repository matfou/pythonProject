from tkinter import *
import tkinter as tk

window = Tk()

#
window.title("Jeu de Hex : Page d'accueil")
window.geometry("1100x700")
window.configure(bg="wheat")

label1 = Label(window, text = "JEU DE HEX DE GUEDIN", bg  = "wheat", font = ("Courier", 60))
label1.place(x = 370, y = 60)

frame_button = Frame(window, bg="wheat")
frame_button.place(x = 280, y = 600, width = 600, height = 100)

frame_j1ps = Frame(window, bg="white", borderwidth=1, relief="solid")
frame_j1ps.place(x = 425, y = 225, width = 500, height = 50)

label_functionpseudo = Label(frame_j1ps, text = "Saisir votre pseudo : ", bg="white", font=("Courier",15))
label_functionpseudo.place(x = 30, y = 10, width = 275, height = 30)

entry_functionpseudo = Entry(frame_j1ps, bg = "white",)
entry_functionpseudo.place(x = 330, y = 10, width = 150, height = 30)

frame_j1 = Frame(window, borderwidth=1, relief="solid")
frame_j1.place(x = 300, y = 225, width = 75, height = 50)

label_j1 = Label(frame_j1, text="J1", font=("Courier", 15))
label_j1.place(x = 20, y = 10, width = 25, height = 30)

frame_j2ps = Frame(window, bg="white", borderwidth=1, relief="solid")
frame_j2ps.place(x = 425, y = 325, width = 500, height = 50)

label_functionpseudo = Label(frame_j2ps, text = "Saisir votre pseudo : ", bg="white", font=("Courier",15))
label_functionpseudo.place(x = 30, y = 10, width = 275, height = 30)

entry_functionpseudo = Entry(frame_j2ps, bg = "white",)
entry_functionpseudo.place(x = 330, y = 10, width = 150, height = 30)

frame_j2 = Frame(window, borderwidth=1, relief="solid")
frame_j2.place(x = 300, y = 325, width = 75, height = 50)

label_j2 = Label(frame_j2, text="J2", font=("Courier", 15))
label_j2.place(x = 20, y = 10, width = 25, height = 30)

label2 = Label(window, text = "J1, choisissez votre couleur", bg = "wheat", font=("Courier", 10))
label2.place(x = 225, y = 485)

def createNewWindow():
    newWindow = tk.Tk()
    newWindow.title("Jeu de Hex : Page principale")
    newWindow.geometry("1200x800")
    newWindow.configure(bg="wheat")

app = tk.Tk()

def viewSelected():
    choice = var.get()
    if choice == 1:
        btn = Button(window, text='Commencer', font=("Courier", 20), command=createNewWindow)
        btn.place(x=500, y=600, width=200, height=80)

    elif choice == 2:
        btn = Button(window, text='Commencer', font=("Courier", 20), command=createNewWindow)
        btn.place(x=500, y=600, width=200, height=80)



var = IntVar()

frame_rouge = Frame(window, borderwidth=1, relief = "solid", bg="red")
frame_rouge.place(x = 500, y = 475, width = 45, height = 45)

rbuttonRed = Radiobutton(window, variable=var, value=1, command=viewSelected, relief="solid", bg = "wheat")
rbuttonRed.place(x = 565, y =475, width = 45, height = 45)

frame_bleu = Frame(window, borderwidth=1, relief = "solid", bg="blue")
frame_bleu.place(x = 740, y = 475, width = 45, height = 45)

rbuttonBlue = Radiobutton(window, variable=var, value=2, command=viewSelected, relief="solid", bg = "wheat")
rbuttonBlue.place(x = 805, y =475, width = 45, height = 45)

window.mainloop()



