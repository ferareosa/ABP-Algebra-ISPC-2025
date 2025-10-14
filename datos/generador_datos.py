import random
from typing import List, Dict

def generar_dataset_propiedades(n: int = 30) -> List[Dict]:
    """
    Genera un dataset sintético de propiedades inmobiliarias
    
    Args:
        n: Número de propiedades a generar
        
    Returns:
        Lista de diccionarios con información de propiedades
    """
    # Ubicaciones disponibles
    ubicaciones = ["Centro", "Norte", "Sur", "Este", "Oeste", "Zona Céntrica", 
                   "Barrio Residencial", "Área Suburbana", "Distrito Financiero"]
    
    dataset = []
    
    for i in range(n):
        # Generar metros cuadrados (entre 40 y 300 m²)
        metros_cuadrados = random.randint(40, 300)
        
        # Precio base por m² (entre 1500 y 4000 USD/m²)
        precio_base_m2 = random.uniform(1500, 4000)
        
        # Calcular precio base
        precio_base = metros_cuadrados * precio_base_m2
        
        # Ajustes por características adicionales
        habitaciones = random.randint(1, 5)
        banios = max(1, habitaciones - random.randint(0, 1))
        
        # Ajuste por habitaciones y baños
        ajuste_habitaciones = precio_base * (habitaciones * 0.05)
        ajuste_banios = precio_base * (banios * 0.03)
        
        # Ajuste por ubicación (factor aleatorio entre 0.8 y 1.5)
        factor_ubicacion = random.uniform(0.8, 1.5)
        
        # Precio final
        precio_final = (precio_base + ajuste_habitaciones + ajuste_banios) * factor_ubicacion
        
        # Redondear a miles
        precio_final = round(precio_final / 1000) * 1000
        
        propiedad = {
            'id': i + 1,
            'metros_cuadrados': metros_cuadrados,
            'precio': precio_final,
            'ubicacion': random.choice(ubicaciones),
            'habitaciones': habitaciones,
            'banios': banios
        }
        
        dataset.append(propiedad)
    
    return dataset

if __name__ == "__main__":
    # Test del generador
    propiedades = generar_dataset_propiedades(5)
    for prop in propiedades:
        print(f"{prop['metros_cuadrados']} m² - ${prop['precio']:,.0f} - {prop['ubicacion']}")