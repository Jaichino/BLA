from view_admin import InterfazAdmin,InterfazEliminar,InterfazNuevoUsuario
from modelo_login import ModeloLogin
from modelo_admin import ModeloAdmin
from tkinter import Tk,messagebox,Toplevel

################################################################################################################################################
#################################################### CONTROLADOR ADMINISTRADOR #################################################################

# En este fichero se llevará a cabo la construcción del controlador del módulo administrador

class ControladorAdmin:

    def __init__(self,root):
        self.root = root
        self.vista_admin = InterfazAdmin(root)
        self.modelo_login = ModeloLogin()
        self.modelo_admin = ModeloAdmin()

        # Configuración botones para iniciar ventanas
        self.vista_admin.boton_crearusuario.config(command=self.nueva_cuenta)
        self.vista_admin.boton_eliminarusuario.config(command=self.eliminar_cuenta)
        self.vista_admin.boton_eliminarbd.config(command=self.boton_limpiar_basedatos)
    
    ################################################### INICIALIZACIÓN DE VENTANAS ###############################################################
    
    # Función que crea un TopLevel encargado de abrir la ventana de nueva cuenta
    def nueva_cuenta(self):
        self.toplevel_nuevacuenta = Toplevel(self.root)
        self.ventana_nuevacuenta = InterfazNuevoUsuario(self.toplevel_nuevacuenta)
        self.toplevel_nuevacuenta.grab_set()

        # Configuración de botones
        self.ventana_nuevacuenta.boton_crearusuario.config(command=self.boton_crear_cuenta)

    # Función que crea un TopLevel encargado de abrir la ventana de eliminar cuenta
    def eliminar_cuenta(self):
        self.toplevel_eliminarcuenta = Toplevel(self.root)
        self.ventana_eliminarcuenta = InterfazEliminar(self.toplevel_eliminarcuenta)
        self.toplevel_eliminarcuenta.grab_set()

        # Configuración de usuarios dentro de ComboBox
        self.ventana_eliminarcuenta.entrycuenta.configure(values=self.lista_usuarios())

        # Configuración de botones
        self.ventana_eliminarcuenta.boton_modificarcontraseña.config(command=self.boton_eliminar_cuenta)

    ########################################################### LLENADO DE COMBOBOX ################################################################

    def lista_usuarios(self):
        # Recuperación de usuarios de la base de datos
        lista_usuarios_bd = self.modelo_admin.recuperar_usuarios()

        # Verificación
        if lista_usuarios_bd:
            lista_usuarios = [usuario[0] for usuario in lista_usuarios_bd]
        else:
            lista_usuarios = []
        
        return lista_usuarios

    ########################################################### ACCIÓN DE BOTONES ##################################################################
    # Botón para crear nueva cuenta
    def boton_crear_cuenta(self):
        try:
            # Obtención de datos para crear cuenta
            usuario = self.ventana_nuevacuenta.entrycuenta.get()
            contraseña = self.ventana_nuevacuenta.entrycontraseña.get()
            rol = self.ventana_nuevacuenta.entryrol.get()

            # Encryptación de contraseña
            contraseña_segura = ModeloLogin.contraseña_segura(contraseña)

            # Insersión de datos en base de datos
            ModeloLogin.nuevo_usuario(usuario,contraseña_segura,rol)

            # Se cierra ventana
            self.toplevel_nuevacuenta.destroy()

            # Mensaje de confirmación
            messagebox.showinfo('Usuarios',f'Usuario {usuario} craedo correctamente!')


        except Exception as error:
            messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')
    
    # Botón para eliminar cuenta
    def boton_eliminar_cuenta(self):
        try:
            # Obtención de la cuenta a eliminar
            cuenta = self.ventana_eliminarcuenta.entrycuenta.get()

            confirmacion = messagebox.askyesno('Eliminar Usuario',f'¿Desea eliminar al usuario: {cuenta}?')

            if confirmacion:

                # Eliminación de la cuenta
                self.modelo_admin.eliminar_usuario(cuenta)

                # Cierre de ventana
                self.toplevel_eliminarcuenta.destroy()

                # Mensaje de confirmación
                messagebox.showinfo('Usuarios',f'Usuario {cuenta} eliminado correctamente!')

        except Exception as error:
            messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')


    # Botón limpiar base de datos
    def boton_limpiar_basedatos(self):
        # Confirmación de eliminación
        confirmacion = messagebox.askyesno('Eliminar Datos','¿Eliminar todos los datos existentes?')

        if confirmacion:
            try:
                # Eliminación de datos en base de datos. Primero se elimina de CuentaCorriente, luego DetalleVentas, Ventas y finalmente Productos
                self.modelo_admin.eliminar_tabla_cc()
                self.modelo_admin.eliminar_tabla_detalleventas()
                self.modelo_admin.eliminar_tabla_ventas()
                self.modelo_admin.eliminar_tabla_productos()

                # Mensaje de confirmación
                messagebox.showinfo('Base Eliminada','Se han eliminado todos los registros de la base de datos!')
            
            except Exception as error:
                messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')
    