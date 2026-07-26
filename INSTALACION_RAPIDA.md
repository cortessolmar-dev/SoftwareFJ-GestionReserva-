# Guía Rápida de Instalación

## ⚡ Inicio Rápido (5 minutos)

### Requisitos Previos
- Python 3.8 o superior instalado
- Git instalado
- Terminal/CMD disponible

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/cortessolmar-dev/SoftwareFJ-GestionReserva-.git
cd SoftwareFJ-GestionReserva-
```

### Paso 2: Ejecutar el Sistema

```bash
python main.py
```

### Paso 3: Ver los Resultados

En la terminal verás:

```
################################################################################
#                                                                              #
#     SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS        #
#    Desarrollado en Python con manejo robusto de excepciones                 #
#                                                                              #
################################################################################

✓ Sistema de logging inicializado
  Archivo de logs: /ruta/a/logs/gestion_reservas.log

[... 10 operaciones ejecutándose ...]

================================================================================
RESUMEN DE SIMULACIONES
================================================================================

  Total de operaciones: 10
  ✓ Operaciones exitosas: 5
  ✗ Errores controlados: 5

  Total de clientes creados: 1
  Total de servicios creados: 3
  Total de reservas: 3

  Archivo de logs: /ruta/a/logs/gestion_reservas.log
```

### Paso 4: Revisar los Logs

```bash
# Ver el archivo de logs completo
cat logs/gestion_reservas.log

# O en Windows
type logs\gestion_reservas.log
```

## 📋 Estructura del Proyecto

```
SoftwareFJ-GestionReserva-/
├── README.md                    # Documentación completa
├── GITHUB_FLUJO.md              # Flujo colaborativo
├── INSTALACION_RAPIDA.md        # Este archivo
├── main.py                      # Punto de entrada ☝️
├── excepciones.py               # Excepciones personalizadas
├── cliente.py                   # Clase Cliente
├── servicio.py                  # Clases de Servicio
├── reserva.py                   # Clase Reserva
├── logger.py                    # Sistema de logging
├── simulacion.py                # Simulaciones de operaciones
├── .gitignore                   # Archivos ignorados
├── requirements.txt             # Dependencias (ninguna requerida)
├── logs/                        # Directorio de logs (creado automáticamente)
└── .git/                        # Repositorio Git
```

## 🧪 Solución de Problemas

### Problema: "Python no se reconoce"

**Solución**:
```bash
# Verifica que Python esté instalado
python --version
# o
python3 --version
```

Si no aparece, instala Python desde: https://www.python.org/downloads/

### Problema: "ModuleNotFoundError: No module named 'cliente'"

**Solución**:
Asegúrate de estar en el directorio correcto:
```bash
cd SoftwareFJ-GestionReserva-
python main.py
```

### Problema: "Permission denied" (en Linux/Mac)

**Solución**:
```bash
chmod +x main.py
python main.py
```

---

**¡Listo! Ya tienes el sistema funcionando.**
