from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print('Benvenuto nel mio convertitore di immagini! Per iniziare sceglia il file da convertire')

path = input('Inserisci la cartella (METTI \ ALLA FINE) ')

estensione_corrente = input("Inserisci l'estensione corrente: " )

estensione_nuova = input("Inserisci la nuova estensione: " )

files = os.listdir(path=path)

for file in files:

    im = Image.open(path + file)

    nuovo_file = file.replace(estensione_corrente, estensione_nuova)

    im = Image.open(path + file)
    im.save(path + nuovo_file)

for file in files:
    
    if file.endswith(estensione_corrente):
        
        os.remove(path + file)