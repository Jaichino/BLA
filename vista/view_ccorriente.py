##############################################################################
# Importaciones
##############################################################################

from tkinter import Frame, Label, Button, Entry
from tkinter import ttk
from vista.view_config import ConfigView

###################### VENTANA DE CUENTA CORRIENTE ###########################

''' En este fichero se lleva a cabo la creacion de la interfaz grafica del 
    modulo de Cuentas Corrientes.
'''

class CuentaCorriente:

    ''' Clase para la creacion de la ventana principal del modulo de cuentas
        corrientes
    '''

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Cuentas Corrientes')
        self.root.geometry('1000x590+183+79')
        self.root.resizable(False,False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()
    
    
    def widgets(self):

        # Referencia a imagenes
        self.img['consulta_ventas'] = ConfigView.formateo_imagen(
            ConfigView.img['consultaventa'], 30, 30
        )
        self.img['ventas'] = ConfigView.formateo_imagen(
            ConfigView.img['ventas'], 30, 30
        )
        self.img['modificar'] = ConfigView.formateo_imagen(
            ConfigView.img['modificar'], 30, 30
        )
        self.img['eliminar'] = ConfigView.formateo_imagen(
            ConfigView.img['eliminar'], 30, 30
        )

        #Frames
        self.frame_titulo = Frame(self.root)
        self.frame_titulo.config(
            width=1000, height=50, background=ConfigView.clr['soft']
        )
        self.frame_titulo.place(x=0,y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(
            width=1000, height=2, background=ConfigView.clr['hard']
        )
        self.frame_separador.place(x=0,y=40)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(
            width=1000, height=80, background=ConfigView.clr['soft']
        )
        self.frame_busqueda.place(x=0,y=50)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(
            width=1000, height=360, background=ConfigView.clr['soft']
        )
        self.frame_treeview.place(x=0,y=130)

        self.frame_resumencc = Frame(self.root)
        self.frame_resumencc.config(
            width=1000, height=105, background=ConfigView.clr['soft']
        )
        self.frame_resumencc.place(x=0,y=455)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(
            width=1000, height=30, background=ConfigView.clr['medium']
        )
        self.frame_informacion.place(x=0,y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(
            text='CUENTAS CORRIENTES',
            font=ConfigView.fnt['titmodulo'],
            background=ConfigView.clr['soft'],
            foreground=ConfigView.clr['hard']
        )
        self.label_titulo.place(relx=0.5,rely=0.42,anchor='center')

        self.label_cliente = Label(self.frame_busqueda)
        self.label_cliente.config(
            text='Cliente', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_cliente.place(relx=0.05,rely=0.5,anchor='center')

        self.label_deudatotal = Label(self.frame_resumencc)
        self.label_deudatotal.config(
            text=f'Deuda Total: $ ',
            font=ConfigView.fnt['text16-b'],
            background=ConfigView.clr['soft']
        )
        self.label_deudatotal.place(relx=0.5,rely=0.25,anchor='center')

        self.label_usuario = Label(
            self.frame_informacion,
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['medium']
        )
        self.label_usuario.place(relx=0.1,rely=0.5,anchor='center')

        #Entries
        self.entry_cliente = ttk.Combobox(self.frame_busqueda)
        self.entry_cliente.config(font=ConfigView.fnt['text12'],width=20)
        self.entry_cliente.place(relx=0.2,rely=0.5,anchor='center')

        #Buttons
        self.boton_buscar = Button(self.frame_busqueda)
        self.boton_buscar.config(
            text='Buscar',
            font=ConfigView.fnt['text14-b'],
            width=120,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['consulta_ventas'],
            compound='left'
        )
        self.boton_buscar.place(relx=0.4,rely=0.5,anchor='center')

        self.boton_agregarpago = Button(self.frame_resumencc)
        self.boton_agregarpago.config(
            text='Agregar pago',
            font=ConfigView.fnt['text14-b'],
            width=200,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['ventas'],
            compound='left'
        )
        self.boton_agregarpago.place(relx=0.2,rely=0.7,anchor='center')

        self.boton_actualizarpago = Button(self.frame_resumencc)
        self.boton_actualizarpago.config(
            text='Actualizar Deuda',
            font=ConfigView.fnt['text14-b'],
            width=200,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['modificar'],
            compound='left'
        )
        self.boton_actualizarpago.place(relx=0.5,rely=0.7,anchor='center')

        self.boton_borraroperacion = Button(self.frame_resumencc)
        self.boton_borraroperacion.config(
            text='Borrar Operación',
            font=ConfigView.fnt['text14-b'],
            width=200,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['eliminar'],
            compound='left'
        )
        self.boton_borraroperacion.place(relx=0.8,rely=0.7,anchor='center')

        #Treeview
        self.tv_cc = ttk.Treeview(
            self.frame_treeview,
            columns=('col1','col2','col3','col4'),
            height=15
        )

        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading", font=ConfigView.fnt['text12-b']
        )
        self.style.configure("Treeview",font=ConfigView.fnt['text10'])
        
        self.tv_cc.heading('#0',text='N° Operación',anchor='center')
        self.tv_cc.heading('col1',text='Fecha',anchor='center')
        self.tv_cc.heading('col2',text='Tipo',anchor='center')
        self.tv_cc.heading('col3',text='Monto Operación',anchor='center')
        self.tv_cc.heading('col4',text='Monto Pendiente',anchor='center')

        self.tv_cc.column('#0',width=140,anchor='center')
        self.tv_cc.column('col1',width=150,anchor='center')
        self.tv_cc.column('col2',width=290,anchor='center')
        self.tv_cc.column('col3',width=200,anchor='center')
        self.tv_cc.column('col4',width=200,anchor='center')

        self.tv_cc.grid(column=0,row=0,sticky='nsew')

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview, orient='vertical', command=self.tv_cc.yview
        )
        self.tv_cc.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,sticky='ns')

        self.frame_treeview.grid_rowconfigure(0,weight=1)
        self.frame_treeview.grid_columnconfigure(0,weight=1)

    # Metodo para limpiar los entry
    def limpiar_cajas(self):
        self.entry_cliente.delete(0,'end')
    
    # Metodo para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_cc.get_children():
            self.tv_cc.delete(item)


class SaldarCuentaCorriente:
    
    ''' Esta clase crea la ventana de confirmación de pago de una cuenta 
        corriente, donde se ingresará el monto abonado de acuerdo a la venta
        seleccionada en el Treeview de cuentas corrientes.
    '''
    
    def __init__(self, root):
            self.root = root
            self.root.title('Agregar pago a cuenta corriente')
            self.root.geometry('400x100+483+324')
            self.root.resizable(False,False)
            self.img = {}
            self.root.iconbitmap(
                ConfigView.formateo_imagen(ConfigView.img['icosec'])
            )
            self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['mas'] = ConfigView.formateo_imagen(
            ConfigView.img['mas'], 30, 30
        )

        #Frames
        self.frame_saldocc = Frame(self.root)
        self.frame_saldocc.config(
            width=400, height=100, background=ConfigView.clr['soft']
        )
        self.frame_saldocc.place(x=0,y=0)

        #Labels
        self.label_nuevopago = Label(self.frame_saldocc)
        self.label_nuevopago.config(
            text=f'Abona $',
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_nuevopago.place(relx=0.25,rely=0.28,anchor='center')

        #Entries
        self.entry_nuevopago = Entry(self.frame_saldocc)
        self.entry_nuevopago.config(
            font=ConfigView.fnt['text14'], width=15, bd=1, relief='solid'
        )
        self.entry_nuevopago.place(relx=0.6,rely=0.28,anchor='center')

        #Buttons
        self.boton_nuevopago = Button(self.frame_saldocc)
        self.boton_nuevopago.config(
            text='Agregar',
            font=ConfigView.fnt['text12-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['mas'],
            compound='left'
        )
        self.boton_nuevopago.place(relx=0.5,rely=0.75,anchor='center')


class ActualizarCuentaCorriente:

    ''' Esta clase crea la ventana de confirmacion de pago de una cuenta
        corriente, donde se ingresara el monto abonado de acuerdo a la venta
        seleccionada en el Treeview de cuentas corrientes.
    '''
    
    def __init__(self,root):

        self.root = root
        self.root.title('Actualizar cuenta corriente')
        self.root.geometry('400x100+483+324')
        self.root.resizable(False,False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()

    
    def widgets(self):

        # Referencia a imagenes
        self.img['mas'] = ConfigView.formateo_imagen(
            ConfigView.img['mas'], 30, 30
        )

        #Frames
        self.frame_actualizacioncc = Frame(self.root)
        self.frame_actualizacioncc.config(
            width=400, height=100, background=ConfigView.clr['soft']
        )
        self.frame_actualizacioncc.place(x=0,y=0)
        
        #Labels
        self.label_actualizacion = Label(self.frame_actualizacioncc)
        self.label_actualizacion.config(
            text=f'Monto $', 
            font=ConfigView.fnt['text14'], 
            background=ConfigView.clr['soft']
        )
        self.label_actualizacion.place(relx=0.25,rely=0.28,anchor='center')

        #Entries
        self.entry_actualizacion = Entry(self.frame_actualizacioncc)
        self.entry_actualizacion.config(
            font=ConfigView.fnt['text14'], width=15, bd=1, relief='solid'
        )
        self.entry_actualizacion.place(relx=0.6,rely=0.28,anchor='center')

        #Buttons
        self.boton_actualizacion = Button(self.frame_actualizacioncc)
        self.boton_actualizacion.config(
            text='Agregar',
            font=ConfigView.fnt['text12-b'],
            width=140,
            background=ConfigView.clr['medium'],
            bd=2,
            padx=10,
            relief='groove',
            image=self.img['mas'],
            compound='left'
        )
        self.boton_actualizacion.place(relx=0.5,rely=0.75,anchor='center')