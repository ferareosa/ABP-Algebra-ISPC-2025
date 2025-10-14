# modelo/servicios_modelo.py
import numpy as np

def preparar_entrada_prediccion(m2, habitaciones, antiguedad, zona, tipo_propiedad):
    return np.array([[m2, habitaciones, antiguedad, zona, tipo_propiedad]])

def obtener_metricas_modelo(modelo, X, Y):
    try:
        if not hasattr(modelo, 'entrenado') or not modelo.entrenado:
            return {'error': 'Modelo no entrenado'}

        Y_pred = modelo.predecir(X)
        mae = np.mean(np.abs(Y - Y_pred))
        rmse = np.sqrt(np.mean((Y - Y_pred)**2))
        
        # Cálculo simple y robusto de R²
        ss_res = np.sum((Y - Y_pred) ** 2)
        ss_tot = np.sum((Y - np.mean(Y)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        return {
            'R²': max(0.0, r2),  # R² nunca negativo
            'MAE (USD)': mae,
            'RMSE (USD)': rmse,
            'precision_porcentaje': max(0.0, r2) * 100
        }
        
    except Exception as e:
        return {'error': str(e)}

def obtener_coeficientes(modelo, dataset=None):
    try:
        if not hasattr(modelo, 'entrenado') or not modelo.entrenado:
            return {'error': 'Modelo no entrenado'}
        
        return modelo.obtener_coeficientes()
            
    except Exception as e:
        return {'error': str(e)}

def validar_datos_entrada(m2, habitaciones, antiguedad, zona, tipo_propiedad):
    errores = []
    
    if m2 <= 0 or m2 > 1000:
        errores.append("Metros cuadrados deben ser entre 1 y 1000")
    
    if habitaciones <= 0 or habitaciones > 10:
        errores.append("Habitaciones deben ser entre 1 y 10")
    
    if antiguedad < 0 or antiguedad > 100:
        errores.append("Antigüedad debe ser entre 0 y 100 años")
    
    if zona < 1 or zona > 5:
        errores.append("Zona debe ser entre 1 y 5")
    
    if tipo_propiedad not in [1, 2]:
        errores.append("Tipo de propiedad debe ser 1 (Casa) o 2 (Departamento)")
    
    return errores