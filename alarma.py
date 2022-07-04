from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound


def run():
    import tkinter as tk

    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()    
    
    ruta = '/home/linux-t/Music/still_loving_you.mp3'
    playsound(ruta)
    


if __name__=='__main__':
    run()