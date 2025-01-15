#Fichero para la creación de la interfaz gráfica del modulo de ventas
from tkinter import Frame,Entry,Button,Label,LabelFrame,IntVar
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from PIL import Image,ImageTk
import sys
import os
################################################################################################################################################
################################################### VENTANA DE NUEVA VENTA #####################################################################

class VentanaVentas:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Módulo de ventas')
        self.root.resizable(False,False)
        self.root.geometry("1250x590+58+79")
        self.root.iconbitmap(self.rutas("imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(width=1250,height=40,background='#EDE2E0')
        self.frame_titulo.place(x=0,y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(width=1250,height=4,background='#C18484')
        self.frame_separador.place(x=0,y=36)

        self.frame_entradas = Frame(self.root)
        self.frame_entradas.config(width=1250,height=152,background='#EDE2E0')
        self.frame_entradas.place(x=0,y=38)

        self.frame_detalle_ventas = Frame(self.root)
        self.frame_detalle_ventas.config(width=1250,height=250)
        self.frame_detalle_ventas.place(x=0,y=190)

        self.frame_resumen_venta = Frame(self.root)
        self.frame_resumen_venta.config(width=1250,height=80,background='#EDE2E0')
        self.frame_resumen_venta.place(x=0,y=400)

        self.frame_finalizar_venta = Frame(self.root)
        self.frame_finalizar_venta.config(width=1250,height=80,background='#EDE2E0')
        self.frame_finalizar_venta.place(x=0,y=480)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(width=1250,height=30,background='#D3B9B4')
        self.frame_informacion.place(x=0,y=560)
        
        #Labels
        self.label_titulo = Label(self.frame_titulo,text='VENTAS',font=('century gothic',20,'bold'),background='#EDE2E0',foreground='#C18484')
        self.label_titulo.place(relx=0.5,rely=0.5,anchor='center')

        self.label_codigo_producto = Label(self.frame_entradas,text='Código',font=('century gothic',12),background='#EDE2E0')
        self.label_codigo_producto.place(relx=0.054,rely=0.5,anchor='center')

        self.label_cliente = Label(self.frame_entradas,text='Cliente',font=('century gothic',12),background='#EDE2E0')
        self.label_cliente.place(relx=0.05,rely=0.2,anchor='center')

        self.label_precio = Label(self.frame_entradas,text='Precio',font=('century gothic',12),background='#EDE2E0')
        self.label_precio.place(relx=0.38,rely=0.5,anchor='center')

        self.label_cantidad = Label(self.frame_entradas,text='Cantidad',font=('century gothic',12),background='#EDE2E0')
        self.label_cantidad.place(relx=0.38,rely=0.8,anchor='center')

        self.label_vencimiento = Label(self.frame_entradas,text='Vencimiento',font=('century gothic',12),background='#EDE2E0')
        self.label_vencimiento.place(relx=0.05,rely=0.8,anchor='center')
        
        self.label_total_venta = Label(self.frame_resumen_venta,text=f'Total de la venta: $ ',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_total_venta.place(relx=0.75,rely=0.5,anchor='center')

        self.label_usuario = Label(self.frame_informacion,font=('century gothic',12),background='#D3B9B4')
        self.label_usuario.place(relx=0.05,rely=0.5,anchor='center')

        self.label_en_stock = Label(self.frame_entradas,text='En stock:',font=('century gothic',12),background='#EDE2E0')
        self.label_en_stock.place(relx=0.53,rely=0.8,anchor='center')

        self.label_descripcion_producto = Label(self.frame_entradas,font=('century gothic',12),text='Producto: ',background='#D3B9B4')
        self.label_descripcion_producto.place(x=450,y=15)

        #Entries
        self.entry_codigo_producto = Entry(self.frame_entradas,width=20,font=('century gothic',12),bd=1,relief='solid')
        self.entry_codigo_producto.place(relx=0.18,rely=0.5,anchor='center') 

        self.entry_cliente = ttk.Combobox(self.frame_entradas,width=18,font=('century gothic',12))
        self.entry_cliente.place(relx=0.18,rely=0.2,anchor='center')

        self.entry_precio = Entry(self.frame_entradas,width=15,font=('century gothic',12),bd=1,relief='solid')
        self.entry_precio.place(relx=0.48,rely=0.5,anchor='center')

        self.entry_cantidad = Entry(self.frame_entradas,width=5,font=('century gothic',12),bd=1,relief='solid')
        self.entry_cantidad.place(relx=0.445,rely=0.8,anchor='center')

        self.entry_vencimiento = ttk.Combobox(self.frame_entradas,width=18,font=('century gothic',12))
        self.entry_vencimiento.place(relx=0.18,rely=0.8,anchor='center')

        #Botones
        ruta = self.rutas('imagenes','consulta_ventas.png')
        self.boton_buscar = Button(self.frame_entradas,font=('century gothic',14,'bold'),width=50,height=35,background='#D3B9B4',bd=2,relief='groove')
        imagen_buscar_pil = Image.open(ruta)
        imagen_buscar_pil_resize = imagen_buscar_pil.resize((30,30))
        imagen_buscar_tk = ImageTk.PhotoImage(imagen_buscar_pil_resize)
        self.boton_buscar.config(image=imagen_buscar_tk,compound='left',padx=10)
        self.boton_buscar.place(relx=0.3,rely=0.65,anchor='center')
        self.boton_buscar.image = imagen_buscar_tk

        ruta = self.rutas('imagenes','agregar_carrito.png')
        self.boton_carrito = Button(self.frame_entradas,text='Agregar al carrito',font=('century gothic',14,'bold'),width=200,height=35,background='#D3B9B4',bd=2,relief='groove')
        imagen_carrito_pil = Image.open(ruta)
        imagen_carrito_pil_resize = imagen_carrito_pil.resize((30,30))
        imagen_carrito_tk = ImageTk.PhotoImage(imagen_carrito_pil_resize)
        self.boton_carrito.config(image=imagen_carrito_tk,compound='left',padx=10)
        self.boton_carrito.place(relx=0.89,rely=0.25,anchor='center')
        self.boton_carrito.image = imagen_carrito_tk

        ruta = self.rutas('imagenes','eliminar.png')
        self.boton_eliminar_venta = Button(self.frame_entradas,text='Eliminar',font=('century gothic',14,'bold'),width=200,height=35,background='#D3B9B4',bd=2,relief='groove')
        imagen_eliminar_pil = Image.open(ruta)
        imagen_eliminar_pil_resize = imagen_eliminar_pil.resize((30,30))
        imagen_eliminar_tk = ImageTk.PhotoImage(imagen_eliminar_pil_resize)
        self.boton_eliminar_venta.config(image=imagen_eliminar_tk,compound='left',padx=10)
        self.boton_eliminar_venta.place(relx=0.89,rely=0.75,anchor='center')
        self.boton_eliminar_venta.image = imagen_eliminar_tk

        ruta = self.rutas('imagenes','listo.png')
        self.boton_finalizar_venta = Button(self.frame_resumen_venta,text='Finalizar Venta',font=('century gothic',14,'bold'),width=250,height=35,background='#D3B9B4',bd=2,relief='groove')
        imagen_finalizar_pil = Image.open(ruta)
        imagen_finalizar_pil_resize = imagen_finalizar_pil.resize((30,30))
        imagen_finalizar_tk = ImageTk.PhotoImage(imagen_finalizar_pil_resize)
        self.boton_finalizar_venta.config(image=imagen_finalizar_tk,compound='left',padx=10)
        self.boton_finalizar_venta.place(relx=0.45,rely=0.55,anchor='center')
        self.boton_finalizar_venta.image = imagen_finalizar_tk

        ruta = self.rutas('imagenes','consulta_ventas.png')
        self.boton_consultaventas = Button(self.frame_finalizar_venta)
        self.boton_consultaventas.config(text="Consultar\n Ventas",width=200,font=('century gothic',14,'bold'),background='#D3B9B4',bd=2,relief='groove')
        imagen_consultaventa_pil = Image.open(ruta)
        imagen_consultaventa_resize = imagen_consultaventa_pil.resize((30,30))
        imagen_consultaventa_tk = ImageTk.PhotoImage(imagen_consultaventa_resize)
        self.boton_consultaventas.config(image=imagen_consultaventa_tk,compound='left',padx=10)
        self.boton_consultaventas.place(relx=0.1,rely=0.5,anchor='center')
        self.boton_consultaventas.image = imagen_consultaventa_tk
        
        #Treeview
        self.style = ttk.Style(self.frame_detalle_ventas)
        self.style.configure("Treeview.Heading", font=('century gothic',12,'bold'))
        self.style.configure("Treeview", font=('century gothic',10))

        self.tv_ventas = ttk.Treeview(self.frame_detalle_ventas,columns=("col1","col2","col3","col4"),height=9)
        
        self.tv_ventas.column("#0",width=50,anchor='center')
        self.tv_ventas.column("col1",width=150,anchor='center')
        self.tv_ventas.column("col2",width=650,anchor='center')
        self.tv_ventas.column("col3",width=200,anchor='center')
        self.tv_ventas.column("col4",width=200,anchor='center')

        self.tv_ventas.heading("#0",text="#",anchor='center')
        self.tv_ventas.heading("col1",text='Código',anchor='center')
        self.tv_ventas.heading("col2",text='Descripción',anchor='center')
        self.tv_ventas.heading("col3",text='Precio Unitario',anchor='center')
        self.tv_ventas.heading("col4",text='Cantidad',anchor='center')

        self.tv_ventas.pack(side='left',fill='y')

    # Función para limpiar los entry
    def limpiar_cajas(self):
        self.entry_codigo_producto.delete(0,'end')
        self.entry_precio.delete(0,'end')
        self.entry_cantidad.delete(0,'end')
        self.entry_vencimiento.delete(0,'end')
    
    # Función para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_ventas.get_children():
            self.tv_ventas.delete(item)

################################################################################################################################################
################################################### VENTANA DE CONFIRMACIÓN DE VENTA ###########################################################

#Esta clase crea la ventana de confirmación de venta, donde se da un resumen de la venta, el monto total a pagar y se crean radiobuttons para la
#elección del modo de pago, además de eso se crea un entry para que se ingrese el monto abonado.

class ConfirmacionVenta:
    
    def __init__(self,root):
        self.root = root
        self.root.title('Confirmación de venta')
        self.root.geometry('400x450+483+149')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas("imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_confirmacion = Frame(self.root)
        self.frame_confirmacion.config(width=400,height=450,background='#EDE2E0')
        self.frame_confirmacion.place(relx=0,rely=0)

        #Labels
        self.label_numero_venta = Label(self.frame_confirmacion)
        self.label_numero_venta.config(text=f'Venta #',font=('century gothic',20,'bold'),background='#EDE2E0')
        self.label_numero_venta.place(relx=0.5,rely=0.1,anchor='center')

        self.label_total_venta = Label(self.frame_confirmacion)
        self.label_total_venta.config(text=f'Total a pagar: $',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_total_venta.place(relx=0.5,rely=0.2,anchor='center')

        self.label_entrega = Label(self.frame_confirmacion)
        self.label_entrega.config(text='Entrega: $',font=('century gothic',16,'bold'),background='#EDE2E0')
        self.label_entrega.place(relx=0.06,rely=0.68)

        #Entries
        self.entry_entrega = Entry(self.frame_confirmacion)
        self.entry_entrega.config(width=18,font=('century gothic',16),bd=1,relief='solid')
        self.entry_entrega.place(relx=0.35,rely=0.68)

        #Radiobuttons y labelframe
        #Se crea primero el LabelFrame que contendrá a los radiobuttons
        self.labelframe = LabelFrame(self.frame_confirmacion)
        self.labelframe.config(text='Medio de pago',padx=10,pady=10,width=100,background='#EDE2E0',font=('century gothic',14))
        self.labelframe.place(relx=0.5,rely=0.43,anchor='center')

        #Se crea una variable IntVar que almacenará los valores elegidos en los radiobuttons
        self.opcion = IntVar()
        self.opcion.set(1) #Se setea la opción en 1, de este modo aparecerá por defecto elegido en el primer boton

        #Se crea un estilo ttk.Style para poder asignarle background y tipo de fuente a los radiobuttos creados con ttk
        self.style = ttk.Style()
        self.style.configure("Custom.TRadiobutton",background='#EDE2E0',font=('century gothic',12))
        self.modo_pago_1 = ttk.Radiobutton(self.labelframe,text='Efectivo',variable=self.opcion,value=1,style="Custom.TRadiobutton",command=self.seleccion_radiobutton)
        self.modo_pago_1.config(width=30)
        self.modo_pago_1.pack(anchor='w',fill='both')
        self.modo_pago_2 = ttk.Radiobutton(self.labelframe,text='Transferencia',variable=self.opcion,value=2,style="Custom.TRadiobutton",command=self.seleccion_radiobutton)
        self.modo_pago_2.config(width=30)
        self.modo_pago_2.pack(anchor='w',fill='both')
        self.modo_pago_3 = ttk.Radiobutton(self.labelframe,text='Débito/Crédito',variable=self.opcion,value=3,style="Custom.TRadiobutton",command=self.seleccion_radiobutton)
        self.modo_pago_3.config(width=30)
        self.modo_pago_3.pack(anchor='w',fill='both')

        #Buttons
        ruta = self.rutas('imagenes','ventas.png')
        self.boton_confirmar = Button(self.frame_confirmacion)
        self.boton_confirmar.config(text='Confirmar',font=('century gothic',14,'bold'),width=150,padx=15,background='#D3B9B4',bd=2,relief='groove')
        imagen_confirmar_pil = Image.open(ruta)
        imagen_confirmar_resize = imagen_confirmar_pil.resize((30,30))
        imagen_confirmar_tk = ImageTk.PhotoImage(imagen_confirmar_resize)
        self.boton_confirmar.config(image=imagen_confirmar_tk,compound='left',anchor='center')
        self.boton_confirmar.place(relx=0.5,rely=0.9,anchor='center')
        self.boton_confirmar.image = imagen_confirmar_tk

    #Función que retornará la selección de los radiobuttons(1,2,3)
    def seleccion_radiobutton(self):
        return self.opcion.get()

################################################################################################################################################
################################################### VENTANA CONSULTA DE VENTAS #################################################################

#Clase para la creación de la ventana de consulta de ventas, donde se puede buscar las ventas entre dos fechas determinadas, luego se crean botones para
#filtrar ventas, ver detalle de ventas y eliminar ventas.

class ConsultaVentas:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Consulta de Ventas')
        self.root.geometry('1000x590+183+79')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas("imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(width=1000,height=40,background='#EDE2E0')
        self.frame_titulo.place(x=0,y=0)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(width=1000,height=90,background='#EDE2E0')
        self.frame_busqueda.place(x=0,y=40)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(width=1000,height=430,background="#EDE2E0")
        self.frame_treeview.place(x=0,y=130)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(width=1000,height=30,background='#EDE2E0')
        self.frame_informacion.place(x=0,y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(text='CONSULTA DE VENTAS',font=('century gothic',18,'bold'),background="#EDE2E0",foreground='#C18484')
        self.label_titulo.place(relx=0.5,rely=0.5,anchor='center')

        self.label_desde = Label(self.frame_busqueda)
        self.label_desde.config(text='Desde:',font=('century gothic',14),background="#EDE2E0")
        self.label_desde.place(relx=0.05,rely=0.2,anchor='center')

        self.label_hasta = Label(self.frame_busqueda)
        self.label_hasta.config(text='Hasta:',font=('century gothic',14),background="#EDE2E0")
        self.label_hasta.place(relx=0.05,rely=0.7,anchor='center')

        self.label_cliente = Label(self.frame_busqueda)
        self.label_cliente.config(text='Cliente',font=('century gothic',14),background="#EDE2E0")
        self.label_cliente.place(relx=0.35,rely=0.2,anchor='center')

        #Entries
        self.entry_desde = DateEntry(self.frame_busqueda,font=('century gothic',12),width=20,date_pattern="dd-mm-yyyy")
        self.entry_desde.place(relx=0.2,rely=0.22,anchor='center')

        self.entry_hasta = DateEntry(self.frame_busqueda,font=('century gothic',12),width=20,date_pattern="dd-mm-yyyy")
        self.entry_hasta.place(relx=0.2,rely=0.72,anchor='center')

        self.entry_cliente = ttk.Combobox(self.frame_busqueda)
        self.entry_cliente.config(font=('century gothic',14),width=18)
        self.entry_cliente.place(relx=0.5,rely=0.22,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','consulta_ventas.png')
        self.boton_buscar = Button(self.frame_busqueda)
        self.boton_buscar.config(text='Buscar',font=('century gothic',14,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_buscar_pil = Image.open(ruta)
        imagen_buscar_resize = imagen_buscar_pil.resize((25,25))
        imagen_buscar_tk = ImageTk.PhotoImage(imagen_buscar_resize)
        self.boton_buscar.config(image=imagen_buscar_tk,compound='left',padx=5)
        self.boton_buscar.place(relx=0.74,rely=0.25,anchor='center')
        self.boton_buscar.image = imagen_buscar_tk

        ruta = self.rutas('imagenes','pago_pendiente.png')
        self.boton_pendientes = Button(self.frame_busqueda)
        self.boton_pendientes.config(text='Pendientes',font=('century gothic',14,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_pendientes_pil = Image.open(ruta)
        imagen_pendientes_resize = imagen_pendientes_pil.resize((25,25))
        imagen_pendientes_tk = ImageTk.PhotoImage(imagen_pendientes_resize)
        self.boton_pendientes.config(image=imagen_pendientes_tk,compound='left',padx=5)
        self.boton_pendientes.place(relx=0.74,rely=0.73,anchor='center')
        self.boton_pendientes.image = imagen_pendientes_tk
        
        ruta = self.rutas('imagenes','detalle.png')
        self.boton_detalle = Button(self.frame_busqueda)
        self.boton_detalle.config(text='Detalle',font=('century gothic',14,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_detalle_pil = Image.open(ruta)
        imagen_detalle_resize = imagen_detalle_pil.resize((25,25))
        imagen_detalle_tk = ImageTk.PhotoImage(imagen_detalle_resize)
        self.boton_detalle.config(image=imagen_detalle_tk,compound='left',padx=5)
        self.boton_detalle.place(relx=0.9,rely=0.25,anchor='center')
        self.boton_detalle.image = imagen_detalle_tk

        ruta = self.rutas('imagenes','eliminar.png')
        self.boton_eliminar = Button(self.frame_busqueda)
        self.boton_eliminar.config(text='Eliminar',font=('century gothic',14,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_eliminar_pil = Image.open(ruta)
        imagen_eliminar_resize = imagen_eliminar_pil.resize((25,25))
        imagen_eliminar_tk = ImageTk.PhotoImage(imagen_eliminar_resize)
        self.boton_eliminar.config(image=imagen_eliminar_tk,compound='left',padx=5)
        self.boton_eliminar.place(relx=0.9,rely=0.73,anchor='center')
        self.boton_eliminar.image = imagen_eliminar_tk

        #Treeview

        self.tv_consultaventas = ttk.Treeview(self.frame_treeview,columns=('col1','col2','col3','col4','col5'),height=20)
        
        self.style = ttk.Style(self.frame_treeview)
        self.style.configure("Treeview.Heading", font=('century gothic',11,'bold'))
        self.style.configure("Treeview", font=('century gothic',10))

        self.tv_consultaventas.column("#0",width=80,anchor='center')
        self.tv_consultaventas.column("col1",width=150,anchor='center')
        self.tv_consultaventas.column("col2",width=300,anchor='center')
        self.tv_consultaventas.column("col3",width=150,anchor='center')
        self.tv_consultaventas.column("col4",width=150,anchor='center')
        self.tv_consultaventas.column("col5",width=150,anchor='center')

        self.tv_consultaventas.heading("#0",text="id_venta",anchor='center')
        self.tv_consultaventas.heading("col1",text='Fecha',anchor='center')
        self.tv_consultaventas.heading("col2",text='Cliente',anchor='center')
        self.tv_consultaventas.heading("col3",text='Monto Total',anchor='center')
        self.tv_consultaventas.heading("col4",text='Medio Pago',anchor='center')
        self.tv_consultaventas.heading("col5",text='Estado Venta',anchor='center')

        self.tv_consultaventas.grid(row=0,column=0,sticky='nsew')

        # Scrollbar Treeview
        self.scrollbar = ttk.Scrollbar(self.frame_treeview,orient='vertical',command=self.tv_consultaventas.yview)
        self.tv_consultaventas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,sticky='ns')

        self.frame_treeview.grid_rowconfigure(0,weight=1)
        self.frame_treeview.grid_columnconfigure(0,weight=1)

    #Función para limpiar los entry
    def limpiar_cajas(self):
        self.entry_cliente.delete(0,'end')
        self.entry_desde.delete(0,'end')
        self.entry_hasta.delete(0,'end')
    
    # Función para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_consultaventas.get_children():
            self.tv_consultaventas.delete(item)

################################################################################################################################################
################################################### VENTANA DETALLES DE VENTAS #################################################################

class DetalleVentas:

    def __init__(self,root):
        self.root = root
        self.root.title('Detalle de Venta')
        self.root.geometry('900x400+233+174')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas("imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_infoventa = Frame(self.root)
        self.frame_infoventa.config(width=900,height=50,background="#EDE2E0")
        self.frame_infoventa.place(x=0,y=0)

        self.frame_tvdetalle = Frame(self.root)
        self.frame_tvdetalle.config(width=900,height=300,background="#EDE2E0")
        self.frame_tvdetalle.place(x=0,y=50)

        self.frame_imprimir = Frame(self.root)
        self.frame_imprimir.config(width=900,height=50,background="#EDE2E0")
        self.frame_imprimir.place(x=0,y=350)

        #Labels
        self.label_nroventa = Label(self.frame_infoventa)
        self.label_nroventa.config(text='Venta # ',font=('century gothic',16,'bold'),background="#EDE2E0")
        self.label_nroventa.place(relx=0.5,rely=0.5,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','pdf.png')
        self.boton_pdf = Button(self.frame_imprimir)
        self.boton_pdf.config(text='Imprimir',font=('century gothic',12,'bold'),background='#D3B9B4',bd=2,relief='groove')
        imagen_pdf_pil = Image.open(ruta)
        imagen_pdf_resize = imagen_pdf_pil.resize((25,25))
        imagen_pdf_tk = ImageTk.PhotoImage(imagen_pdf_resize)
        self.boton_pdf.config(image=imagen_pdf_tk,compound='left',padx=10)
        self.boton_pdf.place(relx=0.5,rely=0.5,anchor='center')
        self.boton_pdf.image = imagen_pdf_tk

        #Treeview
        self.tv_detalleventas = ttk.Treeview(self.frame_tvdetalle,columns=('col1','col2','col3'),height=300)
        
        self.style = ttk.Style(self.frame_tvdetalle)
        self.style.configure("Treeview.Heading", font=('century gothic',10,'bold'))

        self.tv_detalleventas.column("#0",width=200,anchor='center')
        self.tv_detalleventas.column("col1",width=500,anchor='center')
        self.tv_detalleventas.column("col2",width=100,anchor='center')
        self.tv_detalleventas.column("col3",width=100,anchor='center')

        self.tv_detalleventas.heading("#0",text="Código",anchor='center')
        self.tv_detalleventas.heading("col1",text='Producto',anchor='center')
        self.tv_detalleventas.heading("col2",text='Precio',anchor='center')
        self.tv_detalleventas.heading("col3",text='Cantidad',anchor='center')
        
        self.tv_detalleventas.pack(side='left',fill='y')

################################################################################################################################################
################################################### VENTANA DETALLES DE VENTAS #################################################################

# Clase para la creación de una ventana que se va a llamar cuando el medio de pago elegido sea debito/credito, se permitirá poner un monto de
# dinero el cuál se sumará al monto total de la venta

class InterfazInteres:

    def __init__(self,root):
        self.root = root
        self.root.title('Interés por pago Débito/Crédito')
        self.root.geometry('400x200+483+274')
        self.root.resizable(False,False)
        self.root.iconbitmap(self.rutas("imagenes", "logosec_fondo.ico"))
        self.widgets()
    
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    def widgets(self):
        #Frames
        self.frame_interes = Frame(self.root)
        self.frame_interes.config(width=400,height=300,background='#EDE2E0')
        self.frame_interes.place(x=0,y=0)

        #Labels
        self.label_titulo = Label(self.frame_interes)
        self.label_titulo.config(text='Ingreso de Intereses',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_titulo.place(relx=0.5,rely=0.1,anchor='center')

        self.label_interes = Label(self.frame_interes)
        self.label_interes.config(text='Monto interés',font=('century gothic',14),background='#EDE2E0')
        self.label_interes.place(relx=0.3,rely=0.3,anchor='center')

        #Entries
        self.entry_interes = Entry(self.frame_interes)
        self.entry_interes.config(font=('century gothic',14),width=10,bd=1,relief='solid')
        self.entry_interes.place(relx=0.7,rely=0.3,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','mas.png')
        self.boton_interes = Button(self.frame_interes)
        self.boton_interes.config(text='Ingresar',font=('century gothic',14,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_interes_pil = Image.open(ruta)
        imagen_interes_resize = imagen_interes_pil.resize((20,20))
        imagen_interes_tk = ImageTk.PhotoImage(imagen_interes_resize)
        self.boton_interes.config(image=imagen_interes_tk,compound='left',padx=15)
        self.boton_interes.place(relx=0.5,rely=0.55,anchor='center')
        self.boton_interes.image = imagen_interes_tk
