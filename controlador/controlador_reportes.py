from vista.view_reportes import InterfazReportes,GananciasTotales,GananciasMensuales,MontoInventario,DeudasTotales
from modelo.modelo_reportes import ModeloReportes
from tkinter import Toplevel,messagebox
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,StrMethodFormatter

################################################################################################################################################
#################################################### CONTROLADOR DE REPORTES ###################################################################

# En este fichero se llevará a cabo la construcción del controlador del módulo de reportes

class ControladorReportes:

    def __init__(self,root):
        self.root = root
        self.vista_reportes = InterfazReportes(root)
        self.modelo_reportes = ModeloReportes()

        # Configuración de botones para inicializar ventanas
        self.vista_reportes.boton_gananciastotales.config(command=self.ganancias_totales)
        self.vista_reportes.boton_montocc.config(command=self.deudas_totales)
        self.vista_reportes.boton_monto_inventario.config(command=self.monto_inventario)
        self.vista_reportes.boton_var_ganancias.config(command=self.ganancias_mensuales)
        self.vista_reportes.boton_masvendidos.config(command=self.grafico_barras_productos)

    ##############################################################################################################################################    
    ################################################### INICIALIZACIÓN DE VENTANAS ###############################################################

    def ganancias_totales(self):
        self.toplevel_ganancias = Toplevel(self.root)
        self.ventana_ganancias = GananciasTotales(self.toplevel_ganancias)
        self.toplevel_ganancias.grab_set()

        # Seteo de comboboxs
        year = self.modelo_reportes.distintos_year()
        month = self.modelo_reportes.distintos_month()
        self.ventana_ganancias.entry_año.config(values=year)
        self.ventana_ganancias.entry_mes.config(values=month)

        self.ventana_ganancias.boton_calcular.config(command=self.calcular_ganancia_total)
    
    def deudas_totales(self):
        self.toplevel_deudas = Toplevel(self.root)
        self.ventana_deudas = DeudasTotales(self.toplevel_deudas)
        self.toplevel_deudas.grab_set()

        # Inicialización con la deuda
        deuda = self.modelo_reportes.deuda_cuentascorrientes()[0][0]
        if deuda:
            self.ventana_deudas.label_monto.config(text=f'$ {deuda}')
        else:
            self.ventana_deudas.label_monto.config(text='$0')
    
    def monto_inventario(self):
        self.toplevel_monto_inventario = Toplevel(self.root)
        self.ventana_monto_inventario = MontoInventario(self.toplevel_monto_inventario)
        self.toplevel_monto_inventario.grab_set()

        # Inicialización con monto total en inventario
        monto_inventario = self.modelo_reportes.monto_en_inventarios()[0][0]
        if monto_inventario:
            self.ventana_monto_inventario.label_valorinventario.config(text=f'$ {monto_inventario}')
        else:
            self.ventana_monto_inventario.label_valorinventario.config(text='$ 0')

    def ganancias_mensuales(self):
        self.toplevel_ganancias_mensuales = Toplevel(self.root)
        self.ventana_ganancias_mensuales = GananciasMensuales(self.toplevel_ganancias_mensuales)
        self.toplevel_ganancias_mensuales.grab_set()

        # Seteo de comboboxs
        year = self.modelo_reportes.distintos_year()
        self.ventana_ganancias_mensuales.entry_año.config(values=year)

        # Asignación de gráfico al boton
        self.ventana_ganancias_mensuales.boton_calcular.config(command=self.grafico_ganancias_mensuales)

    ###############################################################################################################################################
    ################################################### CÁLCULO DE INDICADORES ####################################################################

    # Función para mostrar ganancias totales según año y mes elegido en Comboboxs
    def calcular_ganancia_total(self):
        try:
            # Obtención de entradas de usuario
            year = int(self.ventana_ganancias.entry_año.get())
            month = int(self.ventana_ganancias.entry_mes.get())

            # Verificación de que se completen los campos
            if year == '' or month == '':
                messagebox.showerror('Error','Completar todos los campos')
            # Cálculo de ganancia
            ganancia = self.modelo_reportes.ganancias_totales(year,month)
            
            if ganancia:
                # Actualización del label de ganancia total
                self.ventana_ganancias.label_monto.config(text=f'$ {ganancia[0][2]}')
            else:
                messagebox.showinfo('Ganancias','No se encontraron resultados')

        except ValueError:
            messagebox.showerror('Error','Verificar campos')

        except Exception as error:
            messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')

    # Función para generar grafico de barras 5 productos más vendidos
    def grafico_barras_productos(self):
        # Obtención de la información de productos vendidos
        lista_productos = self.modelo_reportes.cinco_mas_vendidos()

        if lista_productos:
            # Separación de los distitos valores (se obtienen 3 listas con zip)
            codigo,descripcion,cantidad = zip(*lista_productos)

            # Creación gráfico
            plt.bar(codigo,cantidad,color ='#C18484')

            plt.title('5 Productos más vendidos',fontsize = 16)
            plt.xlabel('Códigos',fontsize=12)
            plt.ylabel('Cantidades Vendidas',fontsize=12)
            
            plt.show()
        else:
            messagebox.showinfo('Top Productos','No se encontraron resultados')

    # Función para generar gráfico de líneas para mostrar la evolución anual de las ganancias
    def grafico_ganancias_mensuales(self):
        try:
            # Obtención de año
            year_entry = int(self.ventana_ganancias_mensuales.entry_año.get())

            # Obtención de resultados
            ganancias_mensuales = self.modelo_reportes.ganancias_totales_grafico(year_entry)

            # Si se encuentran resultados, se genera gráfico, en caso contrario se muestra mensaje
            if ganancias_mensuales:
                year,month,ganancia = zip(*ganancias_mensuales)

                # Creación de gráfico
                plt.plot(month,ganancia,marker='o',linestyle='-',color='#C18484')
                plt.title(f'Ganancias mensuales - {year[0]}',fontsize=16)
                plt.xlabel('Mes',fontsize=12)
                plt.ylabel('Ganancia',fontsize=12)

                plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
                plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

                plt.show()
            
            else:
                messagebox.showinfo('Ganancias Mensuales','No se encontraron resultados')
        
        except ValueError:
            messagebox.showerror('Error','Revisar campo')
        except Exception as error:
            messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')
        

