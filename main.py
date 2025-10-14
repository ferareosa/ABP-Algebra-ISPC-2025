## proyecto_valuacion/
## │
## ├── 📁 .streamlit/                 # Configuración de Streamlit
## │   └── ⚙️ config.toml
## │
## ├── 📁 datos/                      # Todo lo relacionado a datos
## │   ├── 🐍 dataset_inmobiliario.py
## │   └── 🗃️ database_manager.py     # NUEVO - Base de datos
## │
## ├── 📁 modelo/                     # Modelos matemáticos
## │   ├── 🐍 regresor_lineal.py
## │   └── 🐍 validador_modelo.py
## │
## ├── 📁 interfaz/                   # Interfaz de usuario
## │   └── 🐍 app_streamlit.py
## │
## ├── 🚀 lanzador.py                 # NUEVO - Lanzador mejorado
## ├── 🪟 lanzador.bat                # NUEVO - Para Windows
## ├── 📋 requirements.txt
## └── 🐍 main.py

### Main - Ejecucion Principal

# main.py

### main.py - SISTEMA DEFINITIVO DE VALUACIÓN INMOBILIARIA

"""
🏠 SISTEMA DE VALUACIÓN INMOBILIARIA - VERSIÓN DEFINITIVA
ABP Álgebra Lineal - Regresión Lineal Múltiple
🌟 PROYECTO ESTRELLA - Arquitectura POO Completa
"""

from datos.dataset_inmobiliario import DatasetInmobiliario
from modelo.regresor_lineal import RegresorLinealMultiple
from modelo.validador_modelo import ValidadorModelo

