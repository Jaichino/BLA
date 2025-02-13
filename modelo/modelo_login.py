from modelo.database import BaseDatos
import bcrypt

############################ MODELO DE LOGIN ################################
'''
En este fichero se realizará la lógica del modelo de Lógin, donde se 
recuperarán contraseñas de usuarios y se ingresarán nuevos usuarios
'''
class ModeloLogin:

# Metodo para recuperar contraseña de acuerdo al usuario elegido
    @staticmethod
    def recuperar_contraseña(usuario):
        
        query = 'SELECT contraseña FROM Usuarios WHERE usuario = %s'
        
        return BaseDatos.realizar_consulta(query, (usuario,), 'SELECT')


# Metodo para obtener el rol del usuario que inicio sesión
    @staticmethod
    def recuperar_rol(usuario):
        
        query = 'SELECT rol FROM Usuarios WHERE usuario = %s'
        
        return BaseDatos.realizar_consulta(query, (usuario,), 'SELECT')
    

# Metodo insertar un nuevo usuario en la base de datos
    @staticmethod
    def nuevo_usuario(usuario,contraseña,rol):
        
        query = ''' INSERT INTO Usuarios (usuario,contraseña,rol)
                    VALUES (%s,%s,%s)
                '''
        
        BaseDatos.realizar_consulta(query, (usuario,contraseña,rol), None)


# Metodo para generar una contraseña segura, utilizando la librería bcrypt
    @staticmethod
    def contraseña_segura(contraseña):
        
        # Se pasa la contraseña ingresada a bites
        contraseña_bites = contraseña.encode()
        # Se genera una "salt" (fuerza) de la encryptación de la contraseña
        salt = bcrypt.gensalt() 
        # Se crea la contraseña encryptada
        contraseña_hasheada = bcrypt.hashpw(contraseña_bites, salt) 

        #Se obtiene la contraseña encryptada
        return contraseña_hasheada.decode() 


