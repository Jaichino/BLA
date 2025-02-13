import sys
import os
from tkinter import Frame, Label, Button, Entry
from tkinter import ttk
from PIL import Image,ImageTk

######################## VENTANA DE ADMINISTRADOR ############################
''' En este fichero se desarrolla la interfaz para el menu del administrador, 
    donde se podran crear nuevas cuentas, modificar contraseñas, asignar 
    roles, limpiar base de datos, etc.
'''

class InterfazAdmin:

    ''' Clase para la creacion de la ventana principal de administrador,
        desde la cual se accede a las demas ventanas del modulo
    '''
    def __init__(self,root):
        self.root = root
        self.root.title('Administrador')
        self.root.geometry('300x300+533+224')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas('../imagenes','logosec_fondo.ico'))
        self.widgets()
    
    def rutas(self, *paths):

        ''' Metodo para el manejo de rutas de imagenes a la hora de
            generar el ejecutable con Pyinstaller
        '''
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)

    def widgets(self):
        
        ''' Metodo que contiene los widgets que conforman la ventana del
            modulo de administrador
        '''
        # Frames
        self.frame_admin = Frame(self.root)
        self.frame_admin.config(width=300,height=450,background='#EDE2E0')
        self.frame_admin.place(relx=0,rely=0)
        
        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(width=300,height=2,background='#C18484')
        self.frame_divisor.place(relx=0,rely=0.4)

        # Botones
        ruta = self.rutas('../imagenes','crear_usuario.png')
        self.boton_crearusuario = Button(self.frame_admin)
        self.boton_crearusuario.config(
            text='Crear Usuario',
            font=('century gothic',14,'bold'),
            width=230,
            padx=15,
            background='#D3B9B4',
            bd=2,
            relief='groove'
        )
        imagen_crearusuario_pil = Image.open(ruta)
        imagen_crearusuario_resize = imagen_crearusuario_pil.resize((30,30))
        imagen_crearusuario_tk = ImageTk.PhotoImage(
            imagen_crearusuario_resize
        )
        self.boton_crearusuario.config(
            image=imagen_crearusuario_tk,
            compound='left',
            anchor='center'
        )
        self.boton_crearusuario.place(relx=0.5,rely=0.1,anchor='center')
        self.boton_crearusuario.image = imagen_crearusuario_tk

        ruta = self.rutas('../imagenes','eliminar.png')
        self.boton_eliminarusuario = Button(self.frame_admin)
        self.boton_eliminarusuario.config(
            text='Eliminar Cuenta',
            font=('century gothic',14,'bold'),
            width=230,
            padx=15,
            background='#D3B9B4',
            bd=2,
            relief='groove'
        )
        imagen_eliminarusuario_pil = Image.open(ruta)
        imagen_eliminarusuario_resize = (
            imagen_eliminarusuario_pil.resize((30,30))
        )
        imagen_eliminarusuario_tk = ImageTk.PhotoImage(
            imagen_eliminarusuario_resize
        )
        self.boton_eliminarusuario.config(
            image=imagen_eliminarusuario_tk,
            compound='left',
            anchor='center'
        )
        self.boton_eliminarusuario.place(relx=0.5,rely=0.2,anchor='center')
        self.boton_eliminarusuario.image = imagen_eliminarusuario_tk

        ruta = self.rutas('../imagenes','eliminar.png')
        self.boton_eliminarbd = Button(self.frame_admin)
        self.boton_eliminarbd.config(
            text='Limpiar Base de Datos',
            font=('century gothic',14,'bold'),
            width=230,
            padx=15,
            background='#D3B9B4',
            bd=2,
            relief='groove'
        )
        imagen_eliminarbd_pil = Image.open(ruta)
        imagen_eliminarbd_resize = imagen_eliminarbd_pil.resize((30,30))
        imagen_eliminarbd_tk = ImageTk.PhotoImage(imagen_eliminarbd_resize)
        self.boton_eliminarbd.config(
            image=imagen_eliminarbd_tk,
            compound='left',
            anchor='center'
        )
        self.boton_eliminarbd.place(relx=0.5,rely=0.35,anchor='center')
        self.boton_eliminarbd.image = imagen_eliminarbd_tk


