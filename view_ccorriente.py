from tkinter import Frame, Label, Button, Entry
from tkinter import ttk
from PIL import Image,ImageTk
import sys
import os
################################################################################################################################################
################################################### VENTANA DE CUENTA CORRIENTE ################################################################

#En este fichero se lleva a cabo la creación de la interfaz gráfica del módulo de Cuentas Corrientes.


class CuentaCorriente:

    def __init__(self,root):
        self.root = root
        self.root.title('BLA Estética - Cuentas Corrientes')
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
        self.frame_titulo.config(width=1000,height=50,background='#EDE2E0')
        self.frame_titulo.place(x=0,y=0)

        self.frame_separador = Frame(self.root)
        self.frame_separador.config(width=1000,height=2,background='#C18484')
        self.frame_separador.place(x=0,y=40)

        self.frame_busqueda = Frame(self.root)
        self.frame_busqueda.config(width=1000,height=80,background='#EDE2E0')
        self.frame_busqueda.place(x=0,y=50)

        self.frame_treeview = Frame(self.root)
        self.frame_treeview.config(width=1000,height=360,background='#EDE2E0')
        self.frame_treeview.place(x=0,y=130)

        self.frame_resumencc = Frame(self.root)
        self.frame_resumencc.config(width=1000,height=105,background='#EDE2E0')
        self.frame_resumencc.place(x=0,y=455)

        self.frame_informacion = Frame(self.root)
        self.frame_informacion.config(width=1000,height=30,background='#D3B9B4')
        self.frame_informacion.place(x=0,y=560)

        #Labels
        self.label_titulo = Label(self.frame_titulo)
        self.label_titulo.config(text='CUENTAS CORRIENTES',font=('century gothic',20,'bold'),background="#EDE2E0",foreground='#C18484')
        self.label_titulo.place(relx=0.5,rely=0.42,anchor='center')

        self.label_cliente = Label(self.frame_busqueda)
        self.label_cliente.config(text='Cliente',font=('century gothic',14),background="#EDE2E0")
        self.label_cliente.place(relx=0.05,rely=0.5,anchor='center')

        self.label_deudatotal = Label(self.frame_resumencc)
        self.label_deudatotal.config(text=f'Deuda Total: $ ',font=('century gothic',16,'bold'),background="#EDE2E0")
        self.label_deudatotal.place(relx=0.5,rely=0.25,anchor='center')

        self.label_usuario = Label(self.frame_informacion,font=('century gothic',12),background='#D3B9B4')
        self.label_usuario.place(relx=0.1,rely=0.5,anchor='center')

        #Entries
        self.entry_cliente = ttk.Combobox(self.frame_busqueda)
        self.entry_cliente.config(font=('century gothic',12),width=20)
        self.entry_cliente.place(relx=0.2,rely=0.5,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','consulta_ventas.png')
        self.boton_buscar = Button(self.frame_busqueda)
        self.boton_buscar.config(text='Buscar',font=('century gothic',14,'bold'),width=120,background='#D3B9B4',bd=2,relief='groove')
        imagen_buscar_pil = Image.open(ruta)
        imagen_buscar_resize = imagen_buscar_pil.resize((30,30))
        imagen_buscar_tk = ImageTk.PhotoImage(imagen_buscar_resize)
        self.boton_buscar.config(image=imagen_buscar_tk,compound='left',padx=15)
        self.boton_buscar.place(relx=0.4,rely=0.5,anchor='center')
        self.boton_buscar.image = imagen_buscar_tk

        ruta = self.rutas('imagenes','ventas.png')
        self.boton_agregarpago = Button(self.frame_resumencc)
        self.boton_agregarpago.config(text='Agregar pago',font=('century gothic',14,'bold'),width=180,background='#D3B9B4',bd=2,relief='groove')
        imagen_agregarpago_pil = Image.open(ruta)
        imagen_agregarpago_resize = imagen_agregarpago_pil.resize((30,30))
        imagen_agregarpago_tk = ImageTk.PhotoImage(imagen_agregarpago_resize)
        self.boton_agregarpago.config(image=imagen_agregarpago_tk,compound='left',padx=15)
        self.boton_agregarpago.place(relx=0.2,rely=0.7,anchor='center')
        self.boton_agregarpago.image = imagen_agregarpago_tk

        ruta = self.rutas('imagenes','modificar.png')
        self.boton_actualizarpago = Button(self.frame_resumencc)
        self.boton_actualizarpago.config(text='Actualizar Deuda',font=('century gothic',14,'bold'),width=180,background='#D3B9B4',bd=2,relief='groove')
        imagen_actualizarpago_pil = Image.open(ruta)
        imagen_actualizarpago_resize = imagen_actualizarpago_pil.resize((30,30))
        imagen_actualizarpago_tk = ImageTk.PhotoImage(imagen_actualizarpago_resize)
        self.boton_actualizarpago.config(image=imagen_actualizarpago_tk,compound='left',padx=15)
        self.boton_actualizarpago.place(relx=0.5,rely=0.7,anchor='center')
        self.boton_actualizarpago.image = imagen_actualizarpago_tk

        ruta = self.rutas('imagenes','eliminar.png')
        self.boton_borraroperacion = Button(self.frame_resumencc)
        self.boton_borraroperacion.config(text='Borrar Operación',font=('century gothic',14,'bold'),width=180,background='#D3B9B4',bd=2,relief='groove')
        imagen_borraroperacion_pil = Image.open(ruta)
        imagen_borraroperacion_resize = imagen_borraroperacion_pil.resize((30,30))
        imagen_borraroperacion_tk = ImageTk.PhotoImage(imagen_borraroperacion_resize)
        self.boton_borraroperacion.config(image=imagen_borraroperacion_tk,compound='left',padx=15)
        self.boton_borraroperacion.place(relx=0.8,rely=0.7,anchor='center')
        self.boton_borraroperacion.image = imagen_borraroperacion_tk

    
        #Treeview
        self.tv_cc = ttk.Treeview(self.frame_treeview,columns=('col1','col2','col3','col4'),height=15)

        self.style = ttk.Style(self.frame_treeview)
        self.style.configure("Treeview.Heading", font=('century gothic',12,'bold'))
        self.style.configure("Treeview",font=('century gothic',10))
        
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
        self.scrollbar = ttk.Scrollbar(self.frame_treeview,orient='vertical',command=self.tv_cc.yview)
        self.tv_cc.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,sticky='ns')

        self.frame_treeview.grid_rowconfigure(0,weight=1)
        self.frame_treeview.grid_columnconfigure(0,weight=1)

    # Función para limpiar los entry
    def limpiar_cajas(self):
        self.entry_cliente.delete(0,'end')
    
    # Función para limpiar el treeview
    def limpiar_treeview(self):
        for item in self.tv_cc.get_children():
            self.tv_cc.delete(item)

