import sys
import os
from tkinter import messagebox, Toplevel
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from vista.view_ventas import VentanaVentas
from vista.view_ventas import ConsultaVentas
from vista.view_ventas import DetalleVentas
from vista.view_ventas import ConfirmacionVenta
from vista.view_ventas import InterfazInteres
from modelo.modelo_ventas import ModeloVentas
from modelo.modelo_producto import ModeloProducto
from modelo.modelo_ccorriente import ModeloCuentaCorriente

######################## CONTROLADOR DE VENTAS ###############################

''' En este fichero se lleva a cabo la vinculacion entre la vista y el modelo
    del modulo Ventas
'''

class ControladorVentas:

    def __init__(self,root):
        self.root = root
        self.vista_ventas = VentanaVentas(self.root)
        self.modelo_ventas = ModeloVentas()

        # Foco en entry codigo
        self.vista_ventas.entry_cliente.focus()

        # Configuracion apertura de ventanas
        self.vista_ventas.boton_consultaventas.config(
            command = self.abrir_ventana_consultaventas
        )
        self.vista_ventas.boton_finalizar_venta.config(
            command = self.abrir_abrir_ventana_finalizacionventa
        )
        self.vista_ventas.boton_buscar.config(
            command = self.boton_buscar_infoproducto
        )
        self.vista_ventas.boton_carrito.config(
            command = self.boton_agregar_carrito
        )
        self.vista_ventas.boton_eliminar_venta.config(
            command = self.eliminar_del_carrito
        )
        
        # Guardado descripcion de producto
        self.descripcion_producto = None

        # Guardado elemento seleccionado en treeview
        self.elemento_seleccionado = []

        # Guardado de "carrito" y seteo monto_total_venta = 0
        self.lista_carrito = []
        self.monto_total_venta = 0
        self.contador_carrito = 0
        
        # Guardado de cliente
        self.cliente_venta = None

        # Asignacion de eventos
        self.vista_ventas.entry_codigo_producto.bind(
            '<KeyRelease>',
            self.vencimientos_codigoingresado
        )
        self.vista_ventas.entry_cliente.bind(
            '<KeyRelease>',
            self.buscar_cliente_nuevaventa
        )

    ######################## INICIALIZACION DE VENTANAS ######################
    def abrir_ventana_consultaventas(self):
        # Creacion de ventana
        self.minimizar_root()
        self.toplevel_consulta_ventas = Toplevel(self.root)
        self.ventana_consulta_ventas = (
            ConsultaVentas(self.toplevel_consulta_ventas)
        )
        self.toplevel_consulta_ventas.grab_set()

        # Protocolo para cerrado de ventana
        self.toplevel_consulta_ventas.protocol(
            "WM_DELETE_WINDOW",
            self.volver_ventana_ventas
        )

        # Evento filtrado de clientes
        self.ventana_consulta_ventas.entry_cliente.bind(
            "<KeyRelease>",
            self.buscar_cliente_consultaventa
        )

        # Configuracion de botones
        self.ventana_consulta_ventas.boton_buscar.config(
            command = self.boton_consultar_ventas
        )
        self.ventana_consulta_ventas.boton_eliminar.config(
            command = self.eliminar_venta
        )
        self.ventana_consulta_ventas.boton_detalle.configure(
            command = self.boton_abrir_detalleventas
        )
        self.ventana_consulta_ventas.boton_pendientes.config(
            command = self.boton_pagos_pendientes
        )
        
        # Guardado numero de venta
        self.nro_venta_consulta = None

    
    def abrir_ventana_detalleventas(self):
        # Creacion de ventana
        self.toplevel_detalle_ventas = Toplevel(self.toplevel_consulta_ventas)
        self.ventana_detalle_ventas = (
            DetalleVentas(self.toplevel_detalle_ventas)
        )
        self.toplevel_detalle_ventas.grab_set()

        # Configuracion label nro_venta
        self.ventana_detalle_ventas.label_nroventa.config(
            text=f'Venta #{self.nro_venta_consulta}'
        )

        # Configuracion de botones
        self.ventana_detalle_ventas.boton_pdf.config(
            command = self.detalleventas_imprimirpdf
        )

    
    def abrir_ventana_interesventa(self):
        # Verificacion que se elige medio de pago Debito/Credito
        modo_pago = self.ventana_finalizacion_venta.seleccion_radiobutton()
        if modo_pago != 3:
            messagebox.showerror(
                'Error',
                'Modo permitido solo para pagos en Débito/Crédito')	
            return

        # Creacion de ventana
        self.toplevel_interes_venta = Toplevel(self.root)
        self.ventana_interes_venta = (
            InterfazInteres(self.toplevel_interes_venta)
        )
        self.toplevel_interes_venta.grab_set()

        # Configuracion de botones
        self.ventana_interes_venta.boton_interes.config(
            command = self.boton_agregar_interes
        )

    
    def abrir_ventana_finalizacionventa(self):
        # Creacion de ventana
        self.toplevel_finalizacion_venta = Toplevel(self.root)
        self.ventana_finalizacion_venta = (
            ConfirmacionVenta(self.toplevel_finalizacion_venta)
        )
        self.toplevel_finalizacion_venta.grab_set()

        # Obtencion del número de venta
        self.nro_venta = self.modelo_ventas.ultimo_nro_venta()
        if self.nro_venta[0][0] is None:
            self.nro_venta = 1
        else:
            self.nro_venta = self.modelo_ventas.ultimo_nro_venta()[0][0] + 1

        # Seteo interes en 0
        self.interes = 0

        # Modificacion del label nro_venta
        self.ventana_finalizacion_venta.label_numero_venta.config(
            text = f'Venta #{self.nro_venta}'
        )
        
        # Inicializacion con el monto_total_venta y nro_venta
        self.ventana_finalizacion_venta.label_total_venta.config(
            text=f'Total Venta: ${self.monto_total_venta}'
        )
        
        # Configuracion de botones
        self.ventana_finalizacion_venta.boton_confirmar.config(
            command = self.boton_confirmar_venta
        )
        self.ventana_finalizacion_venta.boton_interes.config(
            command = self.abrir_ventana_interesventa
        )
        
    
    def minimizar_root(self):
        # Metodo para minimizar el root
        self.root.iconify()
    

    def volver_ventana_ventas(self):
        
        ''' Metodo para cerrar consulta de ventas y volver a abrir
            ventana principal de ventas
        '''
        
        self.toplevel_consulta_ventas.destroy()
        self.root.deiconify()

    ################################## EVENTOS ###############################
    def buscar_cliente_nuevaventa(self,event):
        
        ''' Metodo asociado a evento para rellenar el ComboBox de clientes a
            la hora de realizar una nueva venta. Apareceran los clientes de
            acuerdo a lo que vaya escribiendo el usuario dentro del ComboBox
        '''
        
        # Obtencion de clientes que realizaron compras
        clientes = self.modelo_ventas.clientes()
        
        # Obtencion valor de campo cliente
        entrada_cliente = self.vista_ventas.entry_cliente.get().lower()

        # Verificacion de que existen clientes que coincidan
        if clientes:
            lista_clientes = [
                cliente[0] for cliente in clientes
                if cliente[0].lower().startswith(entrada_cliente)
            ]

            if lista_clientes:
                # Asignacion de coincidencias a ComboBox
                self.vista_ventas.entry_cliente['values'] = lista_clientes
                
            else:
                # Caso contrario, se introduce una lista vacia al ComboBox
                self.vista_ventas.entry_cliente['values'] = []
        else:
            self.vista_ventas.entry_cliente['values'] = []

    
    def buscar_cliente_consultaventa(self, event):

        ''' Metodo asociado a evento para filtrar los clientes e introducirlos
            en ComboBox en ventana consulta de ventas
        '''
        clientes = ModeloVentas.clientes()
        entrada_cliente = (
            self.ventana_consulta_ventas.entry_cliente.get().lower()
        )

        # Verificacion de coincidencias
        if clientes:
            lista_clientes = [
                cliente[0] for cliente in clientes if
                cliente[0].lower().startswith(entrada_cliente)
            ]

            if lista_clientes:
                # Llenado de ComboBox con coincidencias
                self.ventana_consulta_ventas.entry_cliente['values'] = (
                    lista_clientes
                )
            
            else:
                # Se introduce lista vacia en ComboBox
                self.ventana_consulta_ventas.entry_cliente['values'] = []
        else:
            self.ventana_consulta_ventas.entry_cliente['values'] = []

    
    def vencimientos_codigoingresado(self, event):

        ''' Metodo asociado a evento para introducir automaticamente los
            vencimientos correspondientes al codigo ingresado en Entry
            de codigo.
            Primero se obtiene la entrada de usuario en campo de codigo,
            luego se obtienen todos los vencimientos correspondientes a
            ese codigo, y si existen, se introducen en ComboBox de
            vencimientos
        '''
        
        # Obtencion del codigo ingresado
        codigo = self.vista_ventas.entry_codigo_producto.get()

        # Obtencion de los vencimientos según el codigo ingresado
        vencimientos = ModeloProducto.vencimiento_producto_a_vender(codigo)
        
        if vencimientos:
            # Generacion de lista para introducir a ComboBox
            vencimientos_str = [
                v[0].strftime('%d-%m-%Y') for v in vencimientos
            ]
            
            # Introduccion de elementos al ComboBox
            self.vista_ventas.entry_vencimiento['values'] = vencimientos_str
            self.vista_ventas.entry_vencimiento.current(0)
        
        else:
            # Si no se encuentran vencimientos se introduce lista vacia
            self.vista_ventas.entry_vencimiento['values'] = []
            self.vista_ventas.entry_vencimiento.set('')    

    ######################### ACCIONES DE BOTONES ############################
    def abrir_abrir_ventana_finalizacionventa(self):
        
        ''' Metodo para la apertura de la ventana de finalizacion de venta, la
            cual solo se abrira si existen productos dentro del carrito, caso
            contrario se mostrara messagebox
        '''
        
        # Verificacion de cliente
        if self.cliente_venta == '':
            messagebox.showerror('Error','Introducir Cliente')
            return
        
        if not self.lista_carrito:
            messagebox.showerror('Error','No hay productos en el carrito')
        else:
            # Apertura de ventana
            self.abrir_ventana_finalizacionventa()

    
    def boton_buscar_infoproducto(self):

        ''' Metodo para actualizar la informacion del producto en los label
            luego de la eleccion de un codigo y vencimiento a la hora de
            realizar una nueva venta.
            Primero se limpian los campos, luego se obtiene la informacion
            del producto dependiendo del codigo y vencimiento ingresados.
            Finalmente, se inserta esa informacion en los Labels.
        '''
        
        # Limpieza de campos
        self.vista_ventas.entry_precio.delete(0,'end')
        self.vista_ventas.label_en_stock.config(text='En Stock: ')
        self.vista_ventas.label_descripcion_producto.config(text='Producto: ')
        
        try:
            # Obtencion del codigo y vencimiento
            codigo = self.vista_ventas.entry_codigo_producto.get()
            vencimiento = self.vista_ventas.entry_vencimiento.get()
            
            if codigo == '' or vencimiento == '':
                messagebox.showerror('Error','Debes ingresar un código')
                return
            
            # Obtencion de la informacion del producto
            info_producto = ModeloProducto.informacion_producto(
                codigo,
                vencimiento
            )

            if info_producto:
                # Carga de informacion en labels
                self.descripcion_producto = info_producto[0][2]
                self.vista_ventas.entry_precio.insert(0,info_producto[0][3])
                self.vista_ventas.label_en_stock.config(
                    text = f'En Stock: {info_producto[0][4]}'
                )
                self.vista_ventas.label_descripcion_producto.config(
                    text = f'Producto: {self.descripcion_producto}'
                )

            else:
                messagebox.showinfo(
                    'Producto no encontrado',
                    'No se ha encontrado este producto!'
                )

        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Ha sucedido un error inesperado - {error}'
            )

    
    def boton_agregar_carrito(self):

        ''' Metodo para recuperar valores de entrada de usuarios y agregarlos
            al Treeview (Carrito) y a una lista que luego se utilizara para
            cargar la informacion en la base de datos.
            Primero se recuperan las entradas de usuario, se realizan las
            verificaciones correspondientes y se cargan los productos tanto
            en Treeview como en la lista.
        '''
        
        try:
            # Obtencion de entradas de usuario
            codigo = self.vista_ventas.entry_codigo_producto.get()
            descripcion = self.descripcion_producto
            precio = float(self.vista_ventas.entry_precio.get())
            cantidad = int(self.vista_ventas.entry_cantidad.get())
            vencimiento = self.vista_ventas.entry_vencimiento.get()
            cliente = self.vista_ventas.entry_cliente.get()

            # Verificacion de campos completados
            if codigo == '' or precio == '' or cantidad == '':
                messagebox.showerror(
                    'Error',
                    'Se deben completar todos los campos'
                )
                return
            
            # Verificacion cantidad ingresada <= stock disponible
            info_producto = ModeloProducto.informacion_producto(
                codigo,
                vencimiento
            )
            stock_disponible = info_producto[0][4]
            if cantidad > stock_disponible:
                messagebox.showerror(
                    'Error',
                    'La cantidad ingresada es mayor al stock disponible'
                )
                return
            
            # Seteo contador de carrito
            self.contador_carrito += 1
            
            # Se incrementa el monto_total_venta en (cantidad * precio)
            self.monto_total_venta += precio * cantidad

            # Introduccion de valores en Treeview
            self.vista_ventas.tv_ventas.insert(
                '',
                'end',
                text = self.contador_carrito,
                values = (codigo,descripcion,precio,cantidad)
            )

            # Actualizacion del monto_total_venta
            self.vista_ventas.label_total_venta.config(
                text = f'Total de la venta: ${self.monto_total_venta}'
            )

            # Insercion de elementos en lista
            nro_producto = ModeloProducto.obtener_nroproducto(
                codigo,
                vencimiento
            )
            self.lista_carrito.append((nro_producto[0][0],precio,cantidad))

            # Limpieza de entries
            self.vista_ventas.limpiar_cajas()
            self.vista_ventas.label_descripcion_producto.config(
                text = 'Producto: '
            )
            self.vista_ventas.label_en_stock.config(text='En Stock: ')

            # Seteo de cliente para que quede guardado en la instancia
            self.cliente_venta = cliente

            # Se hace foco en entry codigo_producto
            self.vista_ventas.entry_codigo_producto.focus()

        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos!')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    
    def eliminar_del_carrito(self):

        ''' Metodo para eliminar producto del carrito tanto del Treeview
            como de la lista, actualizando tambien el label de monto
            total de venta.
        '''
        
        # Obtener elemento seleccionado del treeview
        self.elemento_seleccionado = self.vista_ventas.tv_ventas.selection()

        # Verificacion de seleccion de elementos
        if not self.elemento_seleccionado:
            messagebox.showerror('Error','Debes seleccionar un producto')
            return
        if len(self.elemento_seleccionado) > 1:
            messagebox.showerror('Error','Seleccionar de a un elemento')
            return
        
        # Obtener precio y cantidad para actualizar Label
        valores_elemento_seleccionado = self.vista_ventas.tv_ventas.item(
            self.elemento_seleccionado,
            'values'
        )
        precio = float(valores_elemento_seleccionado[2])
        cantidad = int(valores_elemento_seleccionado[3])
        numero_carrito = self.vista_ventas.tv_ventas.item(
            self.elemento_seleccionado,
            'text'
        )

        # Actualizacion monto_venta_total
        self.monto_total_venta -= precio * cantidad
        self.vista_ventas.label_total_venta.config(
            text = f'Total de la venta: ${self.monto_total_venta}'
        )

        # Eliminacion de la fila correspondiente en el Treeview
        self.vista_ventas.tv_ventas.delete(self.elemento_seleccionado)

        # Eliminacion del elemento de la lista "carrito"
        del self.lista_carrito[numero_carrito - 1]

        # Actualizacion numeros de carrito
        for contador in self.vista_ventas.tv_ventas.get_children():
            nro_carrito = self.vista_ventas.tv_ventas.item(contador,'text')
            if nro_carrito > numero_carrito:
                # Se resta 1 a los que estan por delante, otros se mantienen
                self.vista_ventas.tv_ventas.item(contador, text=nro_carrito-1)
        
        # Seteo contador para que siempre arranque desde el ultimo ingresado
        children_carritos = self.vista_ventas.tv_ventas.get_children()
        lista_nros_carritos = [
            self.vista_ventas.tv_ventas.item(child,'text') 
            for child in children_carritos
        ]
        
        if not lista_nros_carritos:
            self.contador_carrito = 0
        else:
            self.contador_carrito = lista_nros_carritos[-1]

        # Mensaje de eliminacion de producto
        messagebox.showinfo(
            'Eliminado',
            f'{valores_elemento_seleccionado[1]} eliminado del carrito!'
        )

    
    def boton_consultar_ventas(self):

        ''' Metodo para filtrar las ventas en ventana de consulta de ventas,
            el cual se puede filtrar entre dos fechas o por un determinado
            cliente.
            Primero se recuperan las entradas de usuario y se llama al
            metodo para filtrar las ventas. Si no se encuentran
            ventas para los filtros aplicados, entonces no se muestra
            nada en el Treeview
        '''
        
        # Recuperacion entradas de usuario
        cliente = self.ventana_consulta_ventas.entry_cliente.get()
        fecha_desde = self.ventana_consulta_ventas.entry_desde.get()
        fecha_hasta = self.ventana_consulta_ventas.entry_hasta.get()
        
        cliente = None if cliente == '' else cliente

        # Obtencion de ventas filtradas
        ventas_filtradas = ModeloVentas.consultar_ventas(
            fecha_desde,
            fecha_hasta,
            cliente
        )

        # Llenado de treeview con ventas filtradas
        if ventas_filtradas:
            # Se limpia Treeview antes de insertar datos
            self.ventana_consulta_ventas.limpiar_treeview()
            for venta in ventas_filtradas:
                self.ventana_consulta_ventas.tv_consultaventas.insert(
                    '',
                    'end',
                    text = venta[0],
                    values = (venta[1],venta[2],venta[3],venta[4],venta[5])
                )
                
        # Si no se encuentran registros, se muestra messagebox
        else:
            messagebox.showinfo(
                'Sin coincidencias',
                'No se encontraron ventas!'
            )
            self.ventana_consulta_ventas.limpiar_treeview()

    
    def boton_confirmar_venta(self):

        ''' Metodo para finalizar una determinada venta. Primero se obtienen
            las entradas de usuario de monto abonado y modo de pago, luego
            se verifica si el monto abonado es igual al monto de la venta.
            En caso que el monto abonado sea mayor no se dejara finalizar
            la venta, si el monto es igual se cargara la venta unicamente
            en tabla Ventas y Detalle de ventas, por ultimo, si el monto es
            menor, se cargara tambien en la tabla de Cuenta Corriente.
            Ademas, se consultara en ambos casos si se desea imprimir la
            factura de la venta.
            En ambos casos de venta, se descontaran del stock aquellos
            productos que fueron vendidos.
        '''
        try:
            # Recuperacion entradas de usuario
            monto_abonado = (
                float(self.ventana_finalizacion_venta.entry_entrega.get())
            )
            modo_pago = (
                self.ventana_finalizacion_venta.seleccion_radiobutton()
            )

            # Verificacion de monto abonado
            if monto_abonado > self.monto_total_venta:
                messagebox.showerror('Error','El monto de venta es menor')
                return
            
            if monto_abonado == self.monto_total_venta:
                
                # Registro de venta en Ventas
                self.modelo_ventas.nueva_venta(
                    self.nro_venta,
                    self.cliente_venta,
                    self.monto_total_venta,
                    modo_pago,
                    'Pagado',
                    self.interes
                )
                # Registro en Detalle Ventas
                for producto in self.lista_carrito:
                    self.modelo_ventas.ingresar_detalle_ventas(
                        self.nro_venta,
                        producto[0],
                        producto[1],
                        producto[2]
                    )
                
                # Descuento de productos del stock
                for producto in self.lista_carrito:
                    ModeloProducto.descontar_producto(producto[0],producto[2])
                
                # Confirmacion de venta
                messagebox.showinfo(
                    'Ventas',
                    f'Venta {self.nro_venta} agregada correctamente!'
                )
                
                # Cierre de ventana finalizacion de venta
                self.toplevel_finalizacion_venta.destroy()

                # Limpieza de campos
                self.vista_ventas.entry_cliente.delete(0,'end')
                self.vista_ventas.limpiar_treeview()
                
                # Seteo de atributos
                self.monto_total_venta = 0
                self.vista_ventas.label_total_venta.config(
                    text=f'Total Venta: ${self.monto_total_venta}'
                )
                self.lista_carrito = []
                self.contador_carrito = 0

            # Caso monto abonado < monto de venta
            else:
                pregunta = messagebox.askyesno(
                    'Cuenta Corriente',
                    '¿Agregar venta a cuentas corrientes?'
                    )
                if pregunta:
                    # Registro de Venta con estado_venta = Pendiente
                    self.modelo_ventas.nueva_venta(
                        self.nro_venta,
                        self.cliente_venta,
                        self.monto_total_venta,
                        modo_pago,
                        'Pendiente',
                        self.interes
                    )

                    # Registro Detalle Ventas
                    for producto in self.lista_carrito:
                        self.modelo_ventas.ingresar_detalle_ventas(
                            self.nro_venta,
                            producto[0],
                            producto[1],
                            producto[2]
                        )

                    # Descuento de stock de productos
                    for producto in self.lista_carrito:
                        ModeloProducto.descontar_producto(
                            producto[0],
                            producto[2]
                        )

                    # Registro de la deuda en Cuenta Corriente
                    resultado_ultimo_nro_operacion = (
                        ModeloCuentaCorriente.ultimo_nro_operacion(
                            self.cliente_venta
                        )
                    )
                    
                    if (
                        resultado_ultimo_nro_operacion and
                        resultado_ultimo_nro_operacion[0][0] is not None
                    ):
                        ultimo_nro_operacion = (
                            int(resultado_ultimo_nro_operacion[0][0])
                        )
                        
                    else:
                        ultimo_nro_operacion = 0

                    # Obtencion del monto pendiente de esa determinada venta
                    monto_pendiente_venta = (
                        self.monto_total_venta - monto_abonado
                    )
                    
                    # Se obtiene el ultimo monto_pendiente de cliente
                    resultado_ultimo_monto_pendiente = (
                        ModeloCuentaCorriente.ultimo_monto_pendiente(
                            self.cliente_venta
                        )
                    )
                    
                    if (
                        resultado_ultimo_monto_pendiente and
                        resultado_ultimo_monto_pendiente[0][0] is not None
                    ):
                        ultimo_monto_pendiente = (
                            float(resultado_ultimo_monto_pendiente[0][0])
                        )
                        
                    else:
                        ultimo_monto_pendiente = 0

                    # Actualizacion de monto pendiente
                    monto_pendiente = ultimo_monto_pendiente + monto_pendiente_venta

                    # Insercion de pago en cuenta corriente
                    ModeloCuentaCorriente.ingresar_pago_cc(
                        ultimo_nro_operacion + 1,
                        self.cliente_venta,
                        'Adeuda',
                        monto_abonado,
                        monto_pendiente
                    )

                    # Mensaje de confirmacion
                    messagebox.showinfo(
                        'Ventas',
                        f'Venta {self.nro_venta} cargada a cuenta corriente')

                    # Cierre de ventana finalizacion de venta
                    self.toplevel_finalizacion_venta.destroy()

                    # Limpieza de campos
                    self.vista_ventas.entry_cliente.delete(0,'end')
                    self.vista_ventas.limpiar_treeview()

                    # Seteo de atributos
                    self.monto_total_venta = 0
                    self.vista_ventas.label_total_venta.config(
                        text=f'Total Venta: ${self.monto_total_venta}'
                    )
                    self.lista_carrito = []
                    self.contador_carrito = 0

            # Consulta de generacion de factura PDF
            consulta_generar_factura = messagebox.askyesno(
                'Generar Factura',
                '¿Desea generar la factura de la venta?'
            )
            
            if consulta_generar_factura:
                lista_detalle_venta = (
                    self.modelo_ventas.consultar_detalleventas(
                        self.nro_venta
                    )
                )
                
                # Obtencion de fecha venta
                fecha_venta = (
                    self.modelo_ventas.consultar_venta_nroventa(
                        self.nro_venta
                    )
                )
                
                # Obtencion monto total venta
                monto_total = (
                    self.modelo_ventas.monto_total_venta(
                        self.nro_venta
                    )
                )

                # Generacion de la factura
                self.generar_factura_pdf(
                    self.cliente_venta,
                    lista_detalle_venta,
                    monto_total[0][0],
                    self.nro_venta,
                    fecha_venta[0][0],
                    self.interes
                )   

        # Manejo de excepciones
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')

    
    def eliminar_venta(self):

        ''' Metodo para eliminar una venta existente en la base de datos.
            Para evitar excepciones primero se elimina el detalle de la
            venta y luego se elimina la venta.
            Tambien se consulta si se desea devolver a stock aquellos
            productos que se vendieron en dicha venta.
        '''
        
        # Recuperar elemento seleccionado del Treeview
        elemento_seleccionado = (
            self.ventana_consulta_ventas.tv_consultaventas.selection()
        )
        
        if elemento_seleccionado:
            # Verificar que solo se haya seleccionado un elemento
            if len(elemento_seleccionado) > 1:
                messagebox.showerror(
                    'Error',
                    'Seleccionar de a un elemento'
                )
                return

            # Recuperacion del nro_venta
            nro_venta = self.ventana_consulta_ventas.tv_consultaventas.item(
                elemento_seleccionado,
                'text'
            )

            # Obtencion de productos y cantidades vendidos
            productos_cantidades = (
                self.modelo_ventas.productos_vendidos(nro_venta)
            )
            
            # Eliminacion de venta
            confirmacion = messagebox.askyesno(
                'Eliminar Venta',
                f'¿Eliminar venta #{nro_venta}?'
            )
            if confirmacion:
                self.modelo_ventas.eliminar_detalleventas(nro_venta)
                self.modelo_ventas.eliminar_venta(nro_venta)

                # Consulta para devolver al stock los productos vendidos
                consulta_devolver_stock = messagebox.askyesno(
                    'Devolver Stock',
                    '¿Desea devolver al stock los productos vendidos?'
                )
                if consulta_devolver_stock:
                    for producto_cantidad in productos_cantidades:
                        ModeloProducto.devolver_producto_a_stock(
                            producto_cantidad[0],
                            producto_cantidad[1]
                        )
                    
                    messagebox.showinfo(
                        'Stock Devuelto',
                        'Stock devuelto correctamente!'
                    )

                # Mensaje de confirmacion
                messagebox.showinfo(
                    'Venta eliminada',
                    f'La venta {nro_venta} ha sido eliminada!'
                )
                self.boton_consultar_ventas()
        
        else:
            messagebox.showerror('Error','Seleccionar una venta')

    
    def boton_abrir_detalleventas(self):

        ''' Metodo para abrir ventana de detalle de ventas, verificando
            que se haya seleccionado un elemento en el treeview
        '''
        
        # Recuperar elemento seleccionado en Treeview
        elemento_seleccionado = (
            self.ventana_consulta_ventas.tv_consultaventas.selection()
        )
        
        # Verificacion seleccion de un elemento
        if len(elemento_seleccionado) > 1:
            messagebox.showerror('Error','Se debe elegir solo una venta')
            return
        if elemento_seleccionado:
            self.nro_venta_consulta = (
                self.ventana_consulta_ventas.tv_consultaventas.item(
                    elemento_seleccionado,
                    'text'
                )
            )
            
            # Apertura de ventana
            self.abrir_ventana_detalleventas()

            # Visualizacion del detalle de venta en Treeview
            valores_detalle_ventas = (
                self.modelo_ventas.consultar_detalleventas(
                    self.nro_venta_consulta
                )
            )

            # Llenado de treeview con detalle de venta seleccionada
            for detalle in valores_detalle_ventas:
                self.ventana_detalle_ventas.tv_detalleventas.insert(
                    '',
                    'end',
                    text = detalle[0],
                    values = (detalle[1],detalle[2],detalle[3])
                )
        
        else:
            messagebox.showerror('Error','Se debe seleccionar un elemento')

    
    def detalleventas_imprimirpdf(self):

        ''' Metodo para imprimir factura desde la ventana de detalle de
            ventas. Se recupera el elemento seleccionado en treeview,
            el cual se utiliza para obtener la informacion sobre esa
            determinada venta y utilizar esos parametros para la
            generacion de la factura pdf
        '''
        # Recuperar elemento seleccionado en Treeview
        elemento_seleccionado = (
            self.ventana_consulta_ventas.tv_consultaventas.selection()
        )
        
        if len(elemento_seleccionado) > 1:
            messagebox.showerror('Error','Se debe elegir solo una venta')
            return
            
        if elemento_seleccionado:
            # Obtención numero factura
            nro_factura = (
                self.ventana_consulta_ventas.tv_consultaventas.item(
                    elemento_seleccionado,
                    'text'
                )
            )
            
            # Obtencion informacion de venta
            info_venta = (
                self.modelo_ventas.consultar_venta_nroventa(nro_factura))
            fecha = info_venta[0][0]
            cliente = info_venta[0][1]
            monto_total = info_venta[0][2]
            interes = info_venta[0][3]
            
            # Obtencion lista de productos de la venta
            productos = (
                self.modelo_ventas.consultar_detalleventas(nro_factura))

            # Imprimir factura
            consulta_imprimir_pdf = messagebox.askyesno(
                'Imprimir Factura',
                f'Desea imprimir la factura?'
            )
            if consulta_imprimir_pdf:
                self.generar_factura_pdf(
                    cliente,
                    productos,
                    monto_total,
                    nro_factura,
                    fecha,interes
                ) 
    
    
    def boton_pagos_pendientes(self):

        ''' Metodo para introducir aquellas ventas con pago pendiente
            en el Treeview de la ventana consulta de ventas. En caso
            que no haya pagos pendientes, no se muestra nada.
        '''
        
        # Obtencion de pagos pendientes
        pagos_pendientes = self.modelo_ventas.pagos_pendientes()
        
        # Limpieza de Treeview antes de insertar datos
        self.ventana_consulta_ventas.limpiar_treeview()
        
        # Carga de datos a Treeview
        if pagos_pendientes:
            for pago in pagos_pendientes:
                self.ventana_consulta_ventas.tv_consultaventas.insert(
                    '',
                    'end',
                    text = pago[0],
                    values = (pago[1],pago[2],pago[3],pago[4],pago[5])
                )
        else:
            messagebox.showinfo(
                'Pagos Pendientes',
                'No se encontraron pagos pendientes!'
            )

    
    def boton_agregar_interes(self):

        ''' Metodo para introducir un interes en una determinada
            venta, cuando el metodo de pago elegido fue de Debito
            o Credito. Primero se recupera el valor del campo
            interes y luego se modifica el valor del atributo
            self.interes y tambien se ajusta el valor del
            monto total de venta
        '''
        
        try:
            interes = float(self.ventana_interes_venta.entry_interes.get())
            if interes > 0:
                # Actualizacion del interes y del monto total de venta
                self.interes = interes
                self.monto_total_venta += interes
                
                # Actualizacion del label total_venta
                self.ventana_finalizacion_venta.label_total_venta.config(
                    text = f'Total Venta: ${self.monto_total_venta}'
                )

            # Cierre de ventana
            self.toplevel_interes_venta.destroy()
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Error inesperado - {error}')
    
    
    ########################### GENERACION DE FACTURAS ######################
    def rutas(self, *paths):
        
        ''' Metodo para asignacion de rutas correctamente a la hora de
            realizar el ejecutable con PyInstaller
        '''
        
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(ruta_base, *paths)
    
    
    def generar_factura_pdf(
        self,
        cliente,
        productos,
        total,
        nro_factura,
        fecha,interes
    ):
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_facturas = os.path.join(base_dir,"Facturas")
        if not os.path.exists(ruta_facturas):
            os.makedirs(ruta_facturas)
            
        # Se crea una variable que contendra la ruta y nombre del archivo
        nombre_archivo = f'factura_{nro_factura}_{cliente}.pdf'
        archivo_pdf = os.path.join(ruta_facturas,nombre_archivo)

        # Creacion del canvas
        c = canvas.Canvas(archivo_pdf,pagesize=letter)
        
        # Asignacion de ancho y alto de la pagina como tamaño letter
        width,height = letter

        # Estilos
        styles = getSampleStyleSheet()
        estilo_titulo = styles['Title']
        estilo_normal = styles['Normal']

        # Introduccion del logo de la empresa en esquina superior
        ruta = self.rutas('../imagenes','logo_sin_fondo.png')
        ruta_logo = ruta
        ancho_logo = 200
        alto_logo = 200
        c.drawImage(
            ruta_logo,
            width/2-ancho_logo/2,
            height-alto_logo,
            width=ancho_logo,
            height=alto_logo
        )

        # Informacion del emprendimiento
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

        # Informacion de la venta
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

        # Calcular la posicion inicial de la tabla dinamicamente
        table_height = len(data) * 20  # Aproximadamente 20 puntos por fila
        y_position = height - 400 - table_height
        table.wrapOn(c, width, height)
        table.drawOn(c, 50, y_position)

        if interes > 0:
            c.setFont("Helvetica",14)
            c.drawString(
                50,
                height-570,
                f'Interés por pago en Débito/Crédito: ${interes:.1f}'
            )
        
        # Total a pagar
        c.setFont("Helvetica-Bold",16)
        c.drawString(50,height-600,f'Total a pagar: ${total:.1f}')

        # Linea separadora
        c.line(50,height-630,width-50,height-630)

        # Mensaje
        c.setFont("Helvetica-Bold",14)
        c.drawString(220,height-650,'Gracias por tu compra :)')

        # Guardado de factura
        c.save()
        messagebox.showinfo(
            'Factura generada',
            f'Factura #{nro_factura} creada correctamente'
        )

        # Una vez guardada la factura, abrir automaticamente con os
        try:
            os.startfile(os.path.abspath(archivo_pdf))
        except Exception as error:
            messagebox.showerror(
                'Error',
                f'No se pudo abrir el archivo PDF: {error}'
            )
            

