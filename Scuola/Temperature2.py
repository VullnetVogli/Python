from paho.mqtt.client import Client
import random
from pathlib import Path
import time

# Random temperatura
def get_temperatura():

    return round(random.uniform(RANGE_TEMPERATURE[0] - TOLLERANZA_TEMPERATURE, RANGE_TEMPERATURE[1] + TOLLERANZA_TEMPERATURE), 2)

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

    inizializza_client()

    try:

        for i in range(2):
        
            for casa in CASE:

                time.sleep(PAUSA)

                for stanza in STANZE:

                    for temperatura in range(NUMERO_TEMPERATURE):

                        t = get_temperatura()

                        pubblica(casa + stanza, t)

                        time.sleep(1)

            print('-------------')

    except KeyboardInterrupt:

        client.loop_stop()

        client.disconnect()

        print('\nDisconnesso')

    print('\nFine\n')

if __name__ == "__main__":

    CASE   = ('case/casa1/', 'case/casa2/', 'case/casa3/', 'case/casa4/', 'case/casa5/')
    STANZE = ('cucina/sensori/temperatura', 'camera/sensori/temperatura', 'bagno/sensori/temperatura', 'salotto/sensori/temperatura')

    PAUSA = 5   # In secondi

    RANGE_TEMPERATURE = (10, 40)
    TOLLERANZA_TEMPERATURE = 10
    NUMERO_TEMPERATURE = 2

    IP    = '80.210.122.173'
    PORTA = 1883
    QOS   = 3
    
    main()