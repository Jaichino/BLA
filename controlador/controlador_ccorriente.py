from tkinter import messagebox, Toplevel
from vista.view_ccorriente import CuentaCorriente
from vista.view_ccorriente import SaldarCuentaCorriente
from vista.view_ccorriente import ActualizarCuentaCorriente
from modelo.modelo_ccorriente import ModeloCuentaCorriente
from modelo.modelo_ventas import ModeloVentas

###################### CONTROLADOR DE CUENTA CORRIENTE ######################

''' En este fichero se lleva a cabo la vinculacion entre la vista y el modelo 
    del modulo Cuenta Corriente
'''
class ControladorCuentaCorriente:

    def __init__(self,root):

        self.root = root
        self.vista_ccorriente = CuentaCorriente(self.root)
        self.modelo_ccorriente = ModeloCuentaCorriente()

        # Inicializacion de cliente = None
        self.cliente = None

        # Seteo de botones
        self.vista_ccorriente.boton_buscar.config(
            command =   self.filtrar_cuenta_corriente
        )

        self.vista_ccorriente.boton_agregarpago.config(
            command =   self.abrir_ventana_saldar_cc
        )
        
        self.vista_ccorriente.boton_actualizarpago.config(
            command =   self.abrir_ventana_actualizar_cc
        )
        
        self.vista_ccorriente.boton_borraroperacion.config(
            command =   self.eliminar_ultima_operacion
        )

        # Inicializacion de ComboBox con clientes cuenta corriente
        self.vista_ccorriente.entry_cliente['values'] = (
            self.clientes_cuentacorriente()
        )

    
    ######################## INICIALIZACIoN DE VENTANAS #####################

    def abrir_ventana_saldar_cc(self):
        
        ''' El siguiente metodo se utiliza para abrir la ventana de pago de
            una cuenta corriente, donde primero se verifica que un cliente
            sea seleccionado. Luego se configuran los botones de dicha
            ventana
        '''
        # Verificacion seleccion de cliente
        if self.cliente == None:
            messagebox.showerror(
                'Cuenta Corriente',
                'Debes elegir un cliente'
            )
            return

        # Llamado de ventana
        self.toplevel_saldocc = Toplevel(self.root)
        self.ventana_saldocc = SaldarCuentaCorriente(self.toplevel_saldocc)
        self.toplevel_saldocc.grab_set()

        # Foco en entry_nuevopago
        self.ventana_saldocc.entry_nuevopago.focus()

        # Configuracion de botones de la ventana
        self.ventana_saldocc.boton_nuevopago.config(
            command =   self.saldar_cuenta_corriente
        )

    
    def abrir_ventana_actualizar_cc(self):

        ''' Este metodo abre la ventana de actualizacion de cuenta corriente,
            verificando primero que se haya seleccionado un cliente
        '''
        # Verificacion seleccion de cliente
        if self.cliente == None:
            messagebox.showerror(
                'Cuenta Corriente',
                'Debes elegir un cliente'
            )
            return
        
        # Llamado de ventana
        self.toplevel_actualizarcc = Toplevel(self.root)

        self.ventana_actualizarcc = ActualizarCuentaCorriente(
            self.toplevel_actualizarcc
        )

        self.toplevel_actualizarcc.grab_set()

        # Foco en entry_actualizacion
        self.ventana_actualizarcc.entry_actualizacion.focus()

        # Configuracion de botones de la ventana
        self.ventana_actualizarcc.boton_actualizacion.config(
            command =   self.actualizar_cuenta_corriente
        )

    ############################# COMBOBOX ##################################
    def clientes_cuentacorriente(self):
        
        ''' Metodo para introducir clientes con cuentas corrientes activas
            dentro del ComboBox. Primero se buscan los clientes con la
            funcion del modelo clientes_cuentacorriente() y luego si existen
            clientes, se introducen en una lista que sera utilizada para
            setear el ComboBox
        '''

        # Obtencion de clientes
        clientes_cc = self.modelo_ccorriente.clientes_cuentacorriente()

        # Verificacion de clientes y obtencion de lista
        if clientes_cc:
            lista_clientes_cc = [cliente[0] for cliente in clientes_cc]
            
        else:
            lista_clientes_cc = []
        
        return lista_clientes_cc


    ########################## ACCIONES DE BOTONES ##########################
    def filtrar_cuenta_corriente(self):
        
        ''' Este metodo se utiliza para filtrar la cuenta corriente de un
            cliente determinado, primero se obtiene dicho cliente, luego
            mediante el metodo ver_cuentascorrientes se consulta su estado
            de cuenta corriente. Si se encuentra informacion, esta se
            introduce en el Treeview.
            Se crean tags para colorear las filas dependiendo de su estado
            (Adeuda, Actualizacion o Paga).
            Tambien se obtiene el monto adeudado total del cliente y se
            actualiza el valor del Label.
        '''

        # Obtencion de cliente
        try:
            self.cliente = self.vista_ccorriente.entry_cliente.get()

            # Verificacion de cliente
            if self.cliente == '':
                messagebox.showerror('Error','Introducir nombre de cliente')
                return

            # Obtencion de estado de cuenta corriente del cliente
            informacion_cc = self.modelo_ccorriente.ver_cuentascorrientes(
                self.cliente
            )

            # Limpieza de Treeview
            self.vista_ccorriente.limpiar_treeview()
            
            # Verificacion cuenta corriente
            if informacion_cc:
                for cuentacorriente in informacion_cc:
                    self.vista_ccorriente.tv_cc.insert(
                        '',
                        'end',
                        text=cuentacorriente[0],
                        values=(
                            cuentacorriente[2],
                            cuentacorriente[3],
                            cuentacorriente[4],
                            cuentacorriente[5]
                        )
                    )

                # Creacion de tags
                self.vista_ccorriente.tv_cc.tag_configure(
                    'Rojo',
                    foreground='red',
                    font=('century gothic',10,'bold')
                )

                self.vista_ccorriente.tv_cc.tag_configure(
                    'Azul',
                    foreground='blue',
                    font=('century gothic',10,'bold')
                )

                self.vista_ccorriente.tv_cc.tag_configure(
                    'Verde',
                    foreground='green',
                    font=('century gothic',10,'bold')
                )

                # Asignacion de tags. Se recorren filas con bucle for
                for item in self.vista_ccorriente.tv_cc.get_children():
                    valores = self.vista_ccorriente.tv_cc.item(item,'values')

                    if valores[1] == 'Adeuda':
                        self.vista_ccorriente.tv_cc.item(
                            item,
                            tags=('Rojo',)
                        )

                    elif valores[1] == 'Actualizacion':
                        self.vista_ccorriente.tv_cc.item(
                            item,
                            tags=('Azul',)
                        )

                    elif valores[1] == 'Paga':
                        self.vista_ccorriente.tv_cc.item(
                            item,
                            tags=('Verde',)
                        )

                # Obtencion del monto adeudado total del cliente
                monto_adeudado_total = (
                    self.modelo_ccorriente.ultimo_monto_pendiente(
                        self.cliente
                    )
                )

                # Actualizacion de Label
                self.vista_ccorriente.label_deudatotal.config(
                    text = f'Deuda Total: $ {monto_adeudado_total[0][0]}'
                )

            else: 
                messagebox.showinfo(
                    'Cuenta Corriente',
                    'No se encontraron resultados'
                )
        
        except ValueError:
            messagebox.showerror(
                'Error',
                'Error en el ingreso de datos'
            )
        
        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Ha ocurrido un error inesperado - {error}'
            )


    def saldar_cuenta_corriente(self):

        ''' Este metodo se utiliza para asignar al boton de saldar cuenta
            corriente.
            Primero se obtiene el monto abonado por el cliente. Se obtiene
            el ultimo numero de operacion y ultimo monto pendiente de dicho
            cliente.
            Luego, se calcula el nuevo monto pendiente, donde si el mismo
            llega a cero, se elimina la cuenta corriente y se muestra un
            mensaje diciendo que la deuda se ha saldado. Caso contrario,
            se inserta la nueva fila dentro del Treeview.
        '''
        try:
            # Recuperacion de monto abonado 
            monto_abonado = float(self.ventana_saldocc.entry_nuevopago.get())

            # Obtencion del ultimo numero de operacion
            resultado_ultimo_nro_operacion = (
                self.modelo_ccorriente.ultimo_nro_operacion(
                    self.cliente
                )
            )
            # Verificacion numero de operacion, si no existe, se asigna 0
            if (resultado_ultimo_nro_operacion 
                and resultado_ultimo_nro_operacion[0][0] is not None
            ):
                ultimo_nro_operacion = (
                    int(resultado_ultimo_nro_operacion[0][0])
                )

            else:
                ultimo_nro_operacion = 0

            # Obtencion del ultimo monto pendiente
            resultado_ultimo_montopendiente = (
                self.modelo_ccorriente.ultimo_monto_pendiente(
                    self.cliente
                )
            )

            if (resultado_ultimo_montopendiente and
                resultado_ultimo_montopendiente[0][0] is not None
            ):
                
                ultimo_montopendiente = (
                    float(resultado_ultimo_montopendiente[0][0])
                )

            else:
                ultimo_montopendiente = 0
            
            # Obtencion nuevo monto pendiente
            monto_pendiente = ultimo_montopendiente - monto_abonado

            # Verificacion de saldo de cuenta corriente
            if monto_pendiente <= 0:
                self.modelo_ccorriente.eliminar_cuentacorriente(self.cliente)
                self.toplevel_saldocc.destroy()
                messagebox.showinfo(
                    'Cuenta Corriente',
                    f'{self.cliente} ha saldado completamente su deuda!'
                )

                # Se actualiza el estado de las ventas pendientes a 'Pagado'
                ModeloVentas.actualizacion_estadoventa(self.cliente)

                # Seteo de treeview, combobox, entry, label y atributos
                self.vista_ccorriente.limpiar_treeview()  
                self.filtrar_cuenta_corriente()      
                self.vista_ccorriente.entry_cliente.delete(0,'end')      
                self.vista_ccorriente.label_deudatotal.config(
                    text = 'Deuda Total: $'
                )
                self.cliente = None
                self.vista_ccorriente.entry_cliente['values'] = (
                    self.clientes_cuentacorriente()
                )

            else:
                # Ingreso de pago a base de datos y actualizacion de treeview
                self.modelo_ccorriente.ingresar_pago_cc(
                    ultimo_nro_operacion + 1,
                    self.cliente,
                    'Paga',
                    monto_abonado,
                    monto_pendiente
                )

                self.toplevel_saldocc.destroy()
                messagebox.showinfo(
                    'Cuenta Corriente',
                    'Pago agregado correctamente'
                )
                self.vista_ccorriente.limpiar_treeview()
                self.filtrar_cuenta_corriente()

        except ValueError:
            messagebox.showerror('Error','Error en ingreso de datos')
        
        except Exception as error:
            messagebox.showerror(
                'Error',
                f'Ocurrio un error inesperado - {error}'
            )


    def actualizar_cuenta_corriente(self):

        ''' Este metodo se utiliza para actualizar una cuenta corriente en
            el caso en que se quiera modificar la deuda actual de un cliente,
            por ejemplo, por ajustes de inflacion.
            Se solicita un monto de actualizacion y luego se recupera el
            ultimo numero de operacion y monto pendiente del cliente
            determinado, para luego hacer el ajuste correspondiente al
            monto pendiente. Se ingresa el registro a la base de datos con
            el concepto de "Actualizacion"
        '''
        try:
            # Recuperacion del monto
            monto_actualizacion = (
                float(self.ventana_actualizarcc.entry_actualizacion.get())
            )

            # Recuperacion ultimo nro_operacion
            resultado_ultimo_nrooperacion = (
                self.modelo_ccorriente.ultimo_nro_operacion(
                    self.cliente
                )
            )

            if (
                resultado_ultimo_nrooperacion and
                resultado_ultimo_nrooperacion[0][0] is not None
            ):
                ultimo_nro_operacion = (
                    int(resultado_ultimo_nrooperacion[0][0])
                )
            else:
                ultimo_nro_operacion = 0

            # Recuperacion ultimo monto_pendiente
            resultado_ultimo_montopendiente = (
                self.modelo_ccorriente.ultimo_monto_pendiente(
                    self.cliente
                )
            )

            if (
                resultado_ultimo_montopendiente and
                resultado_ultimo_montopendiente[0][0] is not None
            ):
                ultimo_montopendiente = (
                    float(resultado_ultimo_montopendiente[0][0])
                )
            else:
                ultimo_montopendiente = 0
            
            # Actualizacion monto_pendiente
            monto_pendiente = ultimo_montopendiente + monto_actualizacion

            # Ingreso de registro a base de datos
            self.modelo_ccorriente.ingresar_pago_cc(
                ultimo_nro_operacion + 1,
                self.cliente,
                'Actualizacion',
                monto_actualizacion,
                monto_pendiente
            )
            
            # Mensaje de confirmacion y actualizacion de Treeview
            self.toplevel_actualizarcc.destroy()
            messagebox.showinfo('Cuenta Corriente','Deuda actualizada!')
            self.vista_ccorriente.limpiar_treeview()
            self.filtrar_cuenta_corriente()
        
        except ValueError:
            messagebox.showerror(
                'Cuenta Corriente',
                'Error en el ingreso de datos'
            )

        except Exception as error:
            messagebox.showerror(
                'Cuenta Corriente',
                f'Error inesperado - {error}'
            )


    def eliminar_ultima_operacion(self):
        
        ''' Este metodo se utiliza para eliminar el ultimo registro en la
            cuenta corriente de un determinado cliente.
            Primero se verifica que se ha elegido un cliente, se obtiene el
            ultimo numero de operacion, y en funcion de dicho numero y el
            cliente, se llama al metodo eliminar_ultima_operacion.
        '''
        # Verificacion de cliente
        if self.cliente == None:
            messagebox.showerror(
                'Cuenta Corriente',
                'Debes elegir un cliente'
            )
            return

        # Obtencion ultimo nro_operacion
        resultado_ultimo_nrooperacion = (
            self.modelo_ccorriente.ultimo_nro_operacion(
                self.cliente
            )
        )

        if resultado_ultimo_nrooperacion:
            ultimo_nrooperacion = resultado_ultimo_nrooperacion[0][0]
        
        # Eliminacion de la ultima operacion
        confirmacion = messagebox.askyesno(
            'Cuenta Corriente',
            f'Desea eliminar la ultima operacion hecha para {self.cliente}?'
        )

        if confirmacion:
            self.modelo_ccorriente.eliminar_ultima_operacion(
                ultimo_nrooperacion,
                self.cliente
            )
            messagebox.showinfo(
                'Cuenta Corriente',
                'Operacion eliminada correctamente'
            )
            self.vista_ccorriente.limpiar_treeview()
            self.filtrar_cuenta_corriente()
