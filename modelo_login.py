from database import BaseDatos
import bcrypt

####################################################################################################################################################
####################################################### MODELO DE LOGIN ############################################################################

#En este fichero se realizará la lógica del modelo de Lógin, donde se recuperarán contraseñas de usuarios y se ingresarán nuevos usuarios

class ModeloLogin:

####################################################################################################################################################
#Función para recuperar la contraseña almacenada en la base de datos de acuerdo al usuario elegido
    @staticmethod
    def recuperar_contraseña(usuario):
        query = 'SELECT contraseña FROM Usuarios WHERE usuario = %s'
        return BaseDatos.realizar_consulta(query,(usuario,),'SELECT')

####################################################################################################################################################
#Función para obtener el rol del usuario que inició sesión
    @staticmethod
    def recuperar_rol(usuario):
        query = 'SELECT rol FROM Usuarios WHERE usuario = %s'
        return BaseDatos.realizar_consulta(query,(usuario,),'SELECT')
    
####################################################################################################################################################
#Función insertar un nuevo usuario en la base de datos
    @staticmethod
    def nuevo_usuario(usuario,contraseña,rol):
        query = 'INSERT INTO Usuarios (usuario,contraseña,rol) VALUES (%s,%s,%s)'
        BaseDatos.realizar_consulta(query,(usuario,contraseña,rol),'INSERT')

####################################################################################################################################################
#Función para generar una contraseña segura, utilizando la librería bcrypt

    @staticmethod
    def contraseña_segura(contraseña):

        contraseña_bites = contraseña.encode() #Se pasa la contraseña ingresada a bites

        salt = bcrypt.gensalt() #Se genera una "salt" la cuál representa la "fuerza" de la encryptación de la contraseña (por defecto es 12)

        contraseña_hasheada = bcrypt.hashpw(contraseña_bites,salt) #Se crea la contraseña encryptada

        return contraseña_hasheada.decode() #Se obtiene la contraseña encryptada


