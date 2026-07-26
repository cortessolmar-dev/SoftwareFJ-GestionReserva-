"""Módulo de simulaciones y pruebas.

Ejecuta las 10 operaciones requeridas: 5 de éxito y 5 de error,
con manejo completo de excepciones y logging de eventos.
"""

from cliente import Cliente
from servicio import ServicioHotel, ServicioRestaurante, ServicioTransporte
from reserva import Reserva
from logger import LoggerGestionReserva
from excepciones import (
    DatosClienteInvalidos,
    DatosServicioInvalidos,
    FechaInvalida,
    CapacidadExcedida,
    ReservaNoDisponible
)
from datetime import datetime, timedelta


class SimuladorReservas:
    """Simulador de operaciones de gestión de reservas.
    
    Ejecuta casos de prueba de éxito y error para validar
    la robustez del sistema.
    """
    
    def __init__(self):
        """Inicializa el simulador."""
        self.logger = LoggerGestionReserva()
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.operaciones_exitosas = 0
        self.operaciones_fallidas = 0
    
    def ejecutar_todas_las_simulaciones(self):
        """Ejecuta todas las 10 operaciones de simulación."""
        print("\n" + "="*80)
        print("INICIANDO SIMULACIONES DEL SISTEMA DE GESTIÓN DE RESERVAS")
        print("="*80 + "\n")
        
        # Operaciones Exitosas (5)
        print("\n[OPERACIONES EXITOSAS]\n")
        self.operacion_1_cliente_valido()
        self.operacion_2_servicios_especializados()
        self.operacion_3_reserva_exitosa()
        self.operacion_4_confirmar_reserva()
        self.operacion_5_procesar_reserva()
        
        # Operaciones Fallidas (5)
        print("\n[OPERACIONES CON ERRORES CONTROLADOS]\n")
        self.operacion_6_cliente_invalido()
        self.operacion_7_servicio_invalido()
        self.operacion_8_reserva_fecha_invalida()
        self.operacion_9_reserva_capacidad_excedida()
        self.operacion_10_cancelar_y_procesar_invalido()
        
        # Resumen final
        self._mostrar_resumen_final()
    
    # OPERACIONES EXITOSAS
    
    def operacion_1_cliente_valido(self):
        """OPERACIÓN 1: Crear cliente válido.
        
        Demuestra:
        - Creación exitosa de Cliente
        - Validación de datos
        - Encapsulación
        """
        print("OPERACIÓN 1: Crear cliente válido")
        print("-" * 50)
        
        try:
            cliente = Cliente(
                cedula="1234567890",
                nombre="Juan García",
                email="juan.garcia@email.com",
                telefono="3005551234"
            )
            self.clientes.append(cliente)
            self.operaciones_exitosas += 1
            
            print(f"✓ Cliente creado exitosamente")
            print(f"  - Cédula: {cliente.cedula}")
            print(f"  - Nombre: {cliente.nombre}")
            print(f"  - Email: {cliente.email}")
            print(f"  - Teléfono: {cliente.telefono}")
            print(f"  - Reservas: {len(cliente.obtener_reservas())}\n")
            
            LoggerGestionReserva.registrar_creacion_cliente(
                cliente.cedula, cliente.nombre, cliente.email
            )
            
        except DatosClienteInvalidos as e:
            print(f"✗ Error: {str(e)}\n")
            self.operaciones_fallidas += 1
    
    def operacion_2_servicios_especializados(self):
        """OPERACIÓN 2: Crear los tres servicios especializados.
        
        Demuestra:
        - Herencia: ServicioHotel, ServicioRestaurante, ServicioTransporte heredan de Servicio
        - Polimorfismo: cada uno implementa calcular_costo_adicional() y obtener_tipo_servicio()
        - Abstracción: métodos abstractos de la clase base
        """
        print("OPERACIÓN 2: Crear servicios especializados")
        print("-" * 50)
        
        try:
            # Servicio Hotel
            hotel = ServicioHotel(
                codigo="SRV-001",
                nombre="Hotel Gran Vía",
                descripcion="Hotel de lujo con 5 estrellas",
                precio=150.00,
                capacidad_maxima=50,
                numero_habitaciones=25
            )
            self.servicios.append(hotel)
            print(f"✓ {hotel.obtener_tipo_servicio()} creado: {hotel.nombre}")
            LoggerGestionReserva.registrar_creacion_servicio(
                hotel.codigo, hotel.nombre, hotel.obtener_tipo_servicio()
            )
            
            # Servicio Restaurante
            restaurante = ServicioRestaurante(
                codigo="SRV-002",
                nombre="Restaurante La Sabor",
                descripcion="Restaurante de comida fusión",
                precio=80.00,
                capacidad_maxima=100,
                tipo_cocina="Fusión"
            )
            self.servicios.append(restaurante)
            print(f"✓ {restaurante.obtener_tipo_servicio()} creado: {restaurante.nombre}")
            LoggerGestionReserva.registrar_creacion_servicio(
                restaurante.codigo, restaurante.nombre, restaurante.obtener_tipo_servicio()
            )
            
            # Servicio Transporte
            transporte = ServicioTransporte(
                codigo="SRV-003",
                nombre="Transporte Premium",
                descripcion="Servicio de transporte en autobús de lujo",
                precio=50.00,
                capacidad_maxima=60,
                tipo_vehiculo="Autobús Premium"
            )
            self.servicios.append(transporte)
            print(f"✓ {transporte.obtener_tipo_servicio()} creado: {transporte.nombre}")
            print(f"\n  [Demostración de Polimorfismo]")
            print(f"  - Hotel costo adicional (20 personas): ${hotel.calcular_costo_adicional(20):.2f}")
            print(f"  - Restaurante costo adicional (20 personas): ${restaurante.calcular_costo_adicional(20):.2f}")
            print(f"  - Transporte costo adicional (20 personas): ${transporte.calcular_costo_adicional(20):.2f}\n")
            
            LoggerGestionReserva.registrar_creacion_servicio(
                transporte.codigo, transporte.nombre, transporte.obtener_tipo_servicio()
            )
            self.operaciones_exitosas += 1
            
        except DatosServicioInvalidos as e:
            print(f"✗ Error: {str(e)}\n")
            self.operaciones_fallidas += 1
    
    def operacion_3_reserva_exitosa(self):
        """OPERACIÓN 3: Crear reserva exitosa.
        
        Demuestra:
        - Creación de Reserva con validaciones
        - Manejo de excepciones FechaInvalida y CapacidadExcedida
        - Encapsulación mediante propiedades
        """
        print("OPERACIÓN 3: Crear reserva exitosa")
        print("-" * 50)
        
        try:
            fecha_futura = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
            
            reserva = Reserva(
                cliente=self.clientes[0],
                servicio=self.servicios[0],  # Hotel
                fecha=fecha_futura,
                cantidad_personas=15
            )
            self.reservas.append(reserva)
            self.operaciones_exitosas += 1
            
            print(f"✓ Reserva creada exitosamente")
            print(f"  - ID: {reserva.id}")
            print(f"  - Cliente: {reserva.cliente.nombre}")
            print(f"  - Servicio: {reserva.servicio.nombre}")
            print(f"  - Fecha: {reserva.fecha}")
            print(f"  - Personas: {reserva.cantidad_personas}")
            print(f"  - Estado: {reserva.estado.value}")
            print(f"  - Costo Total: ${reserva.costo_total:.2f}\n")
            
            LoggerGestionReserva.registrar_creacion_reserva(
                reserva.id, reserva.cliente.nombre, reserva.servicio.nombre,
                reserva.fecha, reserva.cantidad_personas
            )
            
        except (FechaInvalida, CapacidadExcedida) as e:
            print(f"✗ Error: {str(e)}\n")
            self.operaciones_fallidas += 1
    
    def operacion_4_confirmar_reserva(self):
        """OPERACIÓN 4: Confirmar reserva.
        
        Demuestra:
        - Método confirmar() de Reserva
        - Manejo de excepciones ReservaNoDisponible
        - Cambio de estado de reserva
        """
        print("OPERACIÓN 4: Confirmar reserva")
        print("-" * 50)
        
        try:
            if self.reservas:
                reserva = self.reservas[0]
                reserva.confirmar()
                self.operaciones_exitosas += 1
                
                print(f"✓ Reserva confirmada exitosamente")
                print(f"  - ID: {reserva.id}")
                print(f"  - Cliente: {reserva.cliente.nombre}")
                print(f"  - Estado: {reserva.estado.value}")
                print(f"  - Costo: ${reserva.costo_total:.2f}")
                print(f"  - Fecha de creación: {reserva.fecha_creacion}\n")
                
                LoggerGestionReserva.registrar_confirmacion_reserva(
                    reserva.id, reserva.cliente.nombre, reserva.costo_total
                )
            
        except ReservaNoDisponible as e:
            print(f"✗ Error: {str(e)}\n")
            self.operaciones_fallidas += 1
    
    def operacion_5_procesar_reserva(self):
        """OPERACIÓN 5: Procesar (completar) reserva.
        
        Demuestra:
        - Método procesar() de Reserva
        - Cambio de estado: CONFIRMADA -> COMPLETADA
        - Manejo de excepciones en el procesamiento
        """
        print("OPERACIÓN 5: Procesar reserva")
        print("-" * 50)
        
        try:
            if self.reservas:
                reserva = self.reservas[0]
                reserva.procesar()
                self.operaciones_exitosas += 1
                
                print(f"✓ Reserva procesada exitosamente")
                print(f"  - ID: {reserva.id}")
                print(f"  - Cliente: {reserva.cliente.nombre}")
                print(f"  - Estado anterior: Confirmada")
                print(f"  - Estado actual: {reserva.estado.value}")
                print(f"  - Servicio prestado: {reserva.servicio.nombre}\n")
                
                LoggerGestionReserva.registrar_procesamiento_reserva(
                    reserva.id, reserva.cliente.nombre
                )
            
        except ReservaNoDisponible as e:
            print(f"✗ Error: {str(e)}\n")
            self.operaciones_fallidas += 1
    
    # OPERACIONES FALLIDAS (CON MANEJO DE EXCEPCIONES)
    
    def operacion_6_cliente_invalido(self):
        """OPERACIÓN 6: Intentar crear cliente con datos inválidos.
        
        Demuestra:
        - Manejo de excepción DatosClienteInvalidos
        - Validación de datos en el constructor
        - Continuidad del sistema ante errores
        """
        print("OPERACIÓN 6: Crear cliente con datos inválidos (EMAIL SIN @)")
        print("-" * 50)
        
        try:
            cliente_invalido = Cliente(
                cedula="9876543210",
                nombre="María López",
                email="maria.lopez.email.com",  # Falta el @
                telefono="3105559876"
            )
            self.clientes.append(cliente_invalido)
            
        except DatosClienteInvalidos as e:
            self.operaciones_fallidas += 1
            print(f"✓ Excepción capturada correctamente")
            print(f"  - Tipo de error: DatosClienteInvalidos")
            print(f"  - Mensaje: {str(e)}")
            print(f"  - El sistema continuó ejecutándose normalmente\n")
            
            LoggerGestionReserva.registrar_error_cliente(
                "9876543210", str(e)
            )
    
    def operacion_7_servicio_invalido(self):
        """OPERACIÓN 7: Intentar crear servicio con precio negativo.
        
        Demuestra:
        - Manejo de excepción DatosServicioInvalidos
        - Validación de valores numéricos
        - Try/except en constructor
        """
        print("OPERACIÓN 7: Crear servicio con precio negativo")
        print("-" * 50)
        
        try:
            servicio_invalido = ServicioHotel(
                codigo="SRV-999",
                nombre="Hotel Fantasma",
                descripcion="Hotel inexistente",
                precio=-100.00,  # Precio negativo
                capacidad_maxima=30
            )
            self.servicios.append(servicio_invalido)
            
        except DatosServicioInvalidos as e:
            self.operaciones_fallidas += 1
            print(f"✓ Excepción capturada correctamente")
            print(f"  - Tipo de error: DatosServicioInvalidos")
            print(f"  - Mensaje: {str(e)}")
            print(f"  - El sistema continuó ejecutándose normalmente\n")
            
            LoggerGestionReserva.registrar_error_servicio(
                "SRV-999", str(e)
            )
    
    def operacion_8_reserva_fecha_invalida(self):
        """OPERACIÓN 8: Intentar crear reserva con fecha pasada.
        
        Demuestra:
        - Manejo de excepción FechaInvalida
        - Validación de fechas en el constructor de Reserva
        - Try/except/finally para excepciones encadenadas
        """
        print("OPERACIÓN 8: Crear reserva con fecha pasada")
        print("-" * 50)
        
        try:
            fecha_pasada = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
            
            reserva_invalida = Reserva(
                cliente=self.clientes[0],
                servicio=self.servicios[1],  # Restaurante
                fecha=fecha_pasada,
                cantidad_personas=10
            )
            self.reservas.append(reserva_invalida)
            
        except FechaInvalida as e:
            self.operaciones_fallidas += 1
            print(f"✓ Excepción capturada correctamente")
            print(f"  - Tipo de error: FechaInvalida")
            print(f"  - Mensaje: {str(e)}")
            print(f"  - Fecha intentada: {fecha_pasada}")
            print(f"  - El sistema continuó ejecutándose normalmente\n")
            
            LoggerGestionReserva.registrar_error_reserva(
                self.clientes[0].nombre, self.servicios[1].nombre, str(e)
            )
    
    def operacion_9_reserva_capacidad_excedida(self):
        """OPERACIÓN 9: Intentar crear reserva que excede capacidad.
        
        Demuestra:
        - Manejo de excepción CapacidadExcedida
        - Método obtener_disponibilidad()
        - Control de capacidad del servicio
        """
        print("OPERACIÓN 9: Crear reserva que excede capacidad")
        print("-" * 50)
        
        try:
            fecha_futura = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")
            
            # Intentar reservar más personas que la capacidad del servicio
            reserva_excedida = Reserva(
                cliente=self.clientes[0],
                servicio=self.servicios[2],  # Transporte (capacidad 60)
                fecha=fecha_futura,
                cantidad_personas=100  # Excede la capacidad
            )
            self.reservas.append(reserva_excedida)
            
        except CapacidadExcedida as e:
            self.operaciones_fallidas += 1
            print(f"✓ Excepción capturada correctamente")
            print(f"  - Tipo de error: CapacidadExcedida")
            print(f"  - Mensaje: {str(e)}")
            print(f"  - Capacidad disponible: {self.servicios[2].obtener_disponibilidad(fecha_futura)} personas")
            print(f"  - Personas solicitadas: 100")
            print(f"  - El sistema continuó ejecutándose normalmente\n")
            
            LoggerGestionReserva.registrar_error_reserva(
                self.clientes[0].nombre, self.servicios[2].nombre, str(e)
            )
    
    def operacion_10_cancelar_y_procesar_invalido(self):
        """OPERACIÓN 10: Intentar procesar una reserva cancelada.
        
        Demuestra:
        - Manejo de excepción ReservaNoDisponible
        - Método cancelar() de Reserva
        - Validación de estados de reserva
        - Encadenamiento de operaciones con control de errores
        """
        print("OPERACIÓN 10: Procesar una reserva cancelada")
        print("-" * 50)
        
        try:
            # Crear y confirmar una nueva reserva
            fecha_futura = (datetime.now() + timedelta(days=20)).strftime("%Y-%m-%d")
            reserva_temporal = Reserva(
                cliente=self.clientes[0],
                servicio=self.servicios[0],
                fecha=fecha_futura,
                cantidad_personas=12
            )
            reserva_temporal.confirmar()
            
            # Ahora cancelarla
            reserva_temporal.cancelar()
            print(f"  - Reserva cancelada: {reserva_temporal.id}")
            print(f"  - Estado: {reserva_temporal.estado.value}")
            
            # Intentar procesarla (esto debe fallar)
            print(f"  - Intentando procesar reserva cancelada...")
            reserva_temporal.procesar()
            
        except ReservaNoDisponible as e:
            self.operaciones_fallidas += 1
            print(f"\n✓ Excepción capturada correctamente")
            print(f"  - Tipo de error: ReservaNoDisponible")
            print(f"  - Mensaje: {str(e)}")
            print(f"  - No se puede procesar una reserva cancelada")
            print(f"  - El sistema continuó ejecutándose normalmente\n")
            
            LoggerGestionReserva.registrar_cancelacion_reserva(
                reserva_temporal.id, reserva_temporal.cliente.nombre
            )
    
    def _mostrar_resumen_final(self):
        """Muestra un resumen de todas las operaciones ejecutadas."""
        print("\n" + "="*80)
        print("RESUMEN DE SIMULACIONES")
        print("="*80)
        print(f"\n  Total de operaciones: {self.operaciones_exitosas + self.operaciones_fallidas}")
        print(f"  ✓ Operaciones exitosas: {self.operaciones_exitosas}")
        print(f"  ✗ Errores controlados: {self.operaciones_fallidas}")
        print(f"\n  Total de clientes creados: {len(self.clientes)}")
        print(f"  Total de servicios creados: {len(self.servicios)}")
        print(f"  Total de reservas: {len(self.reservas)}")
        print(f"\n  Archivo de logs: {LoggerGestionReserva.obtener_archivo_log()}")
        print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    try:
        simulador = SimuladorReservas()
        simulador.ejecutar_todas_las_simulaciones()
    except Exception as e:
        print(f"\n✗ Error inesperado en simulación: {str(e)}")
        LoggerGestionReserva.registrar_error_operacion("SIMULACIÓN GENERAL", str(e))
