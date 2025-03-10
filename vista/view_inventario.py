##############################################################################
# Importaciones
##############################################################################

from tkinter import Entry, Label, Frame, Button
from tkinter import ttk
from tkcalendar import DateEntry
from vista.view_config import ConfigView

########################### VISTA DE INVENTARIO ##############################
''' En este fichero se lleva a cabo la creacion de la interfaz grafica del 
    modulo de Inventarios.
'''

class InterfazInventario:

    def __init__(self,root):

        self.root = root
        self.root.title('BLA Estética - Inventario')
        self.root.geometry('1100x590+133+79')
        self.root.resizable(False,False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()

    
    def widgets(self):

        # Referencia a imagenes
        self.img['filtrar'] = ConfigView.formateo_imagen(
            'filtrar.png', 30, 30
        )
        self.img['sinstock'] = ConfigView.formateo_imagen(
            'sin_stock.png', 30, 30
        )
        self.img['mas'] = ConfigView.formateo_imagen(
            'mas.png', 30, 30
        )
        self.img['modificar'] = ConfigView.formateo_imagen(
            'modificar.png', 30, 30
        )
        self.img['eliminar'] = ConfigView.formateo_imagen(
            'eliminar.png', 30, 30
        )
        self.img['istock'] = ConfigView.formateo_imagen(
            'ingresar_stock.png', 30, 30
        )
        self.img['vencimientos'] = ConfigView.formateo_imagen(
            'vencimientos.png', 30, 30
        )
        self.img['excel'] = ConfigView.formateo_imagen(
            'excel.png', 30, 30
        )

        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(
            width=1100, height=50, background=ConfigView.clr['soft']
        )
        self.frame_titulo.place(x=0,y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(
            width=1100, height=2, background=ConfigView.clr['hard']
        )
        self.frame_separador.place(x=0,y=40)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(
            width=1100, height=80, background=ConfigView.clr['soft']
        )
        self.frame_busqueda.place(x=0,y=50)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(
            width=1100, height=350, background=ConfigView.clr['soft']
        )
        self.frame_treeview.place(x=0,y=130)

        self.frame_botones = Frame(self.root)
        self.frame_botones.config(
            width=1100, height=80, background=ConfigView.clr['soft']
        )
        self.frame_botones.place(x=0,y=480)
        
        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=1100, height=30, background=ConfigView.clr['medium']
        )
        self.frame_informacion.place(x=0,y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(
            text='PRODUCTOS',
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5, rely=0.42, anchor='center')

        self.label_codigo = Label(self.frame_busqueda)
        self.label_codigo.config(
            text='Código',
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['soft']
        )
        self.label_codigo.place(relx=0.08, rely=0.15, anchor='center')

        self.label_descripcion = Label(self.frame_busqueda)
        self.label_descripcion.config(
            text='Descripción',
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['soft']
        )
        self.label_descripcion.place(relx=0.08, rely=0.65, anchor='center')

        self.label_usuario = Label(
            self.frame_informacion,
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['medium']
        )
        self.label_usuario.place(relx=0.1, rely=0.5, anchor='center')

        #Entries
        self.entry_codigo = Entry(self.frame_busqueda)
        self.entry_codigo.config(
            font=ConfigView.fnt['text16'], width=15, bd=1, relief='solid'
        )
        self.entry_codigo.place(relx=0.25, rely=0.2, anchor='center')

        self.entry_descripcion = Entry(self.frame_busqueda)
        self.entry_descripcion.config(
            font=ConfigView.fnt['text16'], width=15, bd=1, relief='solid'
        )
        self.entry_descripcion.place(relx=0.25, rely=0.7, anchor='center')

        #Buttons
        self.boton_filtar = Button(self.frame_busqueda)
        self.boton_filtar.config(
            text='Filtrar',
            font=ConfigView.fnt['text14-b'],
            width=150,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['filtrar'],
            compound='left',
            padx=10
        )
        self.boton_filtar.place(relx=0.45, rely=0.45, anchor='center')

        self.boton_cerostock = Button(self.frame_busqueda)
        self.boton_cerostock.config(
            text='Sin Stock',
            font=ConfigView.fnt['text14-b'],
            width=150,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['sinstock'],
            compound='left',
            padx=10
        )
        self.boton_cerostock.place(relx=0.64, rely=0.45, anchor='center')

        self.boton_nuevo = Button(self.frame_botones)
        self.boton_nuevo.config(
            text='Nuevo',
            font=ConfigView.fnt['text14-b'],
            width=120,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['mas'],
            compound='left',
            padx=10
        )
        self.boton_nuevo.place(relx=0.2, rely=0.5, anchor='center')

        self.boton_modificar = Button(self.frame_botones)
        self.boton_modificar.config(
            text='Modificar',
            font=ConfigView.fnt['text14-b'],
            width=120,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['modificar'],
            compound='left',
            padx=10
        )
        self.boton_modificar.place(relx=0.6,rely=0.5,anchor='center')

        self.boton_eliminar = Button(self.frame_botones)
        self.boton_eliminar.config(
            text='Eliminar',
            font=ConfigView.fnt['text14-b'],
            width=120,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['eliminar'],
            compound='left',
            padx=10
        )
        self.boton_eliminar.place(relx=0.8, rely=0.5, anchor='center')

        self.boton_ingresar = Button(self.frame_botones)
        self.boton_ingresar.config(
            text='Ingresar',
            font=ConfigView.fnt['text14-b'],
            width=120,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['istock'],
            compound='left',
            padx=10
        )
        self.boton_ingresar.place(relx=0.4, rely=0.5, anchor='center')

        self.boton_vencimientos = Button(self.frame_busqueda)
        self.boton_vencimientos.config(
            text="Consultar\nVencimientos",
            width=180,
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['vencimientos'],
            compound='left',
            padx=10
        )
        self.boton_vencimientos.place(relx=0.88, rely=0.4, anchor='center')

        self.boton_excel = Button(self.frame_botones)
        self.boton_excel.config(
            borderwidth=0,
            background=ConfigView.clr['soft'],
            activebackground=ConfigView.clr['soft'],
            width=50,
            height=50,
            image=self.img['excel']
        )
        self.boton_excel.place(relx=0.95, rely=0.01)

        #Treeview
        self.tv_inventario = ttk.Treeview(
            self.frame_treeview,
            columns=('col1','col2','col3','col4'),
            height=16
        )
        
        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading", font=ConfigView.fnt['text12-b']
        )
        self.style.configure("Treeview", font=ConfigView.fnt['text10'])

        self.tv_inventario.column("#0", width=130,anchor='center')
        self.tv_inventario.column("col1", width=570,anchor='center')
        self.tv_inventario.column("col2", width=160,anchor='center')
        self.tv_inventario.column("col3", width=100,anchor='center')
        self.tv_inventario.column("col4", width=120,anchor='center')

        self.tv_inventario.heading(
            "#0", text="Código", anchor='center'
        )
        self.tv_inventario.heading(
            "col1", text='Descripción', anchor='center'
        )
        self.tv_inventario.heading(
            "col2", text='Precio', anchor='center'
        )
        self.tv_inventario.heading(
            "col3", text='Stock', anchor='center'
        )
        self.tv_inventario.heading(
            "col4", text='Vencimiento', anchor='center'
        )

        self.tv_inventario.grid(row=0, column=0, sticky='nsew')

        #Scrollbar vertical para el treeview
        self.scrollbar =  ttk.Scrollbar(
            self.frame_treeview,
            orient='vertical',
            command=self.tv_inventario.yview
        )
        self.tv_inventario.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame_treeview.grid_rowconfigure(0, weight=1)
        self.frame_treeview.grid_columnconfigure(0, weight=1)

    
    # Metodo para limpiar los entry
    def limpiar_cajas(self):
        self.entry_codigo.delete(0,'end')
        self.entry_descripcion.delete(0,'end')

    
    # Metodo para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_inventario.get_children():
            self.tv_inventario.delete(item)


class NuevoProducto:
    
    ''' Esta clase crea la ventana se llamara cuando se presione el boton
        Nuevo, permite crear un producto nuevo que no exista en la base de 
        datos
    '''
    
    def __init__(self,root):
        self.root = root
        self.root.title('Nuevo Producto')
        self.root.geometry('500x400+433+110')
        self.root.resizable(False,False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['guardar'] = ConfigView.formateo_imagen(
            'guardar.png', 30, 30
        )

        #Frames
        self.frame_ventanainformacion = Frame(self.root)
        self.frame_ventanainformacion.config(
            width=500, height=400, background=ConfigView.clr['soft']
        )
        self.frame_ventanainformacion.place(relx=0, rely=0)

        #Labels
        self.label_codigo = Label(self.frame_ventanainformacion)
        self.label_codigo.config(
            text='Código', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_codigo.place(relx=0.05, rely=0.1)

        self.label_descripcion = Label(self.frame_ventanainformacion)
        self.label_descripcion.config(
            text='Descripción',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_descripcion.place(relx=0.05, rely=0.25)

        self.label_precio = Label(self.frame_ventanainformacion)
        self.label_precio.config(
            text='Precio', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_precio.place(relx=0.05, rely=0.4)

        self.label_stock = Label(self.frame_ventanainformacion)
        self.label_stock.config(
            text='Stock', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_stock.place(relx=0.05,rely=0.55)

        self.label_vencimiento = Label(self.frame_ventanainformacion)
        self.label_vencimiento.config(
            text='Vencimiento',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_vencimiento.place(relx=0.05, rely=0.7)

        #Entries
        self.entry_codigo = Entry(self.frame_ventanainformacion)
        self.entry_codigo.config(
            width=28, font=ConfigView.fnt['text14'], bd=1, relief='solid'
        )
        self.entry_codigo.place(relx=0.3, rely=0.1)

        self.entry_descripcion = Entry(self.frame_ventanainformacion)
        self.entry_descripcion.config(
            width=28, font=ConfigView.fnt['text14'], bd=1, relief='solid'
        )
        self.entry_descripcion.place(relx=0.3,rely=0.25)

        self.entry_precio = Entry(self.frame_ventanainformacion)
        self.entry_precio.config(
            width=28, font=ConfigView.fnt['text14'], bd=1, relief='solid'
        )
        self.entry_precio.place(relx=0.3, rely=0.4)

        self.entry_stock = Entry(self.frame_ventanainformacion)
        self.entry_stock.config(
            width=28, font=ConfigView.fnt['text14'], bd=1, relief='solid'
        )
        self.entry_stock.place(relx=0.3, rely=0.55)

        self.entry_vencimiento = DateEntry(
            self.frame_ventanainformacion,
            font=ConfigView.fnt['text14'],
            width=26,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_vencimiento.place(relx=0.3, rely=0.7)
    
        #Buttons
        self.boton_guardar = Button(self.frame_ventanainformacion)
        self.boton_guardar.config(
            text='Guardar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['guardar'],
            compound='left',
            padx=10
        )
        self.boton_guardar.place(relx=0.5, rely=0.9, anchor='center')

    
    # Metodo para limpiar entries
    def limpiar_cajas(self):
        self.entry_codigo.delete(0,'end')
        self.entry_descripcion.delete(0,'end')
        self.entry_stock.delete(0,'end')
        self.entry_precio.delete(0,'end')


class ModificarProducto:

    ''' Esta clase crea la ventana se llamara cuando se presione el boton 
        Modificar, permite modificar los productos existentes.
    '''
    
    def __init__(self,root):
        self.root = root
        self.root.title('Modificación de Producto')
        self.root.geometry('500x300+433+224')
        self.root.resizable(False,False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()
    

    def widgets(self):

        # Referencia a imagenes
        self.img['guardar'] = ConfigView.formateo_imagen(
            'guardar.png', 30, 30
        )

        #Frames
        self.frame_ventanainformacion = Frame(self.root)
        self.frame_ventanainformacion.config(
            width=500, height=300, background=ConfigView.clr['soft']
        )
        self.frame_ventanainformacion.place(relx=0, rely=0)

        #Labels
        self.label_descripcion = Label(self.frame_ventanainformacion)
        self.label_descripcion.config(
            text='Descripción', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_descripcion.place(relx=0.05, rely=0.1)

        self.label_precio = Label(self.frame_ventanainformacion)
        self.label_precio.config(
            text='Precio', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_precio.place(relx=0.05, rely=0.3)

        self.label_stock = Label(self.frame_ventanainformacion)
        self.label_stock.config(
            text='Stock', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_stock.place(relx=0.05, rely=0.5)

        #Entries
        self.entry_descripcion = Entry(self.frame_ventanainformacion)
        self.entry_descripcion.config(
            width=28, 
            font=ConfigView.fnt['text14'], 
            bd=1, 
            relief='solid'
        )
        self.entry_descripcion.place(relx=0.3, rely=0.12)

        self.entry_precio = Entry(self.frame_ventanainformacion)
        self.entry_precio.config(
            width=28, 
            font=ConfigView.fnt['text14'], 
            bd=1, 
            relief='solid'
        )
        self.entry_precio.place(relx=0.3, rely=0.32)

        self.entry_stock = Entry(self.frame_ventanainformacion)
        self.entry_stock.config(
            width=28, font=ConfigView.fnt['text14'], bd=1, relief='solid'
        )
        self.entry_stock.place(relx=0.3, rely=0.52)

        #Buttons
        self.boton_guardar = Button(self.frame_ventanainformacion)
        self.boton_guardar.config(
            text='Guardar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['guardar'],
            compound='left',
            padx=10
        )
        self.boton_guardar.place(relx=0.5, rely=0.8, anchor='center')

    # Función para limpiar los entry
    def limpiar_cajas(self):
        self.entry_descripcion.delete(0,'end')
        self.entry_stock.delete(0,'end')
        self.entry_precio.delete(0,'end')


class IngresoStock:

    ''' Esta clase crea la ventana se llamara cuando se presione el boton
        Ingresar, permite agregar stock a un producto ya existente en la 
        base de datos
    '''
    
    def __init__(self, root):

        self.root = root
        self.root.title('Ingreso de stock')
        self.root.geometry('400x200+483+274')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()

    
    def widgets(self):

        # Referencia a imagenes
        self.img['istock'] = ConfigView.formateo_imagen(
            'ingresar_stock.png', 30, 30
        )

        #Frames
        self.frame_ingresostock = Frame(self.root)
        self.frame_ingresostock.config(
            width=400, height=300, background=ConfigView.clr['soft']
        )
        self.frame_ingresostock.place(x=0, y=0)

        #Labels
        self.label_titulo = Label(self.frame_ingresostock)
        self.label_titulo.config(
            text='Ingreso de stock',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_titulo.place(relx=0.5, rely=0.1, anchor='center')

        self.label_ingresostock = Label(self.frame_ingresostock)
        self.label_ingresostock.config(
            text='Cantidad a ingresar',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_ingresostock.place(relx=0.3, rely=0.3, anchor='center')

        #Entries
        self.entry_ingresostock = Entry(self.frame_ingresostock)
        self.entry_ingresostock.config(
            font=ConfigView.fnt['text14'], width=10, bd=1, relief='solid'
        )
        self.entry_ingresostock.place(relx=0.7, rely=0.3, anchor='center')

        #Buttons
        self.boton_ingresostock = Button(self.frame_ingresostock)
        self.boton_ingresostock.config(
            text='Ingresar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['istock'],
            compound='left',
            padx=10
        )
        self.boton_ingresostock.place(relx=0.5, rely=0.55, anchor='center')

    
    # Metodo para limpiar los entry
    def limpiar_cajas(self):
        self.entry_ingresostock.delete(0,'end')


class Vencimientos:

    ''' Clase para crear la ventana para consultar vencimientos de productos
        entre dos fechas determinadas o filtrando por codigo de producto
    '''
    
    def __init__(self, root):
        self.root = root
        self.root.title('BLA Estética - Vencimiento de productos')
        self.root.geometry('1100x590+133+79')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['consultaventas'] = ConfigView.formateo_imagen(
            'consulta_ventas.png', 30, 30
        )
        self.img['vencimientos'] = ConfigView.formateo_imagen(
            'vencimientos.png', 30, 30
        )

        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(
            width=1100, height=50, background=ConfigView.clr['soft']
        )
        self.frame_titulo.place(x=0, y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(
            width=1100, height=2, background=ConfigView.clr['hard']
        )
        self.frame_separador.place(x=0, y=40)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(
            width=1100, height=80, background=ConfigView.clr['soft']
        )
        self.frame_busqueda.place(x=0, y=50)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(
            width=1100, height=430, background=ConfigView.clr['soft']
        )
        self.frame_treeview.place(x=0, y=130)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=1100, height=30, background=ConfigView.clr['soft']
        )
        self.frame_informacion.place(x=0, y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(
            text='CONSULTA DE VENCIMIENTOS',
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5, rely=0.42, anchor='center')

        self.label_codigo = Label(self.frame_busqueda)
        self.label_codigo.config(
            text='Código',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_codigo.place(relx=0.05, rely=0.25, anchor='center')
        
        self.label_desde = Label(self.frame_busqueda)
        self.label_desde.config(
            text='Desde:',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_desde.place(relx=0.32, rely=0.2, anchor='center')

        self.label_hasta = Label(self.frame_busqueda)
        self.label_hasta.config(
            text='Hasta:',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_hasta.place(relx=0.32, rely=0.7, anchor='center')


        #Entries
        self.entry_codigo = Entry(self.frame_busqueda)
        self.entry_codigo.config(
            font=ConfigView.fnt['text12'], width=20, bd=1, relief='solid'
        )
        self.entry_codigo.place(relx=0.18, rely=0.25, anchor='center')

        self.entry_desde = DateEntry(
            self.frame_busqueda,
            font=ConfigView.fnt['text12'],
            width=20,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_desde.place(relx=0.45, rely=0.25, anchor='center')

        self.entry_hasta = DateEntry(
            self.frame_busqueda,
            font=ConfigView.fnt['text12'],
            width=20,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_hasta.place(relx=0.45, rely=0.75, anchor='center')

        #Buttons
        self.boton_buscar = Button(self.frame_busqueda)
        self.boton_buscar.config(
            text='Buscar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['consultaventas'],
            compound='left',
            padx=10
        )
        self.boton_buscar.place(relx=0.68, rely=0.45, anchor='center')

        self.boton_vencido = Button(self.frame_busqueda)
        self.boton_vencido.config(
            text='Vencidos',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['vencimientos'],
            compound='left',
            padx=10
        )
        self.boton_vencido.place(relx=0.85, rely=0.45, anchor='center')

        #Treeview
        self.tv_vencimientos = ttk.Treeview(
            self.frame_treeview,
            columns=('col1','col2','col3','col4'),
            height=20
        )
        
        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading", font=ConfigView.fnt['text12-b']
        )
        self.style.configure("Treeview",font=ConfigView.fnt['text10'])

        self.tv_vencimientos.column("#0", width=150, anchor='center')
        self.tv_vencimientos.column("col1", width=550, anchor='center')
        self.tv_vencimientos.column("col2", width=80, anchor='center')
        self.tv_vencimientos.column("col3", width=150, anchor='center')
        self.tv_vencimientos.column("col4", width=150, anchor='center')
        
        self.tv_vencimientos.heading(
            "#0", text="Código", anchor='center'
        )
        self.tv_vencimientos.heading(
            "col1", text='Descripción', anchor='center'
        )
        self.tv_vencimientos.heading(
            "col2", text='Stock', anchor='center'
        )
        self.tv_vencimientos.heading(
            "col3", text='Vencimiento', anchor='center'
        )
        self.tv_vencimientos.heading(
            "col4", text='Vence en', anchor='center'
        )

        self.tv_vencimientos.grid(row=0, column=0, sticky='nsew')

        #Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview,
            orient='vertical',
            command=self.tv_vencimientos.yview
        )
        self.tv_vencimientos.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame_treeview.grid_rowconfigure(0, weight=1)
        self.frame_treeview.grid_columnconfigure(0, weight=1)


    # Metodo para limpiar los entry
    def limpiar_cajas(self):
        self.entry_codigo.delete(0,'end')
        self.entry_desde.delete(0,'end')
        self.entry_hasta.delete(0,'end')


    # Metodo para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_vencimientos.get_children():
            self.tv_vencimientos.delete(item)