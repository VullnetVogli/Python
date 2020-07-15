import time
import sys
import math

'''
Autore: Vogli Vullnet
Classe: 4 AI
Data: 28/05/2020

Consegna: creare un cronometro
'''

class Cronometro:
    
    # Gli anni possono essere infiniti (2^31)
    massimi = (sys.maxsize, 364, 23, 59, 59, 59, 99)
    
    # Costruttore: 
    # tempo = anni, giorni, ore, minuti, secondi, centesimi
    def __init__(self, tempo = [0, 0, 0, 0, 0, 0]):
        
        self.__controlla_input__(tempo)
        
        self.tempo = tempo

    # Set e Get
    def setTempo(self, tempo):
        
        self.__controlla_input__(tempo)
        
        self.tempo = tempo
        
    def getTempo(self):
        
        return self.tempo
    
    def __controlla_input__(self, t):
        
        if len(t) > 7: raise Exception('Controlla bene il la lunghezza del parametro!') 
        
        # Se l'utente inserisce per esempio solo i minuti aggiungo io le altre informazioni riguardante gli anni, giorni, ecc...
        while (len(t)) < 7:
                
            t.insert(0, 0)
            
        # Gli anni possono essere anche infiniti
        if t[0] < 0 or type(t[0]) != int:
        
            raise Exception('Controlla bene i dati e i tipi nel parametro!')
        
        # Il resto va controllato
        for i in range(1, len(t)):
            
            # Se sbaglia i valori (troppo grandi o negativi) o sbaglia il tipo di dato
            if t[i] < 0 or t[i] > self.massimi[i] or type(t[i]) != int:
    
                raise Exception('Controlla bene i dati e i tipi nel parametro!')

    # Metodi
    def cronometro(self):
        
        t = time.time() * 100
        
        try:
            
            while True:
            
                time.sleep(0.01)
                
                t = self.__calcola_centesimi__(t)   # Si potrebbe fare molto meglio se si potesse passare la variabile per valore e non per referenza così da non essere obligato a ritornare t.
                
                self.visualizza()

        except KeyboardInterrupt:
            
            quit()

    def countDown(self):
        
        t = time.time() * 100
        
        try:
            
            while True:
            
                time.sleep(0.01)
                
                t = self.__calcola_centesimi__(t, True)   # Si potrebbe fare molto meglio se si potesse passare la variabile per valore e non per referenza così da non essere obligato a ritornare t.
                
                self.visualizza()

        except KeyboardInterrupt:
            
            quit()

    # 0: uguali, -1 parametro t minore di self.tempo, 1 self.tempo maggiore di t
    def compareTo(self, t):
        
        self.__controlla_input__(t)
        
        a = self.__converti_lista_in_intero__(t)
        b = self.__converti_lista_in_intero__(self.tempo)
        
        if a < b:
            
            return -1
        
        elif a == b:
            
            return 0
        
        else:
            
            return 1
    
    def __calcola_centesimi__(self, t, countDown = False):
        
        # Se siamo in modalità count down
        if countDown:
            
            # Teniamo conto dell'indice dei secondi: ci servirà per scalare i secondi/minuti/ore ecc ogni volta che i centesimi di secondo raggiungono lo 0
            i = len(self.tempo) - 2
        
            # Scaliamo un centesimo di secondo dai centesimi
            self.tempo[len(self.tempo) - 1] -= int(time.time() * 100 - t)

            # Quando raggiungono lo 0
            if self.tempo[len(self.tempo) - 1] <= 0:
                
                # Resetto al valore massimo
                self.tempo[len(self.tempo) - 1] = self.massimi[i + 1]
                
                # Vado alla ricerca di un prestito.
                # Esempio: 1:0:0 -> 0:59:59
                #        4:0:0:0 -> 3:59:59:59:59
                while i >= 0 and self.tempo[i] == 0:
                    
                    # Quindi quando andremo a prendere in prestito e il valore sarà 0, metteremo al massimo perché prenderemo da una posizione maggiore (1:0:0 -> 0:59:59)
                    self.tempo[i] = self.massimi[i]
                    
                    i -= 1
                
                # Se l'indice è minore di 0 vuol dire che tutti i prestiti sono finiti e quindi anche il count down.
                if i < 0:

                    print('Raggiunto lo zero!')

                    quit()
                
                else:
                    
                    self.tempo[i] -= 1

        # Altrimenti siamo in modalità cronometro
        else:
            
            # In questo modo riesco a 'bypassare' il problema dello sleep. Ogni tanto, dato che i thread sono imprevedibili, si potrebbero fermare 0.1 secondi come 0.2. Penso sia dovuto al round-robin della CPU.
            # Noi aggiungiamo il delta del tempo passato
            self.tempo[len(self.tempo) - 1] += int(time.time() * 100 - t)       
            
            # Se sfora il valore resetto e aumento di 1 il prossimo
            if self.tempo[len(self.tempo) - 1] >= self.massimi[len(self.tempo) - 1]:
    
                self.tempo[len(self.tempo) - 1] = 0
                
                self.tempo[len(self.tempo) - 2] += 1
            
        return time.time() * 100
    
    def __calcola_secondi__(self):

        # Stessa cosa del calcolo dei centesimi di secodo
        if self.tempo[len(self.tempo) - 2] >= self.massimi[len(self.tempo) - 2]:
                
            self.tempo[len(self.tempo) - 2] = 0
                
            self.tempo[len(self.tempo) - 3] += 1
  
    def __calcola_minuti__(self):

        if self.tempo[len(self.tempo) - 3] == self.massimi[len(self.tempo) - 3]:
                
            self.tempo[len(self.tempo) - 3] = 0
                
            self.tempo[len(self.tempo) - 4] += 1
            
    def __calcola_ore__(self):
        
        if self.tempo[len(self.tempo) - 4] == 24:
            
            self.tempo[len(self.tempo) - 4] = 0
            
            self.tempo[len(self.tempo) - 5] += 1
    
    def __calcola_giorni__(self):
        
        if self.tempo[len(self.tempo) - 5] == self.massimi[len(self.tempo) - 4]:
            
            self.tempo[len(self.tempo) - 5] = 0
            
            self.tempo[len(self.tempo) - 6] += 1
    
    # Il calcolo degli anni non l'ho fatto dato che possono essere anche milioni
    
    def visualizza(self):
        
        print('{}:{}:{}:{}:{}:{}:{}'.format(self.tempo[0], self.tempo[1], self.tempo[2], self.tempo[3], self.tempo[4], self.tempo[5], self.tempo[6]))
    
    # Non modifico in stringa e poi in intero dato che sarebbe troppo 'costoso'
    def __converti_lista_in_intero__(self, t):
       
        if t == None or len(t) == 0: return 0
        
        elif len(t) == 1: return t[0]

        s = t[0]
        i = 1
        
        while i < len(t):
            
            # Condizione del dominio del logaritmo
            if t[i] > 0:
            
                # Alla variabile s verrà aggiunto il numero in posizione t[i]
                # Quindi se [1, 2, 30]:
                #   - s = 1 (prima di entrare nel ciclo)
                #   - s = s * 10 ^ quante cifre ha + t[i] -> s = 1 * 10 ^ 1 + 2 -> 12
                #   - s = s * 10 ^ 2 + 30 -> 1230
                s = int(s * math.pow(10, int(math.floor(math.log10(t[i])) + 1)) + t[i])
            
            i += 1
            
        return s


cronometro = Cronometro([0, 0, 1, 1, 50])

print(cronometro.compareTo([1, 2, 61]))

cronometro.countDown()
    
cronometro.cronometro()