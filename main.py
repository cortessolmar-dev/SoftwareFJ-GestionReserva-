"""Archivo principal del sistema de gestión de reservas.

Punto de entrada para ejecutar las simulaciones del sistema.
"""

from simulacion import SimuladorReservas
from logger import LoggerGestionReserva


def main():
    """Función principal."""
    print("\n" + "#"*80)
    print("#" + " "*78 + "#")
    print("#" + "  SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS".center(78) + "#")
    print("#" + "  Desarrollado en Python con manejo robusto de excepciones".center(78) + "#")
    print("#" + " "*78 + "#")
    print("#"*80 + "\n")
    
    try:
        # Inicializar el logger
        logger = LoggerGestionReserva()
        print(f"\n✓ Sistema de logging inicializado")
        print(f"  Archivo de logs: {LoggerGestionReserva.obtener_archivo_log()}\n")
        
        # Crear y ejecutar el simulador
        simulador = SimuladorReservas()
        simulador.ejecutar_todas_las_simulaciones()
        
        print("\n" + "="*80)
        print("EJECUCIÓN COMPLETADA EXITOSAMENTE")
        print("="*80)
        print(f"\nPara ver los logs detallados, abre el archivo:")
        print(f"{LoggerGestionReserva.obtener_archivo_log()}\n")
        
    except Exception as e:
        print(f"\n✗ Error fatal: {str(e)}")
        LoggerGestionReserva.registrar_error_operacion("MAIN", str(e))
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
