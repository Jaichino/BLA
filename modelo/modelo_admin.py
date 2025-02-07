from modelo.database import BaseDatos

########################### MODELO DE ADMIN #################################
class ModeloAdmin:

    # Metodo para eliminar un usuario de la base de datos
    @staticmethod
    def eliminar_usuario(usuario):
        query = 'DELETE FROM Usuarios WHERE usuario = %s'
        BaseDatos.realizar_consulta(query,(usuario,),None)


    # Metodo para recuperar los usuarios de la base de datos
    @staticmethod
    def recuperar_usuarios():
        query = 'SELECT usuario FROM Usuarios'
        return BaseDatos.realizar_consulta(query,None,'SELECT')


    # Metodo para eliminar datos de tabla CuentaCorriente
    @staticmethod
    def eliminar_tabla_cc():
        query = 'DELETE FROM CuentaCorriente'
        BaseDatos.realizar_consulta(query,None,None)


    # Metodo para eliminar datos de tabla DetalleVentas
    @staticmethod
    def eliminar_tabla_detalleventas():
        query = 'DELETE FROM DetalleVentas'
        BaseDatos.realizar_consulta(query,None,None)


    # Metodo para eliminar datos de tabla Ventas
    @staticmethod
    def eliminar_tabla_ventas():
        query = 'DELETE FROM Ventas'
        BaseDatos.realizar_consulta(query,None,None)


    # Metodo para eliminar datos de tabla Productos
    @staticmethod
    def eliminar_tabla_productos():
        query = 'DELETE FROM Productos'
        BaseDatos.realizar_consulta(query,None,None)



