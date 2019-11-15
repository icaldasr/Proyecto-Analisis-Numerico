# ############################### #
#      INTERFAZ DE PROYECTO       #
# ANALISIS Y COMPUTACION NUMERICA #
# ############################### #

# Librerias o partes de librerias
from tkinter import *
from PIL     import ImageTk, Image
from tkinter import filedialog as tkfd
from tkinter import LEFT, TOP, X, FLAT, RAISED
from tkinter import messagebox
#from tkinter import Menu
#sudo apt-get install python3-pil python3-pil.imagetk

# Variables Globales
imagen         = None   # Imagen en la pantalla
imagen_cargada = None   # Label para cargar la imagen
hay_imagen     = False  # Booleano indica si hay imagen o no



# ######### #
# FUNCIONES #
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

def cargarImagen():
    """
AYUDA:
Funcion que aparece una ventana (depende de OS)
para cargar imagen de los archivos del usuario.
---
ENTRADA/SALIDA:
E: N/A (Input de Usuario en ventana)
S: Imagen imprimido en ventana
    """
    global imagen, imagen_cargada, hay_imagen
    # Abrir imagen con ventana dada por Sistema Operativo
    filename = tkfd.askopenfilename(title="Seleccione su imagen")
    imagen = Image.open(filename)
    # Escalar altura de imagen con ancho de 300 pixeles
    # y mantener Aspect Ratio o Razon de Aspecto
    basewidth = 300
    wpercent = (basewidth/float(imagen.size[0]))
    hsize = int((float(imagen.size[1])*float(wpercent)))
    imagen = imagen.resize((basewidth,hsize), Image.ANTIALIAS)
    # Resize solo funciona antes de convertir a PhotoImage
    imagen = ImageTk.PhotoImage(imagen)
    # Colocar imagen en ventana con Label
    if hay_imagen:
        imagen_cargada.destroy()
    imagen_cargada = Label(image=imagen)
    imagen_cargada.image = imagen
    #label.place(x = 250, y = 100)
    imagen_cargada.config(anchor=CENTER)
    imagen_cargada.pack()
    hay_imagen = True

def guardarImagen():
    """
AYUDA:
Funcion que guarda la imagen cargada en la ventana.
---
ENTRADA/SALIDA:
E: N/A (Input de Usuario en ventana)
S: Imagen imprimido en ventana
    """
    global imagen, imagen_cargada, hay_imagen
    if hay_imagen:
        a = tkfd.asksaveasfilename(title="Guarde",
                                                initialdir="C:/",
                                                defaultextension=".png"
                                                )
        #imagen.save(a)
    else:
        messagebox.showinfo("Aviso", "No hay imagen cargada en la ventana.")


    
# ### #
# GUI #
# ### #

## VENTANA
window = Tk()
window.title("Bezier Stickers")
window.geometry('800x700')
window.configure(background='light grey')

## MENU
menu = Menu(window)
file_items    = Menu(menu, tearoff=0)
tools_items   = Menu(menu, tearoff=0)
options_items = Menu(menu, tearoff=0)
# Tab File
file_items.add_command(label='Nuevo Archivo', command=lambda:tabButtonPlaceholder("A-NA"))
file_items.add_separator()
file_items.add_command(label='Editar Archivo', command=lambda:tabButtonPlaceholder("A-EA"))
# Tab Herramientas
tools_items.add_command(label='Snip', command=lambda:tabButtonPlaceholder("H-S"))
tools_items.add_command(label='Cut', command=lambda:tabButtonPlaceholder("H-C"))
tools_items.add_separator()
tools_items.add_command(label='Ayuda con Herramientas', command=lambda:tabButtonPlaceholder("H-AcH"))
# Tab Opciones
options_items.add_command(label='Cambiar Tamaño', command=lambda:tabButtonPlaceholder("O-CT"))
options_items.add_command(label='Cambiar Apariencia', command=lambda:tabButtonPlaceholder("O-CA"))
options_items.add_command(label='Opcion C', command=lambda:tabButtonPlaceholder("O-OC"))
options_items.add_separator()
options_items.add_command(label='Licencia', command=lambda:tabButtonPlaceholder("O-L"))
# Configurando Menu, agregando a Ventana
menu.add_cascade(label='Archivo', menu=file_items)
menu.add_cascade(label='Herramientas', menu=tools_items)
menu.add_cascade(label='Opciones', menu=options_items)
window.config(menu=menu)


