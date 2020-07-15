import requests
from bs4 import BeautifulSoup
import time
import random

'''
pip install requests
pip install beautifulsoup4
'''


'''
Le prime tre lettere del Codice fiscale sono prese dalle consonanti del cognome o dei cognomi se sono più di uno, in caso di consonanti insufficienti vengono prese anche le vocali, che però vengono sempre dopo le consonanti;
Le seconde tre lettere sono prese dalle consonanti del nome o dei nomi se sono più di uno, se il nome non ha abbastanza consonanti vengono prese anche le vocali, nel caso di due nomi separati da virgola verrà considerato solo il primo nome;
I due numeri coincidono con l’anno di nascita;
Una lettera indica il mese di nascita (a=gennaio, b=febbraio, c=marzo, ecc.);
Altri due numeri indicano il giorno di nascita, per le donne bisogna aggiungere 40, quindi se il giorno di nascita è l’8, le due cifre saranno 48;
Una lettera e tre numeri indicano il Comune di nascita, per chi è nato all’estero la sigla inizia per Z ed è seguita dal numero che identifica lo Stato di nascita;
Un carattere alfabetico di controllo generato attraverso uno speciale algoritmo e che chiude ogni cf valido.

'''

codiceFiscale = ''

def cognome():

    temp = ''
    cognome = ''

    while "123456789" in cognome or cognome is '':
        cognome = input('Inserisci il tuo cognome: ').strip().upper()

        if "123456789" in cognome or cognome is '':
            print('Errore!')

    i = 0
    
    if len(cognome) > 2:

        while len(temp) < 3:
            
            if i is len(cognome):
                i = 0
                
                while len(temp) < 3:
                    if cognome[i] is 'A' or cognome[i] is 'E' or cognome[i] is 'I' or cognome[i] is 'O' or cognome[i] is 'U' and cognome[i] not in temp:
                        temp += cognome[i]
                    i += 1
            else:
                if cognome[i] is not 'A' and cognome[i] is not 'E' and cognome[i] is not 'I' and cognome[i] is not 'O' and cognome[i] is not 'U' and cognome[i]:
                    temp += cognome[i]         

            i += 1

    else:
        temp = cognome

        while len(temp) < 3:
            temp += 'X'

    return temp

def nome(codiceFiscale): 

    temp = ''
    nome = ''

    while "123456789" in nome or nome is '':
        nome = input('Inserisci il tuo nome: ').strip().upper()

        if "123456789" in nome or nome is '':
            print('Errore!')

    i = 0

    while len(temp) < 3:

        if len(nome) > 2:

            if i is not len(nome): # vuol dire sono finite le consonanti

                if nome[i] is not 'A' and nome[i] is not 'E' and nome[i] is not 'I' and nome[i] is not 'O' and nome[i] is not 'U' and nome[i] not in temp:
                    temp += nome[i]
                

            else:
                i = 0
                
                while len(temp) < 3:
                    if nome[i] is 'A' or nome[i] is 'E' or nome[i] is 'I' or nome[i] is 'O' or nome[i] is 'U' and nome[i] not in temp:
                        temp += nome[i]

                    elif i == len(temp)-1 and nome[i] in temp:
                        temp += nome[i]

                    i += 1        

            i += 1
        
        else:

            temp = nome
            
            while len(temp) < 3:
                temp += 'X'


   
    codiceFiscale += temp
    return codiceFiscale

def dataNascita(codiceFiscale):

    mesi        = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
    giorniMesi  = [    31,                  31,       30,      31,       30,        31,        31,       30,         31,          30,        31    ] # febbraio lo mettiamo dopo perché può essere un anno bisestile :)
    lettereMesi = [    'A',      'B',      'C',       'D',    'E',       'H',       'L',      'M',      'P',        'R',         'S',       'T'    ]

    if int(time.strftime("%Y")) % 4 == 0:
        giorniMesi.insert(2, 29)
    else:
        giorniMesi.insert(2, 28)


    anno = 0
    mese = ''
    giorno = 0
    sesso = ''

    while anno < 1919 or anno > int(time.strftime("%Y")):
        anno = int(input("Inserisci l'anno di nascita: "))

        if anno < 1919 or anno > int(time.strftime("%Y")):
            print('Errore!')
    
    while mese not in mesi:
        mese = input('Inserisci il nome del mese di nascita: ').capitalize()

        if mese not in mesi:
            print('Errore!')

    while giorno < 1 or giorno > giorniMesi[mese.index(mese) + 1]:
        giorno = int(input('Inserisci il giorno: '))

        if giorno < 1 or giorno > giorniMesi[mese.index(mese) + 1]:
            print('Errore!')

    while sesso != 'Maschio' and sesso != 'Femmina' and sesso != 'M' and sesso != 'F':
        sesso = input('Inserisci il sesso: ').capitalize()

        if sesso != 'Maschio' and sesso != 'Femmina' and sesso != 'M' and sesso != 'F':
            print('Errore!')

    if sesso[0] is 'F':
        giorno += 40

    anno   = str(anno)
    mese   = str(mese)
    giorno = str(giorno)

    if int(giorno) < 10:                     # se il giorno di nascita è minore di 10 deve venire fuori, per esempio, 01 e non 1
        giorno = '0' + giorno

    codiceFiscale += anno[2:4]
    codiceFiscale += lettereMesi[mesi.index(mese)]
    codiceFiscale += giorno

    return codiceFiscale

def codice_comune(codiceFiscale):

    stato = ''

    while '123456789' in stato or stato is '':
        stato = input('Inserisci lo stato: ').capitalize().replace(' ', '-')

    # per la parte del codice del comune ho realizzato un web scraper :)
    URL = 'http://www.comuniitaliani.it/' + stato + '.htm'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    temp = ''
    i = 0

    for tag in soup.findAll('td'):
        
        if i == 17:
            temp = tag.get_text()

        i+=1

    codiceFiscale += temp

    return codiceFiscale

def ultima_lettera(codiceFiscale):

    # ho fatto un random perché non avevo voglia di calcolare :D
    print(cognome().__getattribute__(cognome))

    temp = random.randint(65, 90)
    
    temp = chr(temp)

    codiceFiscale += temp

    return codiceFiscale

print("Benvenuto nel mio calcolatore del codice fiscale! Per ora funziona solo con i comuni italiani e l'ultima lettera è random :(")

codiceFiscale = cognome()
'''
codiceFiscale = nome(codiceFiscale)
codiceFiscale = dataNascita(codiceFiscale)
codiceFiscale = codice_comune(codiceFiscale)
'''
codiceFiscale = ultima_lettera(codiceFiscale)

print('Codice Fiscale: ', codiceFiscale)
