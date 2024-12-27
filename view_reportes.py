from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sys
import os
################################################################################################################################################
################################################### VENTANA DE REPORTES ########################################################################

# En este fichero se desarrolla la interfaz para el módulo de reportes, el mismo consistirá de distintos botónes los cuáles llamarán a un reporte
# determinado.

class InterfazReportes:
    
    def __init__(self,root):
        self.root = root
        self.root.title('BLA - Reportes')
        self.root.geometry('350x350+508+199')
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
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(width=350,height=350,background='#EDE2E0')
        self.frame_reportes.place(relx=0,rely=0)

        # Botones
        ruta = self.rutas('imagenes','ventas.png')
        self.boton_gananciastotales = Button(self.frame_reportes)
        self.boton_gananciastotales.config(text='Ganancias Totales',font=('century gothic',12,'bold'),width=260,padx=10,background='#D3B9B4',bd=2,relief='groove')
        imagen_gananciastotales_pil = Image.open(ruta)
        imagen_gananciastotales_resize = imagen_gananciastotales_pil.resize((30,30))
        imagen_gananciastotales_tk = ImageTk.PhotoImage(imagen_gananciastotales_resize)
        self.boton_gananciastotales.config(image=imagen_gananciastotales_tk,compound='left',anchor='center')
        self.boton_gananciastotales.place(relx=0.5,rely=0.1,anchor='center')
        self.boton_gananciastotales.image = imagen_gananciastotales_tk

        ruta = self.rutas('imagenes','deuda.png')
        self.boton_montocc = Button(self.frame_reportes)
        self.boton_montocc.config(text='Monto Adeudado',font=('century gothic',12,'bold'),width=260,padx=10,background='#D3B9B4',bd=2,relief='groove')
        imagen_montocc_pil = Image.open(ruta)
        imagen_montocc_resize = imagen_montocc_pil.resize((30,30))
        imagen_montocc_tk = ImageTk.PhotoImage(imagen_montocc_resize)
        self.boton_montocc.config(image=imagen_montocc_tk,compound='left',anchor='center')
        self.boton_montocc.place(relx=0.5,rely=0.3,anchor='center')
        self.boton_montocc.image = imagen_montocc_tk

        ruta = self.rutas('imagenes','dinero_inventario.png')
        self.boton_monto_inventario = Button(self.frame_reportes)
        self.boton_monto_inventario.config(text='Monto en Inventario',font=('century gothic',12,'bold'),width=260,padx=10,background='#D3B9B4',bd=2,relief='groove')
        imagen_monto_inventario_pil = Image.open(ruta)
        imagen_monto_inventario_resize = imagen_monto_inventario_pil.resize((30,30))
        imagen_monto_inventario_tk = ImageTk.PhotoImage(imagen_monto_inventario_resize)
        self.boton_monto_inventario.config(image=imagen_monto_inventario_tk,compound='left',anchor='center')
        self.boton_monto_inventario.place(relx=0.5,rely=0.5,anchor='center')
        self.boton_monto_inventario.image = imagen_monto_inventario_tk

        ruta = self.rutas('imagenes','estadistica.png')
        self.boton_masvendidos = Button(self.frame_reportes)
        self.boton_masvendidos.config(text='Productos más vendidos',font=('century gothic',12,'bold'),width=260,padx=10,background='#D3B9B4',bd=2,relief='groove')
        imagen_masvendidos_pil = Image.open(ruta)
        imagen_masvendidos_resize = imagen_masvendidos_pil.resize((30,30))
        imagen_masvendidos_tk = ImageTk.PhotoImage(imagen_masvendidos_resize)
        self.boton_masvendidos.config(image=imagen_masvendidos_tk,compound='left',anchor='center')
        self.boton_masvendidos.place(relx=0.5,rely=0.7,anchor='center')
        self.boton_masvendidos.image = imagen_masvendidos_tk

        ruta = self.rutas('imagenes','reportes.png')
        self.boton_var_ganancias = Button(self.frame_reportes)
        self.boton_var_ganancias.config(text='Ganancias Mensuales',font=('century gothic',12,'bold'),width=260,padx=10,background='#D3B9B4',bd=2,relief='groove')
        imagen_var_ganancias_pil = Image.open(ruta)
        imagen_var_ganancias_resize = imagen_var_ganancias_pil.resize((30,30))
        imagen_var_ganancias_tk = ImageTk.PhotoImage(imagen_var_ganancias_resize)
        self.boton_var_ganancias.config(image=imagen_var_ganancias_tk,compound='left',anchor='center')
        self.boton_var_ganancias.place(relx=0.5,rely=0.9,anchor='center')
        self.boton_var_ganancias.image = imagen_var_ganancias_tk

