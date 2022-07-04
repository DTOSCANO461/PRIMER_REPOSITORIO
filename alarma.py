# EN ESTE DOCUMENTO EXPLORAMOS EL USO DE TKINTER PARA HACER UNA ALARMA 
# EL VIDEO ESTA BASADO EN https://www.youtube.com/watch?v=jqRHhWjKDD8


from playsound import playsound# playsound es el comando para reproducir musica
# no tiene nada que ver con tkinter que es dedicado a la parte grafica nada mas 


import tkinter 
#importamos tkinter... no ponemos nada de as tk

from tkinter import filedialog
def funcion_cualquiera(nombre):
    print("ejecutado.... funcion cualquiera" + nombre)
    


def run():

    ventana = tkinter.Tk()#creamos la ventana que va a contener todo lo necesario 
    ventana.geometry("300x300")# definimos el tamaño de la pantall
    
    
    # un gidget es un objeto basicamente, etiqueta, boton.. etc 
    etiqueta = tkinter.Label(ventana, text = "hola mundo!")
    etiqueta = tkinter.Label(ventana, text = "hola mundo!", bg = "gray")
    #bg significa back ground
    
    #PACK pone la etiqueta en la ventana con los detalles que pongas, colores etc 
    
    etiqueta.pack()#el metodo pack es el que te deja poner la etiqueta descrita 
    #pone todo en el centro sin mucha confioguracion
    etiqueta.pack(side = tkinter.RIGHT)# por ejemplo ahi movemos el mensaje a la derecha 
    # pack admite diferentes parametros 
    etiqueta.pack(side = tkinter.TOP, fill = tkinter.X)# asi podemos hacer que la etiqueta se "alarge"
   
    
    
    entrada_texto = tkinter.Entry(ventana, font = "Helvetica 20")
    entrada_texto.pack()
    def obtener_texto():
        contenido = entrada_texto.get()
        print(contenido)
   
    boton1 =tkinter.Button(ventana, text = "ejecutar funcion", command = lambda: funcion_cualquiera(entrada_texto.get()))
    boton1.pack()
   
   
    ventana.mainloop()#emepzamos a ejecutar un hilo queeste en loop monitoreando la ventana
   
    
    
    
    
    
    
    ventana.withdraw()
    file_path = filedialog.askopenfilename()
    playsound(file_path)
    


if __name__=='__main__':
    run()