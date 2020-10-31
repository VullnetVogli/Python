from datetime import date
import random
import datetime
from pathlib import Path

'''
Autore: Vogli Vullnet
Classe: 5 AI
Data: 31/10/2020

Compito: Scrivere delle temperature su file e avvisare se son oall'infuori di un range
'''

RANGE_TEMPERATURE = (0, 35)

TOLLERANZA_TEMPERATURE = 10

NUMERO_TEMPERATURE = 10

PATH = Path('E:\\Programmazione\\Python\\Svago\\temps.txt')

def controlla_file(file: Path):

    if file.exists():

        file.touch()

    else:

        print('File esistente')

def scrivi_file(file: Path):
    
    with open(file.absolute(), 'a+') as f:

        for i in range(NUMERO_TEMPERATURE):

            t = random.randint(RANGE_TEMPERATURE[0] - TOLLERANZA_TEMPERATURE, RANGE_TEMPERATURE[1] + TOLLERANZA_TEMPERATURE)

            if t < RANGE_TEMPERATURE[0] :
                
                f.write('Temperatura troppo bassa! \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))

            elif t > RANGE_TEMPERATURE[1]:

                f.write('Temperatura troppo alta! \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))

            else:

                f.write('Temperatura nella norma. \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))
           
        f.close()

if __name__ == "__main__":
    
    controlla_file(PATH) 

    scrivi_file(PATH)