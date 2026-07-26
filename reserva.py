"""Módulo de gestión de reservas.

Define la clase Reserva con métodos para confirmar, cancelar y procesar reservas.
"""

from excepciones import (
    FechaInvalida, CapacidadExcedida, ReservaNoDisponible
)
from datetime import datetime
from enum import Enum


class EstadoReserva(Enum):
    """Estados posibles de una reserva."""
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    COMPLETADA = "Completada"


class Reserva:
    """Clase que representa una reserva en el sistema.
    
    Atributos:
        id (str): Identificador único de la reserva
        cliente (Cliente): Cliente que realiza la reserva
        servicio (Servicio): Servicio a reservar
        fecha (str): Fecha de la reserva en formato YYYY-MM-DD
        cantidad_personas (int): Cantidad de personas
        estado (EstadoReserva): Estado actual de la reserva
        costo_total (float): Costo total de la reserva
        fecha_creacion (str): Fecha de creación de la reserva
    """
    
    _contador_reservas = 0
    
    def __init__(self, cliente, servicio, fecha, cantidad_personas):
        """Inicializa una nueva reserva.
        
        Args:
            cliente (Cliente): Cliente que realiza la reserva
            servicio (Servicio): Servicio a reservar
            fecha (str): Fecha de la reserva en formato YYYY-MM-DD
            cantidad_personas (int): Cantidad de personas
            
        Raises:
            FechaInvalida: Si la fecha es inválida
            CapacidadExcedida: Si se excede la capacidad del servicio
        """
        try:
            self._validar_fecha(fecha)
            self._validar_cantidad_personas(cantidad_personas)
            self._validar_disponibilidad(servicio, fecha, cantidad_personas)
            
            Reserva._contador_reservas += 1
            self._id = f"RES-{Reserva._contador_reservas:05d}"
            self._cliente = cliente
            self._servicio = servicio
            self._fecha = fecha
            self._cantidad_personas = cantidad_personas
            self._estado = EstadoReserva.PENDIENTE
            self._costo_total = self._calcular_costo()
            self._fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        except (ValueError, FechaInvalida, CapacidadExcedida) as e:
            raise
    
    @staticmethod
    def _validar_fecha(fecha):
        """Valida que la fecha sea válida y futura.
        
        Args:
            fecha (str): Fecha en formato YYYY-MM-DD
            
        Raises:
            FechaInvalida: Si la fecha es inválida o pasada
        """
        try:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
            if fecha_obj < datetime.now():
                raise FechaInvalida("La fecha debe ser futura")
        except ValueError:
            raise FechaInvalida(f"Formato de fecha inválido: {fecha}. Use YYYY-MM-DD")
    
    @staticmethod
    def _validar_cantidad_personas(cantidad):
        """Valida la cantidad de personas.
        
        Args:
            cantidad (int): Cantidad de personas
            
        Raises:
            ValueError: Si la cantidad es inválida
        """
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad de personas debe ser un número entero positivo")
    
    @staticmethod
    def _validar_disponibilidad(servicio, fecha, cantidad):
        """Valida la disponibilidad del servicio.
        
        Args:
            servicio (Servicio): Servicio a validar
            fecha (str): Fecha de la reserva
            cantidad (int): Cantidad de personas
            
        Raises:
            CapacidadExcedida: Si se excede la capacidad
        """
        disponibilidad = servicio.obtener_disponibilidad(fecha)
        if cantidad > disponibilidad:
            raise CapacidadExcedida(
                f"Capacidad insuficiente. Disponibles: {disponibilidad}, Solicitados: {cantidad}"
            )
    
    def _calcular_costo(self):
        """Calcula el costo total de la reserva.
        
        Returns:
            float: Costo total de la reserva
        """
        costo_base = self._servicio.precio * self._cantidad_personas
        costo_adicional = self._servicio.calcular_costo_adicional(self._cantidad_personas)
        return costo_base + costo_adicional
    
    def confirmar(self):
        """Confirma la reserva.
        
        Returns:
            bool: True si se confirmó exitosamente
            
        Raises:
            ReservaNoDisponible: Si la reserva no puede confirmarse
        """
        try:
            if self._estado != EstadoReserva.PENDIENTE:
                raise ReservaNoDisponible(
                    f"No se puede confirmar una reserva en estado {self._estado.value}"
                )
            self._estado = EstadoReserva.CONFIRMADA
            self._cliente.agregar_reserva(self)
            self._servicio.reservas.append(self)
            return True
        except ReservaNoDisponible:
            raise
    
    def cancelar(self):
        """Cancela la reserva.
        
        Returns:
            bool: True si se canceló exitosamente
            
        Raises:
            ReservaNoDisponible: Si la reserva no puede cancelarse
        """
        try:
            if self._estado == EstadoReserva.CANCELADA:
                raise ReservaNoDisponible("La reserva ya ha sido cancelada")
            if self._estado == EstadoReserva.COMPLETADA:
                raise ReservaNoDisponible("No se puede cancelar una reserva completada")
            
            self._estado = EstadoReserva.CANCELADA
            if self in self._servicio.reservas:
                self._servicio.reservas.remove(self)
            return True
        except ReservaNoDisponible:
            raise
    
    def procesar(self):
        """Procesa la reserva (cambiar a completada).
        
        Returns:
            bool: True si se procesó exitosamente
            
        Raises:
            ReservaNoDisponible: Si la reserva no puede procesarse
        """
        try:
            if self._estado != EstadoReserva.CONFIRMADA:
                raise ReservaNoDisponible(
                    f"Solo se pueden procesar reservas confirmadas. Estado actual: {self._estado.value}"
                )
            self._estado = EstadoReserva.COMPLETADA
            return True
        except ReservaNoDisponible:
            raise
    
    # Propiedades (Encapsulación)
    @property
    def id(self):
        """Retorna el ID de la reserva."""
        return self._id
    
    @property
    def cliente(self):
        """Retorna el cliente de la reserva."""
        return self._cliente
    
    @property
    def servicio(self):
        """Retorna el servicio de la reserva."""
        return self._servicio
    
    @property
    def fecha(self):
        """Retorna la fecha de la reserva."""
        return self._fecha
    
    @property
    def cantidad_personas(self):
        """Retorna la cantidad de personas de la reserva."""
        return self._cantidad_personas
    
    @property
    def estado(self):
        """Retorna el estado de la reserva."""
        return self._estado
    
    @property
    def costo_total(self):
        """Retorna el costo total de la reserva."""
        return self._costo_total
    
    @property
    def fecha_creacion(self):
        """Retorna la fecha de creación de la reserva."""
        return self._fecha_creacion
    
    def __str__(self):
        """Representación en string de la reserva."""
        return (f"Reserva(id={self._id}, cliente={self._cliente.nombre}, "
                f"servicio={self._servicio.nombre}, fecha={self._fecha}, "
                f"personas={self._cantidad_personas}, estado={self._estado.value})")
    
    def __repr__(self):
        """Representación oficial de la reserva."""
        return self.__str__()
