##############################################################################
# Importaciones
##############################################################################

from tkinter import Button,Label,Frame
from tkinter import ttk
from vista.view_config import ConfigView

######################## VISTA DEL MENU PRINCIPAL ############################

''' En este fichero se encuentra la clase encargada de la creacion del menu
    principal, en donde se puede acceder a todos los modulos del sistema.
'''

class MenuPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Gestión - BLA Estética')
        self.root.geometry('800x510+283+119')
        self.root.resizable(0, 0)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['ventas'] = ConfigView.formateo_imagen(
            ConfigView.img['ventas'], 50, 50
        )
        self.img['cuentacorriente'] = ConfigView.formateo_imagen(
            ConfigView.img['ccorriente'], 50, 50
        )
        self.img['inventario'] = ConfigView.formateo_imagen(
            ConfigView.img['inventario'], 50, 50
        )
        self.img['reportes'] = ConfigView.formateo_imagen(
            ConfigView.img['reportes'], 80, 80
        )
        self.img['admin'] = ConfigView.formateo_imagen(
            ConfigView.img['admin'], 40, 40
        )
        self.img['logo'] = ConfigView.formateo_imagen(
            ConfigView.img['logosinfondo'], 150, 150
        )

        #Frames
        self.frame_encabezado = Frame(self.root)
        self.frame_encabezado.config(width=800, height=120)
        self.frame_encabezado.place(x=0, y=0)

        self.frame_menu = Frame(self.root)
        self.frame_menu.config(width=800, height=350)
        self.frame_menu.place(x=0, y=120)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=800, height=30, background=ConfigView.clr['medium']
        )
        self.frame_informacion.place(x=0, y=480)

        #Imagen
        self.label_imagen = Label(
            self.frame_encabezado, image=self.img['logo']
        )
        self.label_imagen.place(relx=0.1, rely=0.58, anchor='center')

        #Labels
        self.label_encabezado = Label(
            self.frame_encabezado,
            text='Sistema de Gestión - BLA Estética',
            font=ConfigView.fnt['titulo'],
            foreground=ConfigView.clr['hard']
        )
        self.label_encabezado.place(relx=0.58, rely=0.58, anchor='center')

        self.label_usuario = Label(
            self.frame_informacion,
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['medium']
        )
        self.label_usuario.place(relx=0.1, rely=0.5, anchor='center')

        self.label_hora = Label(
            self.frame_informacion,
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['medium']
        )
        self.label_hora.place(relx=0.75, rely=0.5, anchor='center')

        # Botones
        self.boton_ventas = Button(self.frame_menu)
        self.boton_ventas.config(
            text="Ventas",
            width=300,
            height=120,
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['medium'],
            image=self.img['ventas'],
            compound='top',
            pady=10
        )
        self.boton_ventas.place(relx=0.08, rely=0.048)

        self.boton_cuentacorriente = Button(self.frame_menu)
        self.boton_cuentacorriente.config(
            text="Cuentas\n Corrientes",
            width=300,
            height=120,
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['medium'],
            image=self.img['cuentacorriente'],
            compound='top',
            pady=10
        )
        self.boton_cuentacorriente.place(relx=0.5, rely=0.048)

        self.boton_inventario = Button(self.frame_menu)
        self.boton_inventario.config(
            text="Productos",
            width=300,
            height=120,
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['medium'],
            image=self.img['inventario'],
            compound='top',
            pady=10
        )
        self.boton_inventario.place(relx=0.08, rely=0.52)

        self.boton_reportes = Button(self.frame_menu)
        self.boton_reportes.config(
            text="Reportes",
            width=300,
            height=120,
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['medium'],
            image=self.img['reportes'],
            compound='top',
            pady=10
        )
        self.boton_reportes.place(relx=0.5, rely=0.52)
        
        self.boton_administrador = Button(self.frame_menu)
        self.boton_administrador.config(
            width=50, 
            height=50, 
            borderwidth=0,
            image=self.img['admin']
        )
        self.boton_administrador.place(relx=0.93, rely=0.865)