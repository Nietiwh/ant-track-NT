import pandas as pd

def limpiar_datos(df_metodos_pago_sucios):
    df_metodos_pago_limpio = df_metodos_pago_sucios.copy()

# 1. Procesando los textos del dataframe sucio, eliminando los espacios en blanco con strip y convirtiendo 
# a minúsculas con lower para estandarizar los datos. 
# Seleccionar todas columnas de tipo texto y aplicar strip y lower a cada una de ellas  

    columnas_texto = ["forma_pago", "franquicia", "estado", "descripcion"]
    for columna in columnas_texto:
        df_metodos_pago_limpio[columna] = df_metodos_pago_limpio[columna].astype("string").str.strip().str.lower()
        
# 2. Limpiando los textos para controlar valores esperados

    valores_esperados_forma_pago = ['tarjeta de crédito', 'tarjeta de débito', 'efectivo', 'transferencia bancaria', 'paypal']
    df_metodos_pago_limpio["forma_pago"] = df_metodos_pago_limpio["forma_pago"].where(
        df_metodos_pago_limpio["forma_pago"].isin(valores_esperados_forma_pago), pd.NA)
    
    valores_esperados_franquicia = ['visa', 'mastercard', 'american express', 'discover', 'ninguna']
    df_metodos_pago_limpio["franquicia"] = df_metodos_pago_limpio["franquicia"].where(
        df_metodos_pago_limpio["franquicia"].isin(valores_esperados_franquicia), pd.NA)
    
    valores_esperados_estado = ['activo', 'inactivo']
    df_metodos_pago_limpio["estado"] = df_metodos_pago_limpio["estado"].where(
        df_metodos_pago_limpio["estado"].isin(valores_esperados_estado), pd.NA)
    
# 3. limpieza de datos numericos

    df_metodos_pago_limpio["id_metodo_pago"] = pd.to_numeric(df_metodos_pago_limpio["id_metodo_pago"])

#4. Verificar los valores esperados para los campos numéricos, que sean mayores o iguales a 0.

    df_metodos_pago_limpio = df_metodos_pago_limpio[df_metodos_pago_limpio["id_metodo_pago"] >= 1]

# 5. Limpieza de datos de fecha no aplica para MetodoPago, ya que no hay campos de fecha en esta tabla.

# 6. Novedades de datos vacios

    columnas_obligatorias = ["id_metodo_pago", "forma_pago", "franquicia", "estado"]
    df_metodos_pago_limpio = df_metodos_pago_limpio.dropna(subset=columnas_obligatorias)
    return df_metodos_pago_limpio