## BOTONES
# Toolbar
# - Barra para herramientas fuera del Tab
# - Tienen iconos, deben tener tamaño 20x20 con resize
toolbar = Frame(window, bd=1, relief=RAISED)
# Cargar Imagen
#boton_cargar_imagen = Button(window,text="Cargar Imagen",command=cargarImagen)
#boton_cargar_imagen.grid(column=0,row=0)
cargar_imagen_icono = Image.open("imagen_cargar.png")
cargar_imagen_icono = cargar_imagen_icono.resize((20,20), Image.ANTIALIAS)
cargar_imagen_icono = ImageTk.PhotoImage(cargar_imagen_icono)
cargar_imagen_boton = Button(toolbar, image=cargar_imagen_icono, relief=FLAT, command=cargarImagen)
cargar_imagen_boton.image = cargar_imagen_icono
##cargar_imagen_boton = Button(toolbar, text="Cargar Imagen",width=20,command=cargarImagen)
cargar_imagen_boton.pack(side=LEFT, padx=2, pady=2)
# Guardar Imagen
guardar_imagen_icono = Image.open("imagen_guardar.png")
guardar_imagen_icono = guardar_imagen_icono.resize((20,20), Image.ANTIALIAS)
guardar_imagen_icono = ImageTk.PhotoImage(guardar_imagen_icono)
guardar_imagen_boton = Button(toolbar,image=guardar_imagen_icono,relief=FLAT, command=guardarImagen)
guardar_imagen_boton.image = guardar_imagen_icono
##cargar_imagen_boton = Button(toolbar, text="Cargar Imagen",width=20,command=cargarImagen)
guardar_imagen_boton.pack(side=LEFT, padx=2, pady=2)
# Herramientas Placeholder
b1 = Button(toolbar, text="Herramienta 1", width=20, command=buttonPlaceholder)
b1.pack(side=LEFT, padx=2, pady=2)
b2 = Button(toolbar, text="Herramienta 2", width=20, command=buttonPlaceholder)
b2.pack(side=LEFT, padx=2, pady=2)
b3 = Button(toolbar, text="Herramienta 3", width=20, command=buttonPlaceholder)
b3.pack(side=LEFT, padx=2, pady=2)
b4 = Button(toolbar, text="Herramienta 4", width=20, command=buttonPlaceholder)
b4.pack(side=LEFT, padx=2, pady=2)
# Terminar toolbar
toolbar.pack(side=TOP,fill=X)

## LOOP PARA MANTENER VENTANA
window.mainloop()



# ALGUNAS NOTAS
# - En el argumento de "command" para botones, use Lambda para
#   poder pasar argumentos a los Placeholder. Sin Lambda,
#   intentando pasar un argumento a la funcion da
#   comportamiento inesperado.
# - Variables globales indican que imagen esta cargada y
#   uno de ellos es un booleano que indica si hay una
#   imagen en la ventana o no


# VINCULOS VISITADOS
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# https://riptutorial.com/tkinter/example/29713/grid--#:~:text=tkinter%20grid()&text=The%20grid()%20geometry%20manager,%2C%20row%20%2C%20rowspan%20and%20sticky%20.&text=The%20column%20to%20put%20widget%20in.
# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# https://www.reddit.com/r/learnpython/comments/axscem/tkinter_resize_an_image_before_putting_it_on/
# http://zetcode.com/tkinter/menustoolbars/
# https://python-forum.io/Thread-Tkinter-How-do-I-center-this-text-in-tkinter
# https://pythonspot.com/tk-message-box/
# http://www.scoberlin.de/content/media/http/informatik/tkinter/x982-toolbars.htm
