# SoftwareFJ-GestionReserva

Sistema Integral de Gestión de Clientes, Servicios y Reservas desarrollado en Python con arquitectura orientada a objetos y manejo robusto de excepciones.

## 📋 Descripción del Proyecto

Este sistema permite gestionar de manera integral:

- **Clientes**: Creación, validación y gestión de datos de clientes
- **Servicios**: Tres tipos especializados de servicios con diferentes características
  - ServicioHotel: Alojamiento con cálculo de costos por habitaciones
  - ServicioRestaurante: Servicio de comida con costos adicionales por servicio de mesa
  - ServicioTransporte: Transporte con costos de combustible incluidos
- **Reservas**: Creación, confirmación, cancelación y procesamiento de reservas con validaciones completas

## 🏗️ Arquitectura del Sistema

### Estructura Orientada a Objetos (OOP)

```
excepciones.py
├── ErrorGestionReserva (base)
├── ErrorCliente
├── ErrorServicio
└── ErrorReserva

cliente.py
└── Cliente
    ├── Validación de datos
    ├── Gestión de reservas
    └── Encapsulación

servicio.py
├── Servicio (clase abstracta)
│   ├── ServicioHotel (herencia)
│   ├── ServicioRestaurante (herencia)
│   └── ServicioTransporte (herencia)
├── Polimorfismo: calcular_costo_adicional()
└── Polimorfismo: obtener_tipo_servicio()

reserva.py
└── Reserva
    ├── Validación de fechas
    ├── Control de capacidad
    ├── Estados: PENDIENTE, CONFIRMADA, CANCELADA, COMPLETADA
    ├── Métodos: confirmar(), cancelar(), procesar()
    └── Encapsulación mediante propiedades

logger.py
└── LoggerGestionReserva (Singleton)
    ├── Registro centralizado de eventos
    ├── Archivo de logs en logs/gestion_reservas.log
    └── Métodos especializados para cada operación

simulacion.py
└── SimuladorReservas
    ├── 10 operaciones de prueba (5 éxito, 5 error)
    └── Demostración de manejo de excepciones
```

## 🎯 Características Principales

### 1. Manejo Robusto de Excepciones

- ✅ Excepciones personalizadas para cada dominio
- ✅ Try/except/finally en operaciones críticas
- ✅ Encadenamiento de excepciones
- ✅ Continuidad del sistema ante errores
- ✅ Validación de datos en construcción de objetos

### 2. Arquitectura Orientada a Objetos

- ✅ **Abstracción**: Clase base `Servicio` con métodos abstractos
- ✅ **Herencia**: `ServicioHotel`, `ServicioRestaurante`, `ServicioTransporte` heredan de `Servicio`
- ✅ **Polimorfismo**: Implementación específica de `calcular_costo_adicional()` en cada tipo de servicio
- ✅ **Encapsulación**: Propiedades privadas con getters en `Reserva` y `Cliente`
- ✅ **Listas internas**: Gestión de reservas en clientes y servicios

### 3. Sistema de Logging

- ✅ Logger Singleton centralizado
- ✅ Registro de todas las operaciones
- ✅ Archivo de logs con timestamps
- ✅ Niveles de severidad (INFO, WARNING, ERROR)
- ✅ Método especializados para cada tipo de operación

### 4. Simulaciones (10 Operaciones)

#### Operaciones Exitosas (5):
1. **Crear cliente válido** - Demostración de validación y encapsulación
2. **Crear servicios especializados** - Herencia y polimorfismo en acción
3. **Crear reserva exitosa** - Validación de fechas y capacidad
4. **Confirmar reserva** - Cambio de estado y logging
5. **Procesar reserva** - Completar la reserva exitosamente

