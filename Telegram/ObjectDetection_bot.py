from imageai.Detection.keras_retinanet.utils.image import VisualEffect
from telepot import *
from telepot.loop import MessageLoop
from imageai.Detection import ObjectDetection, VideoObjectDetection
from pathlib import Path
import os
from datetime import date, datetime

TOKEN = '1558475944:AAF5VeWeV44q16vZnGcA_7t76GyZuQQlDUM'
MODEL_PATH = 'yolo.h5'

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]= "true"

bot = Bot(token = TOKEN)

def on_message(messaggio: dict):

    content_type, chat_type, chat_id = glance(messaggio)
    
    if content_type == 'photo':
        
        data = str(datetime.now().date()).replace(':', '-')

        ora = str(datetime.now().time()).replace(':', '-')

        bot.download_file(file_id = messaggio['photo'][-1]['file_id'], dest = 'Immagini\Originali\immagine da processare {} {}.png'.format(data, ora))
        
        bot.sendMessage(text = 'Processo la foto...', chat_id= chat_id)

        detections = image_detector.detectObjectsFromImage(input_image = 'Immagini\Originali\immagine da processare {} {}.png'.format(data, ora), output_image_path = 'Immagini\Processate\immagine processata {} {}.png'.format(data, ora), minimum_percentage_probability=60)

        bot.sendPhoto(chat_id = chat_id, photo = open('Immagini\Processate\immagine processata {} {}.png'.format(data, ora), 'rb'), caption = 'Processato!')
        
        if len(detections) == 0:

            # Si potrebbe chiedere all'utente di creare il riquadro e quindi avere più materiale per migliorare il dataset
            bot.sendMessage(text = 'Non sono riuscito a trovare nulla! :(', chat_id = chat_id)

        else:

            for i, detection in enumerate(detections):

                bot.sendMessage(text = '{}) Sono sicuro al {}% che sia {}'.format(i, str(detection['percentage_probability'])[:5], detection['name']), chat_id = chat_id)

    elif content_type == 'video':

        data = str(datetime.now().date()).replace(':', '-')

        ora = str(datetime.now().time()).replace(':', '-')

        bot.download_file(file_id = messaggio['video']['file_id'], dest = 'Video\\Originali\\video da processare {} {}.mp4'.format(data, ora))
        
        bot.sendMessage(text = 'Processo il video, ci impiegherà molto...', chat_id= chat_id)

        detections = video_detector.detectObjectsFromVideo(input_file_path = 'Video\\Originali\\video da processare {} {}.mp4'.format(data, ora), output_file_path = 'Video\\Processati\\video processato {} {}'.format(data, ora), minimum_percentage_probability=60)

        bot.sendVideo(chat_id = chat_id, video = open('Video\\Processati\\video processato {} {}.avi'.format(data, ora), 'rb'), caption = 'Processato!')
        
    elif content_type == 'text':

        if messaggio['text'].split()[0] == '/start':

            bot.sendMessage(text = "Invia una immagine o un video e cercherò di indovinare cosa c'è!", chat_id = chat_id)

def controlla_paths():

    paths = ['//Immagini', '//Video', '//Immagini//Originali', '//Immagini//Processate', '//Video//Originali', '//Video//Processati']

    for path in paths:

        path = Path(str(Path.cwd()) + path)

        if not path.exists():

            path.mkdir()

image_detector = ObjectDetection()
image_detector.setModelTypeAsYOLOv3()
image_detector.setModelPath(MODEL_PATH)
image_detector.loadModel()

video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(MODEL_PATH)
video_detector.loadModel(detection_speed="fast")

#MessageLoop(handle = bot.message_loop(run_forever = True, callback = on_message)).run_as_thread()
controlla_paths()