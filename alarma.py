from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound

def run():
    ruta = '/home/linux-t/Music/still_loving_you.mp3'
    print("jejeje")
    playsound(ruta)


if __name__=='__main__':
    run()