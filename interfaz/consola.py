def mostrar_menu_principal() -> int:
    """
    Muestra el menú principal y obtiene la opción del usuario
    
    Returns:
        Opción seleccionada por el usuario
    """
    print("\n🏠 SISTEMA DE VALUACIÓN INMOBILIARIA")
    print("==================================")
    print("1. 📊 Realizar predicción de precio")
    print("2. 📈 Ver estadísticas del dataset")
    print("3. 🏘️  Ver dataset completo")
    print("4. ❌ Salir")
    print("==================================")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, ingrese un número entre 1 y 4")
        except ValueError:
            print("Por favor, ingrese un número válido")

def mostrar_resultados_prediccion(metros: float, precio_predicho: float, ecuacion: str):
    """
    Muestra los resultados de la predicción de forma formateada
    
    Args:
        metros: Metros cuadrados de la propiedad
        precio_predicho: Precio predicho por el modelo
        ecuacion: Ecuación del modelo
    """
    print(f"\n✅ RESULTADO DE LA PREDICCIÓN:")
    print(f"   • Propiedad: {metros:.1f} m²")
    print(f"   • Precio estimado: ${precio_predicho:,.0f} USD")
    print(f"   • Modelo utilizado: {ecuacion}")
    print(f"   • Valor aproximado: ${precio_predicho/1000:.1f}K USD")