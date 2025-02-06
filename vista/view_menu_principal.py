from tkinter import Button,Label,Frame
from tkinter import ttk
from PIL import Image,ImageTk
import sys
import os
################################################################################################################################################
################################################### VENTANA DE MENÚ PRINCIPAL ##################################################################

#En este fichero se encuentra la clase encargada de la creación del menú principal, en donde se puede acceder a todos los modulos del sistema.

class MenuPrincipal:

    def __init__(self,root):
        self.root = root
        self.root.title('Sistema de Gestión - BLA Estética')
        self.root.geometry('800x510+283+119')
        self.root.resizable(0,0)
        self.root.iconbitmap(self.rutas("../imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_encabezado = Frame(self.root)
        self.frame_encabezado.config(width=800,height=120)
        self.frame_encabezado.place(x=0,y=0)

        self.frame_menu = Frame(self.root)
        self.frame_menu.config(width=800,height=350)
        self.frame_menu.place(x=0,y=120)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(width=800,height=30,background='#D3B9B4')
        self.frame_informacion.place(x=0,y=480)

        #Imagen
        ruta = self.rutas('../imagenes','logo_sin_fondo.png')
        imagen = Image.open(ruta)
        imagen_modificada = imagen.resize((150,150))
        imagen_tk = ImageTk.PhotoImage(imagen_modificada)
        self.label_imagen = Label(self.frame_encabezado,image=imagen_tk)
        self.label_imagen.place(relx=0.1,rely=0.58,anchor='center')
        self.label_imagen.image = imagen_tk

        #Labels
        self.label_encabezado = Label(self.frame_encabezado,text='Sistema de Gestión - BLA Estética',font=('century gothic',28,'bold'),foreground='#C18484')
        self.label_encabezado.place(relx=0.58,rely=0.58,anchor='center')

        self.label_usuario = Label(self.frame_informacion,font=('century gothic',12),background='#D3B9B4')
        self.label_usuario.place(relx=0.1,rely=0.5,anchor='center')

        self.label_hora = Label(self.frame_informacion,font=('century gothic',12),background='#D3B9B4')
        self.label_hora.place(relx=0.75,rely=0.5,anchor='center')

        #Botones del menú
        #Se usa la librería PIL para abrir la imagen, realizarle un cambio de tamaño y luego mediante ImageTk darle el formato adecuado para cargarlo
        ruta = self.rutas('../imagenes','ventas.png')
        self.boton_ventas = Button(self.frame_menu)
        self.boton_ventas.config(text="Ventas",width=300,height=120,font=('century gothic',18,'bold'),background='#D3B9B4')
        imagen_venta_pil = Image.open(ruta)
        imagen_venta_resize = imagen_venta_pil.resize((50,50))
        imagen_venta_tk = ImageTk.PhotoImage(imagen_venta_resize)
        self.boton_ventas.config(image=imagen_venta_tk,compound='top',pady=10)
        self.boton_ventas.place(relx=0.08,rely=0.048)
        self.boton_ventas.image = imagen_venta_tk

        ruta = self.rutas('../imagenes','cuenta_corriente.png')
        self.boton_cuentacorriente = Button(self.frame_menu)
        self.boton_cuentacorriente.config(text="Cuentas\n Corrientes",width=300,height=120,font=('century gothic',18,'bold'),background='#D3B9B4')
        imagen_cuentacorriente_pil = Image.open(ruta)
        imagen_cuentacorriente_resize = imagen_cuentacorriente_pil.resize((50,50))
        imagen_cuentacorriente_tk = ImageTk.PhotoImage(imagen_cuentacorriente_resize)
        self.boton_cuentacorriente.config(image=imagen_cuentacorriente_tk,compound='top',pady=10)
        self.boton_cuentacorriente.place(relx=0.5,rely=0.048)
        self.boton_cuentacorriente.image = imagen_cuentacorriente_tk

        ruta = self.rutas('../imagenes','inventario.png')
        self.boton_inventario = Button(self.frame_menu)
        self.boton_inventario.config(text="Productos",width=300,height=120,font=('century gothic',18,'bold'),background='#D3B9B4')
        imagen_inventario_pil = Image.open(ruta)
        imagen_inventario_resize = imagen_inventario_pil.resize((50,50))
        imagen_inventario_tk = ImageTk.PhotoImage(imagen_inventario_resize)
        self.boton_inventario.config(image=imagen_inventario_tk,compound='top',pady=10)
        self.boton_inventario.place(relx=0.08,rely=0.52)
        self.boton_inventario.image = imagen_inventario_tk

        ruta = self.rutas('../imagenes','reportes.png')
        self.boton_reportes = Button(self.frame_menu)
        self.boton_reportes.config(text="Reportes",width=300,height=120,font=('century gothic',18,'bold'),background='#D3B9B4')
        imagen_reportes_pil = Image.open(ruta)
        imagen_reportes_resize = imagen_reportes_pil.resize((80,80))
        imagen_reportes_tk = ImageTk.PhotoImage(imagen_reportes_resize)
        self.boton_reportes.config(image=imagen_reportes_tk,compound='top',pady=10)
        self.boton_reportes.place(relx=0.5,rely=0.52)
        self.boton_reportes.image = imagen_reportes_tk
        
        ruta = self.rutas('../imagenes','administrador.png')
        self.boton_administrador = Button(self.frame_menu)
        self.boton_administrador.config(width=50,height=50,borderwidth=0)
        imagen_administrador_pil = Image.open(ruta)
        imagen_administrador_resize = imagen_administrador_pil.resize((40,40))
        imagen_administrador_tk = ImageTk.PhotoImage(imagen_administrador_resize)
        self.boton_administrador.config(image=imagen_administrador_tk,compound='top',pady=10)
        self.boton_administrador.place(relx=0.93,rely=0.865)
        self.boton_administrador.image = imagen_administrador_tk
