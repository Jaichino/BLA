##############################################################################
# Importaciones
##############################################################################

from tkinter import Entry,Label,Button,Frame
from tkinter import ttk
from vista.view_config import ConfigView

############################ VISTA DEL LOGIN #################################

''' En este fichero se lleva a cabo la creacion de la ventana de logeo de 
    usuarios.
'''

class LoginApp:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Login')
        self.root.geometry('600x350+383+199')
        self.root.resizable(0, 0)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        ) 
        self.widgets()


    def widgets(self):
        
        # Referencia a imagenes
        self.img['logo'] = ConfigView.formateo_imagen(
            ConfigView.img['logosinfondo'], 250, 250
        )
        
        # Frames
        self.frame_logo = Frame(self.root)
        self.frame_logo.config(width=250, height=350)
        self.frame_logo.place(x=0, y=0)

        self.frame_login = Frame(self.root)
        self.frame_login.config(
            width=350, height=350, bg=ConfigView.clr['soft']
        )
        self.frame_login.place(x=250, y=0)

        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(
            width=3, height=350, background=ConfigView.clr['hard']
        )
        self.frame_divisor.place(x=250, y=0)

        # Creación de Labels
        self.label_user = ttk.Label(self.frame_login, text='Usuario')
        self.label_user.config(
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_user.place(x=20, y=120)

        self.label_password = ttk.Label(self.frame_login, text='Contraseña')
        self.label_password.config(
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_password.place(x=20, y=190)

        self.label_titulo = ttk.Label(
            self.frame_login, text='Inicio de Sesión'
        )
        self.label_titulo.config(
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5, rely=0.15, anchor='center')

        # Creación de Entry
        self.entry_user = Entry(self.frame_login)
        self.entry_user.config(
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['medium'], 
            width=16
        )
        self.entry_user.place(x=145, y=120)

        self.entry_password = Entry(self.frame_login)
        self.entry_password.config(
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['medium'],
            show='*',
            width=16
        )
        self.entry_password.place(x=145, y=190)

        # Creación de Button
        self.login_button = Button(self.frame_login, text='Ingresar')
        self.login_button.config(
            font=ConfigView.fnt['text14-b'],
            foreground=ConfigView.clr['hard'],
            bd=4,
            relief='groove',
            width=10
        )
        self.login_button.place(relx=0.5, rely=0.85, anchor='center')

        #Imagen
        self.label_imagen = Label(self.frame_logo, image=self.img['logo'])
        self.label_imagen.place(relx=0.5, rely=0.48, anchor='center')


    # Metodo para limpiar entry
    def limpiar_caja_password (self):
        self.entry_password.delete(0,'end')
