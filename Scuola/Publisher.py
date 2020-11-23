import configparser
from paho.mqtt.client import Client
from configparser import ConfigParser
import random
from pathlib import Path
import time

'''
Autore: Vogli Vullnet
Classe: 5AI

Consegna:
Simulare in Python la rilevazione delle temperature di una casa con 5 stanze in ogni casa e l'invio al proprietario della segnalazione se al di sotto dei 21 gradi o al di sopra dei 26 gradi.
Intervallo rilevazione di 5 secondi.
La temperatura da simulare varia da +10 gradi a +40 gradi.
Lo script di visualizzazione viene associato al proprietario mediante un file ASCII di configurazione (usare come estensione .conf).
Prevedere versione per fisso e mobile.
Nel caso di mobile scaricare una shell di Python per Android (o altro sistema).

'''

# Random temperatura
def get_temperatura():

    return round(random.uniform(RANGE_TEMPERATURE[0], RANGE_TEMPERATURE[1]), 2)

# Metodi file config
def inizializza_file_config(file_config: Path):

    global CASE

    configurazione = ConfigParser()

    if not file_config.exists():

        print('File non esistente! Creo...')

        file_config.touch

        # Inserisco dei dati di esempio
        riscrivi_file_config(configurazione, file_config)

    else:

        # Leggo il file
        configurazione.read(file_config)

        # Considero il nome di una casa quello che c'è nelle parentesi quadre: es [CASA1], [CASA2]
        for casa in configurazione.sections():
    
            CASE[casa] = {}

            # Ogni casa avrà un certo numero di stanze che verranno salvate in un dizionario
            for stanza in configurazione[casa]:

                # Per ogni stanza ho il massimo ed il minimo accettabile per la temperatura
                CASE[casa][stanza] = configurazione[casa][stanza].split(',')

def riscrivi_file_config(configurazione: ConfigParser, file_config: Path):

    configurazione['CASA1'] = {'cucina': '20,25',
                               'bagno': '15,25',
                               'camera': '20,30'}

    configurazione['CASA2'] = {'cucina': '20,25',
                               'bagno': '15,25',
                               'camera': '20,30',
                               'salotto': '25,30'}

    with open(PATH_CONFIG, 'w') as configfile:
        
        configurazione.write(configfile)

# Callbacks
def on_connect(client, userdata, flags, rc):

    print('\nConnesso con successo\n')

def on_message(client, userdata, message):

    print(message.payload.decode('UTF-8'))

# Metodi client
def pubblica(topic: str, temperatura: float):

    client.publish(topic, temperatura)

    print('Pubblico in "%s" una temperatura di %f' % (topic, temperatura))

def inizializza_client():

    global client

    client = Client('Prova')
        
    client.connect(IP, PORTA, QOS)

    inizializza_callbacks()

    client.loop_start()

def inizializza_callbacks():
    
    client.on_connect = on_connect

    client.on_message = on_message

# Main
def main():

    try:

        for i in range(1):

            # Scorro le case
            for casa in CASE:

                time.sleep(PAUSA)

                # Scorro le stanze nella casa
                for stanza in CASE[casa]:

                    t = get_temperatura()

                    # Controllo che la temperatura sia nel range stabilito di temperatura ottimale, se non lo è invio il dato
                    if t < float(CASE[casa][stanza][0]) or t > float(CASE[casa][stanza][1]):
                                
                        pubblica(FORMATO_TOPIC.format(casa, stanza), t)

                    time.sleep(1)

                print('______________________________________________________________________________\n')
    
    except KeyboardInterrupt:

        client.loop_stop()

        client.disconnect()

        print('\nDisconnesso')

    print('\nFine\n')


if __name__ == "__main__":
    
    PATH_CONFIG = Path('E:\Programmazione\Python\Scuola\Proprietari.conf')

    CASE = {}

    inizializza_file_config(PATH_CONFIG)

    PAUSA = 5   # In secondi

    RANGE_TEMPERATURE       = (10, 40)     # Il range delle temperature da generare con il random
    NUMERO_TEMPERATURE      = 2

    IP    = '80.210.122.173'
    PORTA = 1883
    QOS   = 2
    
    FORMATO_TOPIC = 'case/{}/{}/sensori/temperatura'

    inizializza_client()

    inizializza_callbacks()

    main()