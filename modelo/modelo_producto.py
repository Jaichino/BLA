from modelo.database import BaseDatos

################################################################################################################################################
####################################################### MODELO DE PRODUCTO #####################################################################

#En este fichero se realizará la lógica de negocio del modulo de productos, que luego mediante el controlador, se vinculará con la vista.

class ModeloProducto:

    ####################################################################################################################################################
    #Método para visualizar los productos existentes en la base de datos.
    #Se parte de una query inicial donde se muestra la totalidad de los productos, luego en función de si se agregan o no los parámetros de filtrado
    #(codigo_producto o descripcion) se va ampliando esa query y se agregan los parametros dentro de la lista params, la cuál se pasará como parámetro
    #cuando se hace BaseDatos.realizar_consulta().
    @staticmethod
    def mostrar_productos(codigo_producto = None, descripcion = None):

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
        #Si se quiere filtrar por codigo:
        if codigo_producto is not None:
            query += ' AND codigo_producto = %s'
            params.append(codigo_producto)

        #Si se quiere filtrar por descripcion:
        if descripcion is not None:
            query += ' AND descripcion ILIKE %s'
        
            params.append(f'%{descripcion}%')
        
        #Se finaliza con un ORDER BY para mostrar los productos en orden alfabético:
        query += ' ORDER BY descripcion'
        
        return BaseDatos.realizar_consulta(query,params,'SELECT')
    
    ####################################################################################################################################################
    #Método para obtener información de un producto según un código y vencimiento ingresado
    @staticmethod
    def informacion_producto(codigo_producto,vencimiento):
        query = 'SELECT * FROM Productos WHERE codigo_producto = %s AND vencimiento = %s'
        return BaseDatos.realizar_consulta(query,(codigo_producto,vencimiento),'SELECT')

    ####################################################################################################################################################
    #Método para insertar nuevos productos en la base de datos
    @staticmethod
    def nuevo_producto(codigo_producto,descripcion,precio_unitario,stock,vencimiento):
        query = '''INSERT INTO Productos (codigo_producto,descripcion,precio_unitario,stock,vencimiento) 
                    VALUES (%s,%s,%s,%s,%s)'''
        
        BaseDatos.realizar_consulta(query,(codigo_producto,descripcion,precio_unitario,stock,vencimiento),'INSERT')

    ####################################################################################################################################################
    #Método para actualizar los registros en la base de datos
    @staticmethod
    def actualizar_producto(nro_producto,descripcion,precio_unitario,stock):
        query = ''' UPDATE Productos
                    SET descripcion = %s, precio_unitario = %s, stock = %s
                    WHERE nro_producto = %s'''
        
        BaseDatos.realizar_consulta(query,(descripcion,precio_unitario,stock,nro_producto),'UPDATE')

    ####################################################################################################################################################
    #Método para "eliminar" productos de la base de datos. En este caso, no se eliminará el producto directamente con un DELETE, sino que se cambiará
    #el estado (activo) de True a False, para que luego no se generen problemas con la falta de referencia si se eliminan productos que existen 
    #relacionados en otra tabla de la base de datos.
    @staticmethod
    def eliminar_producto(nro_producto):
        query = 'UPDATE Productos SET activo = False WHERE nro_producto = %s'
        BaseDatos.realizar_consulta(query,(nro_producto,),'UPDATE')

    ####################################################################################################################################################
    #Método para ingresar nuevo stock a un producto existente
    @staticmethod
    def ingreso_stock(nro_producto,stock_ingresado):
        query = 'UPDATE Productos SET stock = stock + %s WHERE nro_producto = %s'
        BaseDatos.realizar_consulta(query,(stock_ingresado,nro_producto),'UPDATE')

    ####################################################################################################################################################
    #Método para descontar productos una vez que se ha realizado una venta
    @staticmethod
    def descontar_producto(nro_producto,cantidad_vendida):
        query = 'UPDATE Productos SET stock = stock - %s WHERE nro_producto = %s'
        BaseDatos.realizar_consulta(query,(cantidad_vendida,nro_producto),'UPDATE')

    ####################################################################################################################################################
    #Método para consulta de vencimiento de productos, los cuales se filtrarán entre dos fechas elegidas por el usuario o, estando también la 
    #posibilidad de filtrar según el código de producto.
    # Si no se ingresa ningún código (None), entonces se filtrará por las fechas, pero si se ingresa un valor de codigo, se filtrará el producto del
    # código ingresado. Los parámetros se irán agregando en una lista vacía "params" que luego se usará para ejecutar la consulta.
    @staticmethod
    def consulta_vencimientos(desde=None,hasta=None,codigo=None):

        params = []

        if codigo is None:

            query = '''SELECT
                            codigo_producto,
                            descripcion,
                            stock,
                            TO_CHAR(vencimiento,'DD-MM-YYYY'),
                            (vencimiento - CURRENT_DATE) AS dias_vencimiento
                        FROM Productos WHERE activo = True AND (vencimiento BETWEEN %s AND %s)
                    '''
            params.append(desde)
            params.append(hasta)

        else: 
            query = '''SELECT
                            codigo_producto,
                            descripcion,
                            stock,
                            TO_CHAR(vencimiento,'DD-MM-YYYY'),
                            (vencimiento - CURRENT_DATE) AS dias_vencimiento
                        FROM Productos WHERE activo = True AND codigo_producto = %s
                    '''
            
            params.append(codigo,)

        return BaseDatos.realizar_consulta(query,params,'SELECT')

    ####################################################################################################################################################
    #Método para mostrar en treeview vencimientos de productos
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
        return BaseDatos.realizar_consulta(query,None,'SELECT')

    ####################################################################################################################################################
    #Método para mostrar productos sin stock (y que tengan un activo = True)
    @staticmethod
    def productos_sinstock():
        query = 'SELECT * FROM Productos WHERE activo = True AND stock = 0'
        return BaseDatos.realizar_consulta(query,None,'SELECT')
    
    ####################################################################################################################################################
    #Método para mostrar la descripción del producto de acuerdo al código ingresado
    @staticmethod
    def descripcion_producto(codigo_producto):
        query = 'SELECT DISTINCT descripcion FROM Productos WHERE codigo_producto = %s'
        return BaseDatos.realizar_consulta(query,(codigo_producto,),'SELECT')
    
    ####################################################################################################################################################
    #Método para obtener el nro_producto dependiendo del código y vencimiento ingresados en una venta 
    @staticmethod
    def obtener_nroproducto(codigo_producto,vencimiento):
        query = 'SELECT nro_producto FROM Productos WHERE codigo_producto = %s AND vencimiento = %s'
        return BaseDatos.realizar_consulta(query,(codigo_producto,vencimiento),'SELECT')
    
    ####################################################################################################################################################
    #Método para obtener los vencimientos correspondientes al código de producto introducido en la venta. Se usa para colocar en ComboBox
    @staticmethod
    def vencimiento_producto_a_vender(codigo_producto):
        query = '''
                SELECT
                vencimiento
                FROM Productos WHERE codigo_producto = %s AND activo = True ORDER BY vencimiento
                '''
        return BaseDatos.realizar_consulta(query,(codigo_producto,),'SELECT')

    ####################################################################################################################################################
    #Método para obtener todos los productos vencidos
    @staticmethod
    def productos_vencidos():
        query = ''' SELECT
                        codigo_producto,
                        descripcion,
                        stock,
                        TO_CHAR(vencimiento,'DD-MM-YYYY'),
                        (vencimiento - CURRENT_DATE) AS dias_vencimiento
                        FROM Productos WHERE activo = True AND (vencimiento - CURRENT_DATE) <= 0
                '''
        return BaseDatos.realizar_consulta(query,None,'SELECT')
    
    ####################################################################################################################################################
    #Función para devolver al stock los productos de una venta que se eliminó, según el nro_producto
    @staticmethod
    def devolver_producto_a_stock(nro_producto,cantidad_devuelta):
        query = 'UPDATE Productos SET stock = stock + %s WHERE nro_producto = %s'
        BaseDatos.realizar_consulta(query,(cantidad_devuelta,nro_producto),'UPDATE')
