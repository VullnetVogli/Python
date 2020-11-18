from paho.mqtt.client import Client
from datetime import datetime
from pathlib import Path
import csv

# Callbacks
def on_message(client, userdata, message):

    print(message.payload.decode('UTF-8'))

    salva_dati(PATH, message.payload.decode('UTF-8'))

def on_connect(client, userdata, flags, rc):

    print('\nConnesso con successo\n')

def on_disconnect(client, userdata, flags, rc):

    print('\nDisconnect con successo\n')

# Inizializzazioni
def inizializza_client():

    global client

    client = Client('Test_1')

    client.connect(IP, PORTA)
    
    client.subscribe(TOPIC)

    inizializza_callbacks()

    client.loop_forever()

def inizializza_callbacks():

    client.on_message = on_message

    client.on_connect = on_connect

# Salvataggio su file
def salva_dati(file: Path, t: float):
    
    with open(file.absolute(), 'a+') as f:

        with open(file.parent.joinpath(file.name.split('.')[0] + '.csv'), 'a+', newline = '') as c:
            
            csv_writer = csv.writer(c, dialect='excel', delimiter = ';', quotechar = ' ', quoting = csv.QUOTE_MINIMAL)

            f.write(str(t))

            csv_writer.writerow(str(t))

        c.close()

        f.close()

# Main
def main():
    
    print('\nInizio\n')

    inizializza_client()

    print('\nFine\n')

if __name__ == "__main__":
    
    PATH = Path('E:\\Programmazione\\Python\\Svago\\temps.txt')

    IP    = '80.210.122.173'
    PORTA = 1883

    # Spiegazione carattery jolly:
    # https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/
    TOPIC = 'case/casa1/+/sensori/temperatura'

    main()
