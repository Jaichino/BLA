from tkinter import messagebox, Toplevel
from vista.view_inventario import InterfazInventario
from vista.view_inventario import Vencimientos
from vista.view_inventario import NuevoProducto
from vista.view_inventario import IngresoStock
from vista.view_inventario import ModificarProducto
from modelo.modelo_producto import ModeloProducto

####################### CONTROLADOR DE PRODUCTOS ############################

''' En este fichero se lleva a cabo la vinculación entre la vista y el modelo 
    del modulo Productos
'''
class ControladorProducto:

    def __init__(self,root):
        self.root = root
        self.vista_inventario = InterfazInventario(self.root)
        self.modelo_inventario = ModeloProducto()

        # Foco en campo de codigo
        self.vista_inventario.entry_codigo.focus()

        #Configuracion botones inicio de ventanas
        self.vista_inventario.boton_vencimientos.config(
            command = self.abrir_ventana_consulta_vencimientos
        )
        self.vista_inventario.boton_nuevo.config(
            command = self.boton_nuevo
        )
        self.vista_inventario.boton_ingresar.config(
            command = self.boton_ingresar_stock
        )
        self.vista_inventario.boton_modificar.config(
            command = self.boton_modificar
        )
        
        #Configuracion botones de ventana
        self.vista_inventario.boton_filtar.config(
            command = self.boton_filtrar_productos
        )
        self.vista_inventario.boton_cerostock.config(
            command = self.boton_sin_stock
        )
        self.vista_inventario.boton_eliminar.config(
            command = self.boton_eliminar_producto
        )
        
        # Llenado de Treeview en inicio de ventana
        self.llenar_treeview_productos()

        # Guardado de elemento seleccionado treeview
        self.elemento_seleccionado = None
    
    ##################### INICIALIZACION DE VENTANAS ########################
    
    ''' Metodos para inicializar las ventanas del modulo de productos.
        Se crea un TopLevel de root y se llama a las ventanas.
        Dentro de estos metodos se configuran las funcionalidades
        correspondientes a cada ventana (botones, eventos, atributos)
    '''
    
    def abrir_ventana_consulta_vencimientos(self):
        # Creacion de ventana
        self.toplevel_vencimientos = Toplevel(self.root)
        self.ventana_vencimientos = Vencimientos(self.toplevel_vencimientos)
        self.toplevel_vencimientos.grab_set()

        # Foco en campo de codigo
        self.ventana_vencimientos.entry_codigo.focus()
        
        # Llenado de Treeview
        self.llenar_treeview_vencimientos()

        # Configuracion de botones
        self.ventana_vencimientos.boton_buscar.config(
            command = self.boton_filtrar_vencimientos
        )
        self.ventana_vencimientos.boton_vencido.config(
            command = self.boton_todos_vencimientos
        )

    
    def abrir_ventana_nuevoproducto(self):
        # Creacion de ventana
        self.toplevel_nuevo_producto = Toplevel(self.root)
        self.ventana_nuevo_producto = NuevoProducto(
            self.toplevel_nuevo_producto
        )
        self.toplevel_nuevo_producto.grab_set()

        # Foco en campo de codigo
        self.ventana_nuevo_producto.entry_codigo.focus()

        # Configuracion de botones
        self.ventana_nuevo_producto.boton_guardar.config(
            command = self.boton_guardar_nuevoproducto
        )

        # Asignacion de eventos
        self.ventana_nuevo_producto.entry_codigo.bind(
            "<KeyRelease>",
            self.actualizar_entrydescripcion
        )
    
    def abrir_ventana_modificar_producto(self):
        # Creacion de ventana
        self.toplevel_modificar_producto = Toplevel(self.root)
        self.ventana_modificar_producto = ModificarProducto(
            self.toplevel_modificar_producto
        )
        self.toplevel_modificar_producto.grab_set()
        
        # Configuracion de botones
        self.ventana_modificar_producto.boton_guardar.config(
            command = self.guardar_modificacion_producto
        )

    
    def abrir_ventana_ingresostock(self):
        # Creacion de ventana
        self.toplevel_ingreso_stock = Toplevel(self.root)
        self.ventana_ingreso_stock = IngresoStock(
            self.toplevel_ingreso_stock
        )
        self.toplevel_ingreso_stock.grab_set()

        # Foco en campo ingreso stock
        self.ventana_ingreso_stock.entry_ingresostock.focus()

        # Configuracion de botones
        self.ventana_ingreso_stock.boton_ingresostock.config(
            command = self.boton_guardar_ingresostock
        )
    
    ######################## INICIALIZACION TREEVIEW ########################
    def llenar_treeview_productos(self):
        
        ''' Este metodo se encarga de llenar el Treeview de productos, donde
            se recuperan los productos de la base de datos con el metodo
            mostrar_productos().
            Tambien se crean tags para pintar de rojo aquellas filas donde
            el stock sea igual a 0
        '''
        productos = self.modelo_inventario.mostrar_productos()
        for producto in productos:
            self.vista_inventario.tv_inventario.insert(
                '',
                'end',
                text=producto[1],
                values=(producto[2],producto[3],producto[4],producto[5]))

        # Creacion de tag
        self.vista_inventario.tv_inventario.tag_configure(
            'Rojo',
            foreground='red',font=('century gothic',10,'bold')
        )
        # Se recorren filas de treeview con bucle for
        for item in self.vista_inventario.tv_inventario.get_children():
            valores = self.vista_inventario.tv_inventario.item(
                item,
                'values'
            )
            
            stock = int(valores[2])
            # Si stock = 0, se aplica tag creado
            if stock == 0:
                self.vista_inventario.tv_inventario.item(
                    item,
                    tags=('Rojo',)
                )
            
    
    def llenar_treeview_vencimientos(self):

        ''' Metodo para llenar el treeview de la ventana vencimientos.
            Se crea un tag para pintar de rojo aquellas filas del treeview
            donde el producto se encuentre vencido
        '''
        # Llenado de treeview
        consulta_vencimientos = (
            self.modelo_inventario.mostrar_vencimientos_todosproductos()
        )
        for producto in consulta_vencimientos:
            self.ventana_vencimientos.tv_vencimientos.insert(
                '',
                'end',
                text=producto[0],
                values=(producto[1],producto[2],producto[3],producto[4])
            )
        
        # Creacion de tag
        self.ventana_vencimientos.tv_vencimientos.tag_configure(
            'Rojo',
            foreground='red',
            font=('century gothic',10,'bold')
        )

        # Recorrido de filas y aplicacion de tag
        for item in self.ventana_vencimientos.tv_vencimientos.get_children():
            valores = self.ventana_vencimientos.tv_vencimientos.item(
                item,
                'values'
            )
            if int(valores[3]) <= 0:
                self.ventana_vencimientos.tv_vencimientos.item(
                    item,
                    tags=('Rojo',)
                )
    
    
    ################################# EVENTOS ###############################
    def actualizar_entrydescripcion(self, event):
        
        ''' Metodo que se vincula a un evento en el cual si se ingresa un
            codigo ya existente a la hora de crear un nuevo producto, se
            introduce automaticamente la descripcion del mismo en el entry
            producto
        '''
        
        codigo_producto = self.ventana_nuevo_producto.entry_codigo.get()
        
        # Obtencion de la descripcion del producto
        descripcion = ModeloProducto.descripcion_producto(codigo_producto)
        
        # Insercion de descripcion en Entry y foco en siguiente Entry
        if descripcion:
            self.ventana_nuevo_producto.entry_descripcion.delete(0,'end')
            self.ventana_nuevo_producto.entry_descripcion.insert(
                0,
                descripcion[0][0]
            )
            self.ventana_nuevo_producto.entry_precio.focus()
        
        # Si no se encuentran coincidencias, el entry queda vacio
        else:
            self.ventana_nuevo_producto.entry_descripcion.insert(0,'')


    ########################### ACCIONES DE BOTONES ######################### 
    def boton_nuevo(self):
        
        ''' Metodo para apertura de ventana de creacion de nuevo producto'''

        self.abrir_ventana_nuevoproducto()
    

    def boton_modificar(self):

        ''' Metodo para la apertura de la ventana de modificacion de producto
            Se verifica primeramente que se seleccione unicamente un elemento
            Si se selecciono un elemento, se inicia la ventana con los entry
            autocompletados con la informacion del producto seleccionado.
        '''
        
        # Verificacion seleccion de elemento
        self.elemento_seleccionado = (
            self.vista_inventario.tv_inventario.selection()
        )
        
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return

        # Apertura de ventana y llenado de campos
        if self.elemento_seleccionado:
            self.abrir_ventana_modificar_producto()
            
            valores = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'values'
            )
            
            self.ventana_modificar_producto.entry_descripcion.insert(
                0,
                valores[0]
            )
            self.ventana_modificar_producto.entry_precio.insert(
                0,
                valores[1]
            )
            self.ventana_modificar_producto.entry_stock.insert(
                0,
                valores[2]
            )
            
        else:
            messagebox.showerror('Error','Debes seleccionar un producto')

    
    def guardar_modificacion_producto(self):

        ''' Metodo para guardar la modificacion de un producto. Primero se
            recuperan los valores de los Entry, se obtiene el nro_producto
            y vencimiento correspondiente a dicho producto. Finalmente,
            se llama al metodo de modificacion de productos.
        '''
        
        try:
            # Recuperar valores de los entry
            descripcion = (
                self.ventana_modificar_producto.entry_descripcion.get()
            )
            precio = (
                float(self.ventana_modificar_producto.entry_precio.get())
            )
            stock = (
                int(self.ventana_modificar_producto.entry_stock.get())
            )

            # Obtencion nro_producto y vencimiento
            codigo_producto = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'text'
            )
            valores = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'values'
            )
            vencimiento = valores[3]
            nro_producto = self.modelo_inventario.obtener_nroproducto(
                codigo_producto,
                vencimiento
            )

            # Actualizacion de producto
            self.modelo_inventario.actualizar_producto(
                nro_producto[0],
                descripcion,
                precio,
                stock
            )
            
            # Cerrado de ventana y actualizacion de treeview
            self.toplevel_modificar_producto.destroy()
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()

            # Mensaje de confirmacion
            messagebox.showinfo(
                'Producto Modificado',
                f'Producto {descripcion} modificado!'
            )
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    
    def boton_guardar_nuevoproducto(self):

        ''' Metodo para guardar un nuevo producto. Primero se recuperan los
            valores de los Entry, se verifica que ese producto ya no exista
            en la base de datos y finalmente se carga dicho producto a stock
        '''

        # Obtencion de entradas de usuario
        codigo_producto = self.ventana_nuevo_producto.entry_codigo.get()
        descripcion = self.ventana_nuevo_producto.entry_descripcion.get()
        vencimiento = self.ventana_nuevo_producto.entry_vencimiento.get()
        try:
            precio_unitario = (
                float(self.ventana_nuevo_producto.entry_precio.get())
            )
            stock = int(self.ventana_nuevo_producto.entry_stock.get())

            # Comprobacion que producto no existe en base de datos
            nro_producto = ModeloProducto.obtener_nroproducto(
                codigo_producto,
                vencimiento
            )
            if nro_producto:
                messagebox.showerror(
                    'Producto Existente',
                    f'El producto {descripcion} ya existe en el inventario!'
                )
                
            else:
                # Carga de producto
                ModeloProducto.nuevo_producto(
                    codigo_producto,
                    descripcion,
                    precio_unitario,
                    stock,
                    vencimiento
                )
                
                messagebox.showinfo(
                    'Producto Ingresado',
                    f'Producto: {descripcion} creado correctamente!'
                )
                
                self.vista_inventario.limpiar_treeview()
                self.ventana_nuevo_producto.limpiar_cajas()
                self.llenar_treeview_productos()
                self.toplevel_nuevo_producto.destroy()
        
        except ValueError:
            messagebox.showerror('Error','Error en ingreso de datos')
        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Se ha producido un error inesperado - {error}'
            )


    def boton_eliminar_producto(self):

        ''' Metodo para realizar la eliminacion de un producto. Primero se
            verifica que se haya seleccionado solamente un elemento, luego
            se obtiene nro_producto para proceder a la eliminacion.
        '''

        # Verificacion seleccion de elemento
        self.elemento_seleccionado = (
            self.vista_inventario.tv_inventario.selection()
        )
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return
            
        # Obtencion de informacion de producto
        if self.elemento_seleccionado:
            producto = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'values'
            )
            descripcion = producto[0]
            
            # Consulta de eliminacion
            confirmacion = messagebox.askyesno(
                'Eliminar Producto',
                f'Desea eliminar el producto {descripcion}?'
            )
            
            if confirmacion:
                # Obtencion del nro_producto
                codigo_producto = self.vista_inventario.tv_inventario.item(
                    self.elemento_seleccionado,
                    'text'
                )
                valores = self.vista_inventario.tv_inventario.item(
                    self.elemento_seleccionado,
                    'values')
                vencimiento = valores[3]
                
                nro_producto = self.modelo_inventario.obtener_nroproducto(
                    codigo_producto,
                    vencimiento
                )

                # Eliminacion del producto
                self.modelo_inventario.eliminar_producto(nro_producto[0])
                self.vista_inventario.limpiar_treeview()
                self.llenar_treeview_productos()
                messagebox.showinfo(
                    'Producto Eliminado',
                    f'Producto {valores[0]} eliminado!'
                )

        else:
            messagebox.showerror(
                'Eliminar Producto',
                'Debes seleccionar un producto'
            )

    
    def boton_ingresar_stock(self):
        
        ''' Metodo para apertura de ventana de ingreso de stock.
            Se verifica que se elija solo un elemento para poder abrir la
            ventana
        '''
        
        # Verificacion seleccion de elemento
        self.elemento_seleccionado = (
            self.vista_inventario.tv_inventario.selection()
        )
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar solo un elemento')
            return
        
        # Apertura de ventana
        if self.elemento_seleccionado:
            self.abrir_ventana_ingresostock()
        else:
            messagebox.showerror('Error','Debes seleccionar un producto')
    
    
    def boton_guardar_ingresostock(self):
        
        ''' Metodo para ingresar stock de un determinado producto que ya
            exista en la base de datos. Primero se recupera el valor de
            stock ingresado y se obtiene el nro_producto y vencimiento.
            Finalmente, se realiza la carga del stock de dicho producto
        '''
        try:
            #Se recupera valor de stock ingresado por usuario
            stock_ingresado = (
                int(self.ventana_ingreso_stock.entry_ingresostock.get())
            )

            # Obtencion nro_producto y vencimiento
            codigo_producto = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'text'
            )
            valores = self.vista_inventario.tv_inventario.item(
                self.elemento_seleccionado,
                'values'
            )
            vencimiento = valores[3]
            nro_producto = self.modelo_inventario.obtener_nroproducto(
                codigo_producto,
                vencimiento
            )
            
            # Ingreso de stock
            self.modelo_inventario.ingreso_stock(
                nro_producto[0],
                stock_ingresado
            )
            self.toplevel_ingreso_stock.destroy()
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()
            messagebox.showinfo(
                'Stock Ingresado',
                f'Stock de {valores[0]} ingresado!'
            )
    
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de valores')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')


    def boton_filtrar_productos(self):

        ''' Metodo para realizar el filtrado de productos en Treeview.
            Se obtienen entradas de los campos de codigo y descripcion, y
            luego se llama al metodo de filtrado de productos.
            Tambien se crea tag para resaltar aquellas filas donde el
            stock sea 0.
        '''
        # Borrar elementos del treeview
        self.vista_inventario.limpiar_treeview()

        # Obtencion de entradas de usuario
        codigo = self.vista_inventario.entry_codigo.get()
        descripcion = self.vista_inventario.entry_descripcion.get()
        self.vista_inventario.limpiar_cajas()
        codigo = None if codigo == '' else codigo
        descripcion = None if descripcion == '' else descripcion

        try:
            # Si ambos entry son vacios, solo se llena el treeview
            if codigo == '' and descripcion == '':
                self.llenar_treeview_productos()
            
            else:
                # Se llama a metodo para mostrar productos segun filtro
                productos_filtrados = (
                    self.modelo_inventario.mostrar_productos(
                        codigo,
                        descripcion
                    )
                )
                
                if productos_filtrados:
                    #Se llena el treeview con los elementos filtrados
                    for producto in productos_filtrados:
                        self.vista_inventario.tv_inventario.insert(
                            '',
                            'end',
                            text=producto[1],
                            values=(
                                producto[2],
                                producto[3],
                                producto[4],
                                producto[5]
                            )
                        )

                    # Creacion y aplicacion de tag
                    self.vista_inventario.tv_inventario.tag_configure(
                        'Rojo',
                        foreground='red',
                        font=('century gothic',10,'bold')
                    )
                    for item in (
                        self.vista_inventario.tv_inventario.get_children()
                    ):
                        valores = self.vista_inventario.tv_inventario.item(
                            item,
                            'values'
                        )
                        stock = int(valores[2])
                        if stock == 0:
                            self.vista_inventario.tv_inventario.item(
                                item,
                                tags=('Rojo',)
                            )
                else:
                    messagebox.showinfo(
                        'Productos',
                        'No se ha encontrado ningún producto'
                    )
                    self.llenar_treeview_productos()

        except Exception as error:
            messagebox.showerror('Error',f'Error Inesperado - {error}')


    def boton_sin_stock(self):

        ''' Metodo para filtrado de productos que se encuentran sin stock.
            Primero se limpia treeview y se obtienen aquellos productos
            que tengan stock 0. Si no hay productos sin stock se llena el
            treeview con todos los productos, caso contrario se filtra el
            treeview con aquellos productos donde el stock es 0
        '''
        
        # Limpiar treeview
        self.vista_inventario.limpiar_treeview()

        # Obtencion de productos sin stock
        productos_sin_stock = self.modelo_inventario.productos_sinstock()

        # Comprobacion productos sin stock
        if not productos_sin_stock:
            messagebox.showinfo(
                'Productos sin stock',
                'No se encontraron productos sin stock'
            )
            self.llenar_treeview_productos()
            return
            
        # Llenado de treeview con productos sin stock
        for producto in productos_sin_stock:
            self.vista_inventario.tv_inventario.insert(
                '',
                'end',
                text=producto[1],
                values=(producto[2],producto[3],producto[4],producto[5]))

        # Creacion y aplicacion de tag para resaltar filas
        self.vista_inventario.tv_inventario.tag_configure(
            'Rojo',
            foreground='red',
            font=('century gothic',10,'bold')
        )
        
        for item in self.vista_inventario.tv_inventario.get_children():
            valores = self.vista_inventario.tv_inventario.item(
                item,
                'values'
            )
            stock = int(valores[2])
            if stock == 0:
                self.vista_inventario.tv_inventario.item(
                    item,
                    tags=('Rojo',)
                )
                
    
    def boton_filtrar_vencimientos(self):

        ''' Metodo para filtrar los productos que se encuentran vencidos en
            la ventana de vencimientos. Primero se obtienen las entradas de
            usuario y se ejecuta el metodo de filtrado de vencimientos. Si
            existen productos vencidos, se limpia treeview y se insertan
            los productos vencidos dependiendo de los filtros aplicados.
            Se crea un tag para resaltar aquellas filas donde el producto
            este vencido.
        '''
        
        try:
            # Obtencion de las entradas de usuario
            codigo_producto = self.ventana_vencimientos.entry_codigo.get()
            fecha_desde = self.ventana_vencimientos.entry_desde.get()
            fecha_hasta = self.ventana_vencimientos.entry_hasta.get()
            
            codigo_producto = (
                None if codigo_producto == '' else codigo_producto
            )
            
            # Ejecucion metodo filtrado de vencimientos
            filtrado_vencimientos = (
                self.modelo_inventario.consulta_vencimientos(
                    fecha_desde,
                    fecha_hasta,
                    codigo_producto
                )
            )

            # Llenado de treeview
            if filtrado_vencimientos:
                self.ventana_vencimientos.limpiar_treeview()

                for producto in filtrado_vencimientos:
                    self.ventana_vencimientos.tv_vencimientos.insert(
                        '',
                        'end',
                        text=producto[0],
                        values=(
                            producto[1],
                            producto[2],
                            producto[3],
                            producto[4])
                    )
                
                # Creacion y aplicacion de tag
                self.ventana_vencimientos.tv_vencimientos.tag_configure(
                    'Rojo',
                    foreground='red',
                    font=('century gothic',10,'bold')
                )
                for item in (
                    self.ventana_vencimientos.tv_vencimientos.get_children()
                ):
                    
                    valores = self.ventana_vencimientos.tv_vencimientos.item(
                        item,
                        'values'
                    )
                    
                    if int(valores[3]) <= 0:
                        self.ventana_vencimientos.tv_vencimientos.item(
                            item,
                            tags=('Rojo',)
                        )
                        
            else:
                messagebox.showinfo(
                    'Sin coincidencias',
                    'No se han encontrado productos'
                )
                self.ventana_vencimientos.limpiar_treeview()
                self.llenar_treeview_vencimientos()

        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')


    def boton_todos_vencimientos(self):

        ''' Metodo para filtrar todos los productos vencidos sin importar lo
            que se haya ingresado en los campos de filtrado.
            Si no existen productos vencidos, se muestra messagebox y se
            llena el treeview con todos los productos, caso contrario se
            muestran todos aquellos productos vencidos.
            Tambien se crea un tag para resaltar las filas.
        '''
        
        # Obtencion de productos vencidos
        vencimientos = self.modelo_inventario.productos_vencidos()
        
        # Limpieza de treeview
        self.ventana_vencimientos.limpiar_treeview()
        
        # Inserción de vencimientos
        if vencimientos:
            for producto_vencido in vencimientos:
                self.ventana_vencimientos.tv_vencimientos.insert(
                    '',
                    'end',
                    text=producto_vencido[0],
                    values=(
                        producto_vencido[1],
                        producto_vencido[2],
                        producto_vencido[3],
                        producto_vencido[4])
                )

            # Creacion y aplicacion de tag
            self.ventana_vencimientos.tv_vencimientos.tag_configure(
                'Rojo',
                foreground='red',
                font=('century gothic',10,'bold')
            )
            for item in (
                self.ventana_vencimientos.tv_vencimientos.get_children()
            ):
                valores = self.ventana_vencimientos.tv_vencimientos.item(
                    item,
                    'values'
                )
                
                if int(valores[3]) <= 0:
                    self.ventana_vencimientos.tv_vencimientos.item(
                        item,
                        tags=('Rojo',)
                    )
        
        else:
            messagebox.showinfo(
                'Sin resultados',
                'No se encontraron productos vencidos!'
            )
            self.llenar_treeview_vencimientos()
            
