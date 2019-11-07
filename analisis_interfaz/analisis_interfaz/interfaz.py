# ############################### #
#      INTERFAZ DE PROYECTO       #
# ANALISIS Y COMPUTACION NUMERICA #
# ############################### #

from tkinter import *
#from tkinter import Menu
from PIL import ImageTk, Image


# ######### #
# Funciones #
# ######### #

def tabButtonPlaceholder(nombreTabBoton):
    """
AYUDA:
Funcion "placeholder" para reemplazar mas tarde
con funciones distintas para cada boton.
---
ENTRADA/SALIDA:
E: String del nombre del boton
S: Impresion por pantalla a terminal Python
    """
    print("Presionaste este boton:",nombreTabBoton)


def buttonPlaceholder():
    """
AYUDA:
Funcion "placeholder" para reemplazar mas tarde
con funciones distintas para cada boton.
---
ENTRADA/SALIDA:
E: N/A
S: Impresion por pantalla a terminal Python
    """
    print("Presionaste un Boton.")


def loadImage():
    """
AYUDA:
Funcion "placeholder" para el boton de Cargar Imagen.
Carga una imagen en la carpeta de este archivo de codigo fuente.
---
ENTRADA/SALIDA:
E: N/A
S: Carga imagen "bunny.jpg" en la ventana
    """
    img_panel.configure(image=img_bunny)



# ### #
# GUI #
# ### #

## VENTANA
window = Tk()
window.title("Bezier Stickers")
window.geometry('800x800')
#window.configure(background='grey',fill="none")
window.configure(background='grey')

## MENU
menu = Menu(window)
file_items    = Menu(menu, tearoff=0)
tools_items   = Menu(menu, tearoff=0)
options_items = Menu(menu, tearoff=0)
# Tab File
file_items.add_command(label='Nuevo Archivo', command=lambda:tabButtonPlaceholder("NA"))
file_items.add_separator()
file_items.add_command(label='Editar Archivo', command=lambda:tabButtonPlaceholder("EA"))
# Tab Herramientas
tools_items.add_command(label='Snip', command=lambda:tabButtonPlaceholder("S"))
tools_items.add_command(label='Cut', command=lambda:tabButtonPlaceholder("C"))
tools_items.add_separator()
tools_items.add_command(label='Ayuda con Herramientas', command=lambda:tabButtonPlaceholder("AcH"))
# Tab Opciones
options_items.add_command(label='Cambiar Tamaño', command=lambda:tabButtonPlaceholder("CT"))
options_items.add_command(label='Cambiar Apariencia', command=lambda:tabButtonPlaceholder("CA"))
options_items.add_command(label='Opcion C', command=lambda:tabButtonPlaceholder("OC"))
options_items.add_separator()
options_items.add_command(label='Licencia', command=lambda:tabButtonPlaceholder("L"))
# Configurando Menu, agregando a Ventana
menu.add_cascade(label='Archivo', menu=file_items)
menu.add_cascade(label='Herramientas', menu=tools_items)
menu.add_cascade(label='Opciones', menu=options_items)
window.config(menu=menu)


## BOTONES
# Cargar Imagen
boton_cargar_imagen = Button(window,text="Cargar Imagen",command=loadImage)
boton_cargar_imagen.grid(column=0,row=0)
# Herramientas
label_herramientas = Label(window, text="Herramientas")
label_herramientas.grid(column=0,row=1)
boton_herramienta_1 = Button(window,text="Herramienta 1",command=buttonPlaceholder)
boton_herramienta_1.grid(column=0,row=2)
boton_herramienta_2 = Button(window,text="Herramienta 2",command=buttonPlaceholder)
boton_herramienta_2.grid(column=1,row=2)
boton_herramienta_3 = Button(window,text="Herramienta 3",command=buttonPlaceholder)
boton_herramienta_3.grid(column=0,row=3)
boton_herramienta_4 = Button(window,text="Herramienta 4",command=buttonPlaceholder)
boton_herramienta_4.grid(column=1,row=3)
# Recortar
boton_recortar = Button(window,text="Recortar",command=buttonPlaceholder)
boton_recortar.grid(column=0,row=4)


## IMAGEN
# Deja Imagen cargada, se reemplaza con una funcion loadImage
img_path = "scenery.jpg"
img = ImageTk.PhotoImage(Image.open(img_path))
img_panel = Label(window,image=img)
#panel.pack(side="right",expand="false",fill="none")
#panel.pack(side="right")
img_panel.grid(column=2,row=5)
# Imagen que la funcion loadImage utiliza para reemplazo
img_path_bunny = "bunny.jpg"
img_bunny = ImageTk.PhotoImage(Image.open(img_path_bunny))


## LOOP PARA MANTENER VENTANA
window.mainloop()



# ALGUNAS NOTAS
# - En el argumento de "command" para botones, use Lambda para
#   poder pasar argumentos a los Placeholder. Sin Lambda,
#   intentando pasar un argumento a la funcion da
#   comportamiento inesperado.


# VINCULOS VISITADOS
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# https://riptutorial.com/tkinter/example/29713/grid--#:~:text=tkinter%20grid()&text=The%20grid()%20geometry%20manager,%2C%20row%20%2C%20rowspan%20and%20sticky%20.&text=The%20column%20to%20put%20widget%20in.
# https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
# https://stackoverflow.com/questions/29523018/display-new-image-on-tkinter-button-command
