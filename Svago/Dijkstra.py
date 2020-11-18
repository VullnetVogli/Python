import sys
import math

def ricerca_minimo(tabella, controllato):
    
    minimo = sys.maxsize
    indice = 0
    i = len(tabella) - 1
    
    while i >= 0:
        
        if tabella[i][1] != 0 and tabella[i][1] < minimo and not controllato[i]:
        
            minimo = tabella[i][1]

            indice = i
            
            controllato[i] = True

        i -= 1

    # + 1 perché la prima lista è l'elenco dei nodi
    return indice + 1

# Confronto la tabella del nodo con quella del nodo con peso minore
def comparaTabelle(i, indice, matrice):

    # Scorro i nodi a cui è collegato il nodo matrice[i]
    for j in range(1, len(matrice[i])):
       
        # Se il nodo nella tabella con cui vado ad affettuare il confronto è più vantaggioso
        if  matrice[indice][j][1] + matrice[i][indice][1] < matrice[i][j][1]:
        
            # Creo una tuple con destinazione, peso e nodo precedente
            matrice[i][j] = (matrice[i][j][0], matrice[i][indice][1] + matrice[indice][j][1], matrice[indice][0])

            # Dato lo specchio della matrice, ricopio i valori. Questo trucco mi permetterà di ottimizzare il programma.
            matrice[j][i] = (matrice[j][i][0], matrice[i][indice][1] + matrice[indice][j][1], matrice[indice][0])

def visualizza(matrice):

    print()

    for i in range(1, len(matrice)):

        print('Tabella nodo %s: ' % (matrice[i][0]), end = '')
        
        for j in range(1, len(matrice[i])):

            print(matrice[i][j], '\t', end='')

        print()
        
    print()

def carica_file(path):
    
    with open(path) as file:

        matrice_temp = []
        controlli_temp = []

        # Leggo il file
        for riga in file.readlines():

            a = []
            b = []

            # Tolgo gli spazi 
            riga = riga.strip().replace(' ', '')
            
            # Scorro la riga
            for j in range(len(riga)):
                
                # Se non si sa quanto sia la distanza
                if  riga[j] == '?':

                    # Aggiungo i dati: il primo sarà la destinazione, il secondo il peso e ultimo lo contrassegno 'come da trovare'
                    a.append((matrice_temp[0][j], sys.maxsize, '?'))

                # Se è un numero
                elif riga[j].isdigit():

                    # Aggiungo i dati: il primo sarà la destinazione, il secondo il peso e ultimo il nodo precedente
                    a.append((matrice_temp[0][j], int(riga[j]), a[0]))
                   
                # Altrimenti è una stringa (ed è il nome del nodo)
                else:
                        
                    a.append(riga[j])
                
                # Mi salvo quali nodi ho già controllato e quali no    
                b.append(False)

            # Inserisco tutte le informazioni di ciascun nodo nella matrice
            matrice_temp.append(a)
           
            controlli_temp.append(b)
            
        return matrice_temp, controlli_temp

'''        
Per la strutture della matrice su file:
    - Se il router è se stesso mettere 0: risulterà una diagonale di 0.
    - Quando la distanza non si sa mettere ? altrimenti il peso
    - Non dimenticare i nomi dei nodi
'''

PATH = 'E:\Programmazione\Python\Svago\dati_Dijkstra.txt'

matrice, controlli = carica_file(PATH)

for x in range(len(matrice)):

    # Non ho bisogno di controllare il primo dato visto che è il nome del nodo
    # Non ho neanche bisogno di controllare l'ultimo nodo
    for i in range(1, len(matrice)):
        
        # Ricerco il numero minimo e salvo l'indice
        indice = ricerca_minimo(matrice[i][1::], controlli[i])
        
        # Confronto i dati del nodo con quelli del nodo più visino (con peso minore)
        comparaTabelle(i, indice, matrice)
        
visualizza(matrice)