################################################################################################################################################
################################################### VENTANA INGRESO PAGO CUENTA CORRIENTE ######################################################

#Esta clase crea la ventana de confirmación de pago de una cuenta corriente, donde se ingresará el monto abonado de acuerdo a la venta seleccionada
#en el Treeview de cuentas corrientes.

class SaldarCuentaCorriente:
    
    def __init__(self,root):
        self.root = root
        self.root.title('Agregar pago a cuenta corriente')
        self.root.geometry('400x100+483+324')
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
        self.frame_saldocc = Frame(self.root)
        self.frame_saldocc.config(width=400,height=100,background='#EDE2E0')
        self.frame_saldocc.place(x=0,y=0)
        
        #Labels
        self.label_nuevopago = Label(self.frame_saldocc)
        self.label_nuevopago.config(text=f'Abona $',font=('century gothic',14),background='#EDE2E0')
        self.label_nuevopago.place(relx=0.25,rely=0.28,anchor='center')

        #Entries
        self.entry_nuevopago = Entry(self.frame_saldocc)
        self.entry_nuevopago.config(font=('century gothic',14),width=15,bd=1,relief='solid')
        self.entry_nuevopago.place(relx=0.6,rely=0.28,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','mas.png')
        self.boton_nuevopago = Button(self.frame_saldocc)
        self.boton_nuevopago.config(text='Agregar',font=('century gothic',12,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_nuevopago_pil = Image.open(ruta)
        imagen_nuevopago_resize = imagen_nuevopago_pil.resize((25,25))
        imagen_nuevopago_tk = ImageTk.PhotoImage(imagen_nuevopago_resize)
        self.boton_nuevopago.config(image=imagen_nuevopago_tk,compound='left',padx=15)
        self.boton_nuevopago.place(relx=0.5,rely=0.75,anchor='center')
        self.boton_nuevopago.image = imagen_nuevopago_tk 

################################################################################################################################################
################################################### VENTANA INGRESO PAGO CUENTA CORRIENTE ######################################################

#Esta clase crea la ventana de confirmación de pago de una cuenta corriente, donde se ingresará el monto abonado de acuerdo a la venta seleccionada
#en el Treeview de cuentas corrientes.

class ActualizarCuentaCorriente:
    
    def __init__(self,root):
        self.root = root
        self.root.title('Actualizar cuenta corriente')
        self.root.geometry('400x100+483+324')
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
        self.frame_actualizacioncc = Frame(self.root)
        self.frame_actualizacioncc.config(width=400,height=100,background='#EDE2E0')
        self.frame_actualizacioncc.place(x=0,y=0)
        
        #Labels
        self.label_actualizacion = Label(self.frame_actualizacioncc)
        self.label_actualizacion.config(text=f'Monto $',font=('century gothic',14),background='#EDE2E0')
        self.label_actualizacion.place(relx=0.25,rely=0.28,anchor='center')

        #Entries
        self.entry_actualizacion = Entry(self.frame_actualizacioncc)
        self.entry_actualizacion.config(font=('century gothic',14),width=15,bd=1,relief='solid')
        self.entry_actualizacion.place(relx=0.6,rely=0.28,anchor='center')

        #Buttons
        ruta = self.rutas('imagenes','mas.png')
        self.boton_actualizacion = Button(self.frame_actualizacioncc)
        self.boton_actualizacion.config(text='Agregar',font=('century gothic',12,'bold'),width=140,background='#D3B9B4',bd=2,relief='groove')
        imagen_actualizacion_pil = Image.open(ruta)
        imagen_actualizacion_resize = imagen_actualizacion_pil.resize((25,25))
        imagen_actualizacion_tk = ImageTk.PhotoImage(imagen_actualizacion_resize)
        self.boton_actualizacion.config(image=imagen_actualizacion_tk,compound='left',padx=15)
        self.boton_actualizacion.place(relx=0.5,rely=0.75,anchor='center')
        self.boton_actualizacion.image = imagen_actualizacion_tk 


