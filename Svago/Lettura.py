from pathlib import Path
import time

PATH = 'E:\Programmazione\Python\Svago\case2.csv'

def inizializza_file():

    file = Path(PATH)

    if not file.exists():

        print('File inesistente!')
    
def leggi():

    with open(PATH, 'r') as file_excel:

        while True:

            linea = file_excel.readline()

            if not linea:

                time.sleep(1)

            else:

                print(linea)

        
if __name__ == "__main__":
    
    leggi()