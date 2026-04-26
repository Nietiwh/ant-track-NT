
🐜 ant-track — Análisis de Gastos Hormiga con Python
Equipo de desarrollo:

Maria Fernanda Herrera A.

Santiago

Aureliano Velasquez

Maricela

Julian P

"Las hormigas son pequeñas, pero en colonia pueden mover montañas... y vaciar tu billetera."

ant-track es el módulo de análisis de datos del ecosistema AntTrack, una solución educativa integral para la gestión y control de gastos hormiga. Este repositorio se encarga de la simulación, limpieza y procesamiento de micro-gastos diarios.

Este repositorio forma parte de una arquitectura de tres capas:

  Capa	                   Tecnología	             Repositorio
📊 Análisis de datos	   Python + Pandas	       ← Estámos aquí
🎨 Frontend	             React	                 ant-track-frontend
⚙️ Backend	             Spring Boot	           ant-track-backend

🎯 ¿Qué hace este módulo?
🎲 Simulación de datos: Generación de transacciones realistas con métodos de pago y franquicias.

🧪 Limpieza automatizada: Procesamiento de strings (strip/lower) y manejo de valores nulos o erróneos.

📁 Gestión de archivos: Exportación de resultados a formatos JSON y CSV para integración con el backend.

📈 Análisis estadístico: Detección de patrones de consumo y proyecciones financieras.

📁 Estructura del proyecto (Real)
Plaintext
ant-track/
│
├── 📂 data/                    # Archivos generados (JSON/CSV)
├── 📂 notebook/                # Procesamiento y limpieza
│   └── limpieza.py             # Funciones de depuración de datos
├── 📂 utils/                   # Herramientas de soporte
│   └── simulacion_MetodoPago.py # Lógica de simulación aleatoria
├── main.py                     # Script principal de ejecución
├── generador.py                # Funciones de exportación de archivos
└── README.md
🧱 Tecnologías principales
🐍 Python 3.10+

🐼 Pandas — Manipulación de datos tabulares.

🎲 Random — Generación de datos sintéticos con probabilidad de error controlada.

📂 OS — Manejo dinámico de rutas y directorios.

🚀 Uso Rápido
Para ejecutar el pipeline de simulación y limpieza actual:

from utils.simulacion_MetodoPago import generar_metodos_pago
from notebook.limpieza import limpiar_datos
import pandas as pd

# Generar 10 simulaciones
data = generar_metodos_pago(10)
df = pd.DataFrame(data)

# Aplicar limpieza estandarizada
df_limpio = limpiar_datos(df)
print(df_limpio)

🤝 Contribuciones
Haz un fork del repositorio 🍴

Crea una rama: git checkout -b feature/nueva-funcionalidad

Realiza tus cambios y haz commit: git commit -m "✨ Agrega nueva funcionalidad"

Envía un pull request 🚀