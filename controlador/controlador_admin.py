from vista.view_admin import InterfazAdmin
from vista.view_admin import InterfazEliminar
from vista.view_admin import InterfazNuevoUsuario
from modelo.modelo_login import ModeloLogin
from modelo.modelo_admin import ModeloAdmin
from tkinter import messagebox,Toplevel

########################## CONTROLADOR ADMINISTRADOR ########################
''' En este fichero se llevará a cabo la construccion del 
    controlador del modulo administrador
'''
class ControladorAdmin:

    def __init__(self,root):
        
        self.root = root
        self.vista_admin = InterfazAdmin(root)
        self.modelo_login = ModeloLogin()
        self.modelo_admin = ModeloAdmin()

        # Configuracion botones para iniciar ventanas
        self.vista_admin.boton_crearusuario.config(
            command = self.nueva_cuenta
        )

        self.vista_admin.boton_eliminarusuario.config(
            command = self.eliminar_cuenta
        )
        
        self.vista_admin.boton_eliminarbd.config(
            command = self.boton_limpiar_basedatos
        )
    
    ##################### INICIALIZACION DE VENTANAS ########################
    
    def nueva_cuenta(self):

        ''' Este metodo se encarga de inicializar la ventana de nueva venta,
            se crea un TopLevel de root y se llama a la clase de
            InterfazNuevoUsuario. En este metodo tambien se setean las
            funcionalidades de los widgets que pertenecen a dicha vista
        '''
        # Creacion de ventana
        self.toplevel_nuevacuenta = Toplevel(self.root)
        self.ventana_nuevacuenta = InterfazNuevoUsuario(
            self.toplevel_nuevacuenta
        )
        self.toplevel_nuevacuenta.grab_set()

        # Configuracion de botones
        self.ventana_nuevacuenta.boton_crearusuario.config(
            command = self.boton_crear_cuenta
        )

    
    def eliminar_cuenta(self):
        
        ''' Este metodo se encarga de inicializar la ventana de eliminacion 
            de cuentas, donde tambien se setean las funcionalidades de los 
            widgets que pertenecen a dicha vista
        '''
        self.toplevel_eliminarcuenta = Toplevel(self.root)
        self.ventana_eliminarcuenta = InterfazEliminar(
            self.toplevel_eliminarcuenta
        )
        self.toplevel_eliminarcuenta.grab_set()

        # Configuracion de usuarios dentro de ComboBox
        self.ventana_eliminarcuenta.entrycuenta.configure(
            values = self.lista_usuarios()
        )

        # Configuracion de botones
        self.ventana_eliminarcuenta.boton_modificarcontraseña.config(
            command = self.boton_eliminar_cuenta
        )

    ######################### LLENADO DE COMBOBOX ###########################

    def lista_usuarios(self):
        
        ''' Este metodo se encarga de la recuperacion de los usuarios que
            existen en la base de datos, luego devolvera una lista con todos
            ellos (en caso de que existan).
        '''

        lista_usuarios_bd = self.modelo_admin.recuperar_usuarios()

        if lista_usuarios_bd:
            lista_usuarios = [usuario[0] for usuario in lista_usuarios_bd]
        else:
            lista_usuarios = []
        
        return lista_usuarios

    ######################### ACCION DE BOTONES #############################

    def boton_crear_cuenta(self):

        ''' Este metodo crea nuevas cuentas para acceder al sistema, primero
            se obtienen las credenciales pasadas en los Entry, luego se
            encripta con el metodo contraseña_segura de ModeloLogin, se
            cargan dichas credenciales a la base de datos y se da un mensaje
            de confirmacion
        '''
        try:
            # Obtencion de datos para crear cuenta
            usuario = self.ventana_nuevacuenta.entrycuenta.get()
            contraseña = self.ventana_nuevacuenta.entrycontraseña.get()
            rol = self.ventana_nuevacuenta.entryrol.get()

            # Encryptacion de contraseña
            contraseña_segura = ModeloLogin.contraseña_segura(contraseña)

            # Insersion de datos en base de datos
            ModeloLogin.nuevo_usuario(usuario, contraseña_segura, rol)

            # Se cierra ventana
            self.toplevel_nuevacuenta.destroy()

            # Mensaje de confirmacion
            messagebox.showinfo(
                'Usuarios',
                f'Usuario {usuario} craedo correctamente!'
            )
        
        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Ha ocurrido un error inesperado - {error}'
            )
    
    # Boton para eliminar cuenta
    def boton_eliminar_cuenta(self):

        ''' Este metodo configura el boton para eliminar una cuenta de la
            base de datos, primero se obtiene la cuenta que se desea eliminar
            luego se realiza una consulta mediante un messagebox y si se
            decide eliminar la cuenta, se llama al metodo eliminar_usuario
            para llevar a cabo la eliminacion.
        '''
        try:
            # Obtencion de la cuenta a eliminar
            cuenta = self.ventana_eliminarcuenta.entrycuenta.get()

            confirmacion = messagebox.askyesno(
                'Eliminar Usuario',
                f'¿Desea eliminar al usuario: {cuenta}?'
            )

            if confirmacion:
                # Eliminacion de la cuenta
                self.modelo_admin.eliminar_usuario(cuenta)

                # Cierre de ventana
                self.toplevel_eliminarcuenta.destroy()

                # Mensaje de confirmacion
                messagebox.showinfo(
                    'Usuarios',
                    f'Usuario {cuenta} eliminado correctamente!'
                )

        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Ha ocurrido un error inesperado - {error}'
            )


    # Boton limpiar base de datos
    def boton_limpiar_basedatos(self):

        ''' Este metodo configura el boton de limpieza de base de datos,
            donde primero se consulta si se desean eliminar todos los
            registros existentes y en caso de confirmacion, se eliminan
            todos los datos de todas las tablas que conforman la base de
            datos
        '''
        # Confirmacion
        confirmacion = messagebox.askyesno(
            'Eliminar Datos',
            '¿Eliminar todos los datos existentes?'
        )

        if confirmacion:
            try:
                self.modelo_admin.eliminar_tabla_cc()
                self.modelo_admin.eliminar_tabla_detalleventas()
                self.modelo_admin.eliminar_tabla_ventas()
                self.modelo_admin.eliminar_tabla_productos()

                # Mensaje de confirmacion
                messagebox.showinfo(
                    'Base Eliminada',
                    'Se han eliminado todos los registros!'
                )
            
            except Exception as error:

                messagebox.showerror(
                    'Error',
                    f'Ha ocurrido un error inesperado - {error}'
                )
