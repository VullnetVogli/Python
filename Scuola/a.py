from configparser import ConfigParser

configurazione = ConfigParser()

configurazione['CASA1'] = {'stanze': 'cucina;bagno;camera',
                           'temperature': '20,25;15,25;20,30'}

configurazione['CASA2'] = {'stanze': 'cucina;bagno;camera,soggiorno',
                           'temperature': '20,25;15,25;20,30;25,30'}

with open('proprietario.conf', 'w') as configfile:
    
    configurazione.write(configfile)

configurazione.read('E:\Programmazione\Python\Scuola\proprietario.conf')

for casa in configurazione.sections():
    
    stanze = configurazione[casa]['stanze'].split(';')
    
    for stanza in stanze:
    
        print('case/%s/%s/sensori/temperatura' % (casa, stanza))
    
    temperature = [temperatura_stanza.split(',') for temperatura_stanza in configurazione[casa]['temperature'].split(';')]

    print(temperature)
    