def demostrar_sistema_completo():
    """DEMOSTRACIÓN DEL SISTEMA POO COMPLETO"""
    print("🌟" * 60)
    print("🏠 SISTEMA DE VALUACIÓN INMOBILIARIA - VERSIÓN DEFINITIVA")
    print("🌟" * 60)
    
    # 1. INICIALIZACIÓN DEL SISTEMA
    print("\n🎯 1. INICIALIZANDO SISTEMA COMPLETO...")
    dataset = DatasetInmobiliario()
    df = dataset.crear_dataset()
    print(f"   ✅ Base de datos: {len(df)} propiedades registradas")
    
    # 2. ESTADÍSTICAS AVANZADAS
    print("\n📊 2. ESTADÍSTICAS DEL MERCADO INMOBILIARIO:")
    print(f"   💰 Precio promedio: ${df['precio_usd'].mean():,.0f} USD")
    print(f"   📏 Metros cuadrados promedio: {df['m2'].mean():.1f} m²")
    print(f"   🛏️  Habitaciones promedio: {df['habitaciones'].mean():.1f}")
    print(f"   🏛️  Antigüedad promedio: {df['antiguedad'].mean():.1f} años")
    print(f"   📍 Distribución por zonas: {dict(df['zona_categoria'].value_counts().sort_index())}")
    
    # 3. ENTRENAMIENTO DEL MODELO DE MACHINE LEARNING
    print("\n🤖 3. ENTRENANDO MODELO DE REGRESIÓN LINEAL MÚLTIPLE...")
    X, Y = dataset.obtener_matrices_entrenamiento()
    modelo = RegresorLinealMultiple()
    exito = modelo.entrenar(X, Y, verbose=False)
    
    if exito:
        print(f"   ✅ Modelo entrenado con {X.shape[1]} variables predictoras")
        print(f"   🎯 Precisión del modelo (R²): {modelo.r2:.4f}")
        print(f"   📉 Error absoluto medio: ${modelo.mae:,.0f} USD")
        print(f"   ⚡ Raíz del error cuadrático: ${modelo.rmse:,.0f} USD")
    else:
        print("   ❌ Error en el entrenamiento del modelo")
        return
    
    # 4. VALIDACIÓN AVANZADA DEL MODELO
    print("\n🔍 4. VALIDACIÓN DEL MODELO CON MÉTRICAS AVANZADAS...")
    validador = ValidadorModelo(modelo)
    resultado = validador.validacion_train_test(X, Y)
    
    print(f"   ✅ Validación train/test completada")
    print(f"   📈 R² en entrenamiento: {resultado['r2_entrenamiento']:.4f}")
    print(f"   📊 R² en prueba: {resultado['r2_prueba']:.4f}")
    print(f"   💰 Error MAE en prueba: ${resultado['mae_prueba']:,.0f} USD")
    
    # 5. DEMOSTRACIÓN DE PREDICCIONES
    print("\n🔮 5. DEMOSTRACIÓN DE PREDICCIONES EN TIEMPO REAL:")
    
    # Ejemplo 1: Casa familiar
    print("\n   🏡 EJEMPLO 1 - CASA FAMILIAR:")
    print("      • 150m², 3 habitaciones, 8 años, Zona 2 (Céntrica), Casa")
    pred1 = modelo.predecir_instancia(150, 3, 8, 2, 1)
    print(f"      💰 Precio estimado: ${pred1:,.0f} USD")
    print(f"      📐 Precio por m²: ${pred1/150:,.0f} USD/m²")
    
    # Ejemplo 2: Departamento moderno
    print("\n   🏢 EJEMPLO 2 - DEPARTAMENTO MODERNO:")
    print("      • 85m², 2 habitaciones, 3 años, Zona 1 (Centro), Departamento")
    pred2 = modelo.predecir_instancia(85, 2, 3, 1, 2)
    print(f"      💰 Precio estimado: ${pred2:,.0f} USD")
    print(f"      📐 Precio por m²: ${pred2/85:,.0f} USD/m²")
    
    # Ejemplo 3: Propiedad económica
    print("\n   💰 EJEMPLO 3 - PROPIEDAD ECONÓMICA:")
    print("      • 90m², 2 habitaciones, 25 años, Zona 5 (Periferia), Casa")
    pred3 = modelo.predecir_instancia(90, 2, 25, 5, 1)
    print(f"      💰 Precio estimado: ${pred3:,.0f} USD")
    print(f"      📐 Precio por m²: ${pred3/90:,.0f} USD/m²")
    
    # 6. COEFICIENTES DEL MODELO
    print("\n🧮 6. ANÁLISIS DE COEFICIENTES DEL MODELO:")
    if hasattr(modelo, 'coeficientes') and modelo.coeficientes is not None:
        coefs = modelo.coeficientes
        variables = [
            "Intercepto (Valor base)",
            "Metros cuadrados (m²)",
            "Número de habitaciones", 
            "Antigüedad (años)",
            "Zona de ubicación",
            "Tipo de propiedad"
        ]
        
        for i, (var, coef) in enumerate(zip(variables, coefs)):
            impacto = "📈 Aumenta precio" if coef > 0 else "📉 Disminuye precio" if coef < 0 else "⚖️ Neutral"
            print(f"   • {var}: {coef:,.0f} USD - {impacto}")
    
    # 7. RESUMEN FINAL
    print("\n" + "⭐" * 60)
    print("🎉 ¡SISTEMA LISTO PARA PRODUCCIÓN!")
    print("⭐" * 60)
    print("\n🚀 PARA USAR LA INTERFAZ WEB:")
    print("   Ejecuta: python lanzador.py")
    print("   O directamente: streamlit run interfaz/app_streamlit.py")
    print("\n📊 CARACTERÍSTICAS DEL SISTEMA:")
    print("   • ✅ Base de datos SQLite integrada")
    print("   • ✅ 5 variables predictoras")
    print("   • ✅ Validación cruzada automática") 
    print("   • ✅ Interfaz web moderna con Streamlit")
    print("   • ✅ Gestión completa de propiedades")
    print("   • ✅ Análisis estadísticos avanzados")
    print("\n🌟 ¡PROYECTO ESTRELLA - LISTO PARA BRILLAR! 🌟")

if __name__ == "__main__":
    demostrar_sistema_completo()