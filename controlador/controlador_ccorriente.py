from vista.view_ccorriente import CuentaCorriente,SaldarCuentaCorriente,ActualizarCuentaCorriente
from modelo.modelo_ccorriente import ModeloCuentaCorriente
from modelo.modelo_ventas import ModeloVentas
from tkinter import messagebox, Toplevel

################################################################################################################################################
################################################### CONTROLADOR DE CUENTA CORRIENTE ############################################################

# En este fichero se lleva a cabo la vinculación entre la vista y el modelo del modulo Cuenta Corriente

class ControladorCuentaCorriente:

    def __init__(self,root):
        self.root = root
        self.vista_ccorriente = CuentaCorriente(self.root)
        self.modelo_ccorriente = ModeloCuentaCorriente()

        # Inicialización de cliente = None
        self.cliente = None
        # Seteo de botones
        self.vista_ccorriente.boton_buscar.config(command=self.filtrar_cuenta_corriente)
        self.vista_ccorriente.boton_agregarpago.config(command=self.abrir_ventana_saldar_cc)
        self.vista_ccorriente.boton_actualizarpago.config(command=self.abrir_ventana_actualizar_cc)
        self.vista_ccorriente.boton_borraroperacion.config(command=self.eliminar_ultima_operacion)

        # Inicialización de ComboBox con clientes que tienen cuentas corrientes abiertas
        self.vista_ccorriente.entry_cliente['values'] = self.clientes_cuentacorriente()

    ###############################################################################################################################################
    #################################################### INICIALIZACIÓN DE VENTANAS ###############################################################

    def abrir_ventana_saldar_cc(self):
        # Si no se elige un cliente, entonces no permitirá abrir la ventana de saldar cuenta corriente
        if self.cliente == None:
            messagebox.showerror('Cuenta Corriente','Debes elegir un cliente')
            return
    
        self.toplevel_saldocc = Toplevel(self.root)
        self.ventana_saldocc = SaldarCuentaCorriente(self.toplevel_saldocc)
        self.toplevel_saldocc.grab_set()
        self.ventana_saldocc.entry_nuevopago.focus()
        self.ventana_saldocc.boton_nuevopago.config(command=self.saldar_cuenta_corriente)

    
    def abrir_ventana_actualizar_cc(self):
        # Si no se elige un cliente, entonces no permitirá abrir la ventana de actualizar cuenta corriente
        if self.cliente == None:
            messagebox.showerror('Cuenta Corriente','Debes elegir un cliente')
            return
        
        self.toplevel_actualizarcc = Toplevel(self.root)
        self.ventana_actualizarcc = ActualizarCuentaCorriente(self.toplevel_actualizarcc)
        self.toplevel_actualizarcc.grab_set()
        self.ventana_actualizarcc.entry_actualizacion.focus()
        self.ventana_actualizarcc.boton_actualizacion.config(command=self.actualizar_cuenta_corriente)

    ###############################################################################################################################################
    ############################################################# EVENTOS #########################################################################
    
    # Función para introducir clientes con cuentas corrientes en ComboBox
    def clientes_cuentacorriente(self):
        # Clientes con cuentas corrientes:
        clientes_cc = self.modelo_ccorriente.clientes_cuentacorriente()

        if clientes_cc:
            lista_clientes_cc = [cliente[0] for cliente in clientes_cc]
            
        else:
            lista_clientes_cc = []
        
        return lista_clientes_cc

    ###############################################################################################################################################
    ####################################################### ACCIONES DE BOTONES ###################################################################

    # Función para filtrar cuentas corrientes por cliente, luego se insertan los resultados en Treeview
    def filtrar_cuenta_corriente(self):
        # Obtención de entradas de usuario
        try:
            self.cliente = self.vista_ccorriente.entry_cliente.get()

            if self.cliente == '':
                messagebox.showerror('Error','Introducir nombre de cliente')
                return

            # Información de la cuenta corriente de acuerdo al cliente ingresado
            informacion_cc = self.modelo_ccorriente.ver_cuentascorrientes(self.cliente)

            # Limpieza de Treeview
            self.vista_ccorriente.limpiar_treeview()
            
            # Verificación cuenta corriente, si existen entonces se introducen en el Treeview, caso contrario se muestra messagebox
            if informacion_cc:
                for cuentacorriente in informacion_cc:
                    self.vista_ccorriente.tv_cc.insert('','end',text=cuentacorriente[0],values=(cuentacorriente[2],cuentacorriente[3],cuentacorriente[4],cuentacorriente[5]))

                # Se recorren elementos insertados en el Treeview y se pintan en rojo los que tengan un tipo_operacion = 'Adeuda'
                # y en azul cuando se introduce una actualización de cuenta corriente (tipo_operacion = 'Actualizacion')
                self.vista_ccorriente.tv_cc.tag_configure('Rojo',foreground='red',font=('century gothic',10,'bold'))
                self.vista_ccorriente.tv_cc.tag_configure('Azul',foreground='blue',font=('century gothic',10,'bold'))
                self.vista_ccorriente.tv_cc.tag_configure('Verde',foreground='green',font=('century gothic',10,'bold'))

                for item in self.vista_ccorriente.tv_cc.get_children():
                    valores = self.vista_ccorriente.tv_cc.item(item,'values')
                    if valores[1] == 'Adeuda':
                        self.vista_ccorriente.tv_cc.item(item,tags=('Rojo',))
                    elif valores[1] == 'Actualizacion':
                        self.vista_ccorriente.tv_cc.item(item,tags=('Azul',))
                    elif valores[1] == 'Paga':
                        self.vista_ccorriente.tv_cc.item(item,tags=('Verde',))

                # Obtención del monto adeudado total del cliente
                monto_adeudado_total = self.modelo_ccorriente.ultimo_monto_pendiente(self.cliente)
                self.vista_ccorriente.label_deudatotal.config(text=f'Deuda Total: $ {monto_adeudado_total[0][0]}')

            else:
                messagebox.showinfo('Cuenta Corriente','No se encontraron resultados')
        
        except ValueError:
            messagebox.showerror('Error','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Ha ocurrido un error inesperado - {error}')

    # Función para saldar deuda de cuenta corriente, en función de la deuda, se ingresa un monto a pagar. Si se salda completamente entonces se 
    # consulta si se elimina la venta de cuenta corriente y se actualiza en la tabla de Ventas como 'Pagado'
    def saldar_cuenta_corriente(self):
        try:
            # Recuperación de monto_abonado 
            monto_abonado = float(self.ventana_saldocc.entry_nuevopago.get())

            # Obtención del último número de operación
            resultado_ultimo_nro_operacion = self.modelo_ccorriente.ultimo_nro_operacion(self.cliente)
            if resultado_ultimo_nro_operacion and resultado_ultimo_nro_operacion[0][0] is not None:
                ultimo_nro_operacion = int(resultado_ultimo_nro_operacion[0][0])
            else:
                ultimo_nro_operacion = 0

            # Obtención del ultimo monto pendiente
            resultado_ultimo_montopendiente = self.modelo_ccorriente.ultimo_monto_pendiente(self.cliente)
            if resultado_ultimo_montopendiente and resultado_ultimo_montopendiente[0][0] is not None:
                ultimo_montopendiente = float(resultado_ultimo_montopendiente[0][0])
            else:
                ultimo_montopendiente = 0
            
            # El nuevo monto_pendiente será el último monto pendiente  - monto_abonado
            monto_pendiente = ultimo_montopendiente - monto_abonado

            # Si la cuenta_corriente se salda por completo, entonces se elimina:
            if monto_pendiente <= 0:
                self.modelo_ccorriente.eliminar_cuentacorriente(self.cliente)
                self.toplevel_saldocc.destroy()
                messagebox.showinfo('Cuenta Corriente',f'{self.cliente} ha saldado completamente su deuda!')
                # Se actualiza el estado de las ventas pendientes a 'Pagado'
                ModeloVentas.actualizacion_estadoventa(self.cliente)
                self.vista_ccorriente.limpiar_treeview()
                self.filtrar_cuenta_corriente()
                self.vista_ccorriente.entry_cliente.delete(0,'end')
                self.vista_ccorriente.label_deudatotal.config(text='Deuda Total: $')
                self.cliente = None
                self.vista_ccorriente.entry_cliente['values'] = self.clientes_cuentacorriente()

            else:

                # Ingreso del monto_abonado en la cuenta corriente (se insertará como 'Paga')
                self.modelo_ccorriente.ingresar_pago_cc(ultimo_nro_operacion + 1,self.cliente,'Paga',monto_abonado,monto_pendiente)

                # Mensaje de confirmación de pago y actualización de Treeview
                self.toplevel_saldocc.destroy()
                messagebox.showinfo('Cuenta Corriente','Pago agregado correctamente')
                self.vista_ccorriente.limpiar_treeview()
                self.filtrar_cuenta_corriente()

        except ValueError:
            messagebox.showerror('Error','Error en ingreso de datos')
        except Exception as error:
            messagebox.showerror('Error',f'Ocurrio un error inesperado - {error}')


    # Función para actualizar la cuenta corriente. Se solicitará un monto el cuál se sumará al monto_pendiente anterior para actualizar la cuenta
    # corriente en aquellos casos donde el usuario lo requiera. Se ingresará un registro cuyo tipo_operacion será 'Actualización'
    def actualizar_cuenta_corriente(self):
        try:
            # Recuperación del monto
            monto_actualizacion = float(self.ventana_actualizarcc.entry_actualizacion.get())

            # Recuperación último nro_operacion
            resultado_ultimo_nrooperacion = self.modelo_ccorriente.ultimo_nro_operacion(self.cliente)
            if resultado_ultimo_nrooperacion and resultado_ultimo_nrooperacion[0][0] is not None:
                ultimo_nro_operacion = int(resultado_ultimo_nrooperacion[0][0])
            else:
                ultimo_nro_operacion = 0

            # Recuperación último monto_pendiente
            resultado_ultimo_montopendiente = self.modelo_ccorriente.ultimo_monto_pendiente(self.cliente)
            if resultado_ultimo_montopendiente and resultado_ultimo_montopendiente[0][0] is not None:
                ultimo_montopendiente = float(resultado_ultimo_montopendiente[0][0])
            else:
                ultimo_montopendiente = 0
            
            # El nuevo monto_pendiente será igual al monto_pendiente anterior + monto_actualizacion
            monto_pendiente = ultimo_montopendiente + monto_actualizacion

            # Ingreso de registro a base de datos
            self.modelo_ccorriente.ingresar_pago_cc(ultimo_nro_operacion + 1,self.cliente,'Actualizacion',monto_actualizacion,monto_pendiente)
            
            # Mensaje de confirmación y actualización de Treeview
            self.toplevel_actualizarcc.destroy()
            messagebox.showinfo('Cuenta Corriente','Deuda actualizada!')
            self.vista_ccorriente.limpiar_treeview()
            self.filtrar_cuenta_corriente()
        
        except ValueError:
            messagebox.showerror('Cuenta Corriente','Error en el ingreso de datos')
        except Exception as error:
            messagebox.showerror('Cuenta Corriente',f'Error inesperado - {error}')


    def eliminar_ultima_operacion(self):
        # Verificación de que se ha elegido un cliente
        if self.cliente == None:
            messagebox.showerror('Cuenta Corriente','Debes elegir un cliente')
            return

        # Obtención último nro_operación
        resultado_ultimo_nrooperacion = self.modelo_ccorriente.ultimo_nro_operacion(self.cliente)
        if resultado_ultimo_nrooperacion:
            ultimo_nrooperacion = resultado_ultimo_nrooperacion[0][0]
        
        # Eliminación de la última operación. Primero se consultará si se desea eliminar
        confirmacion = messagebox.askyesno('Cuenta Corriente',f'Desea eliminar la última operación hecha para {self.cliente}?')
        if confirmacion:
            self.modelo_ccorriente.eliminar_ultima_operacion(ultimo_nrooperacion,self.cliente)
            messagebox.showinfo('Cuenta Corriente','Operación eliminada correctamente')
            self.vista_ccorriente.limpiar_treeview()
            self.filtrar_cuenta_corriente()
