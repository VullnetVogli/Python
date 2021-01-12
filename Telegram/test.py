from datetime import datetime

data = str(datetime.now().date()).replace(':', '-')

ora = str(datetime.now().time()).replace('.', '-')

print(f'Immagini\Originali\immagine da processare {data} {ora}.png')