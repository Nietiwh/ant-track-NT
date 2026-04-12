
# 🐜 ant-track — Análisis de Gastos Hormiga con Python

# Maria Fernanda Herrera A.
# Santiago 
# Aureliano Velasquez
# Maricela 
# Julian P


> *"Las hormigas son pequeñas, pero en colonia pueden mover montañas... y vaciar tu billetera."*

**ant-track** es el módulo de análisis de datos del ecosistema **AntTrack**, una solución educativa integral para la gestión y control de **gastos hormiga** — esos pequeños desembolsos diarios que pasan desapercibidos pero que, acumulados, impactan significativamente tus finanzas personales. ☕🛒🚗

Este repositorio forma parte de una arquitectura de tres capas:

| Capa | Tecnología | Repositorio |
|------|-----------|-------------|
| 📊 Análisis de datos | **Python + Pandas** | ← *Estás aquí* |
| 🎨 Frontend | React | `ant-track-frontend` |
| ⚙️ Backend | Spring Boot | `ant-track-backend` |

---

## 🎯 ¿Qué hace este módulo?

El módulo Python de **ant-track** se encarga de:

- 🔍 **Explorar y limpiar** datos de transacciones financieras
- 📈 **Detectar patrones** de gastos hormiga por categoría, día y frecuencia
- 📉 **Generar métricas** de consumo: promedios, tendencias y proyecciones mensuales
- 📊 **Visualizar** el impacto acumulado de los micro-gastos en el tiempo
- 🤖 **Exportar resultados** procesados para ser consumidos por el backend en Spring Boot

---

## 🧱 Tecnologías principales

- 🐍 **Python 3.10+**
- 🐼 **Pandas** — manipulación y análisis de datos tabulares
- 📊 **Matplotlib / Seaborn** — visualización de datos
- 🔢 **NumPy** — operaciones numéricas
- 📓 **Jupyter Notebook** — exploración interactiva
- 🧪 **pytest** — pruebas unitarias

---

## ⚙️ Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- ✅ Python `>= 3.10`
- ✅ `pip` o `conda`
- ✅ (Opcional) `virtualenv` o `venv`

---

## 🚀 Instalación

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/tu-usuario/ant-track.git
cd ant-track
```

### 2️⃣ Crea y activa un entorno virtual
```bash
# Crear entorno virtual
python -m venv .venv

# Activar en Linux / macOS
source .venv/bin/activate

# Activar en Windows
.venv\Scripts\activate
```

### 3️⃣ Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Instalación manual de las librerías principales
```bash
# Análisis de datos
pip install pandas

# Computación numérica
pip install numpy

# Visualización
pip install matplotlib seaborn

# Notebooks interactivos
pip install jupyter

# Pruebas
pip install pytest
```

---

## 📁 Estructura del proyecto
```
ant-track/
│
├── 📂 data/                  # Datasets de ejemplo y datos crudos
│   ├── raw/                  # Datos sin procesar
│   └── processed/            # Datos limpios y transformados
│
├── 📂 notebooks/             # Análisis exploratorio (Jupyter)
│   └── exploracion_gastos.ipynb
│
├── 📂 src/                   # Código fuente principal
│   ├── loader.py             # Carga y validación de datos
│   ├── cleaner.py            # Limpieza y normalización
│   ├── analyzer.py           # Análisis de patrones y métricas
│   └── visualizer.py         # Generación de gráficas
│
├── 📂 tests/                 # Pruebas unitarias
│   └── test_analyzer.py
│
├── 📂 exports/               # Resultados exportados para el backend
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Uso rápido
```python
import pandas as pd
from src.loader import cargar_gastos
from src.analyzer import resumen_mensual

# Cargar datos
df = cargar_gastos("data/raw/gastos_marzo.csv")

# Obtener resumen mensual
resumen = resumen_mensual(df)
print(resumen)
```

Para exploración interactiva, lanza Jupyter:
```bash
jupyter notebook notebooks/exploracion_gastos.ipynb
```

---

## 🧪 Ejecutar pruebas
```bash
pytest tests/ -v
```

---

## 🤝 Contribuciones

¡Este es un proyecto educativo y abierto a mejoras! Si deseas contribuir:

1. Haz un fork del repositorio 🍴
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m "✨ Agrega nueva funcionalidad"`
4. Envía un pull request 🚀

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

<p align="center">
  Hecho con 🐜 y ☕ para aprender a cuidar cada peso.
</p># ant-track-NT
