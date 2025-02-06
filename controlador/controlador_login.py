from vista.view_login import LoginApp
from modelo.modelo_login import ModeloLogin
from vista.view_menu_principal import MenuPrincipal
from controlador.controlador_menuprincipal import ControladorMenuPrincipal
from tkinter import Tk,messagebox
import bcrypt
from controlador.controlador_producto import ControladorProducto
################################################################################################################################################
################################################### CONTROLADOR DEL LOGIN ######################################################################

# En este fichero se lleva a cabo la vinculación entre la vista y el modelo del login

class ControladorLogin:

    def __init__(self,root):
        self.root = root
        self.usuario_actual = None
        self.modelo_login = ModeloLogin()
        self.vista_login = LoginApp(self.root)
        self.vista_login.login_button.config(command=self.iniciar_sesion)

        # Se hace foco en el campo de usuario apenas se inicia el login
        self.vista_login.entry_user.focus()

        # Eventos para que cuando se presiona enter, se ejecute la función iniciar_sesion
        self.vista_login.entry_user.bind("<Return>",self.iniciar_sesion)
        self.vista_login.entry_password.bind("<Return>",self.iniciar_sesion)
        
    ###############################################################################################################################################
    #################################################### COMPROBACIÓN CONTRASEÑAS #################################################################

    #Función para recuperar usuario y contraseña ingresada en el login, y luego se compara con la contraseña almacenada en la base
    #de datos según el usuario ingresado
    def iniciar_sesion(self,event=None):

        usuario = self.vista_login.entry_user.get()
        contraseña = self.vista_login.entry_password.get().encode() #Se pasa a bites para compararla con bcrypt
        
        contraseña_almacenada = self.modelo_login.recuperar_contraseña(usuario)
    
        if not contraseña_almacenada:
            messagebox.showerror('Acceso Denegado','Usuario o Contraseña incorrectos')
            self.vista_login.entry_password.delete(0,'end')
            return
        
        contraseña_almacenada_bytes = contraseña_almacenada[0][0].encode()
        self.usuario_actual = usuario
    
        isLogin = bcrypt.checkpw(contraseña,contraseña_almacenada_bytes)
        
        if isLogin:
            self.abrir_menu_principal()
        else:
            messagebox.showerror('Acceso Denegado','Usuario o Contraseña incorrectos')
            self.vista_login.entry_password.delete(0,'end')
    
    ###############################################################################################################################################
    #################################################### INICIALIZACIÓN DE VENTANAS ###############################################################

    # Función para inicializar el menú principal
    def abrir_menu_principal(self):
        self.vista_login.root.destroy()
        self.nueva_root = Tk()
        ControladorMenuPrincipal(self.nueva_root,self.usuario_actual)
        self.nueva_root.mainloop()
        
