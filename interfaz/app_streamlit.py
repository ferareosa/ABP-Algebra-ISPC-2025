####  app_streamlit.py

#### app_streamlit.py - VERSIÓN POO DELGADA
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datos.dataset_inmobiliario import DatasetInmobiliario
from modelo.regresor_lineal import RegresorLinealMultiple
from modelo.validador_modelo import ValidadorModelo
from modelo.servicios_modelo import (preparar_entrada_prediccion, 
                                   obtener_metricas_modelo, 
                                   obtener_coeficientes)

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Valuación Inmobiliaria - Córdoba",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-card {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

def inicializar_modelo():
    """Inicializa y entrena el modelo usando las clases POO"""
    try:
        dataset = DatasetInmobiliario()
        df = dataset.crear_dataset()
        X, Y = dataset.obtener_matrices_entrenamiento()
        
        modelo = RegresorLinealMultiple()
        modelo.entrenar(X, Y, verbose=False)
        
        validador = ValidadorModelo(modelo)
        validador.validacion_train_test(X, Y)
        
        return modelo, dataset, df, validador
    except Exception as e:
        st.error(f"Error al inicializar el modelo: {e}")
        return None, None, None, None

def mostrar_pagina_calculadora(modelo, dataset):
    """Página 1: Calculadora de precios"""
    st.header("🔮 Calculadora de Valuación Inmobiliaria")
    st.markdown("Ingresa las características de la propiedad para obtener una valuación precisa:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏗️ Características Físicas")
        m2 = st.slider("Metros cuadrados (m²)", 50, 500, 120)
        habitaciones = st.selectbox("Número de habitaciones", [1, 2, 3, 4, 5])
        antiguedad = st.slider("Antigüedad (años)", 0, 50, 10)
    
    with col2:
        st.subheader("📍 Ubicación y Tipo")
        zona = st.selectbox("Zona de Córdoba", options=list(dataset.categorias_zona.keys()),
                          format_func=lambda x: dataset.categorias_zona[x])
        tipo_propiedad = st.selectbox("Tipo de propiedad", options=list(dataset.tipos_propiedad.keys()),
                                    format_func=lambda x: dataset.tipos_propiedad[x])
    
    if st.button("🎯 Calcular Valuación", type="primary", use_container_width=True):
        try:
            X_pred = preparar_entrada_prediccion(m2, habitaciones, antiguedad, zona, tipo_propiedad)
            precio_predicho = modelo.predecir(X_pred)[0]
            
            # Mostrar resultado
            st.markdown("---")
            st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("💰 Precio Estimado", f"${precio_predicho:,.0f} USD")
            with col_res2:
                precio_m2 = precio_predicho / m2
                st.metric("📐 Precio por m²", f"${precio_m2:,.0f} USD/m²")
            with col_res3:
                X, Y = dataset.obtener_matrices_entrenamiento()
                metricas = obtener_metricas_modelo(modelo, X, Y)
                st.metric("🎯 Precisión del Modelo", f"{metricas['precision_porcentaje']:.1f}%")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error al calcular el precio: {e}")

def mostrar_pagina_analisis(modelo, dataset, df):
    """Página 2: Análisis del modelo"""
    st.header("📊 Análisis del Modelo Predictivo")
    
    X, Y = dataset.obtener_matrices_entrenamiento()
    metricas = obtener_metricas_modelo(modelo, X, Y)
    coefs = obtener_coeficientes(modelo, dataset)
    
    # Métricas principales
    col_met1, col_met2, col_met3, col_met4 = st.columns(4)
    with col_met1: st.metric("Precisión (R²)", f"{metricas['R²']:.4f}")
    with col_met2: st.metric("Error Absoluto Medio", f"${metricas['MAE (USD)']:,.0f} USD")
    with col_met3: st.metric("Error Cuadrático Medio", f"${metricas['RMSE (USD)']:,.0f} USD")
    with col_met4: st.metric("Propiedades en Dataset", f"{len(df)}")
    
    # Gráficos
    st.subheader("📈 Visualizaciones del Modelo")
    tab1, tab2, tab3 = st.tabs(["🎯 Predicciones vs Reales", "📊 Importancia de Variables", "📉 Análisis de Errores"])
    
    with tab1:
        Y_pred = modelo.predecir(X)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(Y, Y_pred, alpha=0.6, s=50)
        ax.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', lw=2)
        ax.set_xlabel('Precio Real (USD)'); ax.set_ylabel('Precio Predicho (USD)')
        ax.set_title(f'Validación: Real vs Predicho (R² = {metricas["R²"]:.4f})')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    with tab2:
        variables = list(coefs.keys())[1:]
        importancias = [abs(coefs[var]) for var in variables]
        fig, ax = plt.subplots(figsize=(10, 6))
        y_pos = np.arange(len(variables))
        bars = ax.barh(y_pos, importancias)
        ax.set_yticks(y_pos); ax.set_yticklabels(variables)
        ax.set_xlabel('Importancia (Valor Absoluto del Coeficiente)')
        ax.set_title('Importancia Relativa de las Variables')
        st.pyplot(fig)
    
    with tab3:
        residuos = Y - Y_pred
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(Y_pred, residuos, alpha=0.6, s=50)
        ax.axhline(y=0, color='red', linestyle='--', linewidth=2)
        ax.set_xlabel('Precio Predicho (USD)'); ax.set_ylabel('Residuos (USD)')
        ax.set_title('Análisis de Residuos')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

