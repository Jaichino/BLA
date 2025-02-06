import psycopg2

################################################################################################################################################
################################################### DATABASE CONNECTION ########################################################################

# En este fichero se lleva a cabo la conexión con la base de datos, se crea función para establecer conexión, función para cerrar la conexión y luego
# la función encargada de realizar el CRUD a la base de datos

class BaseDatos:

    # Se definen los atributos estáticos para realizar la conexión a la base de datos
    database = 'BLA'
    user = 'postgres'
    password = 'JuaniSQL'
    host = 'localhost'
    port = '5432'

    # Función que se encarga de realizar la conexión a la base de datos mediante psycopg2.connect()
    @staticmethod
    def connect():
        try:
            conn = psycopg2.connect(
                database = BaseDatos.database,
                user = BaseDatos.user,
                password = BaseDatos.password,
                host = BaseDatos.host,
                port = BaseDatos.port
            )
            return conn
        
        except Exception as error:
            print(f'Error al conectar con la base de datos - {error}')
            raise

    # Función para cerrar conexión
    @staticmethod
    def close(conn):
        if conn:
            conn.close()
            
    # Función para realizar consultas SQL del modelo. En caso de que la consulta sea del tipo "SELECT" también se devolverán los valores arrojados por dicha
    # consulta mediante cursor.fetchall()
    @staticmethod
    def realizar_consulta(query,valores=None,tipo=None):
        conn = BaseDatos.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query,valores)
                conn.commit()

                if tipo ==  'SELECT':
                    resultado = cursor.fetchall()
                    return resultado
            
            except Exception as error:
                print(f'Error - {error}')
                conn.rollback()
                raise
            
            finally:
                cursor.close()
                BaseDatos.close(conn)


