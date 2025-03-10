##############################################################################
# Importaciones
##############################################################################

from tkinter import Frame, Label, Button, Entry
from tkinter import ttk
from vista.view_config import ConfigView

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
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen('logosec_fondo.ico')
        )
        self.widgets()
    

    def widgets(self):
        
        ''' Metodo que contiene los widgets que conforman la ventana del
            modulo de administrador
        '''
        
        # Referencia a imagenes
        self.img['crearusuario'] = ConfigView.formateo_imagen(
            'crear_usuario.png', 30, 30
        )
        self.img['eliminar'] = ConfigView.formateo_imagen(
            'eliminar.png', 30, 30
        )
        
        # Frames
        self.frame_admin = Frame(self.root)
        self.frame_admin.config(
            width=300, height=450, background=ConfigView.clr['soft']
        )
        self.frame_admin.place(relx=0,rely=0)
        
        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(
            width=300, height=2, background=ConfigView.clr['hard']
        )
        self.frame_divisor.place(relx=0,rely=0.4)

        # Botones
        self.boton_crearusuario = Button(self.frame_admin)
        self.boton_crearusuario.config(
            text='Crear Usuario',
            font=ConfigView.fnt['text14-b'],
            width=230,
            padx=15,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['crearusuario'],
            compound='left'
        )
        self.boton_crearusuario.place(relx=0.5,rely=0.1,anchor='center')

        self.boton_eliminarusuario = Button(self.frame_admin)
        self.boton_eliminarusuario.config(
            text='Eliminar Cuenta',
            font=ConfigView.fnt['text14-b'],
            width=230,
            padx=15,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['eliminar'],
            compound='left'
        )
        self.boton_eliminarusuario.place(relx=0.5,rely=0.2,anchor='center')

        self.boton_eliminarbd = Button(self.frame_admin)
        self.boton_eliminarbd.config(
            text='Limpiar Base de Datos',
            font=ConfigView.fnt['text14-b'],
            width=230,
            padx=15,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['eliminar'],
            compound='left'
        )
        self.boton_eliminarbd.place(relx=0.5,rely=0.35,anchor='center')


class InterfazNuevoUsuario:
    
    ''' Clase para la creacion de la ventana de creacion de nuevos usuarios
        del sistema
    '''
    def __init__(self,root):
        
        self.root = root
        self.root.title('Admin - Nueva Cuenta')
        self.root.geometry('400x220+483+264')
        self.root.resizable(False,False)
        self.root.iconbitmap(
            ConfigView.formateo_imagen('logosec_fondo.ico')
        )
        self.widgets()


    def widgets(self):
        # Frames
        self.frame_nuevacuenta = Frame(self.root)
        self.frame_nuevacuenta.config(
            width=400, height=220, background=ConfigView.clr['soft']
        )
        self.frame_nuevacuenta.place(x=0,y=0)

        # Labels
        self.labelcuenta = Label(
            self.frame_nuevacuenta,
            text='Cuenta',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.labelcuenta.place(x=15, y=20)

        self.labelcontraseña = Label(
            self.frame_nuevacuenta,
            text='Contraseña',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.labelcontraseña.place(x=15,y=70)

        self.labelrol = Label(
            self.frame_nuevacuenta,
            text='Rol',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.labelrol.place(x=15,y=120)

        #Entries
        self.entrycuenta = Entry(
            self.frame_nuevacuenta,
            font=ConfigView.fnt['text12'],
            width=19
        )
        self.entrycuenta.place(x=150,y=20)

        self.entrycontraseña = Entry(
            self.frame_nuevacuenta,
            font=ConfigView.fnt['text12'],
            width=19
        )
        self.entrycontraseña.place(x=150,y=70)

        self.entryrol = ttk.Combobox(
            self.frame_nuevacuenta, width=18, font=ConfigView.fnt['text12']
        )
        self.entryrol.config(values=['Administrador','Vendedor','Dueño'])
        self.entryrol.place(x=150,y=120)

        # Boton
        self.boton_crearusuario = Button(self.frame_nuevacuenta)
        self.boton_crearusuario.config(
            text='Crear',
            font=ConfigView.fnt['text14-b'],
            width=10,
            background=ConfigView.clr['medium'],
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
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()


    def widgets(self):
        # Frames
        self.frame_modificacion = Frame(self.root)
        self.frame_modificacion.config(
            width=350, height=220, background=ConfigView.clr['soft']
        )
        self.frame_modificacion.place(x=0,y=0)

        # Labels
        self.labelcuenta = Label(
            self.frame_modificacion,
            text='Cuenta',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.labelcuenta.place(x=15,y=20)

        #Entries
        self.entrycuenta = ttk.Combobox(
            self.frame_modificacion, width=18, font=ConfigView.fnt['text12']
        )
        self.entrycuenta.place(x=110,y=20)

        # Boton
        self.boton_modificarcontraseña = Button(self.frame_modificacion)
        self.boton_modificarcontraseña.config(
            text='Eliminar',
            font=ConfigView.fnt['text14-b'],
            width=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove'
        )
        self.boton_modificarcontraseña.place(
            relx=0.5, rely=0.4, anchor='center'
        )
        