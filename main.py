import pandas as pd

#Zona para importar simulaciones
from utils.simulacion_MetodoPago import generar_metodos_pago

#Zona para importar limpieza
from notebook.limpieza import limpiar_datos

#Creando las simulaciones para la tabla MetodoPago
metodos_pago_simulados = generar_metodos_pago(10)

#Ordenando las simulaciones 
simulaciones_ordenadas_metodo_pago = pd.DataFrame(metodos_pago_simulados)

# Limpiando el set de datos
df_metodos_pago_limpio = limpiar_datos(simulaciones_ordenadas_metodo_pago)
print(df_metodos_pago_limpio)












