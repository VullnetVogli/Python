from paho.mqtt.client import Client
from datetime import date
import random
import datetime
from pathlib import Path
import csv

'''
Autore: Vogli Vullnet
Classe: 5 AI
Data: 31/10/2020
Versione 0.2: Aggiunta la scrittura su file csv che può essere letto da Excel.

Compito: Scrivere delle temperature su file e avvisare se son oall'infuori di un range
'''

RANGE_TEMPERATURE = (0, 35)
TOLLERANZA_TEMPERATURE = 10
NUMERO_TEMPERATURE = 2

PATH = Path('E:\\Programmazione\\Python\\Svago\\temps.txt')

IP = '80.210.122.173'
PORTA = 1883
client = Client('Prova')

def get_temperatura():

    return random.randint(RANGE_TEMPERATURE[0] - TOLLERANZA_TEMPERATURE, RANGE_TEMPERATURE[1] + TOLLERANZA_TEMPERATURE)

def scrivi_file(file: Path):
    
    with open(file.absolute(), 'a+') as f:

        with open(file.parent.joinpath(file.name.split('.')[0] + '.csv'), 'a+', newline = '') as c:
          
            csv_writer = csv.writer(c, dialect='excel', delimiter = ';', quotechar = ' ', quoting = csv.QUOTE_MINIMAL)

            for i in range(NUMERO_TEMPERATURE):
                
                t = get_temperatura()

                if t < RANGE_TEMPERATURE[0]:
                    
                    f.write('temperatura troppo bassa! \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))

                    csv_writer.writerow(['Temperatura troppo bassa;%s;%s' % (t, datetime.datetime.now().strftime('%c'))])
               
                elif t > RANGE_TEMPERATURE[1]:

                    f.write('Temperatura troppo alta! \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))

                    csv_writer.writerow(['Temperatura troppo alta;%s;%s' % (t, datetime.datetime.now().strftime('%c'))])

                else:

                    f.write('Temperatura nella norma. \t%s --> %s\n' % (t, datetime.datetime.now().strftime('%c')))

                    csv_writer.writerow(['Temperatura nella norma;%s;%s' % (t, datetime.datetime.now().strftime('%c'))])
               
        c.close()

        f.close()

def inizializza_client():

    global client

    client.connect(host=IP, port=PORTA)

    client.subscribe(topic=TOPIC)

if __name__ == "__main__":

    #inizializza_client()

    scrivi_file(PATH)