from controlador.controlador_producto import ControladorProducto
from controlador.controlador_ventas import ControladorVentas
from controlador.controlador_ccorriente import ControladorCuentaCorriente
from controlador.controlador_admin import ControladorAdmin
from controlador.controlador_reportes import ControladorReportes
from modelo.modelo_login import ModeloLogin
from vista.view_menu_principal import MenuPrincipal
from tkinter import messagebox,Toplevel
from datetime import datetime

######################### CONTROLADOR MENU PRINCIPAL ########################

''' En este fichero se lleva a cabo la vinculacion entre las distintas vistas
    y modelos. Por medio del menu principal se accederá a los distintos 
    controladores
'''

def fecha_y_hora_actual():
    ''' Funcion para obtener la fecha y hora actuales, el cual se usara para
        visualizar la hora en el menu principal
    '''
    ahora = datetime.now()
    ahora_formateado = ahora.strftime("%d/%m/%Y %H:%M:%S")
    return ahora_formateado

class ControladorMenuPrincipal:

    def __init__(self, root, usuario_actual):
        self.root = root
        self.usuario_actual = usuario_actual
        self.vista_mp = MenuPrincipal(self.root)
        
        # Configuracion de Label con usuario que ingresa al sistema
        self.vista_mp.label_usuario.config(
            text=f'Usuario: {self.usuario_actual}'
        )

        # Llamado de metodo para actualizar la hora en label_hora
        self.actualizar_hora()

        #Configuracion de los botones del menu principal
        self.vista_mp.boton_inventario.config(
            command = self.abrir_moduloproductos
        )

        self.vista_mp.boton_ventas.config(
            command = self.abrir_moduloventas
        )
        
        self.vista_mp.boton_cuentacorriente.config(
            command = self.abrir_moduloccorriente
        )

        self.vista_mp.boton_administrador.config(
            command = self.abrir_moduloadministrador
        )

        self.vista_mp.boton_reportes.config(
            command = self.abrir_moduloreportes
        )

        # Obtencion de rol de usuario logueado
        self.rol_usuariologueado = ModeloLogin.recuperar_rol(
            self.usuario_actual
        )
    

    def actualizar_hora(self):

        ''' Metodo para actualizar la hora cada un segundo, llamando a la
            funcion fecha_y_hora_actual() y configurando el label_hora con
            el metodo after para generar una actualizacion del mismo cada
            1 segundo (1000 ms)
        '''

        ahora = fecha_y_hora_actual()
        self.vista_mp.label_hora.config(text= f'Día y Hora: {ahora}')
        self.vista_mp.label_hora.after(1000,self.actualizar_hora)


    ##################### INICIALIZACION DE VENTANAS ########################
    
    ''' Los siguientes metodos tienen la funcion de abrir los modulos
        respectivos del sistema. Para ello se llama al metodo para minimizar
        el menu principal, y luego se crea un TopLevel utilizando el root
        del menu principal. Con dicho TopLevel se instancia a las distintas
        clases controladoras encargadas de abrir las ventanas de los modulos.
        Finalmente, mediante un protocolo "WM_DELETE_WINDOW" se llama al
        metodo cerrar_modulo cada vez que se cierra un modulo.
    '''
    
    def abrir_moduloproductos(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_producto = ControladorProducto(self.toplevel)
        self.vista_producto.vista_inventario.label_usuario.config(
            text=f'Usuario: {self.usuario_actual}'
        )
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)
        
    def abrir_moduloventas(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_moduloventas = ControladorVentas(self.toplevel)
        self.vista_moduloventas.vista_ventas.label_usuario.config(
            text=f'Usuario: {self.usuario_actual}'
        )
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloccorriente(self):
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_moduloccorriente = ControladorCuentaCorriente(
            self.toplevel
        )
        self.vista_moduloccorriente.vista_ccorriente.label_usuario.config(
            text=f'Usuario: {self.usuario_actual}'
        )
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloadministrador(self):
        # Verificacion de rol
        if not self.rol_usuariologueado[0][0] == 'Administrador':
            messagebox.showerror('Error','No tienes permisos para ingresar')
            return
        
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_administrador = ControladorAdmin(self.toplevel)
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    def abrir_moduloreportes(self):
        # Verificacion de rol
        if not self.rol_usuariologueado[0][0] in ['Administrador','Dueño']:
            messagebox.showerror('Error','No tienes permisos para ingresar')
            return
        self.minimizar_menu_principal()
        self.toplevel = Toplevel(self.root)
        self.vista_reportes = ControladorReportes(self.toplevel)
        self.toplevel.grab_set()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    
    def minimizar_menu_principal(self):
        ''' Metodo para minimizar menu principal mediante iconify()'''
        self.root.iconify()
    
    
    def cerrar_modulo(self):

        ''' Metodo para cerrar modulos, primero se destruye el TopLevel con
            el metodo destroy(), y luego se abre nuevamente el menu principal
            usando el metodo deiconify()
        '''
        self.toplevel.destroy()
        self.root.deiconify()
