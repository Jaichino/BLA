from tkinter import Tk,messagebox
import bcrypt
from vista.view_login import LoginApp
from modelo.modelo_login import ModeloLogin
from vista.view_menu_principal import MenuPrincipal
from controlador.controlador_menuprincipal import ControladorMenuPrincipal
from controlador.controlador_producto import ControladorProducto


############################ CONTROLADOR DEL LOGIN ##########################

''' En este fichero se lleva a cabo la vinculacion entre la vista y el modelo
    del login
'''

class ControladorLogin:

    def __init__(self, root):
        self.root = root
        self.usuario_actual = None
        self.modelo_login = ModeloLogin()
        self.vista_login = LoginApp(self.root)
        self.vista_login.login_button.config(command = self.iniciar_sesion)

        # Foco en campo de usuario
        self.vista_login.entry_user.focus()

        # Asignacion de eventos
        self.vista_login.entry_user.bind("<Return>", self.iniciar_sesion)
        self.vista_login.entry_password.bind("<Return>", self.iniciar_sesion)
        

    def iniciar_sesion(self,event=None):

        ''' Este metodo se encarga de validar el inicio de sesion del usuario
            al sistema.
            Primero se obtienen los valores de los campos de usuario y
            contraseña. En funcion del cliente introducido, se busca la
            contraseña almacenada, si no existe, se denega el ingreso, caso
            contrario, se verifica que la contraseña ingresada sea igual a la
            almacenada. Si la contraseña es correcta, se abre menu principal
        '''
        # Obtencion entradas de usuario
        usuario = self.vista_login.entry_user.get()
        #Se pasa contraseña a bites para compararla con bcrypt
        contraseña = self.vista_login.entry_password.get().encode()
        
        # Obtencion de contraseña almacenada en funcion de usuario ingresado
        contraseña_almacenada = self.modelo_login.recuperar_contraseña(
            usuario
        )

        # Verificacion de contraseña
        if not contraseña_almacenada:
            messagebox.showerror(
                'Acceso Denegado',
                'Usuario o Contraseña incorrectos'
            )
            self.vista_login.entry_password.delete(0,'end')
            return
        
        # Se pasa contraseña almacenada a bytes para comparacion
        contraseña_almacenada_bytes = contraseña_almacenada[0][0].encode()
        self.usuario_actual = usuario

        # Verificacion de contraseñas usando bcrypt
        isLogin = bcrypt.checkpw(contraseña,contraseña_almacenada_bytes)
        
        # Si las contraseñas son iguales, se entra a sistema
        if isLogin:
            self.abrir_menu_principal()
        else:
            messagebox.showerror(
                'Acceso Denegado',
                'Usuario o Contraseña incorrectos'
            )
            self.vista_login.entry_password.delete(0,'end')
    

    def abrir_menu_principal(self):

        ''' Metodo para inicializar la ventana del menu principal, se inicia
            un nuevo root que sera heredado a los modulos siguientes
        '''
        self.vista_login.root.destroy()
        self.nueva_root = Tk()
        ControladorMenuPrincipal(self.nueva_root,self.usuario_actual)
        self.nueva_root.mainloop()
        
