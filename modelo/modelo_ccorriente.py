from modelo.database import BaseDatos

####################### MODELO DE CUENTA CORRIENTE ##########################
'''
En este fichero se realizara la logica de negocio para el modulo de cuentas 
corrientes, que luego mediante el controlador, se vinculara con la vista.
'''
class ModeloCuentaCorriente:

    # Metodo para mostrar los clientes que tienen cuentas corrientes
    @staticmethod
    def clientes_cuentacorriente():
        query = ''' SELECT
                        DISTINCT cliente
                    FROM CuentaCorriente
                    ORDER BY cliente
                '''
        return BaseDatos.realizar_consulta(query,None,'SELECT')
        

    # Metodo para mostrar informacion de cuentas corrientes
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
    

    # Metodo para ingregar un pago dentro de una cuenta corriente determinada
    @staticmethod
    def ingresar_pago_cc(
                            nro_operacion, 
                            cliente,
                            tipo_operacion,
                            monto_operacion,
                            monto_pendiente
                        ):

        query = ''' INSERT INTO CuentaCorriente 
                    (nro_operacion,
                    cliente,
                    tipo_operacion,
                    monto_operacion,
                    monto_pendiente)
                    VALUES (%s,%s,%s,%s,%s)
                '''
        
        BaseDatos.realizar_consulta(query,
                                    (nro_operacion,
                                    cliente,
                                    tipo_operacion,
                                    monto_operacion,
                                    monto_pendiente),
                                    None)


    # Metodo para eliminar una cuenta corriente
    @staticmethod
    def eliminar_cuentacorriente(cliente):
        
        query = 'DELETE FROM CuentaCorriente WHERE cliente = %s'
        
        BaseDatos.realizar_consulta(query,(cliente,),None)


    # Metodo para obtener ultimo nro_operación de acuerdo a cliente
    @staticmethod
    def ultimo_nro_operacion(cliente):
        
        query = ''' SELECT MAX(nro_operacion) 
                    FROM CuentaCorriente WHERE cliente = %s
                '''
        
        return BaseDatos.realizar_consulta(query,(cliente,),'SELECT')
    

    # Metodo para obtener ultimo monto_pendiente de un cliente determinado
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
    

    # Metodo para eliminar ultima operacion que se hizo en cuenta corriente
    @staticmethod
    def eliminar_ultima_operacion(nro_operacion,cliente):
        
        query = ''' DELETE FROM CuentaCorriente 
                    WHERE nro_operacion = %s AND cliente = %s
                '''
        
        BaseDatos.realizar_consulta(query,(nro_operacion,cliente),None)
