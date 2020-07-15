import time, math

class Nodo:

    # Costruttore
    def __init__(self):

        super().__init__()

        self._nome = ''

        self._destinazioni = []

        self._pesi = []

        self._nextHop = []

        self.chiedi_input()

        self.ordina()

    # SET && GET
    def set_nome(self, nome):
    
        self._nome = nome

    def set_destinazioni(self, destinazioni):
    
        self._destinazioni = destinazioni

    def set_pesi(self, pesi):
    
        self._pesi = pesi

    def set_nextHop(self, nextHop):

        self._nextHop = nextHop

    def get_nome(self):
        
        return self._nome

    def get_destinazioni(self):
    
        return self._destinazioni

    def get_pesi(self):
    
        return self._pesi

    def get_nextHop(self):
    
        return self._nextHop

    # Metodi
    # Chiedo in input le informazioni del nodo
    def chiedi_input(self):

        dim = 0

        while self._nome.strip() == '':

            self._nome = input('Inserisci il nome di questo nodo: ').upper()

        while dim < 1:

            dim = int(input("A quanti nodi è connesso il nodo %s? " % (self._nome)))

        self._destinazioni.append(self._nome)

        self._nextHop.append(self._nome)

        self._pesi.append(0)

        while dim > 0:

            nomeNodo = ''

            peso = 0

            while nomeNodo.strip() == '' or nomeNodo == self._nome:

                nomeNodo = input('Inserisci il nome del destinatario (%d rimasti): ' % (dim)).upper()

            while peso < 1:

                peso = int(input('Inserisci il peso tra %s e %s: ' % (self._nome, nomeNodo)))

            # Salvo le infoormazioni
            self._destinazioni.append(nomeNodo)

            self._nextHop.append(nomeNodo)

            self._pesi.append(peso)

            dim -= 1

        print()

    # Metodo che mi visualizza la tabella di routing del nodo
    def visualizza(self):

        print('Tabella del nodo: ', self._nome)

        # Scorro la tabella
        for i in range(len(self._destinazioni)):

            print('%s %d %s' % (self._destinazioni[i], self._pesi[i], self._nextHop[i]))

    # Piccolo ordinamento Inseritionsort
    def ordina(self):

        if len(self._destinazioni) < 2:
            return

        # Scorro la tabella
        for i in range(1, len(self._destinazioni)):

            j = i

            while j > 0 and self._destinazioni[j] < self._destinazioni[j - 1]:

                # Swappo le _destinazioni
                self._destinazioni[j], self._destinazioni[j - 1] = self._destinazioni[j - 1], self._destinazioni[j]

                # Swappo i _nextHop
                self._nextHop[j], self._nextHop[j - 1] = self._nextHop[j - 1], self._nextHop[j]

                # Swappo i _pesi
                self._pesi[j], self._pesi[j - 1] = self._pesi[j - 1], self._pesi[j]

                j -= 1

    # Ricerca binaria per cercare la destinazioni nella tabella
    def cerca(self, nomeDestinazione):

        sinistra = 0
        destra = len(self._destinazioni) - 1

        # Fintantoché gli indici non si incontrano
        while sinistra <= destra:

            # Calcolo l'indice medio
            medio = int((sinistra + destra) / 2)

            # Se il nome del nodo è uguale a quello passato come parametro
            if self._destinazioni[medio] == nomeDestinazione:

                # Ritorno indice
                return medio

            # Altrimenti
            else:

                # Se il nome del nodo con indice 'medio' è minore di quello passato come parametro
                if self._destinazioni[medio] < nomeDestinazione:

                    # Cerco nella metà destra
                    sinistra = medio + 1

                # Altrimenti
                else:

                    # Cerco nella metà sinistra.
                    destra = medio - 1

        return -1

    # Metodo per confrontare due nodi
    def compareTo(self, n):
        
        # Scorro le destinazioni
        for i in range(len(n.get_destinazioni())):

            # Se la destinazione è già nelle nostre destinazioni
            if n.get_destinazioni()[i] in self._destinazioni:

                # Andremo a confrontare i pesi
                self.confrontaDati(n, i)

            # Altrimenti
            else:

                # Lo aggiungiamo alle nostre destinazioni
                self.salva_nodo(n, i)
                
        self.ordina()
 
    # Metodo per aggiungere un nodo alla tabella
    def salva_nodo(self, n, i):
        
        # Mi salvo la destinazione.
        self._destinazioni.append(n.get_destinazioni()[i])

        # Il peso tra questo nodo (self) e il peso tra questo ndodo (self) il nodo di arrivo, sarà la somma del peso dei nodi.
        self._pesi.append(n.get_pesi()[i] + self._pesi[self._destinazioni.index(n.get_nome())])

        # Il nextHop sarà il nome del nodo passato come parametro.
        self._nextHop.append(n.get_nome())

        self.ordina()

    # Metodo per confrontare i pesi dei nodi e di conseguenza modificare i pesi e i nextHop.
    def confrontaDati(self, n, i):
        
        # Se controlla sè stesso e quindi esce dal metodo
        if n.get_destinazioni()[i] == n.get_nome():
            return
        
        indiceDestinazione = self.cerca(n.get_destinazioni()[i])
        
        indicePeso = self.cerca(n.get_nome())

        if n.get_pesi()[i] + self._pesi[indicePeso] < self._pesi[indiceDestinazione]:
            
            self._pesi[indiceDestinazione] = n.get_pesi()[i] + self._pesi[indicePeso]

            self._nextHop[indiceDestinazione] = n.get_nome()

