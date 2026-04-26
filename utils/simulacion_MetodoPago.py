# Simulando datos de la tabla MetodoPago

import random

# Listas definidas fuera de la función
LISTA_FORMA_PAGO = ['Tarjeta de Crédito', 'Tarjeta de Débito', 'Efectivo',
                    'Transferencia Bancaria', 'PayPal']

LISTA_FRANQUICIA = ['Visa', 'MasterCard', 'American Express', 'Discover', 'Ninguna']

LISTA_ESTADO = ['Activo', 'Inactivo']

LISTA_DESCRIPCION = [
    'Pago realizado con tarjeta de crédito',
    'Pago realizado con tarjeta de débito',
    'Efectivo entregado al vendedor',
    'Pago realizado mediante transferencia bancaria',
    'Pago realizado a través de PayPal'
]

# Función para generar datos simulados de MetodoPago

def generar_metodos_pago(cantidad):
    metodos_pago_simulados = []
    
    for i in range(1, cantidad + 1):  
        metodo = {
            'id_metodo_pago': i, 
            'forma_pago': random.choice(LISTA_FORMA_PAGO),
            'franquicia': random.choice(LISTA_FRANQUICIA),
            'estado': random.choice(LISTA_ESTADO),
            'descripcion': random.choice(LISTA_DESCRIPCION)
        }

        #Inyectamos errores controlados para simular datos más realistas

        probabilidad_error=random.random()  # Genera un número entre 0 y 1 
        if probabilidad_error < 0.05:  # 5% de probabilidad de error
            metodo['forma_pago'] = 'Desconocida'  # Valor no válido para forma_pago
        elif probabilidad_error < 0.10:  # Otro 5% de probabilidad de error
            metodo['franquicia'] = 'N/A'  # Valor no válido para franquicia
        elif probabilidad_error < 0.15:  # Otro 5% de probabilidad de error
            metodo['estado'] = 'Pendiente'  # Valor no válido para estado
        
        
        metodos_pago_simulados.append(metodo)
    
    return metodos_pago_simulados






