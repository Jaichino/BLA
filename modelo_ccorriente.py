from database import BaseDatos

################################################################################################################################################
###################################################### MODELO DE CUENTA CORRIENTE ##############################################################

#En este fichero se realizará la lógica de negocio para el modulo de cuentas corrientes, que luego mediante el controlador, se vinculará con la vista.

class ModeloCuentaCorriente:

    ####################################################################################################################################################
    #Método para mostrar los clientes que tienen cuentas corrientes, para vincular en el combobox
    @staticmethod
    def clientes_cuentacorriente():
        query = ''' SELECT
                        DISTINCT cliente
                    FROM CuentaCorriente
                    ORDER BY cliente
                '''
        return BaseDatos.realizar_consulta(query,None,'SELECT')
        
    ####################################################################################################################################################
    #Método para mostrar información de cuentas corrientes para visualizar en treeview
    @staticmethod
    def ver_cuentascorrientes(cliente):
        query = ''' SELECT 
                        nro_operacion,
                        cliente,
                        TO_CHAR(fecha_operacion,'DD-MM-YYYY'),
                        tipo_operacion,
                        monto_operacion,
                        monto_pendiente
                    FROM CuentaCorriente WHERE cliente = %s'''
        return BaseDatos.realizar_consulta(query,(cliente,),'SELECT')
    
    ####################################################################################################################################################
    #Método para ingregar un pago dentro de una cuenta corriente determinada
    @staticmethod
    def ingresar_pago_cc(nro_operacion,cliente,tipo_operacion,monto_operacion,monto_pendiente):
        query = 'INSERT INTO CuentaCorriente (nro_operacion,cliente,tipo_operacion,monto_operacion,monto_pendiente) VALUES (%s,%s,%s,%s,%s)'
        BaseDatos.realizar_consulta(query,(nro_operacion,cliente,tipo_operacion,monto_operacion,monto_pendiente),'INSERT')

    ####################################################################################################################################################
    #Método para eliminar una cuenta corriente, se llamará a este método una vez que el monto pendiente llegue a 0.
    @staticmethod
    def eliminar_cuentacorriente(cliente):
        query = 'DELETE FROM CuentaCorriente WHERE cliente = %s'
        BaseDatos.realizar_consulta(query,(cliente,),'DELETE')

    ####################################################################################################################################################
    # Obtención del último nro_operación de acuerdo con el cliente elegido
    @staticmethod
    def ultimo_nro_operacion(cliente):
        query = 'SELECT MAX(nro_operacion) FROM CuentaCorriente WHERE cliente = %s'
        return BaseDatos.realizar_consulta(query,(cliente,),'SELECT')
    
    ####################################################################################################################################################
    # Obtención del último monto_pendiente de un determinado cliente
    @staticmethod
    def ultimo_monto_pendiente(cliente):
        query = ''' SELECT
                        monto_pendiente
                    FROM CuentaCorriente
                    WHERE cliente = %s
                    ORDER BY nro_operacion DESC
                    LIMIT 1
                '''
        return BaseDatos.realizar_consulta(query,(cliente,),'SELECT')
    

    ####################################################################################################################################################
    # Función para eliminar la última operación que se hizo en la cuenta corriente de un determinado cliente
    @staticmethod
    def eliminar_ultima_operacion(nro_operacion,cliente):
        query = 'DELETE FROM CuentaCorriente WHERE nro_operacion = %s AND cliente = %s'
        BaseDatos.realizar_consulta(query,(nro_operacion,cliente),'DELETE')
