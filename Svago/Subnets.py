import math

'''
------ PROGRAMMA COMPATIBILE SOLO CON PYTHON 3.7+ ------

Autore: Vogli Vullnet

Consegna: Scrivere un programma in Python che dato un indirizzo IP restituisca:

    * subnet mask
    * classe
    * rete di appartenenza
    * indirizzo broadcast
    * ip gateway

Metodo di suddivisione: CIDR

'''

def calcola_classe():

    global ip
    global classe
    global classi

    for i in classi:
        
        # Se il primo elemento (il numero massimo dell'host di quella classe) della tuple della classe è maggiore del primo otteto dell'host
        if i[1] > int(ip[0]):

            print("L'indirizzo ip: ", ip, " è di calsse: ", i[0])

            # Suddivido la subnet della classe di appartenenza e la assegno alla lista classe (preferisco fare così perché successivamente risulta più facile l'end bit a bit)
            classe = i[2].split('.')

            # Aggiungo l'indice della classe all'indirizzo dioo appertenenza, mi servirà per non effettuare condizioni in più per la subnet.
            # Il +2 mi serve dato che le classi sono tre e non quattro
            indirizzo_appartenenza.append(classi.index(i) + 2)
           
            break           # ho dovuto 

def calcola_indirizzo_appartenenza():

    global ip
    global classe
    global indirizzo_appartenenza
    
    for i in zip(ip, classe):
       
        # Appendo il risultato dell'operazione end bit a bit a 'indirizzo_appartenenza'
        indirizzo_appartenenza.append(int(i[0]) & int(i[1]))
    
    # Stampo l'indirizzo di appartenenza (senza la classe di cui fa parte)
    print("L'indirizzo di appartenenza è: ", indirizzo_appartenenza[1:5])

def calcola_subnet_mask():

    global ip
    global subnet_mask
    global classe

    suddivisioni = int(input('Quante subnets vorresti creare? '))

    # Utilizzo un minimo di matematica per calcolarmi quanti bit mi serviranno per tot sottoclassi
    bit = math.ceil(math.log2(suddivisioni))
 
    if bit < 0 or bit > 6:

        print('Errore nel calcolo della subnet!')

        return

    subnet_mask += bit

    for i in classe:

        # Faccio l'end bit a bit con l'indirizzo di classe e conto gli 1 presenti
        subnet_mask += str(bin(int(i))).count('1')

    print("La subnet mask è: /%d\n" % subnet_mask)
    
    calcola_subnets(suddivisioni, bit)

def calcola_subnets(suddivisioni, bit):
    
    global indirizzo_appartenenza
    
    aumento = 256 / pow(2, bit)

    print('N   Indirizzo  \t\t\t\t Gateway             \t\t\t Hosts            \t\t\t\t Broadcast')

    for i in range(suddivisioni):
     
        # CALCOLO INDIRIZZO DI APPARTENENZA
        # Cambio la rete di appartenenza per ogni subnet
        indirizzo_appartenenza[indirizzo_appartenenza[0]] = i * aumento


        # CALCOLO GATEWAY
        # Se mettessi gateway = indirizzo_appartenenza punterebbe alla stessa cella
        gateway = [j for j in indirizzo_appartenenza[1::]]

        # Per determinare il gateway prendo indirizzo di appartenenza e lo aumento di uno
        gateway[3] = gateway[3] + 1


        # CALCOLO DEL BROADCAST
        broadcast = [j for j in gateway]
        
        for j in range(indirizzo_appartenenza[0], 4):

            broadcast[j] = 255

        # L'indirizzo di broadcast sarà l'indirizzo di rete successivo - 1
        broadcast[indirizzo_appartenenza[0] - 1] = (i + 1) * aumento - 1 
        
        
        # CALCOLO IL RANGE DEGLI HOSTS
        hosts = [j for j in broadcast]

        for j in range(indirizzo_appartenenza[0], 4):

            hosts[j] = (0, 255)

        # Calcolo l'indirizzo di appartenenza successivo
        hosts[indirizzo_appartenenza[0] - 1] = (i * aumento, broadcast[indirizzo_appartenenza[0] - 1])

        # Calcolo l'ultimo otteto degli hosts
        hosts[3] = (gateway[3] + 1, broadcast[3] - 1)

        print('%d - %s     \t\t %s \t\t %s \t\t %s' % (i, indirizzo_appartenenza[1::], gateway, hosts, broadcast))

    print()


ip = []

while len(ip) != 4:

    ip = input("Inserisci l'indirizzo ip: ").split('.')

classi = [('A', 127, '255.0.0.0'), ('B', 191, '255.255.0.0'), ('C', 223, '255.255.255.0')]

classe = []

indirizzo_appartenenza = []

subnet_mask = 0

calcola_classe()

calcola_indirizzo_appartenenza()

calcola_subnet_mask()