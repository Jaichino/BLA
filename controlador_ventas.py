from view_ventas import VentanaVentas,ConsultaVentas,DetalleVentas,ConfirmacionVenta,InterfazInteres
from modelo_ventas import ModeloVentas
from modelo_producto import ModeloProducto
from modelo_ccorriente import ModeloCuentaCorriente
from tkinter import messagebox, Toplevel
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import sys
import os

################################################################################################################################################
################################################### CONTROLADOR DE VENTAS ######################################################################

# En este fichero se lleva a cabo la vinculación entre la vista y el modelo del modulo Ventas

class ControladorVentas:

    def __init__(self,root):
        self.root = root
        self.vista_ventas = VentanaVentas(self.root)
        self.modelo_ventas = ModeloVentas()

        # Inicialización del foco en entry codigo
        self.vista_ventas.entry_cliente.focus()

        # Inicialización de funciones para apertura de ventanas
        self.vista_ventas.boton_consultaventas.config(command=self.abrir_ventana_consultaventas)
        self.vista_ventas.boton_finalizar_venta.config(command=self.abrir_abrir_ventana_finalizacionventa)
        self.vista_ventas.boton_buscar.config(command=self.boton_buscar_infoproducto)
        self.vista_ventas.boton_carrito.config(command=self.boton_agregar_carrito)
        self.vista_ventas.boton_eliminar_venta.config(command=self.eliminar_del_carrito)

        # Atributo que guarda la descripción del producto que se busca al realizar una venta, ya que el mismo se lo visualiza como un label
        self.descripcion_producto = None

        # Atributo para guardar el elemento seleccionado en los treeview
        self.elemento_seleccionado = []

        # lista vacía para guardar "carrito" e inicializar monto_total_venta = 0
        self.lista_carrito = []
        self.monto_total_venta = 0
        self.contador_carrito = 0
        
        # Se guarda cliente que está realizando la compra para luego utilizarlo en la función agregar_venta
        self.cliente_venta = None

        # bind para que cuando se escriba en entry codigo, se ejecute automáticamente la funcion vencimientos_codigoingresado
        self.vista_ventas.entry_codigo_producto.bind('<KeyRelease>',self.vencimientos_codigoingresado)
        # bind para filtrar la lista de clientes en el ComboBox según las entradas del usuario
        self.vista_ventas.entry_cliente.bind('<KeyRelease>',self.buscar_cliente_nuevaventa)

    ##############################################################################################################################################
    ################################################### INICIALIZACIÓN DE VENTANAS ###############################################################
    
    # Función que inicializa la ventana consulta de ventas   
    def abrir_ventana_consultaventas(self):
        self.minimizar_root()
        self.toplevel_consulta_ventas = Toplevel(self.root)
        self.ventana_consulta_ventas = ConsultaVentas(self.toplevel_consulta_ventas)
        self.toplevel_consulta_ventas.grab_set()
        self.toplevel_consulta_ventas.protocol("WM_DELETE_WINDOW",self.volver_ventana_ventas)

        # bind para filtrar la lista de clientes en el ComboBox según las entradas del usuario
        self.ventana_consulta_ventas.entry_cliente.bind("<KeyRelease>",self.buscar_cliente_consultaventa)

        # Acciones de botones
        self.ventana_consulta_ventas.boton_buscar.config(command=self.boton_consultar_ventas)
        self.ventana_consulta_ventas.boton_eliminar.config(command=self.eliminar_venta)
        self.ventana_consulta_ventas.boton_detalle.configure(command=self.boton_abrir_detalleventas)
        self.ventana_consulta_ventas.boton_pendientes.config(command=self.boton_pagos_pendientes)

        # Se guarda el valor de nro_venta que se selecciona en Treeview. Se inicializa como None
        self.nro_venta_consulta = None

    # Función que inicializa la ventana Detalle de ventas
    def abrir_ventana_detalleventas(self):
        self.toplevel_detalle_ventas = Toplevel(self.toplevel_consulta_ventas)
        self.ventana_detalle_ventas = DetalleVentas(self.toplevel_detalle_ventas)
        self.toplevel_detalle_ventas.grab_set()

        # Inicialización de label nro_venta según elemento elegido en Treeview
        self.ventana_detalle_ventas.label_nroventa.config(text=f'Venta #{self.nro_venta_consulta}')

        # Configuración boton imprimir factura
        self.ventana_detalle_ventas.boton_pdf.config(command=self.detalleventas_imprimirpdf)

    # Función para abrir ventana interés de venta
    def abrir_ventana_interesventa(self):
        # Si se selecciona un medio de pago que no sea débito/crédito, se muestra mensaje de error
        modo_pago = self.ventana_finalizacion_venta.seleccion_radiobutton()
        if modo_pago != 3:
            messagebox.showerror('Error','Solo se puede agregar interés si el modo de pago es Débito/Crédito')	
            return
        
        self.toplevel_interes_venta = Toplevel(self.root)
        self.ventana_interes_venta = InterfazInteres(self.toplevel_interes_venta)
        self.toplevel_interes_venta.grab_set()

        self.ventana_interes_venta.boton_interes.config(command=self.boton_agregar_interes)

    # Función que inicializa la ventana Finalización de venta
    def abrir_ventana_finalizacionventa(self):

        self.toplevel_finalizacion_venta = Toplevel(self.root)
        self.ventana_finalizacion_venta = ConfirmacionVenta(self.toplevel_finalizacion_venta)
        self.toplevel_finalizacion_venta.grab_set()

        # Obtención del número de venta
        self.nro_venta = self.modelo_ventas.ultimo_nro_venta()
        if self.nro_venta[0][0] is None:
            self.nro_venta = 1
        else:
            self.nro_venta = self.modelo_ventas.ultimo_nro_venta()[0][0] + 1

        self.interes = 0

        # Modificación del label nro_venta
        self.ventana_finalizacion_venta.label_numero_venta.config(text = f'Venta #{self.nro_venta}')
        
        # Inicialización con el monto_total_venta y nro_venta
        self.ventana_finalizacion_venta.label_total_venta.config(text=f'Total Venta: ${self.monto_total_venta}')
        
        #Configuración de la función del boton
        self.ventana_finalizacion_venta.boton_confirmar.config(command=self.boton_confirmar_venta)
        self.ventana_finalizacion_venta.boton_interes.config(command=self.abrir_ventana_interesventa)

    # Función para minimizar el root
    def minimizar_root(self):
        self.root.iconify()
    
    # Función para cerrar consulta de venta y volver a abrir ventana de ventas
    def volver_ventana_ventas(self):
        self.toplevel_consulta_ventas.destroy()
        self.root.deiconify()

    ###############################################################################################################################################
    ############################################################# EVENTOS #########################################################################

    # Función para filtrar los clientes que han realizado compras, para incluir en el ComboBox de cliente y se rellene automáticamente cuando va 
    # encontrando coincidencias. Para ello se lo vinculará a un event <KeyRelease>
    def buscar_cliente_nuevaventa(self,event):
        # Obtención de los clientes que realizaron compras anteriormente
        clientes = self.modelo_ventas.clientes()
        # Obtención de la entrada de cliente
        entrada_cliente = self.vista_ventas.entry_cliente.get().lower()
    
        if clientes:
            # Se filtra la lista de clientes original según la entrada del usuario, con el método startswith() se filtran solo los que coincidan
            # con la entrada del cliente
            lista_clientes = [cliente[0] for cliente in clientes if cliente[0].lower().startswith(entrada_cliente)]

            if lista_clientes:
                # Si se encuentran coincidencias (la lista no está vacía) se asigna esos valores al ComboBox
                self.vista_ventas.entry_cliente['values'] = lista_clientes

            else:
                # Caso contrario, se introduce una lista vacía al ComboBox
                self.vista_ventas.entry_cliente['values'] = []
        else:
            self.vista_ventas.entry_cliente['values'] = []

    #Función para filtrar los clientes en el módulo consulta de clientes, para introducirlos en el ComboBox
    def buscar_cliente_consultaventa(self,event):
        clientes = ModeloVentas.clientes()
        entrada_cliente = self.ventana_consulta_ventas.entry_cliente.get().lower()

        if clientes:
            lista_clientes = [cliente[0] for cliente in clientes if cliente[0].lower().startswith(entrada_cliente)]

            if lista_clientes:
                self.ventana_consulta_ventas.entry_cliente['values'] = lista_clientes
            else:
                self.ventana_consulta_ventas.entry_cliente['values'] = []
        else:
            self.ventana_consulta_ventas.entry_cliente['values'] = []

    # Función para introducir los vencimientos de productos en el ComboBox que existen para el código de producto introducido
    def vencimientos_codigoingresado(self,event):
        # Obtención del código ingresado
        codigo = self.vista_ventas.entry_codigo_producto.get()

        # Obtención de los vencimientos según el código ingresado
        vencimientos = ModeloProducto.vencimiento_producto_a_vender(codigo)
        
        if vencimientos:
            # Generación de lista con vencimientos en formato string adecuado para cargar al ComboBox
            vencimientos_str = [v[0].strftime('%d-%m-%Y') for v in vencimientos]
            # Introducción de elementos al ComboBox, con .current(0) se selecciona por defecto el primer elemento del ComboBox
            self.vista_ventas.entry_vencimiento['values'] = vencimientos_str
            self.vista_ventas.entry_vencimiento.current(0)
        
        else:
            # Si no se encuentran vencimientos, se introduce una lista vacía al ComboBox, y .set() sirve para borrar el contenido hasta que se 
            # encuentra coincidencia
            self.vista_ventas.entry_vencimiento['values'] = []
            self.vista_ventas.entry_vencimiento.set('')    

    ###############################################################################################################################################
    ####################################################### ACCIONES DE BOTONES ###################################################################

    # Función para abrir la ventana de finalización de venta, en caso de que la lista de carrito esté vacía, no se debe dejar abrir dicha ventana
    def abrir_abrir_ventana_finalizacionventa(self):
        if self.cliente_venta == '':
            messagebox.showerror('Error','Introducir Cliente')
            return
        
        if not self.lista_carrito:
            messagebox.showerror('Error','No hay productos en el carrito')
        else:
            self.abrir_ventana_finalizacionventa()

    # Función para introducir en el boton "buscar", que hará aparecer la información del producto, precio y cantidad en los entry en función del
    # código y vencimientos ingresados por el usuario
    def boton_buscar_infoproducto(self):
        # Limpieza de campos
        self.vista_ventas.entry_precio.delete(0,'end')
        self.vista_ventas.label_en_stock.config(text='En Stock: ')
        self.vista_ventas.label_descripcion_producto.config(text='Producto: ')
        
        try:
            # Obtención del código y vencimiento elegido por el usuario
            codigo = self.vista_ventas.entry_codigo_producto.get()
            vencimiento = self.vista_ventas.entry_vencimiento.get()
            
            if codigo == '' or vencimiento == '':
                messagebox.showerror('Error','Debes ingresar un código')
                return
            
            # Obtención de la información del producto según código y vencimiento
            info_producto = ModeloProducto.informacion_producto(codigo,vencimiento)

            if info_producto:
                #Carga de información (producto,precio,stock)
                self.descripcion_producto = info_producto[0][2]
                self.vista_ventas.entry_precio.insert(0,info_producto[0][3])
                self.vista_ventas.label_en_stock.config(text=f'En Stock: {info_producto[0][4]}')
                self.vista_ventas.label_descripcion_producto.config(text=f'Producto: {self.descripcion_producto}')

            else:
                messagebox.showinfo('Producto no encontrado','No se ha encontrado este producto!')

        except Exception as error:
            messagebox.showerror('Error',f'Ha sucedido un error inesperado - {error}')

    # Función para el botón "Agregar al carrito", recuperará valores de los entry y los insertará en Treeview y en una lista "carrito", la cuál se
    # utilizará luego para ejecutar la carga a base de datos.
    def boton_agregar_carrito(self):
        try:
            # Obtención de entradas de usuario
            codigo = self.vista_ventas.entry_codigo_producto.get()
            descripcion = self.descripcion_producto
            precio = float(self.vista_ventas.entry_precio.get())
            cantidad = int(self.vista_ventas.entry_cantidad.get())
            vencimiento = self.vista_ventas.entry_vencimiento.get()
            cliente = self.vista_ventas.entry_cliente.get()

            # Verificación de que se han llenado los campos
            if codigo == '' or precio == '' or cantidad == '':
                messagebox.showerror('Error','Se deben completar todos los campos')
                return
            
            # Verificación cantidad ingresada es menor que el stock disponible del producto, para ello se busca dentro de la información
            # del producto, con codigo y vencimiento

            info_producto = ModeloProducto.informacion_producto(codigo,vencimiento)
            stock_disponible = info_producto[0][4]
            if cantidad > stock_disponible:
                messagebox.showerror('Error','La cantidad ingresada es mayor al stock disponible')
                return
            
            # Se suma 1 al contador del carrito
            self.contador_carrito += 1
            
            # Se incrementa el monto_total_venta en (cantidad * precio)
            self.monto_total_venta += precio * cantidad

            # Introducción de valores en Treeview
            self.vista_ventas.tv_ventas.insert('','end',text=self.contador_carrito,values=(codigo,descripcion,precio,cantidad))

            # Actualización del monto_total_venta
            self.vista_ventas.label_total_venta.config(text=f'Total de la venta: ${self.monto_total_venta}')

            # Se hace append en lista_carrito de la información del producto agregado al carrito, primero se obtiene nro_prod
            nro_producto = ModeloProducto.obtener_nroproducto(codigo,vencimiento)
            self.lista_carrito.append((nro_producto[0][0],precio,cantidad))

            # Limpieza de entries
            self.vista_ventas.limpiar_cajas()
            self.vista_ventas.label_descripcion_producto.config(text='Producto: ')
            self.vista_ventas.label_en_stock.config(text='En Stock: ')

            # Seteo de cliente para que quede guardado en la instancia
            self.cliente_venta = cliente

            # Se hace foco en entry codigo_producto una vez que se limpian los entries
            self.vista_ventas.entry_codigo_producto.focus()

        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos!')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    # Función para eliminar un producto del carrito, se eliminará la fila en el Treeview, el elemento correspondiente en la lista_carrito y se restará
    # el monto de ese producto del monto_total_venta
    def eliminar_del_carrito(self):
        # Obtener elemento seleccionado del treeview
        self.elemento_seleccionado = self.vista_ventas.tv_ventas.selection()

        if not self.elemento_seleccionado:
            messagebox.showerror('Error','Debes seleccionar un producto')
            return
        
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return
        
        # Obtener precio y cantidad del elemento seleccionado para actualizar el monto_venta_total
        valores_elemento_seleccionado = self.vista_ventas.tv_ventas.item(self.elemento_seleccionado,'values')
        precio = float(valores_elemento_seleccionado[2])
        cantidad = int(valores_elemento_seleccionado[3])
        numero_carrito = self.vista_ventas.tv_ventas.item(self.elemento_seleccionado,'text')

        # Actualización monto_venta_total
        self.monto_total_venta -= precio * cantidad
        self.vista_ventas.label_total_venta.config(text=f'Total de la venta: ${self.monto_total_venta}')

        # Eliminación de la fila correspondiente en el Treeview
        self.vista_ventas.tv_ventas.delete(self.elemento_seleccionado)

        # Eliminación del elemento de la lista "carrito"
        del self.lista_carrito[numero_carrito - 1]

        # Actualización números de carrito (#)
        for contador in self.vista_ventas.tv_ventas.get_children():
            nro_carrito = self.vista_ventas.tv_ventas.item(contador,'text')
            if nro_carrito > numero_carrito:
                self.vista_ventas.tv_ventas.item(contador,text=nro_carrito-1)
        
        # Actualizacion del contador para que siempre arranque desde el ultimo ingresado
        children_carritos = self.vista_ventas.tv_ventas.get_children()
        lista_nros_carritos = [self.vista_ventas.tv_ventas.item(child,'text') for child in children_carritos]
        if not lista_nros_carritos:
            self.contador_carrito = 0
        else:
            self.contador_carrito = lista_nros_carritos[-1] #Se setea contador de carrito como el ultimo elemento de la lista

        # Mensaje de eliminación de producto
        messagebox.showinfo('Eliminado',f'{valores_elemento_seleccionado[1]} eliminado del carrito!')

    # Función para consulta de ventas, se toman entradas de usuario y luego mediante el botón buscar se filtran las ventas. Si no se ingresa cliente,
    # se filtrará por fechas, caso contrario, se filtra unicamente por cliente.
    def boton_consultar_ventas(self):
        # Entradas de usuario
        cliente = self.ventana_consulta_ventas.entry_cliente.get()
        fecha_desde = self.ventana_consulta_ventas.entry_desde.get()
        fecha_hasta = self.ventana_consulta_ventas.entry_hasta.get()

        # Se asigna None en caso de no ingresarse ningún cliente
        cliente = None if cliente == '' else cliente

        # Lista filtrada de ventas
        ventas_filtradas = ModeloVentas.consultar_ventas(fecha_desde,fecha_hasta,cliente)

        # Si se encontraron coincidencias, se rellena Treeview con dichos registros
        if ventas_filtradas:
            # Se limpia Treeview antes de insertar datos
            self.ventana_consulta_ventas.limpiar_treeview()
            for venta in ventas_filtradas:
                self.ventana_consulta_ventas.tv_consultaventas.insert('','end',text=venta[0],values=(venta[1],venta[2],venta[3],venta[4],venta[5]))
        # Si no se encuentran registros, se muestra messagebox
        else:
            messagebox.showinfo('Sin coincidencias','No se encontraron ventas!')
            self.ventana_consulta_ventas.limpiar_treeview()

    # Función para confirmar la venta realizada, se realizarán los siguientes pasos importantes:
    # 1) Se verificará si el pago fue completo, es decir, si monto_abonado = monto_total_venta, si no se paga completo se ejecuta la función agregar a
    #    cuenta corriente
    # 2) Se agrega la venta en tabla Ventas (se extrae nro_venta, cliente, monto_total, id_modo_pago de los radiobuttons) - Si la venta se pago completa
    #    entonces estado_venta = Pagado. Caso contrario estado_venta = Pendiente
    # 3) Se agregan los productos del carrito a la tabla DetalleVentas, con un bucle for que recorra la lista_carrito
    # 4) Se descuentan las cantidades de los respectivos productos vendidos para actualizar su stock en la tabla Productos
    # 5) Se pregunta si se desea generar un pdf de la factura correspondiente
    def boton_confirmar_venta(self):
        try:
            # Se obtienen entradas del usuario (monto entregado y la opción de los Radiobuttons para el modo de pago)
            monto_abonado = float(self.ventana_finalizacion_venta.entry_entrega.get())
            modo_pago = self.ventana_finalizacion_venta.seleccion_radiobutton()

            # Si el monto abonado, es igual al monto total de la venta, entonces se registra la venta como Pagada y se registra en Detalle de Ventas pero no
            # en cuenta corriente. Por otro lado, también se descuentan los productos vendidos.
            if monto_abonado > self.monto_total_venta:
                messagebox.showerror('Error','El monto de venta es menor')
                return
            
            if monto_abonado == self.monto_total_venta:

                # Registro de venta en Ventas
                self.modelo_ventas.nueva_venta(self.nro_venta,self.cliente_venta,self.monto_total_venta,modo_pago,'Pagado',self.interes)

                # Registro en Detalle Ventas
                for producto in self.lista_carrito:
                    self.modelo_ventas.ingresar_detalle_ventas(self.nro_venta,producto[0],producto[1],producto[2])
                
                # Descuento de productos del stock
                for producto in self.lista_carrito:
                    ModeloProducto.descontar_producto(producto[0],producto[2])
                
                # Confirmación de venta
                messagebox.showinfo('Ventas',f'Venta {self.nro_venta} agregada correctamente!')
                
                # Cierre de ventana finalización de venta
                self.toplevel_finalizacion_venta.destroy()

                # Limpieza de campos
                self.vista_ventas.entry_cliente.delete(0,'end')
                self.vista_ventas.limpiar_treeview()
                
                # Seteo de atributos
                self.monto_total_venta = 0
                self.vista_ventas.label_total_venta.config(text=f'Total Venta: ${self.monto_total_venta}')
                self.lista_carrito = []
                self.contador_carrito = 0

            # En caso de que se ingrese menos del monto total, se agregará la venta como Pendiente y a su vez se agregará a Cuentas Corrientes
            else:
                pregunta = messagebox.askyesno('Cuenta Corriente','La venta se agregará a cuentas corrientes, ¿Desea seguir?')
                if pregunta:
                    # Registro de Venta con estado_venta = Pendiente
                    self.modelo_ventas.nueva_venta(self.nro_venta,self.cliente_venta,self.monto_total_venta,modo_pago,'Pendiente',self.interes)

                    # Registro Detalle Ventas
                    for producto in self.lista_carrito:
                        self.modelo_ventas.ingresar_detalle_ventas(self.nro_venta,producto[0],producto[1],producto[2])

                    # Descuento de stock de productos
                    for producto in self.lista_carrito:
                        ModeloProducto.descontar_producto(producto[0],producto[2])

                    # Registro de la deuda en Cuenta Corriente
                    # Se debe obtener el último nro_operación de la tabla de CuentaCorriente para el cliente al cual se le realizó la venta
                    # Si no se encuentran resultados, el ultimo numero de operacion será 1
                    resultado_ultimo_nro_operacion = ModeloCuentaCorriente.ultimo_nro_operacion(self.cliente_venta)
                    if resultado_ultimo_nro_operacion and resultado_ultimo_nro_operacion[0][0] is not None:
                        ultimo_nro_operacion = int(resultado_ultimo_nro_operacion[0][0])
                    else:
                        ultimo_nro_operacion = 0

                    # Obtención del monto pendiente de esa determinada venta
                    monto_pendiente_venta = self.monto_total_venta - monto_abonado
                    # Se obtiene el último monto_pendiente de la tabla CuentaCorriente para dicho cliente. Si no se encuentran resultados entonces
                    # el ultimo monto_pendiente es 0
                    resultado_ultimo_monto_pendiente = ModeloCuentaCorriente.ultimo_monto_pendiente(self.cliente_venta)
                    if resultado_ultimo_monto_pendiente and resultado_ultimo_monto_pendiente[0][0] is not None:
                        ultimo_monto_pendiente = float(resultado_ultimo_monto_pendiente[0][0])
                    else:
                        ultimo_monto_pendiente = 0

                    # El monto_pendiente que se cargará sera ultimo_monto_pendiente + monto_pendiente_venta
                    monto_pendiente = ultimo_monto_pendiente + monto_pendiente_venta

                    ModeloCuentaCorriente.ingresar_pago_cc(ultimo_nro_operacion + 1,self.cliente_venta,'Adeuda',monto_abonado,monto_pendiente)

                    # Mensaje de confirmación
                    messagebox.showinfo('Ventas',f'La venta {self.nro_venta} se cargó a cuenta corriente')

                    # Cierre de ventana finalización de venta
                    self.toplevel_finalizacion_venta.destroy()

                    # Limpieza de campos
                    self.vista_ventas.entry_cliente.delete(0,'end')
                    self.vista_ventas.limpiar_treeview()

                    # Seteo de atributos
                    self.monto_total_venta = 0
                    self.vista_ventas.label_total_venta.config(text=f'Total Venta: ${self.monto_total_venta}')
                    self.lista_carrito = []
                    self.contador_carrito = 0

            # Consulta de generación de factura PDF
            consulta_generar_factura = messagebox.askyesno('Generar Factura','¿Desea generar la factura de la venta?') 
            if consulta_generar_factura:

                lista_detalle_venta = self.modelo_ventas.consultar_detalleventas(self.nro_venta)
                # Obtención de fecha venta
                fecha_venta = self.modelo_ventas.consultar_venta_nroventa(self.nro_venta)[0][0]
                # Obtención monto total venta
                monto_total = self.modelo_ventas.monto_total_venta(self.nro_venta)[0][0]

                # Generación de la factura
                self.generar_factura_pdf(self.cliente_venta,lista_detalle_venta,monto_total,self.nro_venta,fecha_venta,self.interes)   

        # Manejo de errores
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    # Función para eliminar una venta. Primero, para evitar excepciones en la base de datos se debe eliminar el nro_venta de la tabla
    # DetalleVentas y finalmente eliminarlo desde la tabla Ventas
    def eliminar_venta(self):
        # Recuperar elemento seleccionado del Treeview
        elemento_seleccionado = self.ventana_consulta_ventas.tv_consultaventas.selection()
        if elemento_seleccionado:
            # Verificar que solo se haya seleccionado un elemento
            if len(elemento_seleccionado)>1:
                messagebox.showerror('Error','Seleccionar de a un elemento')
                return

            # Recuperación del nro_venta
            nro_venta = self.ventana_consulta_ventas.tv_consultaventas.item(elemento_seleccionado,'text')

            # Eliminación. Primero se elimina del detalle y luego de la venta
            confirmacion = messagebox.askyesno('Eliminar Venta',f'¿Eliminar venta #{nro_venta}?')
            if confirmacion:
                self.modelo_ventas.eliminar_detalleventas(nro_venta)
                self.modelo_ventas.eliminar_venta(nro_venta)

                # Mensaje de confirmación
                messagebox.showinfo('Venta eliminada',f'La venta {nro_venta} ha sido eliminada!')
                self.boton_consultar_ventas()
        else:
            messagebox.showerror('Error','Seleccionar una venta')

    # Función para abrir ventana de detalle de ventas. Se verifica que haya un elemento seleccionado en Treeview consulta de ventas
    def boton_abrir_detalleventas(self):
        # Recuperar elemento seleccionado en Treeview
        elemento_seleccionado = self.ventana_consulta_ventas.tv_consultaventas.selection()
        # Apertura de la ventana de detalle ventas. Si se selecciona más de un elemento se muestra error
        if len(elemento_seleccionado) > 1:
            messagebox.showerror('Error','Se debe elegir solo una venta')
            return
        if elemento_seleccionado:
            self.nro_venta_consulta = self.ventana_consulta_ventas.tv_consultaventas.item(elemento_seleccionado,'text')
            self.abrir_ventana_detalleventas()

            # Visualización del detalle de venta en Treeview
            valores_detalle_ventas = self.modelo_ventas.consultar_detalleventas(self.nro_venta_consulta)
            for detalle in valores_detalle_ventas:
                self.ventana_detalle_ventas.tv_detalleventas.insert('','end',text=detalle[0],values=(detalle[1],detalle[2],detalle[3]))
        else:
            messagebox.showerror('Error','Se debe seleccionar un elemento')

    # Función para incluir en el boton "Imprimir Factura" de la ventana Detalle de ventas
    def detalleventas_imprimirpdf(self):
        # Recuperar elemento seleccionado en Treeview
        elemento_seleccionado = self.ventana_consulta_ventas.tv_consultaventas.selection()
        # Apertura de la ventana de detalle ventas. Si se selecciona más de un elemento se muestra error
        if len(elemento_seleccionado) > 1:
            messagebox.showerror('Error','Se debe elegir solo una venta')
            return
        if elemento_seleccionado:
            # Obtención numero factura
            nro_factura = self.ventana_consulta_ventas.tv_consultaventas.item(elemento_seleccionado,'text')
            # Obtención información de venta
            info_venta = self.modelo_ventas.consultar_venta_nroventa(nro_factura)
            fecha = info_venta[0][0]
            cliente = info_venta[0][1]
            monto_total = info_venta[0][2]
            interes = info_venta[0][3]
            # Obtención lista de productos de la venta
            productos = self.modelo_ventas.consultar_detalleventas(nro_factura)

            # Imprimir factura
            consulta_imprimir_pdf = messagebox.askyesno('Imprimir Factura',f'Desea imprimir la factura')
            if consulta_imprimir_pdf:
                self.generar_factura_pdf(cliente,productos,monto_total,nro_factura,fecha,interes) 
    
    # Función para introducir pagos 'Pendiente' en el Treeview de Consulta de Ventas. En caso de que no haya pagos pendientes, se muestra mensaje
    def boton_pagos_pendientes(self):
        # Obtención de pagos pendientes
        pagos_pendientes = self.modelo_ventas.pagos_pendientes()
        # Limpieza de Treeview antes de insertar datos
        self.ventana_consulta_ventas.limpiar_treeview()
        # Carga de datos a Treeview, si no hay, muestra mensaje
        if pagos_pendientes:
            for pago in pagos_pendientes:
                self.ventana_consulta_ventas.tv_consultaventas.insert('','end',text=pago[0],values=(pago[1],pago[2],pago[3],pago[4],pago[5]))
        else:
            messagebox.showinfo('Pagos Pendientes','No se encontraron pagos pendientes!')

    # Función para agregar interes de venta
    def boton_agregar_interes(self):
        try:

            interes = float(self.ventana_interes_venta.entry_interes.get())
            if interes > 0:
                # Actualización del interés y del monto total de venta
                self.interes = interes
                self.monto_total_venta += interes
                # Actualización del label total_venta
                self.ventana_finalizacion_venta.label_total_venta.config(text=f'Total Venta: ${self.monto_total_venta}')

            # Cierre de ventana
            self.toplevel_interes_venta.destroy()
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')
    ###############################################################################################################################################
    ###################################################### GENERACIÓN DE FACTURAS #################################################################
    # Función para que no haya problemas con la ruta a imagenes
    def rutas(self, *paths):
        if getattr(sys, 'frozen', False):  # Ejecutable generado con PyInstaller
            ruta_base = sys._MEIPASS
        else:  # Ejecución normal en el entorno de desarrollo
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    # Función para generar facturas en PDF
    def generar_factura_pdf(self,cliente,productos,total,nro_factura,fecha,interes):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_facturas = os.path.join(base_dir,"Facturas")
        if not os.path.exists(ruta_facturas):
            os.makedirs(ruta_facturas)
            
        # Se crea una variable que contendrá la ruta y nombre del archivo
        nombre_archivo = f'factura_{nro_factura}_{cliente}.pdf'
        archivo_pdf = os.path.join(ruta_facturas,nombre_archivo)

        # Creación del canvas
        c = canvas.Canvas(archivo_pdf,pagesize=letter)
        # Asignación de ancho y alto de la pagina como tamaño letter
        width,height = letter

        # Estilos
        styles = getSampleStyleSheet()
        estilo_titulo = styles['Title']
        estilo_normal = styles['Normal']

        # Introducción del logo de la empresa en esquina superior
        ruta = self.rutas('imagenes','logo_sin_fondo.png')
        ruta_logo = ruta
        ancho_logo = 200
        alto_logo = 200
        c.drawImage(ruta_logo,width/2-ancho_logo/2,height-alto_logo,width=ancho_logo,height=alto_logo)

        # Información del emprendimiento
        c.setFont("Helvetica-Bold",20)
        c.drawString(50,height-200,'BLA Estética')

        c.setFont("Helvetica",12)
        c.drawString(50,height-220,'Dirección: Hipolito Yrigoyen 561')

        c.setFont("Helvetica",12)
        c.drawString(50,height-240,'Teléfono: 353-4230926')

        c.setFont("Helvetica",12)
        c.drawString(50,height-260,'email: aichinobrenda@gmail.com')

        # Línea separadora
        c.line(50,height-280,width-50,height-280)

        # Información de la venta
        c.setFont("Helvetica-Bold",16)
        c.drawString(50,height-300,f'Venta número #{nro_factura}')

        c.setFont("Helvetica",12)
        c.drawString(50,height-320,f'Cliente: {cliente}')

        c.setFont("Helvetica",12)
        c.drawString(50,height-340,f'Fecha: {fecha}')

        # Tabla de productos
        c.setFont("Helvetica-Bold",15)
        c.drawString(50,height-380,'Detalle de la venta')

        data = [['Código','Producto','Precio Unit.','Cantidad']] + productos
            # Crear la tabla con estilo
        table = Table(data, colWidths=[100, 260, 100, 60])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Calcular la posición inicial de la tabla dinámicamente
        table_height = len(data) * 20  # Aproximadamente 20 puntos por fila
        y_position = height - 400 - table_height
        table.wrapOn(c, width, height)
        table.drawOn(c, 50, y_position)
        
        # Si hay interés, ya sea para cuando se imprime la factura en el momento de la venta o luego de realizada la venta, se muestra
        # dicho interes usando el valor guardado (self.interes) o consultando la base de datos para obtener el interés que se guardó en
        # el momento de realizar la venta (interes_registro).

        if interes > 0:
            c.setFont("Helvetica",14)
            c.drawString(50,height-570,f'Interés por pago en Débito/Crédito: ${interes:.1f}')
        
        # Total a pagar
        c.setFont("Helvetica-Bold",16)
        c.drawString(50,height-600,f'Total a pagar: ${total:.1f}')

        # Línea separadora
        c.line(50,height-630,width-50,height-630)

        # Mensaje
        c.setFont("Helvetica-Bold",14)
        c.drawString(220,height-650,'Gracias por tu compra :)')

        # Guardado de factura
        c.save()
        messagebox.showinfo('Factura generada',f'Factura #{nro_factura} creada correctamente')

        # Una vez guardada la factura, abrir automaticamente con os
        try:
            os.startfile(os.path.abspath(archivo_pdf))
        except Exception as error:
            messagebox.showerror('Error',f'No se pudo abrir el archivo PDF: {error}')