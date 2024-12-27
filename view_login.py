from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import os
################################################################################################################################################
################################################### VENTANA DE LOGIN ###########################################################################

# En este fichero se lleva a cabo la creación de la ventana de logeo de usuarios.

class LoginApp:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Login')
        self.root.geometry('600x350+383+199')
        self.root.resizable(0,0)
        self.root.iconbitmap(self.rutas('imagenes','logosec_fondo.ico')) 
        self.create_widgets()

    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def create_widgets(self):
        # Creación de Frames
        self.frame_logo = Frame(self.root)
        self.frame_logo.config(width=250,height=350)
        self.frame_logo.place(x=0,y=0)

        self.frame_login = Frame(self.root)
        self.frame_login.config(width=350,height=350,bg='#EDE2E0')
        self.frame_login.place(x=250,y=0)

        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(width=3,height=350,background='#C18484')
        self.frame_divisor.place(x=250,y=0)

        # Creación de Labels
        self.label_user = ttk.Label(self.frame_login,text='Usuario')
        self.label_user.config(font=('century gothic',14,'bold'),background='#EDE2E0',foreground='#C18484')
        self.label_user.place(x=20,y=120)

        self.label_password = ttk.Label(self.frame_login,text='Contraseña')
        self.label_password.config(font=('century gothic',14,'bold'),background='#EDE2E0',foreground='#C18484')
        self.label_password.place(x=20,y=190)

        self.label_titulo = ttk.Label(self.frame_login,text='Inicio de Sesión')
        self.label_titulo.config(font=('century gothic',20,'bold'),background='#EDE2E0',foreground='#C18484')
        self.label_titulo.place(relx=0.5,rely=0.15,anchor='center')

        # Creación de Entry
        self.entry_user = Entry(self.frame_login)
        self.entry_user.config(font=('century gothic',14),background='#D3B9B4',width=16)
        self.entry_user.place(x=145,y=120)

        self.entry_password = Entry(self.frame_login)
        self.entry_password.config(font=('century gothic',14),background='#D3B9B4',show='*',width=16)
        self.entry_password.place(x=145,y=190)

        # Creación de Button
        self.login_button = Button(self.frame_login,text='Ingresar')
        self.login_button.config(font=('century gothic',14,'bold'),foreground='#C18484',bd=4,relief='groove',width=10)
        self.login_button.place(relx=0.5,rely=0.85,anchor='center')

        #Imagen
        ruta = self.rutas('imagenes','logo_sin_fondo.png')
        imagen = Image.open(ruta)
        imagen_modificada = imagen.resize((250,250))
        imagen_tk = ImageTk.PhotoImage(imagen_modificada)
        self.label_imagen = Label(self.frame_logo,image=imagen_tk)
        self.label_imagen.place(relx=0.5,rely=0.48,anchor='center')
        self.label_imagen.image = imagen_tk #Se crea una propiedad para evitar que python elimine la imagen

    def limpiar_caja_password (self):
        self.entry_password.delete(0,'end')


