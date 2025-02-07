from modelo.database import BaseDatos


########################## MODELO DE PRODUCTO ###############################
'''
En este fichero se realizará la lógica de negocio del modulo de productos, 
que luego mediante el controlador, se vinculará con la vista.
'''
class ModeloProducto:

    #Método para visualizar los productos existentes en la base de datos.
    @staticmethod
    def mostrar_productos(codigo_producto=None, descripcion=None):
        
        ''' En este metodo, primeramente se parte de una query inicial en la 
            cual se muestran los productos sin ser aplicado ningun filtro, y
            en funcion de si se pasa como parametro un codigo o una
            descripcion, la query cambia y sus parametros (params) tambien
        '''

        query = ''' SELECT
                        nro_producto,
                        codigo_producto,
                        descripcion,
                        precio_unitario,
                        stock,
                        TO_CHAR(vencimiento,'DD-MM-YYYY'),
                        activo
                    FROM Productos
                    WHERE activo = True '''
        
        params = []

        # Si se quiere filtrar por codigo:
        if codigo_producto is not None:
            query += ' AND codigo_producto = %s'
            params.append(codigo_producto)

        # Si se quiere filtrar por descripcion:
        if descripcion is not None:
            query += ' AND descripcion ILIKE %s'
            params.append(f'%{descripcion}%')
        
        # Se ordenan alfabeticamente los productos segun descripcion
        query += ' ORDER BY descripcion'
        
        return BaseDatos.realizar_consulta(query, params, 'SELECT')
    

    # Metodo para obtener info de un producto segun un codigo y vencimiento
    @staticmethod
    def informacion_producto(codigo_producto, vencimiento):
        
        query = ''' SELECT * FROM Productos 
                    WHERE codigo_producto = %s AND vencimiento = %s
                '''
        
        return BaseDatos.realizar_consulta(
            query,
            (codigo_producto, vencimiento),
            'SELECT'
        )


    # Metodo para insertar nuevos productos en la base de datos
    @staticmethod
    def nuevo_producto  (codigo_producto,
                        descripcion,
                        precio_unitario,
                        stock,
                        vencimiento
                        ):
        
        query = ''' INSERT INTO Productos 
                    (codigo_producto,descripcion,precio_unitario,stock,vencimiento) 
                    VALUES (%s,%s,%s,%s,%s)
                '''
        
        BaseDatos.realizar_consulta(
            query,
            (codigo_producto,descripcion,precio_unitario,stock,vencimiento),
            'INSERT'
        )


    # Metodo para actualizar los registros en la base de datos
    @staticmethod
    def actualizar_producto(
        nro_producto, 
        descripcion, 
        precio_unitario, 
        stock
    ):
        query = ''' UPDATE Productos
                    SET descripcion = %s, precio_unitario = %s, stock = %s
                    WHERE nro_producto = %s
                '''
        
        BaseDatos.realizar_consulta(
            query,
            (descripcion, precio_unitario, stock, nro_producto),
            None
        )


    # Metodo para "eliminar" productos de la base de datos
    @staticmethod
    def eliminar_producto(nro_producto):
        
        query = 'UPDATE Productos SET activo = False WHERE nro_producto = %s'
        
        BaseDatos.realizar_consulta(query, (nro_producto,), None)


    # Metodo para ingresar nuevo stock a un producto existente
    @staticmethod
    def ingreso_stock(nro_producto, stock_ingresado):
        
        query = ''' UPDATE Productos 
                    SET stock = stock + %s WHERE nro_producto = %s
                '''
        
        BaseDatos.realizar_consulta(
            query,
            (stock_ingresado,nro_producto),
            None
        )


    # Metodo para descontar productos una vez que se ha realizado una venta
    @staticmethod
    def descontar_producto(nro_producto, cantidad_vendida):
        
        query = ''' UPDATE Productos 
                    SET stock = stock - %s WHERE nro_producto = %s
                '''
        
        BaseDatos.realizar_consulta(
            query,
            (cantidad_vendida,nro_producto),
            None
        )


    # Metodo para consulta de vencimiento de productos entre fechas o codigo
    @staticmethod
    def consulta_vencimientos(desde=None, hasta=None, codigo=None):

        params = []

        if codigo is None:
            query = ''' SELECT
                            codigo_producto,
                            descripcion,
                            stock,
                            TO_CHAR(vencimiento,'DD-MM-YYYY'),
                            (vencimiento - CURRENT_DATE) AS dias_vencimiento
                        FROM Productos 
                        WHERE activo = True AND (vencimiento BETWEEN %s AND %s)
                    '''
            
            params.append(desde)
            params.append(hasta)

        else: 
            query = ''' SELECT
                            codigo_producto,
                            descripcion,
                            stock,
                            TO_CHAR(vencimiento,'DD-MM-YYYY'),
                            (vencimiento - CURRENT_DATE) AS dias_vencimiento
                        FROM Productos 
                        WHERE activo = True AND codigo_producto = %s
                    '''
            
            params.append(codigo,)

        return BaseDatos.realizar_consulta(query, params, 'SELECT')


    # Metodo para obtener vencimientos de productos
    @staticmethod
    def mostrar_vencimientos_todosproductos():
        
        query = '''SELECT
                        codigo_producto,
                        descripcion,
                        stock,
                        TO_CHAR(vencimiento,'DD-MM-YYYY'),
                        (vencimiento - CURRENT_DATE) AS dias_vencimiento
                    FROM Productos WHERE activo = True
                    ORDER BY dias_vencimiento
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')


    # Metodo para mostrar productos sin stock (y que tengan un activo = True)
    @staticmethod
    def productos_sinstock():
        
        query = 'SELECT * FROM Productos WHERE activo = True AND stock = 0'
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')
    

    # Metodo para mostrar descripcion del producto de acuerdo al codigo
    @staticmethod
    def descripcion_producto(codigo_producto):
        
        query = ''' SELECT DISTINCT descripcion 
                    FROM Productos WHERE codigo_producto = %s
                '''
        
        return BaseDatos.realizar_consulta(
            query,
            (codigo_producto,),
            'SELECT'
        )
    

    # Metodo para obtener nro_producto segun codigo y vencimiento
    @staticmethod
    def obtener_nroproducto(codigo_producto,vencimiento):
        
        query = ''' SELECT nro_producto 
                    FROM Productos 
                    WHERE codigo_producto = %s AND vencimiento = %s
                '''
        
        return BaseDatos.realizar_consulta(
            query,
            (codigo_producto,vencimiento),
            'SELECT'
        )
    

    # Metodo para obtener los vencimientos correspondientes a un codigo
    @staticmethod
    def vencimiento_producto_a_vender(codigo_producto):
        
        query = ''' SELECT
                        vencimiento
                    FROM Productos 
                    WHERE codigo_producto = %s AND activo = True
                    ORDER BY vencimiento
                '''
        
        return BaseDatos.realizar_consulta(
            query,
            (codigo_producto,),
            'SELECT'
        )


    # Metodo para obtener todos los productos vencidos
    @staticmethod
    def productos_vencidos():
        
        query = ''' SELECT
                        codigo_producto,
                        descripcion,
                        stock,
                        TO_CHAR(vencimiento,'DD-MM-YYYY'),
                        (vencimiento - CURRENT_DATE) AS dias_vencimiento
                    FROM Productos 
                    WHERE activo = True AND (vencimiento - CURRENT_DATE) <= 0
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')
    

    # Metodo para devolver al stock los productos de una venta que se elimino
    @staticmethod
    def devolver_producto_a_stock(nro_producto, cantidad_devuelta):
        
        query = ''' UPDATE Productos 
                        SET stock = stock + %s 
                    WHERE nro_producto = %s
                '''
        
        BaseDatos.realizar_consulta(
            query,
            (cantidad_devuelta, nro_producto),
            None
        )