class GananciasTotales:
    def __init__(self,root):
        self.root = root
        self.root.title('Ganancias Totales')
        self.root.geometry('350x220+508+264')
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
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(width=350,height=220,background='#EDE2E0')
        self.frame_reportes.place(relx=0,rely=0)

        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(width=350,height=2,background='#C18484')
        self.frame_divisor.place(x=0,y=120)

        # Labels
        self.label_año = Label(self.frame_reportes,text='Año',font=('century gothic',12),background='#EDE2E0')
        self.label_año.place(x=10,y=20)

        self.label_mes = Label(self.frame_reportes,text='Mes',font=('century gothic',12),background='#EDE2E0')
        self.label_mes.place(x=180,y=20)

        self.label_monto = Label(self.frame_reportes,text='$',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_monto.place(relx=0.5,rely=0.75,anchor='center')

        # Entry
        self.entry_año = ttk.Combobox(self.frame_reportes,font=('century gothic',12),width=6)
        self.entry_año.place(x=60,y=20)

        self.entry_mes = ttk.Combobox(self.frame_reportes,font=('century gothic',12),width=6)
        self.entry_mes.place(x=230,y=20)

        # Boton
        self.boton_calcular = Button(self.frame_reportes)
        self.boton_calcular.config(text='Calcular',font=('century gothic',12,'bold'),width=10,padx=10,background='#D3B9B4',bd=2,relief='groove')
        self.boton_calcular.place(relx=0.5,rely=0.4,anchor='center')

class DeudasTotales:
    def __init__(self,root):
        self.root = root
        self.root.title('Deudas Totales')
        self.root.geometry('350x100+508+324')
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
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(width=350,height=100,background='#EDE2E0')
        self.frame_reportes.place(relx=0,rely=0)

        self.label_monto = Label(self.frame_reportes,text='$',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_monto.place(relx=0.5,rely=0.5,anchor='center')

class MontoInventario:
    def __init__(self,root):
        self.root = root
        self.root.title('Valor total de Inventario')
        self.root.geometry('350x100+508+324')
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
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(width=350,height=100,background='#EDE2E0')
        self.frame_reportes.place(relx=0,rely=0)

        self.label_valorinventario = Label(self.frame_reportes,text='$',font=('century gothic',18,'bold'),background='#EDE2E0')
        self.label_valorinventario.place(relx=0.5,rely=0.5,anchor='center')

class GananciasMensuales:
    def __init__(self,root):
        self.root = root
        self.root.title('Ganancias Mensuales')
        self.root.geometry('350x100+508+324')
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
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(width=350,height=100,background='#EDE2E0')
        self.frame_reportes.place(relx=0,rely=0)

        # Labels
        self.label_año = Label(self.frame_reportes,text='Año',font=('century gothic',12),background='#EDE2E0')
        self.label_año.place(relx=0.32,rely=0.25,anchor='center')

        # Entry
        self.entry_año = ttk.Combobox(self.frame_reportes,font=('century gothic',12),width=10)
        self.entry_año.place(relx=0.6,rely=0.24,anchor='center')

        # Boton
        self.boton_calcular = Button(self.frame_reportes)
        self.boton_calcular.config(text='Mostrar',font=('century gothic',12,'bold'),width=10,padx=10,background='#D3B9B4',bd=2,relief='groove')
        self.boton_calcular.place(relx=0.5,rely=0.75,anchor='center')

