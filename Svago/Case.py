import csv
from random import randint
import datetime
import time
from threading import Thread

SLEEP = 1
RANGE = (-10, 40)
MIN, MAX = -8, 38
PATH = 'E:\Programmazione\Python\Svago\case.csv'

def scrivi_con_csv():

	with open(PATH, 'w+', newline='') as excel:

		csv_writer = csv.writer(excel, dialect='excel', delimiter=';', quotechar=' ')

		for casa in range(10): 

			for stanza in range(5):

				csv_writer.writerow(['casa' + str(casa), 'stanza' + str(stanza), str(randint(RANGE[0], RANGE[1])), str(datetime.datetime.date()), str(datetime.datetime.now().time())])

		excel.close()

def scrivi_senza_csv():

	with open(PATH, 'a+') as excel:

		for casa in range(5):

			for stanza in range(5):
																																							# giorno,mese,anno ; ora,minuto,secondo,microsecondo
				excel.writelines(['casa' + str(casa), ';stanza' + str(stanza), ';' + str(randint(RANGE[0], RANGE[1])), ';' + str(datetime.datetime.now().strftime("%d/%m/%Y;%H:%M:%S:%f")), '\n'])

				time.sleep(SLEEP) # ogni quanto ricontrolla la temperatura

			excel.close()

		time.sleep(5)

def leggi():
	print('leggo')
	with open(PATH, 'r') as excel:
		
		case = excel.readlines()

		for casa in case:
				
			casa = casa.split(';')

			if int(casa[2]) > MAX:

				print('Temperatura  alta in ', casa[0])

			elif int(casa[2]) < MIN:

				print('Temperatura bassa in ', casa[0])


if __name__ == "__main__":
	
	Thread(leggi()).start()

	Thread(scrivi_senza_csv()).start()

	print('ok')