def mostrar_pagina_dataset(modelo, dataset, df, validador):
    """Página 3: Dataset y validación"""
    st.header("📈 Dataset y Validación del Modelo")
    
    # Mostrar dataset
    st.subheader("🏠 Dataset de Propiedades de Córdoba")
    df_display = df.copy()
    df_display['zona_categoria'] = df_display['zona_categoria'].map(dataset.categorias_zona)
    df_display['tipo_propiedad'] = df_display['tipo_propiedad'].map(dataset.tipos_propiedad)
    df_display['precio_usd'] = df_display['precio_usd'].apply(lambda x: f"${x:,.0f}")
    st.dataframe(df_display, use_container_width=True)
    
    # Estadísticas
    st.subheader("📊 Estadísticas Descriptivas")
    col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
    with col_stats1: st.metric("Precio Promedio", f"${df['precio_usd'].mean():,.0f} USD")
    with col_stats2: st.metric("Precio Mínimo", f"${df['precio_usd'].min():,.0f} USD")
    with col_stats3: st.metric("Precio Máximo", f"${df['precio_usd'].max():,.0f} USD")
    with col_stats4: st.metric("m² Promedio", f"{df['m2'].mean():.1f} m²")
    
    # Validación
    st.subheader("🔍 Validación del Modelo")
    st.text(validador.obtener_resumen_validacion())

def mostrar_pagina_gestion_datos(dataset):
    """Página 4: Gestión de datos"""
    st.header("🗃️ Gestión de Base de Datos")
    
    df_db = dataset.db.obtener_inmuebles()
    
    # Estado de la base de datos
    if len(df_db) == 0:
        st.info("🎯 **Sistema listo** - Se cargarán automáticamente datos de ejemplo")
    else:
        st.success(f"✅ **Base de datos activa** - {len(df_db)} propiedades cargadas")
    
    # Botones de administración
    col_admin1, col_admin2, col_admin3 = st.columns(3)
    with col_admin1:
        if st.button("🔄 Recargar datos de ejemplo"):
            dataset.limpiar_base_datos()
            dataset.cargar_datos_ejemplo()
            st.success("✅ Datos de ejemplo recargados")
            st.rerun()
    with col_admin2:
        if st.button("🗑️ Limpiar base de datos", type="secondary"):
            dataset.limpiar_base_datos()
            st.success("✅ Base de datos limpiada")
            st.rerun()
    
    # Tabs de gestión
    tab1, tab2, tab3 = st.tabs(["📊 Ver Datos", "➕ Agregar Propiedad", "✏️ Editar/Eliminar"])
    
    with tab1:
        st.subheader("Base de Datos Actual")
        if len(df_db) > 0:
            df_display = df_db.copy()
            df_display['zona'] = df_display['zona_categoria'].map(dataset.categorias_zona)
            df_display['tipo'] = df_display['tipo_propiedad'].map(dataset.tipos_propiedad)
            df_display['precio_usd'] = df_display['precio_usd'].apply(lambda x: f"${x:,.0f}")
            st.dataframe(df_display[['id', 'm2', 'habitaciones', 'antiguedad', 'zona', 'tipo', 'precio_usd']])
        else:
            st.warning("No hay propiedades en la base de datos")
    
    with tab2:
        st.subheader("Agregar Nueva Propiedad")
        with st.form("form_agregar"):
            col1, col2 = st.columns(2)
            with col1:
                m2_nuevo = st.number_input("Metros cuadrados (m²)", min_value=20, max_value=1000, value=100)
                habitaciones_nuevo = st.selectbox("Habitaciones", [1, 2, 3, 4, 5], index=2)
                antiguedad_nuevo = st.slider("Antigüedad (años)", 0, 100, 10)
            with col2:
                zona_nuevo = st.selectbox("Zona", options=list(dataset.categorias_zona.keys()),
                                        format_func=lambda x: dataset.categorias_zona[x])
                tipo_nuevo = st.selectbox("Tipo de propiedad", options=list(dataset.tipos_propiedad.keys()),
                                        format_func=lambda x: dataset.tipos_propiedad[x])
                precio_nuevo = st.number_input("Precio (USD)", min_value=10000, max_value=1000000, value=150000)
            
            if st.form_submit_button("💾 Guardar Propiedad"):
                dataset.agregar_propiedad(m2_nuevo, habitaciones_nuevo, antiguedad_nuevo, zona_nuevo, tipo_nuevo, precio_nuevo)
                st.success("✅ Propiedad agregada exitosamente!")
                st.rerun()

