import time
from random import randint
import random
from datetime import datetime
from pathlib import Path

PATH = 'E:\Programmazione\Python\Svago\case2.csv'
RANGE = (-10, 40)
SLEEP = 1

stanze = ('cucina', 'salotto', 'camera singola', 'camera matrimoniale', 'bagno', 'sgabuzzino', 'garage')

def inizializza_file():

    file = Path(PATH)

    if not file.exists():

        file.touch()

    # Leggiamo la prima riga: se le celle non sono suddivise in "Casa;Stanza;Temperatura;Data;Ora" vuol dire che il file è stato modificato manualmente e non più valido
    with open(PATH, 'r') as lettura_file_excel:
        
        if lettura_file_excel.readline() != 'Casa;Stanza;Temperatura;Data;Ora\n':
            
            # Quindi se è stato modificato ci tocca riscrivere "l'header"
            with open(PATH, 'w') as scrittura_file_excel:

                scrittura_file_excel.write('Casa;Stanza;Temperatura;Data;Ora\n')
                
def scrivi():

    with open(PATH, 'a') as file_excel:
        
        for i in range(5):

            # Scrivo: idCasa, stanza, temperatura, data, ora
            file_excel.writelines([str(randint(0, 10)), ';', random.choice(stanze), ';', str(randint(RANGE[0], RANGE[1])), ';', datetime.now().strftime("%d/%m/%Y;%H:%M:%S"), '\n'])
            
            time.sleep(1)

if __name__ == "__main__":
    
    inizializza_file()

    scrivi()
