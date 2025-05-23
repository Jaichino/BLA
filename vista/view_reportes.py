##############################################################################
# Importaciones
##############################################################################

from tkinter import Button,Frame,Label
from tkinter import ttk
from vista.view_config import ConfigView

############################ VISTA DE REPORTES ###############################
''' En este fichero se desarrolla la interfaz para el modulo de reportes, el 
    mismo consistira de distintos botones los cuales llamaran a un reporte
    determinado.
'''

class InterfazReportes:
    
    def __init__(self, root):
        self.root = root
        self.root.title('BLA - Reportes')
        self.root.geometry('350x350+508+199')
        self.root.resizable(False, False)
        self.img = {}
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['ventas'] = ConfigView.formateo_imagen(
            ConfigView.img['ventas'], 30, 30
        )
        self.img['deuda'] = ConfigView.formateo_imagen(
            ConfigView.img['deuda'], 30, 30
        )
        self.img['dineroinventario'] = ConfigView.formateo_imagen(
            ConfigView.img['dineroinventario'], 30, 30
        )
        self.img['estadistica'] = ConfigView.formateo_imagen(
            ConfigView.img['estadistica'], 30, 30
        )
        self.img['reportes'] = ConfigView.formateo_imagen(
            ConfigView.img['reportes'], 30, 30
        )

        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(
            width=350, height=350, background=ConfigView.clr['soft']
        )
        self.frame_reportes.place(relx=0, rely=0)

        # Botones
        self.boton_gananciastotales = Button(self.frame_reportes)
        self.boton_gananciastotales.config(
            text='Ganancias Totales',
            font=ConfigView.fnt['text12-b'],
            width=260,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['ventas'],
            compound='left',
        )
        self.boton_gananciastotales.place(
            relx=0.5, rely=0.1, anchor='center'
        )

        self.boton_montocc = Button(self.frame_reportes)
        self.boton_montocc.config(
            text='Monto Adeudado',
            font=ConfigView.fnt['text12-b'],
            width=260,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['deuda'],
            compound='left',
        )
        self.boton_montocc.place(relx=0.5, rely=0.3, anchor='center')

        self.boton_monto_inventario = Button(self.frame_reportes)
        self.boton_monto_inventario.config(
            text='Monto en Inventario',
            font=ConfigView.fnt['text12-b'],
            width=260,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['dineroinventario'],
            compound='left'
        )
        self.boton_monto_inventario.place(relx=0.5, rely=0.5, anchor='center')

        self.boton_masvendidos = Button(self.frame_reportes)
        self.boton_masvendidos.config(
            text='Productos más vendidos',
            font=ConfigView.fnt['text12-b'],
            width=260,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['estadistica'],
            compound='left'
        )
        self.boton_masvendidos.place(relx=0.5, rely=0.7, anchor='center')

        self.boton_var_ganancias = Button(self.frame_reportes)
        self.boton_var_ganancias.config(
            text='Ganancias Mensuales',
            font=ConfigView.fnt['text12-b'],
            width=260,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove',
            image=self.img['reportes'],
            compound='left'
        )
        self.boton_var_ganancias.place(relx=0.5, rely=0.9, anchor='center')

class GananciasTotales:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Ganancias Totales')
        self.root.geometry('350x220+508+264')
        self.root.resizable(False, False)
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()

    
    def widgets(self):

        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(
            width=350, height=220, background=ConfigView.clr['soft']
        )
        self.frame_reportes.place(relx=0, rely=0)

        self.frame_divisor = Frame(self.root)
        self.frame_divisor.config(
            width=350, height=2, background=ConfigView.clr['hard']
        )
        self.frame_divisor.place(x=0, y=120)

        # Labels
        self.label_año = Label(
            self.frame_reportes,
            text='Año',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_año.place(x=10, y=20)

        self.label_mes = Label(
            self.frame_reportes,
            text='Mes',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_mes.place(x=180, y=20)

        self.label_monto = Label(
            self.frame_reportes,
            text='$',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_monto.place(relx=0.5, rely=0.75, anchor='center')

        # ComboBox
        self.entry_año = ttk.Combobox(
            self.frame_reportes,
            font=ConfigView.fnt['text12'],
            width=6
        )
        self.entry_año.place(x=60, y=20)

        self.entry_mes = ttk.Combobox(
            self.frame_reportes,
            font=ConfigView.fnt['text12'],
            width=6
        )
        self.entry_mes.place(x=230, y=20)

        # Boton
        self.boton_calcular = Button(self.frame_reportes)
        self.boton_calcular.config(
            text='Calcular',
            font=ConfigView.fnt['text12-b'],
            width=10,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove'
        )
        self.boton_calcular.place(relx=0.5, rely=0.4, anchor='center')


class DeudasTotales:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Deudas Totales')
        self.root.geometry('350x100+508+324')
        self.root.resizable(False, False)
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec']))
        self.widgets()


    def widgets(self):
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(
            width=350, height=100, background=ConfigView.clr['soft']
        )
        self.frame_reportes.place(relx=0, rely=0)

        self.label_monto = Label(
            self.frame_reportes,
            text='$',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_monto.place(relx=0.5, rely=0.5, anchor='center')


class MontoInventario:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Valor total de Inventario')
        self.root.geometry('350x100+508+324')
        self.root.resizable(False, False)
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec']))
        self.widgets()

    
    def widgets(self):
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(
            width=350, height=100, background=ConfigView.clr['soft']
        )
        self.frame_reportes.place(relx=0, rely=0)

        # Labels
        self.label_valorinventario = Label(
            self.frame_reportes,
            text='$',
            font=ConfigView.fnt['text18-b'],
            background=ConfigView.clr['soft']
        )
        self.label_valorinventario.place(
            relx=0.5, rely=0.5, anchor='center'
        )


class GananciasMensuales:

    def __init__(self, root):
        self.root = root
        self.root.title('Ganancias Mensuales')
        self.root.geometry('350x100+508+324')
        self.root.resizable(False, False)
        self.root.iconbitmap(
            ConfigView.formateo_imagen(ConfigView.img['icosec'])
        )
        self.widgets()


    def widgets(self):
        # Frames
        self.frame_reportes = Frame(self.root)
        self.frame_reportes.config(
            width=350, height=100, background=ConfigView.clr['soft']
        )
        self.frame_reportes.place(relx=0, rely=0)

        # Labels
        self.label_año = Label(
            self.frame_reportes,
            text='Año',
            font=ConfigView.fnt['text12'],
            background=ConfigView.clr['soft']
        )
        self.label_año.place(relx=0.32, rely=0.25, anchor='center')

        # ComboBox
        self.entry_año = ttk.Combobox(
            self.frame_reportes,
            font=ConfigView.fnt['text12'],
            width=10
        )
        self.entry_año.place(relx=0.6, rely=0.24, anchor='center')

        # Boton
        self.boton_calcular = Button(self.frame_reportes)
        self.boton_calcular.config(
            text='Mostrar',
            font=ConfigView.fnt['text12-b'],
            width=10,
            padx=10,
            background=ConfigView.clr['medium'],
            bd=2,
            relief='groove'
        )
        self.boton_calcular.place(relx=0.5, rely=0.75, anchor='center')