class InterfazNuevoUsuario:
    
    ''' Clase para la creacion de la ventana de creacion de nuevos usuarios
        del sistema
    '''
    def __init__(self,root):
        
        self.root = root
        self.root.title('Admin - Nueva Cuenta')
        self.root.geometry('400x220+483+264')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas('../imagenes','logosec_fondo.ico'))
        self.widgets()

    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)

    def widgets(self):
        # Frames
        self.frame_nuevacuenta = Frame(self.root)
        self.frame_nuevacuenta.config(
            width=400, height=220, background='#EDE2E0'
        )
        self.frame_nuevacuenta.place(x=0,y=0)

        # Labels
        self.labelcuenta = Label(
            self.frame_nuevacuenta,
            text='Cuenta',
            font=('century gothic',14),
            background='#EDE2E0'
        )
        self.labelcuenta.place(x=15, y=20)

        self.labelcontraseña = Label(
            self.frame_nuevacuenta,
            text='Contraseña',
            font=('century gothic',14),
            background='#EDE2E0'
        )
        self.labelcontraseña.place(x=15,y=70)

        self.labelrol = Label(
            self.frame_nuevacuenta,
            text='Rol',
            font=('century gothic',14),
            background='#EDE2E0'
        )
        self.labelrol.place(x=15,y=120)

        #Entries
        self.entrycuenta = Entry(
            self.frame_nuevacuenta,
            font=('century gothic',14),
            width=19
        )
        self.entrycuenta.place(x=150,y=20)

        self.entrycontraseña = Entry(
            self.frame_nuevacuenta,
            font=('century gothic',14),
            width=19
        )
        self.entrycontraseña.place(x=150,y=70)

        self.entryrol = ttk.Combobox(
            self.frame_nuevacuenta, width=18, font=('century gothic',14)
        )
        self.entryrol.config(values=['Administrador','Vendedor','Dueño'])
        self.entryrol.place(x=150,y=120)

        # Boton
        self.boton_crearusuario = Button(self.frame_nuevacuenta)
        self.boton_crearusuario.config(
            text='Crear',
            font=('century gothic',14,'bold'),
            width=10,
            background='#D3B9B4',
            bd=2,
            relief='groove'
        )
        self.boton_crearusuario.place(relx=0.5,rely=0.85,anchor='center')


class InterfazEliminar:

    ''' Clase destinada a la creacion de la ventana de eliminacion de
        cuentas de usuario existentes en el sistema
    '''
    
    def __init__(self,root):
        self.root = root
        self.root.title('Admin - Eliminar Cuenta')
        self.root.geometry('350x120+508+314')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas("../imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)

    def widgets(self):
        # Frames
        self.frame_modificacion = Frame(self.root)
        self.frame_modificacion.config(
            width=350, height=220, background='#EDE2E0'
        )
        self.frame_modificacion.place(x=0,y=0)

        # Labels
        self.labelcuenta = Label(
            self.frame_modificacion,
            text='Cuenta',
            font=('century gothic',14),
            background='#EDE2E0'
        )
        self.labelcuenta.place(x=15,y=20)

        #Entries
        self.entrycuenta = ttk.Combobox(
            self.frame_modificacion, width=18, font=('century gothic',14)
        )
        self.entrycuenta.place(x=110,y=20)

        # Boton
        self.boton_modificarcontraseña = Button(self.frame_modificacion)
        self.boton_modificarcontraseña.config(
            text='Eliminar',
            font=('century gothic',14,'bold'),
            width=10,
            background='#D3B9B4',
            bd=2,
            relief='groove'
        )
        self.boton_modificarcontraseña.place(
            relx=0.5, rely=0.4, anchor='center'
        )


