from paho.mqtt.client import Client
from datetime import datetime
from pathlib import Path
import csv

'''
Autore: Vogli Vullnet
Classe: 5AI
'''

# Callbacks
def on_message(client, userdata, message):

    salva_dati(PATH_FILE_CSV, PATH_FILE_TXT, float(message.payload.decode('UTF-8')))

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

    try:

        client.loop_forever()

    except KeyboardInterrupt:

        print('Disconnetto...')

def inizializza_callbacks():

    client.on_message = on_message

    client.on_connect = on_connect

# Salvataggio su file
def controlla_file(file_csv: Path):

    if not file_csv.exists():

        file_csv.touch()

        ripristina_file(PATH_FILE_CSV)
    
    else:

        with open(file_csv.absolute(), 'r') as file:
            
            # Per evitare ridondanza controllo la prima riga così da rendere intuitiva la lettura in futuro.
            if file.readline() != PRIMA_RIGA_FILE_CSV:

                print('File corrotto! Riparo...')
                
                ripristina_file(PATH_FILE_CSV)

            else:

                print('File valido!')

def ripristina_file(file_csv: Path):
    
    with open(file_csv.absolute(), 'w') as file:

        file.write(PRIMA_RIGA_FILE_CSV)

def salva_dati(file_csv: Path, file_txt: Path, t: float):

    try:

        with open(file_txt.absolute(), 'a+') as f:

            with open(file_csv.absolute(), 'a+', newline = '') as c:
            
                csv_writer = csv.writer(c, dialect='excel', delimiter = ';', escapechar = ' ', quoting = csv.QUOTE_NONE)
                    
                # Splitto la data nel file csv
                data = datetime.now().strftime('%c').replace(' ', ';')
            
                f.write('%s --> %s\n' % (t, data))

                csv_writer.writerow(['%s;%s' % (t, data)])
                        
                print('Temperatura: %f' %t)

    except:

        # Se si apre il file mentre si è in scrittura si causa una PermissionError
        print('Non aprire il file su excel!!!')

# Main
def main():
    
    print('\nInizio\n')

    controlla_file(PATH_FILE_CSV)

    inizializza_client()

    print('\nFine\n')

if __name__ == "__main__":
    
    PATH_FILE_TXT       = Path('E:\\Programmazione\\Python\\Scuola\\temps.txt')
    PATH_FILE_CSV       = Path('E:\\Programmazione\\Python\\Scuola\\temps.csv')
    PRIMA_RIGA_FILE_CSV = 'Temperatura ;Giorno ;Mese ;Numero Giorno ;Ora ;Anno\n'

    IP    = '80.210.122.173'
    PORTA = 1883

    # Spiegazione carattery jolly:
    # https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/
    TOPIC = 'case/CASA1/+/sensori/temperatura'

    main()
