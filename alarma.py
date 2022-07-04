from playsound import playsound
import tkinter 
from tkinter import filedialog


def run():

    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    playsound(file_path)
    


if __name__=='__main__':
    run()