from controlador.controlador_producto import ControladorProducto
from controlador.controlador_ventas import ControladorVentas
from controlador.controlador_ccorriente import ControladorCuentaCorriente
from controlador.controlador_admin import ControladorAdmin
from controlador.controlador_reportes import ControladorReportes
from modelo.modelo_login import ModeloLogin
from vista.view_menu_principal import MenuPrincipal
from tkinter import messagebox,Toplevel
from datetime import datetime
################################################################################################################################################
################################################### CONTROLADOR MENÚ PRINCIPAL #################################################################

# En este fichero se lleva a cabo la vinculación entre las distintas vistas y modelos. Por medio del menú principal se accederá a los distintos 
# controladores

#Función para obtener día y hora actual, que luego mediante el método after se actualizará cada un segundo automáticamente.
def fecha_y_hora_actual():
    ahora = datetime.now()
    ahora_formateado = ahora.strftime("%d/%m/%Y %H:%M:%S")
    return ahora_formateado

class ControladorMenuPrincipal:

    def __init__(self,root,usuario_actual):
        self.root = root
        self.usuario_actual = usuario_actual
        self.vista_mp = MenuPrincipal(self.root)
        
        self.vista_mp.label_usuario.config(text=f'Usuario: {self.usuario_actual}')

        self.actualizar_hora()

        #Configuración de los botones del menú principal para abrir los modulos del mismo
        self.vista_mp.boton_inventario.config(command=self.abrir_moduloproductos)
        self.vista_mp.boton_ventas.config(command=self.abrir_moduloventas)
        self.vista_mp.boton_cuentacorriente.config(command=self.abrir_moduloccorriente)
        self.vista_mp.boton_administrador.config(command=self.abrir_moduloadministrador)
        self.vista_mp.boton_reportes.config(command=self.abrir_moduloreportes)

        # Función para obtener el rol del usuario que se logeo
        self.rol_usuariologueado = ModeloLogin.recuperar_rol(self.usuario_actual)
    
    #En esta función se procede a actualizar la hora cada un segundo mediante el método after(milisegundos,función)
    def actualizar_hora(self):
        ahora = fecha_y_hora_actual()
        self.vista_mp.label_hora.config(text= f'Día y Hora: {ahora}')
        self.vista_mp.label_hora.after(1000,self.actualizar_hora)

    ###############################################################################################################################################
    #################################################### INICIALIZACIÓN DE VENTANAS ###############################################################

    # Funciones para abrir los modulos, se crean ventanas secundarias (TopLevel, que derivan de root)
    # Se minimiza primero el menú principal, luego se genera el TopLevel para abrir el nuevo módulo y se establece un
    # protocolo "WM_DELETE_WINDOW" que ejecutará la función cerrar_modulo cuando se cierre la ventana con la cruz roja
    
    def abrir_moduloproductos(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_producto = ControladorProducto(self.toplevel)
        self.vista_producto.vista_inventario.label_usuario.config(text=f'Usuario: {self.usuario_actual}')
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)
        
    def abrir_moduloventas(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_moduloventas = ControladorVentas(self.toplevel)
        self.vista_moduloventas.vista_ventas.label_usuario.config(text=f'Usuario: {self.usuario_actual}')
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloccorriente(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_moduloccorriente = ControladorCuentaCorriente(self.toplevel)
        self.vista_moduloccorriente.vista_ccorriente.label_usuario.config(text=f'Usuario: {self.usuario_actual}')
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloadministrador(self):
        # Se verifica que el rol del usuario que ingreso al sistema sea Administrador, en caso de no serlo, no se
        # permitirá el ingreso al modulo.
        if not self.rol_usuariologueado[0][0] == 'Administrador':
            messagebox.showerror('Error','No tienes permisos para ingresar')
            return
        
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_administrador = ControladorAdmin(self.toplevel)
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloreportes(self):
        if not self.rol_usuariologueado[0][0] in ['Administrador','Dueño']:
            messagebox.showerror('Error','No tienes permisos para ingresar')
            return
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_reportes = ControladorReportes(self.toplevel)
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    # Función para minimizar menú principal mediante el método .iconify()
    def minimizar_menu_principal(self):
        self.root.iconify()
    
    # Función que se ejecutará cuando se cierre un módulo, se destruirá la ventana y se abrirá nuevamente el menú principal
    def cerrar_modulo(self):
        self.toplevel.destroy()
        self.root.deiconify()
