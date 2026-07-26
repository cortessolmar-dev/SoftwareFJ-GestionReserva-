"""Módulo de gestión de logs.

Proporciona funcionalidades para registrar eventos y errores del sistema.
"""

import logging
import os
from datetime import datetime


class LoggerGestionReserva:
    """Gestor centralizado de logs del sistema.
    
    Registra todos los eventos, errores y operaciones en un archivo de log
    con formato estructurado y timestamps.
    """
    
    # Directorio de logs
    DIRECTORIO_LOGS = "logs"
    ARCHIVO_LOG = os.path.join(DIRECTORIO_LOGS, "gestion_reservas.log")
    
    # Logger singleton
    _instancia = None
    _logger = None
    
    def __new__(cls):
        """Implementa el patrón Singleton.
        
        Returns:
            LoggerGestionReserva: Única instancia del logger
        """
        if cls._instancia is None:
            cls._instancia = super(LoggerGestionReserva, cls).__new__(cls)
            cls._instancia._inicializar_logger()
        return cls._instancia
    
    def _inicializar_logger(self):
        """Inicializa el logger con configuración específica."""
        # Crear directorio de logs si no existe
        if not os.path.exists(self.DIRECTORIO_LOGS):
            os.makedirs(self.DIRECTORIO_LOGS)
        
        # Configurar logger
        LoggerGestionReserva._logger = logging.getLogger('GestionReservas')
        LoggerGestionReserva._logger.setLevel(logging.DEBUG)
        
        # Evitar agregar handlers múltiples
        if LoggerGestionReserva._logger.hasHandlers():
            LoggerGestionReserva._logger.handlers.clear()
        
        # Formato del log
        formato = logging.Formatter(
            '[%(asctime)s] - %(levelname)s - %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para archivo
        file_handler = logging.FileHandler(self.ARCHIVO_LOG, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formato)
        LoggerGestionReserva._logger.addHandler(file_handler)
        
        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formato)
        LoggerGestionReserva._logger.addHandler(console_handler)
    
    @classmethod
    def obtener_logger(cls):
        """Obtiene la instancia del logger.
        
        Returns:
            logging.Logger: Logger configurado
        """
        return cls._logger
    
    @staticmethod
    def registrar_creacion_cliente(cedula, nombre, email):
        """Registra la creación de un cliente.
        
        Args:
            cedula (str): Cédula del cliente
            nombre (str): Nombre del cliente
            email (str): Email del cliente
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.info(f"CLIENTE CREADO - Cédula: {cedula}, Nombre: {nombre}, Email: {email}")
    
    @staticmethod
    def registrar_error_cliente(cedula, error):
        """Registra un error en la creación de cliente.
        
        Args:
            cedula (str): Cédula del cliente
            error (str): Descripción del error
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.error(f"ERROR EN CLIENTE - Cédula: {cedula}, Error: {error}")
    
    @staticmethod
    def registrar_creacion_servicio(codigo, nombre, tipo):
        """Registra la creación de un servicio.
        
        Args:
            codigo (str): Código del servicio
            nombre (str): Nombre del servicio
            tipo (str): Tipo de servicio
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.info(f"SERVICIO CREADO - Código: {codigo}, Nombre: {nombre}, Tipo: {tipo}")
    
    @staticmethod
    def registrar_error_servicio(codigo, error):
        """Registra un error en la creación de servicio.
        
        Args:
            codigo (str): Código del servicio
            error (str): Descripción del error
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.error(f"ERROR EN SERVICIO - Código: {codigo}, Error: {error}")
    
    @staticmethod
    def registrar_creacion_reserva(id_reserva, cliente, servicio, fecha, personas):
        """Registra la creación de una reserva.
        
        Args:
            id_reserva (str): ID de la reserva
            cliente (str): Nombre del cliente
            servicio (str): Nombre del servicio
            fecha (str): Fecha de la reserva
            personas (int): Cantidad de personas
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.info(f"RESERVA CREADA - ID: {id_reserva}, Cliente: {cliente}, "
                   f"Servicio: {servicio}, Fecha: {fecha}, Personas: {personas}")
    
    @staticmethod
    def registrar_error_reserva(cliente, servicio, error):
        """Registra un error en la creación de reserva.
        
        Args:
            cliente (str): Nombre del cliente
            servicio (str): Nombre del servicio
            error (str): Descripción del error
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.error(f"ERROR EN RESERVA - Cliente: {cliente}, Servicio: {servicio}, Error: {error}")
    
    @staticmethod
    def registrar_confirmacion_reserva(id_reserva, cliente, costo):
        """Registra la confirmación de una reserva.
        
        Args:
            id_reserva (str): ID de la reserva
            cliente (str): Nombre del cliente
            costo (float): Costo total de la reserva
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.info(f"RESERVA CONFIRMADA - ID: {id_reserva}, Cliente: {cliente}, Costo: ${costo:.2f}")
    
    @staticmethod
    def registrar_cancelacion_reserva(id_reserva, cliente):
        """Registra la cancelación de una reserva.
        
        Args:
            id_reserva (str): ID de la reserva
            cliente (str): Nombre del cliente
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.warning(f"RESERVA CANCELADA - ID: {id_reserva}, Cliente: {cliente}")
    
    @staticmethod
    def registrar_procesamiento_reserva(id_reserva, cliente):
        """Registra el procesamiento de una reserva.
        
        Args:
            id_reserva (str): ID de la reserva
            cliente (str): Nombre del cliente
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.info(f"RESERVA PROCESADA - ID: {id_reserva}, Cliente: {cliente}")
    
    @staticmethod
    def registrar_error_operacion(operacion, error):
        """Registra un error en una operación genérica.
        
        Args:
            operacion (str): Descripción de la operación
            error (str): Descripción del error
        """
        logger = LoggerGestionReserva().obtener_logger()
        logger.error(f"ERROR EN OPERACIÓN - {operacion}: {error}")
    
    @staticmethod
    def obtener_archivo_log():
        """Retorna la ruta del archivo de log.
        
        Returns:
            str: Ruta absoluta del archivo de log
        """
        return os.path.abspath(LoggerGestionReserva.ARCHIVO_LOG)
