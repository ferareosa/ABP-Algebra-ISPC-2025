proyecto_valuacion/
│
├── 📁 .streamlit/                      # Configuración de Streamlit
│   └── ⚙️ config.toml                  # Configuración de tema y servidor
│
├── 📁 datos/                           # Gestión de datos y base de datos
│   ├── 🐍 dataset_inmobiliario.py      # Clase principal del dataset
│   ├── 🗃️ database_manager.py          # Gestor de base de datos SQLite
│   └── 🐍 generador_datos.py           # Generador de datos sintéticos
│
├── 📁 modelo/                          # Modelos de machine learning
│   ├── 🐍 regresor_lineal.py           # RegresorLinealMultiple (modelo principal)
│   ├── 🐍 validador_modelo.py          # Validador con train/test y cross-validation
│   └── 🐍 servicios_modelo.py          # Funciones auxiliares para el modelo
│
├── 📁 interfaz/                        # Interfaz de usuario
│   └── 🐍 app_streamlit.py             # Aplicación web completa con Streamlit
│
├── 🚀 lanzador.py                      # Lanzador automático con navegador
├── 🪟 lanzador.bat                     # Lanzador para Windows
├── 📋 requirements.txt                 # Dependencias del proyecto
└── 🐍 main.py                          # Script principal de demostración


# REQUERIMIENTOS PARA SISTEMA DE VALUACIÓN INMOBILIARIA
# 🌟 PROYECTO ESTRELLA - Álgebra Lineal ABP

Debemos tener instaladas las siguientes versiones de librerias python:

streamlit>=1.28.0
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
seaborn>=0.11.0
scikit-learn>=1.0.0

# 1. Prueba del sistema
python main.py

# 2. Interfaz web completa - Desde Consola
python lanzador.py

# 3. Directo con Streamlit
streamlit run interfaz/app_streamlit.py

# WINDOWS - Doble clic en:
🪟 lanzador.bat

INSTRUCCIONES PARA EJECUTAR EL SISTEMA:

1. Instalar dependencias: pip install -r requirements.txt
2. Ejecutar: python lanzador.py
3. ¡Listo! Se abrirá automáticamente en el navegador