#### Operaciones con Errores Controlados (5):
6. **Cliente inválido** - Email sin @, captura `DatosClienteInvalidos`
7. **Servicio inválido** - Precio negativo, captura `DatosServicioInvalidos`
8. **Fecha pasada** - Intento de reservar en fecha pasada, captura `FechaInvalida`
9. **Capacidad excedida** - Más personas que disponibilidad, captura `CapacidadExcedida`
10. **Procesar reserva cancelada** - Estado inválido, captura `ReservaNoDisponible`

## 📦 Requisitos

- Python 3.8 o superior
- Ninguna dependencia externa (solo biblioteca estándar)

## 🚀 Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/cortessolmar-dev/SoftwareFJ-GestionReserva-.git
cd SoftwareFJ-GestionReserva-
```

### 2. Ejecutar el Sistema

```bash
python main.py
```

### 3. Ver los Logs

Después de ejecutar el programa, los logs se guardarán en:

```
logs/gestion_reservas.log
```

Puedes visualizarlos con:

```bash
cat logs/gestion_reservas.log
```

## 📝 Descripción de Archivos

### `excepciones.py`
Define todas las excepciones personalizadas del sistema:
- `ErrorGestionReserva` (excepción base)
- `DatosClienteInvalidos`, `ClienteNoEncontrado`, `ClienteYaExiste`
- `DatosServicioInvalidos`, `ServicioNoEncontrado`, `ServicioYaExiste`
- `FechaInvalida`, `CapacidadExcedida`, `ReservaNoDisponible`, `ReservaYaExiste`

### `cliente.py`
Implementa la clase `Cliente`:
- Constructor con validación de datos
- Métodos para gestionar reservas
- Propiedades encapsuladas
- Validación de email, cédula, teléfono

### `servicio.py`
Implementa la arquitectura de servicios:
- Clase abstracta `Servicio` con interfaz común
- `ServicioHotel`: Alojamiento con gestión de habitaciones
- `ServicioRestaurante`: Gastronomía con tipo de cocina
- `ServicioTransporte`: Transporte con tipo de vehículo
- Cálculo de costos adicionales específicos por tipo
- Métodos para verificar disponibilidad

### `reserva.py`
Implementa la clase `Reserva`:
- Identificación única con contador automático
- Validación de fechas (deben ser futuras)
- Validación de capacidad del servicio
- Estados de reserva: PENDIENTE, CONFIRMADA, CANCELADA, COMPLETADA
- Métodos para cambio de estado: `confirmar()`, `cancelar()`, `procesar()`
- Cálculo automático del costo total
- Encapsulación mediante propiedades read-only

### `logger.py`
Implementa el sistema de logging:
- Patrón Singleton para instancia única
- Registro en archivo `logs/gestion_reservas.log`
- Métodos especializados para cada tipo de operación
- Formatos de log con timestamps
- Redirección a consola y archivo simultáneamente

### `simulacion.py`
Implementa las 10 operaciones de prueba:
- Clase `SimuladorReservas` con métodos para cada operación
- Manejo completo de excepciones en cada caso
- Logging de eventos exitosos y errores
- Demostraciones de conceptos OOP y validación
- Resumen final de operaciones

### `main.py`
Punto de entrada del sistema:
- Inicialización del logger
- Ejecución del simulador
- Manejo de errores globales
- Información de ubicación de logs

## 🔍 Ejemplo de Uso

```python
from cliente import Cliente
from servicio import ServicioHotel
from reserva import Reserva

# Crear cliente
cliente = Cliente(
    cedula="1234567890",
    nombre="Juan García",
    email="juan@email.com",
    telefono="3005551234"
)

# Crear servicio
hotel = ServicioHotel(
    codigo="SRV-001",
    nombre="Hotel Gran Vía",
    descripcion="Hotel de lujo",
    precio=150.00,
    capacidad_maxima=50
)

# Crear reserva
reserva = Reserva(
    cliente=cliente,
    servicio=hotel,
    fecha="2024-12-25",
    cantidad_personas=5
)

# Confirmar reserva
reserva.confirmar()