class Nodi:

    # Costruttore
    def __init__(self):
        
        self._nodi = []

        self.chiedi_input()

        # Devo ordinare così da garantire il funzoinamento della ricerca binaria
        self.ordina()

    # Metodo per inserire le informazioni dei nodi
    def chiedi_input(self):
       
        dim = 0

        # Chiedo la dimensione dei nodi
        while dim < 1:
    
            dim = int(input('Quanti nodi hai? '))

        # Salvo i nodi in una lista
        self._nodi = [Nodo() for i in range(dim)]

    # Piccolo ordinamento Inseritionsort
    def ordina(self):

        for i in range(1, len(self._nodi)):

            j = i
         
            while j > 0 and self._nodi[j].get_nome() < self._nodi[j - 1].get_nome():
            
                self._nodi[j], self._nodi[j - 1] = self._nodi[j - 1], self._nodi[j]

                j -= 1

    # Ricerca binaria per cercare il nodo, di cui nome passato come parametro, nella lista dei nodi
    def cerca(self, nomeNodo):

        sinistra = 0
        destra = len(self._nodi) - 1

        # Fintantoché gli indici non si incontrano
        while sinistra <= destra:

            # Calcolo l'indice medio
            medio = int((sinistra + destra) / 2)

            # Se il _nome del nodo è uguale a quello passato come parametro
            if self._nodi[medio].get_nome() == nomeNodo:

                # Ritorno indice
                return medio

            # Altrimenti
            else:

                # Se il _nome del nodo con indice 'medio' è minore di quello passato come parametro
                if self._nodi[medio].get_nome() < nomeNodo:

                    # Cerco nella metà destra
                    sinistra = medio + 1

                # Altrimenti
                else:

                    # Cerco nella metà sinistra.
                    destra = medio - 1

        return -1

    # Metodo per trovare le migliori distanze a costo minore
    def controlla(self):

        # Andrò a controllare ogni nodo presente nella lista e per ciascuno lo confronto con la tabella del nodo di destinazione:
		# Se ho tre nodi A, B e C confronterò:
		# 	- A con le tabelle di B e C
		#   - B con le tabele di A e C
		#   - C con le tabelle di A e B

        # Un po' di matematica per sapere quante volte dovrei ricontrollare i nodi per avere il percorso migliore
        # Non so se effettivamente sia il metodo più efficace ma comunque mi permette di calcolare con meno cicli al posto di una complessità O(n^2)
        for i in range(len (self._nodi) - int(math.log2(len(self._nodi)))):

            # Scorro i nodi
            for nodo in self._nodi:
                
                # Per ogni nodo nel vettore scorro la sua tabella
                for j in range(len(nodo.get_destinazioni())):
                        
                    # Cerco l'indice del nodo nella lista
                    indice = self.cerca(nodo.get_destinazioni()[j])
                            
                    # Se il risultato della ricerca sarà un indice del vettore
                    if indice != -1:
                                
                        # Andrò a comparare i nodi
                        nodo.compareTo(self._nodi[indice])

                    # Altrimenti
                    else:
                                
                        # Lancio l'eccezione
                        raise ValueError("Mancano le informazioni del nodo '%s'" % (nodo.get_destinazioni()[j]))
                
    # Metodo che mi visualizza la tabella di routing di ogni nodo       
    def visualizza(self):

        # Scorro i nodi nella lista
        for nodo in self._nodi:

            # Visualizzo la sua tabella
            nodo.visualizza()

n = Nodi()

n.controlla()

n.visualizza()
