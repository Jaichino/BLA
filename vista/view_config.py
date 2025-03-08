##############################################################################
# Importaciones
##############################################################################

import os
import sys
from PIL import Image, ImageTk


class ConfigView():

    imagenes = {
        'admin':'imagenes/administrador.png',
        'acarrito' : 'imagenes/agregar-carrito.png',
        'consultaventa' : 'imagenes/consulta_ventas.png',
        'crearusuario': 'crear_usuario.png',
        'ccorriente': 'imagenes/cuenta_corriente.png',
        'detalle': 'imagenes/detalle.png',
        'deuda': 'imagenes/deuda.png',
        'dineroinventario': 'imagenes/dinero_inventario.png',
        'eliminar': 'eliminar.png',
        'estadistica': 'imagenes/estadistica.png',
        'excel': 'imagenes/excel.png',
        'filtrar': 'imagenes/filtrar.png',
        'guardar': 'imagenes/guardar.png',
        'istock': 'imagenes/ingresar_stock.png',
        'inventario': 'imagenes/inventario.png',
        'listo': 'imagenes/listo.png',
        'logofondo': 'imagenes/logo_fondo.png',
        'logosinfondo': 'imagenes/logo_sin_fondo.png',
        'icosec': 'imagenes/logosec_fondo.ico',
        'logosecfondo': 'imagenes/logosec_fondo.png',
        'logosecsinfondo': 'imagenes/logosec_sinfondo.png',
        'mas': 'imagenes/mas.png',
        'modificar': 'imagenes/modificar.png',
        'pagopendiente': 'imagenes/pago_pendiente.png',
        'pdf': 'imagenes/pdf.png',
        'reportes': 'imagenes/reportes.png',
        'sinstock': 'imagenes/sin_stock.png',
        'tarjeta': 'imagenes/tarjeta.png',
        'vencimientos': 'imagenes/vencimientos.png',
        'ventas': 'imagenes/ventas.png',
    }


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

