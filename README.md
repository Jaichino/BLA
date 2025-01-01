# Sistema BLA Estética

Repositorio que aloja un sistema de gestión de ventas para un emprendimiento dedicado a la venta de cosméticos.

## Lenguaje utilizado y librerías

El mismo fue desarrollado utilizando Python y PostgreSQL como base de datos. Se utilizó Tkinter como herramienta de desarrollo de la interfaz gráfica, 
psycopg2 para interactuar con la base de datos, bcrypt para la generación de contraseñas seguras, matplotlib para la generación de gráficos y ReportLab 
para la generación de PDFs

## Metodología utilizada

La estructura de este proyecto se hizo siguiendo el patrón MVC (Modelo, Vista, Controlador), utilizando programación orientada a objetos (POO).

## Estructura y módulos

El sistema consta de 5 módulos:

  1) Módulo de ventas: en el mismo se generan las respectivas ventas, permitiendo armar un carrito y finalizada la venta se permite elegir el modo de
     pago y el monto abonado, donde si el monto abonado es menor al monto de la venta, se creará una cuenta corriente para el cliente en cuestión.
     Adicionalmente, se permitirá imprimir la factura de la venta. Otra funcionalidad dentro de este módulo es la consulta de ventas realizadas entre
     un determinado periodo de tiempo o filtrando por un determinado cliente.

  2) Módulo de productos: dicho módulo permite la generación de un stock de productos, en el cuál se puede filtrar según codigo o coincidencia parcial
     del nombre del producto; ver productos sin stock; modificar productos; cargar stocks; eliminar productos. Además, se creó una sección de vencimientos,
     donde se puede consultar productos vencidos o próximos a vencer (filtrando entre un rango de fechas o por código de producto).

  3) Módulo de cuentas corrientes: en este módulo se irán registrando todas las deudas de los clientes que no han completado sus pagos. En el mismo se puede
     buscar la cuenta corriente de un determinado cliente (solo aparecerán aquellos clientes que tienen deudas). Para dicho cliente se podrá agregar un saldo
     de deuda (cuando el mismo entrega un monto de dinero para saldar su deuda) o actualizar el monto adeudado (cuando la deuda lleva sin saldarse por un periodo
     largo de tiempo, se permite agregar un monto en concepto de 'Actualización' para ajustar la deuda al aumento de los precios)

  4) Módulo de reportes: este módulo contiene algunos indicadores y gráficos básicos para visualizar el estado del negocio, tales como: ganancias mensuales,
     monto adeudado total, monto en inventario, productos más vendidos o evolución de ingresos a lo largo del año.

  5) Módulo de administrador: en este módulo se pueden hacer funciones básicas de administrador tales como la creación de nuevas cuentas y asignación de roles,
     eliminación de cuentas y limpieza completa de la base de datos.
