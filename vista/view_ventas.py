##############################################################################
# Importaciones
##############################################################################

from tkinter import Frame, Entry, Button, Label, LabelFrame, IntVar, Tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from vista.view_config import ConfigView

############################# VISTA DE VENTAS ################################

''' En este fichero se crean las interfaces graficas del modulo de ventas, se
    crea la ventana principal del modulo, ventana de consulta de ventas,
    ventana de confirmacion de ventas y ventana de ingreso de intereses
'''

class VentanaVentas:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Módulo de ventas')
        self.root.resizable(False, False)
        self.root.geometry("1250x590+58+79")
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
        self.img['acarrito'] = ConfigView.formateo_imagen(
            'agregar_carrito.png', 30, 30
        )
        self.img['eliminar'] = ConfigView.formateo_imagen(
            'eliminar.png', 30, 30
        )
        self.img['listo'] = ConfigView.formateo_imagen(
            'listo.png', 30, 30
        )

        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(
            width=1250, height=40, background=ConfigView.clr['soft']
        )
        self.frame_titulo.place(x=0, y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(
            width=1250, height=4, background=ConfigView.clr['hard']
        )
        self.frame_separador.place(x=0, y=36)

        self.frame_entradas = Frame(self.root)
        self.frame_entradas.config(
            width=1250, height=152, background=ConfigView.clr['soft']
        )
        self.frame_entradas.place(x=0, y=38)

        self.frame_detalle_ventas = Frame(self.root)
        self.frame_detalle_ventas.config(width=1250, height=250)
        self.frame_detalle_ventas.place(x=0, y=190)

        self.frame_resumen_venta = Frame(self.root)
        self.frame_resumen_venta.config(
            width=1250, height=80, background=ConfigView.clr['soft']
        )
        self.frame_resumen_venta.place(x=0, y=400)

        self.frame_finalizar_venta = Frame(self.root)
        self.frame_finalizar_venta.config(
            width=1250, height=80, background=ConfigView.clr['soft']
        )
        self.frame_finalizar_venta.place(x=0, y=480)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=1250, height=30, background=ConfigView.clr['medium']
        )
        self.frame_informacion.place(x=0, y=560)
        
        #Labels
        self.label_titulo = Label(
            self.frame_titulo,
            text='VENTAS',
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5,rely=0.5,anchor='center')

        self.label_codigo_producto = Label(
            self.frame_entradas,
            text='Código',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_codigo_producto.place(
            relx=0.054, rely=0.5, anchor='center'
        )

        self.label_cliente = Label(
            self.frame_entradas,
            text='Cliente',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_cliente.place(relx=0.05, rely=0.2, anchor='center')

        self.label_precio = Label(
            self.frame_entradas,
            text='Precio',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_precio.place(relx=0.38, rely=0.5, anchor='center')

        self.label_cantidad = Label(
            self.frame_entradas,
            text='Cantidad',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_cantidad.place(relx=0.38, rely=0.8, anchor='center')

        self.label_vencimiento = Label(
            self.frame_entradas,
            text='Vencimiento',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_vencimiento.place(relx=0.05, rely=0.8, anchor='center')
        
        self.label_total_venta = Label(
            self.frame_resumen_venta,
            text=f'Total de la venta: $ ',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_total_venta.place(relx=0.75, rely=0.5, anchor='center')

        self.label_usuario = Label(
            self.frame_informacion,
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['medium']
        )
        self.label_usuario.place(relx=0.05, rely=0.5, anchor='center')

        self.label_en_stock = Label(
            self.frame_entradas,
            text='En stock:',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_en_stock.place(relx=0.53, rely=0.8, anchor='center')

        self.label_descripcion_producto = Label(
            self.frame_entradas,
            font=ConfigView.fnt['text12'],
            text='Producto: ',
            background=ConfigView.clr['medium']
        )
        self.label_descripcion_producto.place(x=450, y=15)

        #Entries
        self.entry_codigo_producto = Entry(
            self.frame_entradas,
            width=20,
            font=ConfigView.fnt['text12'],
            bd=1,
            relief='solid'
        )
        self.entry_codigo_producto.place(relx=0.18, rely=0.5, anchor='center') 

        self.entry_cliente = ttk.Combobox(
            self.frame_entradas, width=18, font=ConfigView.fnt['text12']
        )
        self.entry_cliente.place(relx=0.18, rely=0.2, anchor='center')

        self.entry_precio = Entry(
            self.frame_entradas,
            width=15,
            font=ConfigView.fnt['text12'],
            bd=1,
            relief='solid'
        )
        self.entry_precio.place(relx=0.48, rely=0.5, anchor='center')

        self.entry_cantidad = Entry(
            self.frame_entradas,
            width=5,
            font=ConfigView.fnt['text12'],
            bd=1,
            relief='solid'
        )
        self.entry_cantidad.place(relx=0.445, rely=0.8, anchor='center')

        self.entry_vencimiento = ttk.Combobox(
            self.frame_entradas, width=18, font=ConfigView.fnt['text12']
        )
        self.entry_vencimiento.place(relx=0.18, rely=0.8, anchor='center')

        #Botones
        self.boton_buscar = Button(
            self.frame_entradas,
            font=ConfigView.fnt['text14-b'],
            width=50,
            height=35,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['consultaventas'],
            compound='left',
            padx=10
        )
        self.boton_buscar.place(relx=0.3, rely=0.65, anchor='center')

        self.boton_carrito = Button(
            self.frame_entradas,
            text='Agregar al carrito',
            font=ConfigView.fnt['text14-b'],
            width=200,
            height=35,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['acarrito'],
            compound='left',
            padx=10
        )
        self.boton_carrito.place(relx=0.89, rely=0.25, anchor='center')

        self.boton_eliminar_venta = Button(
            self.frame_entradas,
            text='Eliminar',
            font=ConfigView.fnt['text14-b'],
            width=200,
            height=35,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['eliminar'],
            compound='left',
            padx=10
        )
        self.boton_eliminar_venta.place(relx=0.89, rely=0.75, anchor='center')

        self.boton_finalizar_venta = Button(
            self.frame_resumen_venta,
            text='Finalizar Venta',
            font=ConfigView.fnt['text14-b'],
            width=250,
            height=35,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['listo'],
            compound='left',
            padx=10
        )
        self.boton_finalizar_venta.place(
            relx=0.45, rely=0.55, anchor='center'
        )

        self.boton_consultaventas = Button(self.frame_finalizar_venta)
        self.boton_consultaventas.config(
            text="Consultar\n Ventas",
            width=200,
            font=ConfigView.fnt['text14-b'],
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['consultaventas'],
            compound='left',
            padx=10
        )
        self.boton_consultaventas.place(relx=0.1, rely=0.5, anchor='center')
        
        #Treeview
        self.style = ttk.Style(self.frame_detalle_ventas)
        self.style.configure(
            "Treeview.Heading",
            font=ConfigView.fnt['text12-b']
        )
        self.style.configure("Treeview", font=ConfigView.fnt['text10'])

        self.tv_ventas = ttk.Treeview(
            self.frame_detalle_ventas,
            columns=("col1", "col2", "col3", "col4"),
            height=9
        )
        
        self.tv_ventas.column("#0", width=50, anchor='center')
        self.tv_ventas.column("col1", width=150, anchor='center')
        self.tv_ventas.column("col2", width=650, anchor='center')
        self.tv_ventas.column("col3", width=200, anchor='center')
        self.tv_ventas.column("col4", width=200, anchor='center')

        self.tv_ventas.heading(
            "#0", text="#", anchor='center'
        )
        self.tv_ventas.heading(
            "col1", text='Código', anchor='center'
        )
        self.tv_ventas.heading(
            "col2", text='Descripción', anchor='center'
        )
        self.tv_ventas.heading(
            "col3", text='Precio Unitario', anchor='center'
        )
        self.tv_ventas.heading(
            "col4", text='Cantidad', anchor='center'
        )

        self.tv_ventas.pack(side='left', fill='y')

    
    # Metodo para limpiar entries
    def limpiar_cajas(self):
        self.entry_codigo_producto.delete(0,'end')
        self.entry_precio.delete(0,'end')
        self.entry_cantidad.delete(0,'end')
        self.entry_vencimiento.delete(0,'end')

    
    # Metodo para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_ventas.get_children():
            self.tv_ventas.delete(item)


class ConfirmacionVenta:

    ''' Esta clase crea la ventana de confirmacion de venta, donde se da un
        resumen de la venta, el monto total a pagar y se crean radiobuttons 
        para la eleccion del modo de pago, ademas de eso se crea un entry 
        para que se ingrese el monto abonado.
    '''
    
    def __init__(self, root):
        self.root = root
        self.root.title('Confirmación de venta')
        self.root.geometry('400x450+483+149')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['ventas'] = ConfigView.formateo_imagen(
            'ventas.png', 30, 30
        )
        self.img['tarjeta'] = ConfigView.formateo_imagen(
            'tarjeta.png', 30, 30
        )

        #Frames
        self.frame_confirmacion = Frame(self.root)
        self.frame_confirmacion.config(
            width=400, height=450, background=ConfigView.clr['soft']
        )
        self.frame_confirmacion.place(relx=0, rely=0)

        #Labels
        self.label_numero_venta = Label(self.frame_confirmacion)
        self.label_numero_venta.config(
            text=f'Venta #',
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft']
        )
        self.label_numero_venta.place(relx=0.5, rely=0.1, anchor='center')

        self.label_total_venta = Label(self.frame_confirmacion)
        self.label_total_venta.config(
            text=f'Total a pagar: $',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_total_venta.place(relx=0.5, rely=0.2, anchor='center')

        self.label_entrega = Label(self.frame_confirmacion)
        self.label_entrega.config(
            text='Entrega: $',
            font=ConfigView.fnt['text16-b'],
            background=ConfigView.clr['soft']
        )
        self.label_entrega.place(relx=0.06, rely=0.75)

        #Entries
        self.entry_entrega = Entry(self.frame_confirmacion)
        self.entry_entrega.config(
            width=18, font=ConfigView.fnt['text16'], bd=1, relief='solid'
        )
        self.entry_entrega.place(relx=0.35, rely=0.75)

        #Radiobuttons y Labelframe
        self.labelframe = LabelFrame(self.frame_confirmacion)
        self.labelframe.config(
            text='Medio de pago',
            padx=10,
            pady=10,
            width=100,
            background=ConfigView.clr['soft'],
            font=ConfigView.fnt['text14']
        )
        self.labelframe.place(relx=0.5, rely=0.43, anchor='center')

        # Variable IntVar para guardar seleccion de Radiobuttons
        self.opcion = IntVar()
        self.opcion.set(1)
        
        self.style = ttk.Style()
        self.style.configure(
            "Custom.TRadiobutton",
            background=ConfigView.clr['soft'],
            font=ConfigView.fnt['text12']
        )
        self.modo_pago_1 = ttk.Radiobutton(
            self.labelframe,
            text='Efectivo',
            variable=self.opcion,
            value=1,
            style="Custom.TRadiobutton",
            command=self.seleccion_radiobutton
        )
        self.modo_pago_1.config(width=30)
        self.modo_pago_1.pack(anchor='w', fill='both')
        
        self.modo_pago_2 = ttk.Radiobutton(
            self.labelframe,
            text='Transferencia',
            variable=self.opcion,
            value=2,
            style="Custom.TRadiobutton",
            command=self.seleccion_radiobutton
        )
        self.modo_pago_2.config(width=30)
        self.modo_pago_2.pack(anchor='w', fill='both')
        
        self.modo_pago_3 = ttk.Radiobutton(
            self.labelframe,
            text='Débito/Crédito',
            variable=self.opcion,
            value=3,
            style="Custom.TRadiobutton",
            command=self.seleccion_radiobutton
        )
        self.modo_pago_3.config(width=30)
        self.modo_pago_3.pack(anchor='w', fill='both')

        #Buttons
        self.boton_confirmar = Button(self.frame_confirmacion)
        self.boton_confirmar.config(
            text='Confirmar',
            font=ConfigView.fnt['text14-b'],
            width=150,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['ventas'],
            compound='left'
        )
        self.boton_confirmar.place(relx=0.5, rely=0.92, anchor='center')

        self.boton_interes = Button(self.frame_confirmacion)
        self.boton_interes.config(
            text='Recargo',
            font=ConfigView.fnt['text14-b'],
            width=150,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['tarjeta'],
            compound='left'
        )
        self.boton_interes.place(relx=0.5, rely=0.65, anchor='center')

    
    # Metodo para retornar la seleccion de los Radiobuttons
    def seleccion_radiobutton(self):
        return self.opcion.get()


class ConsultaVentas:

    ''' Clase para la creacion de la ventana de consulta de ventas, donde se
        puede buscar las ventas entre dos fechas determinadas, luego se crean
        botones para filtrar ventas, ver detalle de ventas y eliminar ventas.
    '''
    
    def __init__(self, root):
        self.root = root
        self.root.title('BLA Estética - Consulta de Ventas')
        self.root.geometry('1000x590+183+79')
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
        self.img['pagopendiente'] = ConfigView.formateo_imagen(
            'pago_pendiente.png', 30, 30
        )
        self.img['detalle'] = ConfigView.formateo_imagen(
            'detalle.png', 30, 30
        )
        self.img['eliminar'] = ConfigView.formateo_imagen(
            'eliminar.png', 30, 30
        )

        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(
            width=1000, height=40, background=ConfigView.clr['soft']
        )
        self.frame_titulo.place(x=0,y=0)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(
            width=1000, height=90, background=ConfigView.clr['soft']
        )
        self.frame_busqueda.place(x=0, y=40)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(
            width=1000, height=430, background=ConfigView.clr['soft']
        )
        self.frame_treeview.place(x=0, y=130)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=1000, height=30, background=ConfigView.clr['soft']
        )
        self.frame_informacion.place(x=0, y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(
            text='CONSULTA DE VENTAS',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5, rely=0.5, anchor='center')

        self.label_desde = Label(self.frame_busqueda)
        self.label_desde.config(
            text='Desde:',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_desde.place(relx=0.05, rely=0.2, anchor='center')

        self.label_hasta = Label(self.frame_busqueda)
        self.label_hasta.config(
            text='Hasta:',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_hasta.place(relx=0.05, rely=0.7, anchor='center')

        self.label_cliente = Label(self.frame_busqueda)
        self.label_cliente.config(
            text='Cliente', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_cliente.place(relx=0.35, rely=0.2, anchor='center')

        #Entries
        self.entry_desde = DateEntry(
            self.frame_busqueda,
            font=ConfigView.fnt['text12'],
            width=20,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_desde.place(relx=0.2, rely=0.22, anchor='center')

        self.entry_hasta = DateEntry(
            self.frame_busqueda,
            font=ConfigView.fnt['text12'],
            width=20,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_hasta.place(relx=0.2, rely=0.72, anchor='center')

        self.entry_cliente = ttk.Combobox(self.frame_busqueda)
        self.entry_cliente.config(font=ConfigView.fnt['text14'], width=18)
        self.entry_cliente.place(relx=0.5, rely=0.22, anchor='center')

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
        self.boton_buscar.place(relx=0.72, rely=0.25, anchor='center')

        self.boton_pendientes = Button(self.frame_busqueda)
        self.boton_pendientes.config(
            text='Pendientes',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['pagopendiente'],
            compound='left',
            padx=10
        )
        self.boton_pendientes.place(relx=0.72, rely=0.73, anchor='center')
        
        self.boton_detalle = Button(self.frame_busqueda)
        self.boton_detalle.config(
            text='Detalle',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['detalle'],
            compound='left',
            padx=10
        )
        self.boton_detalle.place(relx=0.9, rely=0.25, anchor='center')

        self.boton_eliminar = Button(self.frame_busqueda)
        self.boton_eliminar.config(
            text='Eliminar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['eliminar'],
            compound='left',
            padx=10
        )
        self.boton_eliminar.place(relx=0.9, rely=0.73, anchor='center')

        #Treeview
        self.tv_consultaventas = ttk.Treeview(
            self.frame_treeview,
            columns=('col1', 'col2', 'col3', 'col4', 'col5'),
            height=20
        )
        
        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading",
            font=ConfigView.fnt['text12-b']
        )
        self.style.configure("Treeview", font=ConfigView.fnt['text10'])

        self.tv_consultaventas.column("#0", width=80,anchor='center')
        self.tv_consultaventas.column("col1", width=150,anchor='center')
        self.tv_consultaventas.column("col2", width=300,anchor='center')
        self.tv_consultaventas.column("col3", width=150,anchor='center')
        self.tv_consultaventas.column("col4", width=150,anchor='center')
        self.tv_consultaventas.column("col5", width=150,anchor='center')

        self.tv_consultaventas.heading(
            "#0", text="id_venta", anchor='center'
        )
        self.tv_consultaventas.heading(
            "col1", text='Fecha', anchor='center'
        )
        self.tv_consultaventas.heading(
            "col2", text='Cliente', anchor='center'
        )
        self.tv_consultaventas.heading(
            "col3", text='Monto Total', anchor='center'
        )
        self.tv_consultaventas.heading(
            "col4", text='Medio Pago', anchor='center'
        )
        self.tv_consultaventas.heading(
            "col5", text='Estado Venta', anchor='center'
        )

        self.tv_consultaventas.grid(row=0, column=0, sticky='nsew')

        # Scrollbar Treeview
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview,
            orient='vertical',
            command=self.tv_consultaventas.yview
        )
        self.tv_consultaventas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame_treeview.grid_rowconfigure(0, weight=1)
        self.frame_treeview.grid_columnconfigure(0, weight=1)

    
    # Metodo para limpiar los entry
    def limpiar_cajas(self):
        self.entry_cliente.delete(0,'end')
        self.entry_desde.delete(0,'end')
        self.entry_hasta.delete(0,'end')
    

    # Metodo para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_consultaventas.get_children():
            self.tv_consultaventas.delete(item)


class DetalleVentas:

    ''' En esta clase se crea la interfaz grafica de la ventana de detalle de
        ventas.
    '''
    
    def __init__(self, root):

        self.root = root
        self.root.title('Detalle de Venta')
        self.root.geometry('900x400+233+174')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()

    
    def widgets(self):

        # Referencia a imagenes
        self.img['pdf'] = ConfigView.formateo_imagen(
            'pdf.png', 30, 30
        )

        #Frames
        self.frame_infoventa = Frame(self.root)
        self.frame_infoventa.config(
            width=900, height=50, background=ConfigView.clr['soft']
        )
        self.frame_infoventa.place(x=0, y=0)

        self.frame_tvdetalle = Frame(self.root)
        self.frame_tvdetalle.config(
            width=900, height=300, background=ConfigView.clr['soft']
        )
        self.frame_tvdetalle.place(x=0, y=50)

        self.frame_imprimir = Frame(self.root)
        self.frame_imprimir.config(
            width=900, height=50, background=ConfigView.clr['soft']
        )
        self.frame_imprimir.place(x=0, y=350)

        #Labels
        self.label_nroventa = Label(self.frame_infoventa)
        self.label_nroventa.config(
            text='Venta # ',
            font=ConfigView.fnt['text16-b'],
            background=ConfigView.clr['soft']
        )
        self.label_nroventa.place(relx=0.5, rely=0.5, anchor='center')

        #Buttons
        self.boton_pdf = Button(self.frame_imprimir)
        self.boton_pdf.config(
            text='Imprimir',
            font=ConfigView.fnt['text12-b'],
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['pdf'],
            compound='left',
            padx=10
        )
        self.boton_pdf.place(relx=0.5, rely=0.5, anchor='center')

        #Treeview
        self.tv_detalleventas = ttk.Treeview(
            self.frame_tvdetalle,
            columns=('col1', 'col2', 'col3'),
            height=300
        )
        
        self.style = ttk.Style(self.frame_tvdetalle)
        self.style.configure(
            "Treeview.Heading", font=ConfigView.fnt['text12-b']
        )

        self.tv_detalleventas.column("#0", width=200,anchor='center')
        self.tv_detalleventas.column("col1", width=500,anchor='center')
        self.tv_detalleventas.column("col2", width=100,anchor='center')
        self.tv_detalleventas.column("col3", width=100,anchor='center')

        self.tv_detalleventas.heading(
            "#0", text="Código", anchor='center'
        )
        self.tv_detalleventas.heading(
            "col1", text='Producto', anchor='center'
        )
        self.tv_detalleventas.heading(
            "col2", text='Precio', anchor='center'
        )
        self.tv_detalleventas.heading(
            "col3", text='Cantidad', anchor='center'
        )
        
        self.tv_detalleventas.pack(side='left', fill='y')


class InterfazInteres:

    ''' Clase para la creacion de una ventana que se va a llamar cuando el
        medio de pago elegido sea debito/credito, se permitira poner un monto
        de dinero el cual se sumara al monto total de la venta.
    '''
    
    def __init__(self, root):
        self.root = root
        self.root.title('Interés por pago Débito/Crédito')
        self.root.geometry('400x200+483+274')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen("logosec_fondo.ico")
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['mas'] = ConfigView.formateo_imagen(
            'mas.png', 20, 20
        )

        #Frames
        self.frame_interes = Frame(self.root)
        self.frame_interes.config(
            width=400, height=300, background=ConfigView.clr['soft']
        )
        self.frame_interes.place(x=0, y=0)

        #Labels
        self.label_titulo = Label(self.frame_interes)
        self.label_titulo.config(
            text='Ingreso de Intereses',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_titulo.place(relx=0.5, rely=0.1, anchor='center')

        self.label_interes = Label(self.frame_interes)
        self.label_interes.config(
            text='Monto interés',
            font=ConfigView.fnt['text14'],
            background=ConfigView.clr['soft']
        )
        self.label_interes.place(relx=0.3, rely=0.3, anchor='center')

        #Entries
        self.entry_interes = Entry(self.frame_interes)
        self.entry_interes.config(
            font=ConfigView.fnt['text14'],
            width=10,
            bd=1,
            relief='solid'
        )
        self.entry_interes.place(relx=0.7, rely=0.3, anchor='center')

        #Buttons
        self.boton_interes = Button(self.frame_interes)
        self.boton_interes.config(
            text='Ingresar',
            font=ConfigView.fnt['text14-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['mas'],
            compound='left',
            padx=10
        )
        self.boton_interes.place(relx=0.5, rely=0.55, anchor='center')