# modelo/validador_modelo.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from .regresor_lineal import RegresorLinealMultiple

class ValidadorModelo:
    def __init__(self, regresor):
        self.regresor = regresor
        self.resultados = []
    
    def validacion_train_test(self, X, Y, test_size=0.2, random_state=42):
        try:
            X_train, X_test, Y_train, Y_test = train_test_split(
                X, Y, test_size=test_size, random_state=random_state
            )
            
            modelo_temp = RegresorLinealMultiple()
            success = modelo_temp.entrenar(X_train, Y_train, verbose=False)
            
            if not success:
                return {'error': 'Entrenamiento falló'}
            
            Y_pred_test = modelo_temp.predecir(X_test)
            Y_pred_train = modelo_temp.predecir(X_train)
            
            # ✅ LÍNEAS CORREGIDAS:
            r2_test = r2_score(Y_test, Y_pred_test)
            r2_train = r2_score(Y_train, Y_pred_train)
            r2_test = max(0, r2_test)   # Solo si es negativo
            r2_train = max(0, r2_train) # Solo si es negativo
            
            mae_test = mean_absolute_error(Y_test, Y_pred_test)
            
            resultado = {
                'r2_entrenamiento': round(r2_train, 4),
                'r2_prueba': round(r2_test, 4),
                'mae_prueba': round(mae_test, 2),
                'tamano_entrenamiento': len(X_train),
                'tamano_prueba': len(X_test)
            }
            
            self.resultados.append(resultado)
            return resultado
            
        except Exception as e:
            return {'error': f'Validación falló: {str(e)}'}
    
    def obtener_resumen_validacion(self):
        if not self.resultados:
            return "No hay validaciones"
        
        resumen = "VALIDACIÓN DEL MODELO:\n"
        for i, res in enumerate(self.resultados, 1):
            if 'error' in res:
                resumen += f"{i}. Error: {res['error']}\n"
            else:
                resumen += f"{i}. R² Entrenamiento: {res['r2_entrenamiento']}\n"
                resumen += f"   R² Prueba: {res['r2_prueba']}\n"
                resumen += f"   MAE Prueba: ${res['mae_prueba']:,.0f} USD\n"
        
        return resumen