def mostrar_pagina_tecnica(modelo, dataset):
    """Página 5: Información técnica"""
    st.header("ℹ️ Información Técnica")
    
    col_math1, col_math2 = st.columns(2)
    with col_math1:
        st.markdown("""
        **🧮 Modelo de Regresión Lineal Múltiple:**
        ```
        Precio = β₀ + β₁·m² + β₂·hab + β₃·antig + β₄·zona + β₅·tipo
        ```
        
        **Solución Matricial:**
        ```
        β = (XᵀX)⁻¹XᵀY
        ```
        """)
    with col_math2:
        st.markdown("""
        **📊 Variables del Modelo:**
        - **m²**: Metros cuadrados
        - **hab**: Número de habitaciones  
        - **antig**: Años de antigüedad
        - **zona**: Categoría de ubicación (1-5)
        - **tipo**: Tipo de propiedad (1=Casa, 2=Departamento)
        """)
    
    # Coeficientes
    st.subheader("📈 Coeficientes del Modelo Actual")
    X, Y = dataset.obtener_matrices_entrenamiento()
    coefs = obtener_coeficientes(modelo, dataset)
    
    col_coef1, col_coef2 = st.columns(2)
    with col_coef1:
        for var, valor in list(coefs.items())[:3]:
            st.write(f"**{var}**: {valor:,.0f}")
    with col_coef2:
        for var, valor in list(coefs.items())[3:]:
            st.write(f"**{var}**: {valor:,.0f}")
    
    # Métricas
    st.subheader("🎯 Métricas de Evaluación")
    metricas = obtener_metricas_modelo(modelo, X, Y)
    for nombre, valor in metricas.items():
        if "USD" in nombre: st.write(f"**{nombre}**: {valor:,.0f}")
        else: st.write(f"**{nombre}**: {valor:.4f}")

def main():
    """Función principal de la aplicación Streamlit"""
    # Header principal
    st.markdown('<h1 class="main-header">🏠 Sistema de Valuación Inmobiliaria</h1>', unsafe_allow_html=True)
    st.markdown("### 📍 Córdoba Capital - Modelo Predictivo con Álgebra Lineal")
    
    # Inicializar modelo (solo una vez)
    if 'modelo' not in st.session_state:
        with st.spinner("🤖 Cargando modelo de inteligencia artificial..."):
            modelo, dataset, df, validador = inicializar_modelo()
            if modelo:
                st.session_state.modelo = modelo
                st.session_state.dataset = dataset
                st.session_state.df = df
                st.session_state.validador = validador
                st.success("✅ Modelo cargado exitosamente!")
    
    if 'modelo' not in st.session_state:
        st.error("No se pudo cargar el modelo. Por favor, verifica los archivos.")
        return
    
    # Obtener datos del estado de sesión
    modelo = st.session_state.modelo
    dataset = st.session_state.dataset
    df = st.session_state.df
    validador = st.session_state.validador
    
    # Sidebar - Navegación
    st.sidebar.title("🧭 Navegación")
    pagina = st.sidebar.radio("Selecciona una sección:", [
        "🔮 Calculadora de Precios", "📊 Análisis del Modelo", "📈 Dataset y Validación", 
        "🗃️ Gestión de Datos", "ℹ️ Información Técnica"
    ])
    
    # Navegación entre páginas
    if pagina == "🔮 Calculadora de Precios":
        mostrar_pagina_calculadora(modelo, dataset)
    elif pagina == "📊 Análisis del Modelo":
        mostrar_pagina_analisis(modelo, dataset, df)
    elif pagina == "📈 Dataset y Validación":
        mostrar_pagina_dataset(modelo, dataset, df, validador)
    elif pagina == "🗃️ Gestión de Datos":
        mostrar_pagina_gestion_datos(dataset)
    else:  # Información Técnica
        mostrar_pagina_tecnica(modelo, dataset)

if __name__ == "__main__":
    main()