# Procesar reserva
reserva.procesar()
```

## 📊 Salida Esperada

Al ejecutar `python main.py`, verás:

```
================================================================================
                    SISTEMA INTEGRAL DE GESTIÓN DE...
================================================================================

✓ Sistema de logging inicializado
  Archivo de logs: /ruta/a/logs/gestion_reservas.log

================================================================================
INICIANDO SIMULACIONES DEL SISTEMA DE GESTIÓN DE RESERVAS
================================================================================

[OPERACIONES EXITOSAS]

OPERACIÓN 1: Crear cliente válido
--------------------------------------------------
✓ Cliente creado exitosamente
  - Cédula: 1234567890
  - Nombre: Juan García
  - Email: juan.garcia@email.com
  - Teléfono: 3005551234
  - Reservas: 0

[... más operaciones ...]

[OPERACIONES CON ERRORES CONTROLADOS]

OPERACIÓN 6: Crear cliente con datos inválidos (EMAIL SIN @)
--------------------------------------------------
✓ Excepción capturada correctamente
  - Tipo de error: DatosClienteInvalidos
  - Mensaje: Error al crear cliente: Email debe ser válido
  - El sistema continuó ejecutándose normalmente

[... más operaciones ...]

================================================================================
RESUMEN DE SIMULACIONES
================================================================================

  Total de operaciones: 10
  ✓ Operaciones exitosas: 5
  ✗ Errores controlados: 5

  Total de clientes creados: 1
  Total de servicios creados: 3
  Total de reservas: 3
```

## 📂 Estructura de Directorios

```
SoftwareFJ-GestionReserva-/
├── README.md                    # Este archivo
├── main.py                      # Punto de entrada
├── excepciones.py               # Excepciones personalizadas
├── cliente.py                   # Clase Cliente
├── servicio.py                  # Clases de Servicio (base + especializadas)
├── reserva.py                   # Clase Reserva
├── logger.py                    # Sistema de logging
├── simulacion.py                # Simulaciones y pruebas
├── .gitignore                   # Archivos ignorados por Git
└── logs/                        # Directorio de logs (creado al ejecutar)
    └── gestion_reservas.log     # Archivo de registro de eventos
```

## 🧪 Pruebas y Validaciones

El sistema valida automáticamente:

- ✅ Datos de cliente (cédula, nombre, email válido, teléfono)
- ✅ Datos de servicio (código, nombre, precio positivo, capacidad positiva)
- ✅ Fechas de reserva (deben ser futuras)
- ✅ Capacidad de servicios (no permite exceder límites)
- ✅ Estados de reserva (transiciones válidas únicamente)
- ✅ Encadenamiento de excepciones y manejo completo

## 📈 Conceptos Demostrados

### Programación Orientada a Objetos
- Clases y objetos
- Herencia (3 servicios heredan de clase base)
- Polimorfismo (métodos sobrescritos)
- Abstracción (clase abstracta Servicio)
- Encapsulación (propiedades privadas)

### Manejo de Excepciones
- Excepciones personalizadas
- Try/except/finally
- Encadenamiento de excepciones
- Captura específica de excepciones
- Continuidad ante errores

### Patrones de Diseño
- Singleton (Logger)
- Template Method (validación en constructores)
- Strategy (cálculo de costos adicionales)

### Persistencia
- Logging a archivo
- Timestamps automáticos
- Niveles de severidad

## 👨‍💻 Contribuciones

Este proyecto fue desarrollado como parte de un ejercicio de consolidación de conceptos de programación en Python.

### Flujo de Contribución Git

1. Se creó la rama `feature/logging-testing`
2. Se implementaron todas las clases y módulos
3. Se agregaron simulaciones exhaustivas
4. Se documentó completamente el código
5. Se crearán Pull Requests para revisión y merge a `main`

## 📄 Licencia

Este proyecto es de código abierto y educativo.

## 📞 Contacto

Desarrollado por: **cortessolmar-dev**

---

**Última actualización**: 2026-07-26

