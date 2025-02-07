from modelo.database import BaseDatos


############################ MODELO DE REPORTES #############################
''' En este fichero se realizará la lógica del módulo de Reportes, que luego 
    mediante el controlador, se vinculará con la vista.
'''
class ModeloReportes:

    # Metodo que obtiene los distintos años de la columna fecha_venta
    @staticmethod
    def distintos_year():
        
        query = ''' SELECT
                        DISTINCT EXTRACT(YEAR FROM fecha_venta) AS years
                    FROM Ventas
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')


    # Metodo que obtiene los distintos meses de la columna fecha_venta
    @staticmethod
    def distintos_month():
        
        query = ''' SELECT
                        DISTINCT EXTRACT(MONTH FROM fecha_venta) AS months
                    FROM Ventas
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')

    
    # Metodo para encontrar las ganancias totales, filtrando por año y mes
    @staticmethod
    def ganancias_totales(año, mes):
        
        query = ''' SELECT
                        EXTRACT(YEAR FROM fecha_venta) AS year_sale,
                        EXTRACT(MONTH FROM fecha_venta) AS month_sale,
                        SUM(monto_total) AS revenue
                    FROM Ventas
                    WHERE estado_venta = %s AND 
                        EXTRACT(YEAR FROM fecha_venta) = %s AND 
                        EXTRACT(MONTH FROM fecha_venta) = %s
                    GROUP BY year_sale,month_sale
                '''
        
        return BaseDatos.realizar_consulta(
            query,
            ('Pagado', año, mes),
            'SELECT'
        )

    
    # Metodo para calcular el monto total adeudado en cuentas corrientes
    @staticmethod
    def deuda_cuentascorrientes():
        
        query = '''	WITH ultimos_montos_pendientes AS (
                        SELECT 
                            c1.cliente, 
                            c1.nro_operacion, 
                            c1.monto_pendiente
                        FROM 
                            CuentaCorriente c1
                        INNER JOIN (
                            SELECT 
                                cliente, 
                                MAX(nro_operacion) AS max_operacion
                            FROM 
                                CuentaCorriente
                            GROUP BY 
                                cliente
                        ) c2
                        ON c1.cliente = c2.cliente AND 
                        c1.nro_operacion = c2.max_operacion
                    )

                    SELECT
                        SUM(monto_pendiente)
                    FROM ultimos_montos_pendientes
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')

    
    # Metodo para calcular el monto total en inventarios
    @staticmethod
    def monto_en_inventarios():
        query = ''' SELECT
                        SUM(precio_unitario * stock)
                    FROM Productos
                    WHERE activo = True
                '''
        return BaseDatos.realizar_consulta(query, None, 'SELECT')

    
    # Metodo para visualizar los 5 productos mas vendidos
    @staticmethod
    def cinco_mas_vendidos():
        
        query = ''' SELECT
                        p.codigo_producto AS codigo,
                        p.descripcion AS descripcion,
                        SUM(dv.cantidad) AS cantidad
                    FROM DetalleVentas dv
                    INNER JOIN Productos p ON
                        dv.nro_producto = p.nro_producto
                    GROUP BY codigo,descripcion
                    ORDER BY cantidad DESC
                    LIMIT 5
                '''
        
        return BaseDatos.realizar_consulta(query, None, 'SELECT')

    
    # Metodo para encontrar las ganancias totales, filtrando por año y mes
    @staticmethod
    def ganancias_totales_grafico(año):
        
        query = ''' SELECT
                        EXTRACT(YEAR FROM fecha_venta) AS year_sale,
                        EXTRACT(MONTH FROM fecha_venta) AS month_sale,
                        SUM(monto_total) AS revenue
                    FROM Ventas
                    WHERE EXTRACT(YEAR FROM fecha_venta) = %s
                    GROUP BY year_sale,month_sale
                '''
        
        return BaseDatos.realizar_consulta(query, (año,), 'SELECT')
