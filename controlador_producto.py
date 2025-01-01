from view_inventario import InterfazInventario,Vencimientos,NuevoProducto,IngresoStock,ModificarProducto
from modelo_producto import ModeloProducto
from tkinter import messagebox, Toplevel, Tk

################################################################################################################################################
################################################### CONTROLADOR DE PRODUCTOS ###################################################################

# En este fichero se lleva a cabo la vinculación entre la vista y el modelo del modulo Productos

class ControladorProducto:

    def __init__(self,root):
        self.root = root
        self.vista_inventario = InterfazInventario(self.root)
        self.modelo_inventario = ModeloProducto()

        #Línea para que cada vez que se abra el modulo de productos aparezca el cursor en el entry de código
        self.vista_inventario.entry_codigo.focus()

        #Configuración de botones para que se abran las ventanas
        self.vista_inventario.boton_vencimientos.config(command=self.abrir_ventana_consulta_vencimientos)
        self.vista_inventario.boton_nuevo.config(command=self.boton_nuevo)
        self.vista_inventario.boton_ingresar.config(command=self.boton_ingresar_stock)
        self.vista_inventario.boton_modificar.config(command=self.boton_modificar)

        #Configuración funciones de botones para ejecutar acciones
        self.vista_inventario.boton_filtar.config(command=self.boton_filtrar_productos)
        self.vista_inventario.boton_cerostock.config(command=self.boton_sin_stock)
        self.vista_inventario.boton_eliminar.config(command=self.boton_eliminar_producto)
        
        #Siempre que se inicializa el módulo de productos, los mismos aparecerán automáticamente en el treeview
        self.llenar_treeview_productos()

        #Atributo de clase para almacenar elemento seleccionado en treeview
        self.elemento_seleccionado = None
    
    ##############################################################################################################################################
    ################################################### INICIALIZACIÓN DE VENTANAS ###############################################################
    # Función que crea un TopLevel de InterfazInventario para abrir la ventana de vencimientos
    def abrir_ventana_consulta_vencimientos(self):
        self.toplevel_vencimientos = Toplevel(self.root)
        self.ventana_vencimientos = Vencimientos(self.toplevel_vencimientos)
        self.toplevel_vencimientos.grab_set()
        self.ventana_vencimientos.entry_codigo.focus()
        # Llenado de Treeview
        self.llenar_treeview_vencimientos()

        # Configuración de botones
        self.ventana_vencimientos.boton_buscar.config(command=self.boton_filtrar_vencimientos)
        self.ventana_vencimientos.boton_vencido.config(command=self.boton_todos_vencimientos)

    # Función que crea un TopLevel de InterfazInventario para abrir la ventana de nuevoproducto o modificarproducto
    def abrir_ventana_nuevoproducto(self):
        self.toplevel_nuevo_producto = Toplevel(self.root)
        self.ventana_nuevo_producto = NuevoProducto(self.toplevel_nuevo_producto)
        self.toplevel_nuevo_producto.grab_set()
        self.ventana_nuevo_producto.entry_codigo.focus()
        self.ventana_nuevo_producto.boton_guardar.config(command=self.boton_guardar_nuevoproducto)

        # Evento: cuando se escribe un codigo existente en entry_codigo, se autocompleta entry descripcion
        self.ventana_nuevo_producto.entry_codigo.bind("<KeyRelease>",self.actualizar_entrydescripcion)
    
    def abrir_ventana_modificar_producto(self):
        self.toplevel_modificar_producto = Toplevel(self.root)
        self.ventana_modificar_producto = ModificarProducto(self.toplevel_modificar_producto)
        self.toplevel_modificar_producto.grab_set()
        self.ventana_modificar_producto.boton_guardar.config(command=self.guardar_modificacion_producto)

    # Función que crea un TopLevel de InterfazInventario para abrir la ventana de ingreso de stock
    def abrir_ventana_ingresostock(self):
        self.toplevel_ingreso_stock = Toplevel(self.root)
        self.ventana_ingreso_stock = IngresoStock(self.toplevel_ingreso_stock)
        self.toplevel_ingreso_stock.grab_set()
        self.ventana_ingreso_stock.entry_ingresostock.focus()
        self.ventana_ingreso_stock.boton_ingresostock.config(command=self.boton_guardar_ingresostock)
    
    ################################################################################################################################################
    ####################################################### INICIALIZACIÓN TREEVIEW ################################################################
    #Función para rellenar el treeview con los productos existentes en la base de datos
    def llenar_treeview_productos(self):
        productos = self.modelo_inventario.mostrar_productos()
        for producto in productos:
            self.vista_inventario.tv_inventario.insert('','end',text=producto[1],values=(producto[2],producto[3],producto[4],producto[5]))

        # Se pintan en rojo aquellas filas donde el stock del producto sea cero
        self.vista_inventario.tv_inventario.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
        for item in self.vista_inventario.tv_inventario.get_children():
            valores = self.vista_inventario.tv_inventario.item(item,'values')
            stock = int(valores[2])
            if stock == 0:
                self.vista_inventario.tv_inventario.item(item,tags=('Rojo',))
            
    #Función para rellenar el treeview de vencimientos
    def llenar_treeview_vencimientos(self):
        consulta_vencimientos = self.modelo_inventario.mostrar_vencimientos_todosproductos()
        for producto in consulta_vencimientos:
            self.ventana_vencimientos.tv_vencimientos.insert('','end',text=producto[0],values=(producto[1],producto[2],producto[3],producto[4]))

        # Se define una configuración de tag para que cuando un producto esté vencido, se pinte esa fila de rojo. Para ello se recorren los elementos
        # del Treeview con un bucle for.
        self.ventana_vencimientos.tv_vencimientos.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
        for item in self.ventana_vencimientos.tv_vencimientos.get_children():
            valores = self.ventana_vencimientos.tv_vencimientos.item(item,'values')
            if int(valores[3]) <= 0:
                self.ventana_vencimientos.tv_vencimientos.item(item,tags=('Rojo',))
    
    ################################################################################################################################################
    ############################################################# EVENTOS ##########################################################################
    # Función para rellenar el campo "descripcion" a la hora de crear un nuevo producto, si ya existe el codigo en la base de datos, se mostrara la
    # respectiva descripcion

    def actualizar_entrydescripcion(self,event):
        codigo_producto = self.ventana_nuevo_producto.entry_codigo.get()
        # Obtencion de la descripcion del producto de acuerdo al codigo ingresado
        descripcion = ModeloProducto.descripcion_producto(codigo_producto)
        # Si se encuentra una descripcion, entonces se inserta esa descripcion en el entry descripcion y se hace foco en precio
        if descripcion:
            self.ventana_nuevo_producto.entry_descripcion.delete(0,'end')
            self.ventana_nuevo_producto.entry_descripcion.insert(0,descripcion[0][0])
            self.ventana_nuevo_producto.entry_precio.focus()
        # Si no se encuentran coincidencias, el entry descripcion queda vacio
        else:
            self.ventana_nuevo_producto.entry_descripcion.insert(0,'')

    ###############################################################################################################################################
    ####################################################### ACCIONES DE BOTONES ###################################################################
    #Función para que el boton crear nuevo producto abra la ventana de ingreso de datos 
    def boton_nuevo(self):
        self.abrir_ventana_nuevoproducto()
    
    ###############################################################################################################################################
    #Función para abrir la ventana de modificación de productos solo si se ha seleccionado un elemento en el Treeview
    def boton_modificar(self):
        # Verificación de que se seleccionó un elemento del Treeview
        self.elemento_seleccionado = self.vista_inventario.tv_inventario.selection()
        # Comprobacion de que se eligio solo un elemento del treeview
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return
        # Si hay un elemento seleccionado, entonces se abre la ventana de modificacion de producto
        if self.elemento_seleccionado:
            self.abrir_ventana_modificar_producto()
            #Obtención de la información correspondiente al elemento seleccionado
            valores = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'values')
            #Seteo de los entry con los datos correspondientes al elemento elegido
            self.ventana_modificar_producto.entry_descripcion.insert(0,valores[0])
            self.ventana_modificar_producto.entry_precio.insert(0,valores[1])
            self.ventana_modificar_producto.entry_stock.insert(0,valores[2])

        else:
            messagebox.showerror('Error','Debes seleccionar un producto')
    
    ###############################################################################################################################################
    #Función para guardar la modificación de un producto seleccionado en el Treeview
    def guardar_modificacion_producto(self):
        
        try:
            #Recuperar valores de los entry
            descripcion = self.ventana_modificar_producto.entry_descripcion.get()
            precio = float(self.ventana_modificar_producto.entry_precio.get())
            stock = int(self.ventana_modificar_producto.entry_stock.get())

            #Obtención del nro_producto correspondiente al seleccionado en el Treeview
            codigo_producto = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'text')
            valores = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'values')
            vencimiento = valores[3]
            nro_producto = self.modelo_inventario.obtener_nroproducto(codigo_producto,vencimiento)

            #Ejecución de la función actualizar producto
            self.modelo_inventario.actualizar_producto(nro_producto[0],descripcion,precio,stock)
            self.toplevel_modificar_producto.destroy()
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()
            messagebox.showinfo('Producto Modificado',f'Producto {descripcion} modificado!')
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    ###############################################################################################################################################
    #Función para incluir en el botón guardar
    def boton_guardar_nuevoproducto(self):

        codigo_producto = self.ventana_nuevo_producto.entry_codigo.get()
        descripcion = self.ventana_nuevo_producto.entry_descripcion.get()
        vencimiento = self.ventana_nuevo_producto.entry_vencimiento.get()

        try:
            precio_unitario = float(self.ventana_nuevo_producto.entry_precio.get())
            stock = int(self.ventana_nuevo_producto.entry_stock.get())

            #Se busca en la base de datos si existe un nro_producto que coincida con el código Y el vencimiento ingresados, si ya existe se muestra
            #messagebox diciendo que el producto ya existe en la base de datos con ese mismo código y vencimiento
            nro_producto = ModeloProducto.obtener_nroproducto(codigo_producto,vencimiento)
            if nro_producto:
                messagebox.showerror('Producto Existente',f'El producto {descripcion} ya existe en el inventario!')
            else:
                ModeloProducto.nuevo_producto(codigo_producto,descripcion,precio_unitario,stock,vencimiento)
                messagebox.showinfo('Producto Ingresado',f'Producto: {descripcion} creado correctamente!')
                self.vista_inventario.limpiar_treeview()
                self.ventana_nuevo_producto.limpiar_cajas()
                self.llenar_treeview_productos()
                self.toplevel_nuevo_producto.destroy()
        
        except ValueError: #Si se introducen valores erroneos, por ejemplo un texto en el entry de precio o stock, arrojará un messagebox.
            messagebox.showerror('Error','Error en ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Se ha producido un error inesperado - {error}')

    ###############################################################################################################################################
    #Función para eliminar producto, según la selección del treeview
    def boton_eliminar_producto(self):
        # Seleccion del elemento
        self.elemento_seleccionado = self.vista_inventario.tv_inventario.selection()

        # Verificacion de que no se elija mas de un elemento
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return
        # Obtencion de informacion de producto seleccionado
        if self.elemento_seleccionado:
            producto = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'values')
            descripcion = producto[0]
            #Messagebox solicitando confirmación de eliminación de producto
            confirmacion = messagebox.askyesno('Eliminar Producto',f'Desea eliminar el producto {descripcion}?')
            if confirmacion:
                #Obtención del nro_producto
                codigo_producto = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'text')
                valores = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'values')
                vencimiento = valores[3]
                nro_producto = self.modelo_inventario.obtener_nroproducto(codigo_producto,vencimiento)

                #Eliminación del producto
                self.modelo_inventario.eliminar_producto(nro_producto[0])
                self.vista_inventario.limpiar_treeview()
                self.llenar_treeview_productos()
                messagebox.showinfo('Producto Eliminado',f'Producto {valores[0]} eliminado!')
        
        else:
            messagebox.showerror('Eliminar Producto','Debes seleccionar un producto')

    ###############################################################################################################################################
    #Función para abrir la ventana de ingreso de stock. Se verifica que haya un elemento seleccionado en el Treeview
    def boton_ingresar_stock(self):
        self.elemento_seleccionado = self.vista_inventario.tv_inventario.selection()
        
        # Verificacion de que se eligio solo un elemento
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar solo un elemento')
            return
        
        # Si se eligio solo un elemento, se muestra ventana ingreso de stock
        if self.elemento_seleccionado:
            self.abrir_ventana_ingresostock()
        else:
            messagebox.showerror('Error','Debes seleccionar un producto')
    
    #Función para guardar el stock ingresado para el producto seleccionado en el Treeview
    def boton_guardar_ingresostock(self):
        try:
            #Se recupera valor de stock ingresado por usuario
            stock_ingresado = int(self.ventana_ingreso_stock.entry_ingresostock.get())

            #Obtención nro_producto de acuerdo al elemento seleccionado en Treeview
            codigo_producto = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'text')
            valores = self.vista_inventario.tv_inventario.item(self.elemento_seleccionado,'values')
            vencimiento = valores[3]
            nro_producto = self.modelo_inventario.obtener_nroproducto(codigo_producto,vencimiento)
            
            #Ejecución de la función ingreso_stock
            self.modelo_inventario.ingreso_stock(nro_producto[0],stock_ingresado)
            self.toplevel_ingreso_stock.destroy()
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()
            messagebox.showinfo('Stock Ingresado',f'Stock de {valores[0]} ingresado!')
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de valores')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    ###############################################################################################################################################
    #Función para filtrar los productos según el código o la descripción parcial del mismo
    def boton_filtrar_productos(self):
        #Borrar elementos del treeview
        self.vista_inventario.limpiar_treeview()

        #Filtrar productos y rellenar nuevamente el treeview con productos filtrados:
        codigo = self.vista_inventario.entry_codigo.get()
        descripcion = self.vista_inventario.entry_descripcion.get()
        self.vista_inventario.limpiar_cajas()

        #Si no se ingresa ningún valor en los entry, se le asigna el valor None para que funcione correctamente la función mostrar_productos()
        codigo = None if codigo == '' else codigo
        descripcion = None if descripcion == '' else descripcion

        try:

            if codigo == '' and descripcion == '':
                self.llenar_treeview_productos()
            
            else:
                productos_filtrados = self.modelo_inventario.mostrar_productos(codigo,descripcion)
                if productos_filtrados:
                    #Se llena el treeview con los elementos filtrados
                    for producto in productos_filtrados:
                        self.vista_inventario.tv_inventario.insert('','end',text=producto[1],values=(producto[2],producto[3],producto[4],producto[5]))

                    # Se pintan en rojo aquellas filas donde el stock del producto sea cero
                    self.vista_inventario.tv_inventario.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
                    for item in self.vista_inventario.tv_inventario.get_children():
                        valores = self.vista_inventario.tv_inventario.item(item,'values')
                        stock = int(valores[2])
                        if stock == 0:
                            self.vista_inventario.tv_inventario.item(item,tags=('Rojo',))
                else:
                    messagebox.showinfo('Productos','No se ha encontrado ningún producto')
                    self.llenar_treeview_productos()

        except Exception as error:
            messagebox.showerror('Error',f'Error Inesperado - {error}')

    ###############################################################################################################################################
    #Función para filtrar los productos sin stock
    def boton_sin_stock(self):
        #Borrar elementos del treeview
        self.vista_inventario.limpiar_treeview()

        productos_sin_stock = self.modelo_inventario.productos_sinstock()

        #Comprobación si es una lista vacía (no hay productos sin stock) se arroja un messagebox
        if not productos_sin_stock:
            messagebox.showinfo('Productos sin stock','No se encontraron productos sin stock')
            self.llenar_treeview_productos()
            return
        
        for producto in productos_sin_stock:
            self.vista_inventario.tv_inventario.insert('','end',text=producto[1],values=(producto[2],producto[3],producto[4],producto[5]))

        # Se pintan en rojo aquellas filas donde el stock del producto sea cero
        self.vista_inventario.tv_inventario.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
        for item in self.vista_inventario.tv_inventario.get_children():
            valores = self.vista_inventario.tv_inventario.item(item,'values')
            stock = int(valores[2])
            if stock == 0:
                self.vista_inventario.tv_inventario.item(item,tags=('Rojo',))
                
    ###############################################################################################################################################
    #Función para filtrar los vencimientos de los productos en función de si se quiere filtrar por código o por fechas
    def boton_filtrar_vencimientos(self):
        try:
            #Obtención de las entradas de usuario
            codigo_producto = self.ventana_vencimientos.entry_codigo.get()
            fecha_desde = self.ventana_vencimientos.entry_desde.get()
            fecha_hasta = self.ventana_vencimientos.entry_hasta.get()

            #Se asigna None a codigo_producto si no se ingresa ningún valor, para evitar error.
            codigo_producto = None if codigo_producto == '' else codigo_producto

            #Ejecución de la función consulta_vencimientos para obtener todos los productos dentro del filtro aplicado
            filtrado_vencimientos = self.modelo_inventario.consulta_vencimientos(fecha_desde,fecha_hasta,codigo_producto)

            if filtrado_vencimientos:
                self.ventana_vencimientos.limpiar_treeview()

                for producto in filtrado_vencimientos:
                    self.ventana_vencimientos.tv_vencimientos.insert('','end',text=producto[0],values=(producto[1],producto[2],producto[3],producto[4]))
                
                # Se define una configuración de tag para que cuando un producto esté vencido, se pinte esa fila de rojo. Para ello se recorren los elementos
                # del Treeview con un bucle for.
                self.ventana_vencimientos.tv_vencimientos.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
                for item in self.ventana_vencimientos.tv_vencimientos.get_children():
                    valores = self.ventana_vencimientos.tv_vencimientos.item(item,'values')
                    if int(valores[3]) <= 0:
                        self.ventana_vencimientos.tv_vencimientos.item(item,tags=('Rojo',))

            #Si filtrado_vencimientos es una lista vacia (no se encontraron productos dentro del filtrado ingresado)
            else:
                messagebox.showinfo('Sin coincidencias','No se han encontrado productos')
                self.ventana_vencimientos.limpiar_treeview()
                self.llenar_treeview_vencimientos()

        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    ###############################################################################################################################################
    #Función para filtrar todos los productos vencidos, sin importar lo que esté escrito en codigo o fechas
    def boton_todos_vencimientos(self):
        vencimientos = self.modelo_inventario.productos_vencidos()
        # Limpieza de treeview
        self.ventana_vencimientos.limpiar_treeview()
        # Inserción de vencimientos
        if vencimientos:
            for producto_vencido in vencimientos:
                self.ventana_vencimientos.tv_vencimientos.insert('','end',text=producto_vencido[0],values=(producto_vencido[1],producto_vencido[2],producto_vencido[3],producto_vencido[4]))

            # Se define una configuración de tag para que cuando un producto esté vencido, se pinte esa fila de rojo. Para ello se recorren los elementos
            # del Treeview con un bucle for.
            self.ventana_vencimientos.tv_vencimientos.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
            for item in self.ventana_vencimientos.tv_vencimientos.get_children():
                valores = self.ventana_vencimientos.tv_vencimientos.item(item,'values')
                if int(valores[3]) <= 0:
                    self.ventana_vencimientos.tv_vencimientos.item(item,tags=('Rojo',))
        
        else:
            messagebox.showinfo('Sin resultados','No se encontraron productos vencidos!')
            self.llenar_treeview_vencimientos()
