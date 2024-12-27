from database import BaseDatos

################################################################################################################################################
####################################################### MODELO DE VENTAS #####################################################################

#En este fichero se realizará la lógica de negocio para el modulo de ventas, que luego mediante el controlador, se vinculará con la vista.

class ModeloVentas:

    ####################################################################################################################################################
    #Método para realizar una nueva venta
    @staticmethod
    def nueva_venta(nro_venta,cliente,monto_total,modo_pago,estado_venta):

        query = 'INSERT INTO Ventas (nro_venta,cliente,monto_total,id_modo_pago,estado_venta) VALUES (%s,%s,%s,%s,%s)'

        BaseDatos.realizar_consulta(query,(nro_venta,cliente,monto_total,modo_pago,estado_venta),'INSERT')

    ####################################################################################################################################################
    #Método para realizar una nueva venta
    @staticmethod
    def ingresar_detalle_ventas(nro_venta,nro_producto,precio_unitario,cantidad):

        query = 'INSERT INTO DetalleVentas (nro_venta,nro_producto,precio_unitario,cantidad) VALUES (%s,%s,%s,%s)'

        BaseDatos.realizar_consulta(query,(nro_venta,nro_producto,precio_unitario,cantidad),'INSERT')

    ####################################################################################################################################################
    #Método para obtener los nombres únicos de los clientes para vincular al combobox.
    @staticmethod
    def clientes():
        query = 'SELECT DISTINCT cliente FROM Ventas'
        return BaseDatos.realizar_consulta(query,None,'SELECT')
    
    ####################################################################################################################################################
    #Método para eliminar una venta de detalle de ventas, EJECUTAR PRIMERO y luego eliminar de tabla Ventas para evitar excepcion en la base de datos.
    @staticmethod
    def eliminar_detalleventas(nro_venta):
        query = 'DELETE FROM DetalleVentas WHERE nro_venta = %s'
        BaseDatos.realizar_consulta(query,(nro_venta,),'DELETE')
    
    #Ejecutar luego de eliminar_detalleventas para evitar error de referencia en la base de datos.
    @staticmethod
    def eliminar_venta(nro_venta):
        query = 'DELETE FROM Ventas WHERE nro_venta = %s'
        BaseDatos.realizar_consulta(query,(nro_venta,),'DELETE')
    
    ####################################################################################################################################################
    #Método para consultar ventas existentes en la base de datos, se puede filtrar las ventas por cliente o entre dos fechas elegidas por el usuario. Si 
    #cliente no es nulo (se dio un valor), entonces se filtrará unicamente por cliente. Si cliente es nulo (no se pasa valor), se filtrará por fechas.
    @staticmethod
    def consultar_ventas(desde,hasta,cliente=None):
        params = []
        
        if cliente is None:
            
            query = '''SELECT
                            v.nro_venta,
                            TO_CHAR(v.fecha_venta,'DD-MM-YYYY'),
                            v.cliente,
                            v.monto_total,
                            mp.modo_pago,
                            v.estado_venta
                        FROM Ventas v
                        INNER JOIN ModoPago mp ON v.id_modo_pago = mp.id_modo_pago
                        WHERE v.fecha_venta BETWEEN %s AND %s
                        ORDER BY v.nro_venta
                    '''
            params.append(desde)
            params.append(hasta)
        
        else:

            query = '''SELECT
                            v.nro_venta,
                            TO_CHAR(v.fecha_venta, 'DD-MM-YYYY'),
                            v.cliente,
                            v.monto_total,
                            mp.modo_pago,
                            v.estado_venta
                        FROM Ventas v
                        INNER JOIN ModoPago mp ON v.id_modo_pago = mp.id_modo_pago
                        WHERE v.cliente = %s
                        ORDER BY v.nro_venta
                    '''
            params.append(cliente,)
        

        return BaseDatos.realizar_consulta(query,params,'SELECT')

    ####################################################################################################################################################
    #Método para consultar el detalle de una determinada venta pasada como parámetro.
    @staticmethod
    def consultar_detalleventas(nro_venta):

        query = '''SELECT
                        p.codigo_producto,
                        p.descripcion,
                        dv.precio_unitario,
                        dv.cantidad
                        FROM Productos p
                        INNER JOIN DetalleVentas dv ON p.nro_producto = dv.nro_producto
                        WHERE dv.nro_venta = %s                     
                '''
        return BaseDatos.realizar_consulta(query,(nro_venta,),'SELECT')
    
    ####################################################################################################################################################
    #Método para obtener el monto total de una determinada venta
    @staticmethod
    def monto_total_venta(nro_venta):
        query = 'SELECT monto_total FROM Ventas WHERE nro_venta = %s'
        return BaseDatos.realizar_consulta(query,(nro_venta,),'SELECT')
    
    ####################################################################################################################################################
    #Método para obtener el último número de venta
    @staticmethod
    def ultimo_nro_venta():
        query = 'SELECT MAX(nro_venta) FROM Ventas'
        return BaseDatos.realizar_consulta(query,None,'SELECT')

    ####################################################################################################################################################
    #Método para actualizar estado de venta a Pagado
    @staticmethod
    def actualizacion_estadoventa(cliente):
        query = 'UPDATE Ventas SET estado_venta = %s WHERE cliente = %s'
        BaseDatos.realizar_consulta(query,('Pagado',cliente),'UPDATE')

    ####################################################################################################################################################
    #Método para consultar fecha de una determinada venta
    @staticmethod
    def consultar_venta_nroventa(nro_venta):
        query = ''' SELECT
                        TO_CHAR(fecha_venta,'DD-MM-YYYY'),
                        cliente,
                        monto_total
                    FROM Ventas
                    WHERE nro_venta = %s
                '''
        return BaseDatos.realizar_consulta(query,(nro_venta,),'SELECT')
    
    ####################################################################################################################################################
    #Método para consultar ventas con pagos pendientes
    @staticmethod
    def pagos_pendientes():

        query = ''' SELECT
                        v.nro_venta,
                        TO_CHAR(v.fecha_venta,'DD-MM-YYYY'),
                        v.cliente,
                        v.monto_total,
                        mp.modo_pago,
                        v.estado_venta
                    FROM Ventas v
                    INNER JOIN ModoPago mp ON v.id_modo_pago = mp.id_modo_pago
                    WHERE v.estado_venta = 'Pendiente'
                    ORDER BY v.nro_venta
                '''
        return BaseDatos.realizar_consulta(query,None,'SELECT')
    
