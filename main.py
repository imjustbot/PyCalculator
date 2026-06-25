from tkinter import *

FINESTRA = Tk()

FINESTRA.title("Calcolatrice")

FINESTRA.geometry("350x500")

FINESTRA.configure(bg="#8ff359")

SCHERMO = Label(FINESTRA, text="0")

SCHERMO.grid(row=0, column=0, columnspan=4, sticky="nsew")

ESPRESSIONE = ""

def premi(tasto):

    global ESPRESSIONE

    ESPRESSIONE = ESPRESSIONE + tasto

    SCHERMO.configure(text=ESPRESSIONE)

def cancella():

    global ESPRESSIONE

    ESPRESSIONE = ""

    SCHERMO.configure(text="0")

def calcola():

    global ESPRESSIONE

    CALCOLOCORRETTO = ESPRESSIONE.replace("x", "*")

    ESPRESSIONE = str(eval(CALCOLOCORRETTO))

    SCHERMO.configure(text=ESPRESSIONE)

TASTIERA = [['AC', '/'], ['7', '8', '9', 'x'], ['4', '5', '6', '+'], ['1', '2', '3', '-'], ['0', '=']]

riga_corrente = 1

for riga in TASTIERA:
    colonna_corrente = 0

    for testo in riga:

        if testo == 'AC':
            azione = cancella


        elif testo == '=':
            azione = calcola

        else:

            azione = lambda t=testo: premi(t)       

        BOTTONE = Button(FINESTRA, text=testo, command=azione, font=("Arial", 18))
        BOTTONE.grid(row=riga_corrente, column=colonna_corrente, sticky="nsew")

        colonna_corrente = colonna_corrente + 1
    riga_corrente = riga_corrente + 1


FINESTRA.mainloop()