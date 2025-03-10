##############################################################################
# Importaciones
##############################################################################

import os
import sys
from PIL import Image, ImageTk


class ConfigView():

    ##########################################################################
    # Imagenes de la aplicacion
    ##########################################################################

    img = {
        'admin':'administrador.png',
        'acarrito' : 'agregar_carrito.png',
        'consultaventa' : 'consulta_ventas.png',
        'cusuario': 'crear_usuario.png',
        'ccorriente': 'cuenta_corriente.png',
        'detalle': 'detalle.png',
        'deuda': 'deuda.png',
        'dineroinventario': 'dinero_inventario.png',
        'eliminar': 'eliminar.png',
        'estadistica': 'estadistica.png',
        'excel': 'excel.png',
        'filtrar': 'filtrar.png',
        'guardar': 'guardar.png',
        'istock': 'ingresar_stock.png',
        'inventario': 'inventario.png',
        'listo': 'listo.png',
        'logofondo': 'logo_fondo.png',
        'logosinfondo': 'logo_sin_fondo.png',
        'icosec': 'logosec_fondo.ico',
        'logosecfondo': 'logosec_fondo.png',
        'logosecsinfondo': 'logosec_sinfondo.png',
        'mas': 'mas.png',
        'modificar': 'modificar.png',
        'pagopendiente': 'pago_pendiente.png',
        'pdf': 'pdf.png',
        'reportes': 'reportes.png',
        'sinstock': 'sin_stock.png',
        'tarjeta': 'tarjeta.png',
        'vencimientos': 'vencimientos.png',
        'ventas': 'ventas.png',
    }

    ##########################################################################
    # Colores y fuentes utilizadas
    ##########################################################################

    clr = {
        'hard':'#C18484',
        'medium':'#D3B9B4',
        'soft': '#EDE2E0'
    }

    fnt = {
        'titulo': ('century gothic',28,'bold'),
        'titmodulo': ('century gothic',20,'bold'),
        'btnmenu': ('century gothic',18,'bold'),
        'text10': ('century gothic',10),
        'text12': ('century gothic',12),
        'text14': ('century gothic',14),
        'text16': ('century gothic',16),
        'text12-b': ('century gothic',12,'bold'),
        'text14-b': ('century gothic',14,'bold'),
        'text16-b': ('century gothic',16,'bold'),
        'text18-b': ('century gothic',18,'bold'),
    }

    ##########################################################################
    # Metodo para manejo de rutas
    ##########################################################################

    @staticmethod
    def rutas(*paths):
        
        """ Metodo para el manejo de rutas de imagenes a la hora de
            generar el ejecutable con PyInstaller.
        """

        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)


    ##########################################################################
    # Metodo formateo de imagenes
    ##########################################################################

    @staticmethod
    def formateo_imagen(img, x=None, y=None):

        ''' Método para el formateo de imagenes.
        '''

        imagen = ConfigView.rutas('../imagenes', img)

        if x is None and y is None:
            return imagen
        
        else:
            
            im = Image.open(imagen)
            im_res = im.resize((x,y))
            im_tk = ImageTk.PhotoImage(im_res)

            return im_tk
