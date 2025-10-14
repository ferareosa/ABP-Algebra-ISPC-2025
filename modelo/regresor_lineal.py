# modelo/regresor_lineal.py
import numpy as np

class RegresorLinealMultiple:
    def __init__(self):
        self.coeficientes = None
        self.entrenado = False
        self.r2 = 0.0
        self.mae = 0.0
        self.rmse = 0.0
        self.mse = 0.0
    
    def entrenar(self, X, Y, verbose=True):
        try:
            X = np.array(X)
            Y = np.array(Y).flatten()
            
            X_con_intercepto = np.column_stack([np.ones(len(X)), X])
            
            # Calcular coeficientes
            XT = X_con_intercepto.T
            XTX = XT @ X_con_intercepto
            XTX_inv = np.linalg.pinv(XTX)  # Usar pseudoinversa para estabilidad
            XTY = XT @ Y
            self.coeficientes = XTX_inv @ XTY
            self.entrenado = True
            
            # Calcular métricas
            Y_pred = X_con_intercepto @ self.coeficientes
            self.mae = np.mean(np.abs(Y - Y_pred))
            self.mse = np.mean((Y - Y_pred) ** 2)
            self.rmse = np.sqrt(self.mse)
            
            # R² seguro
            ss_res = np.sum((Y - Y_pred) ** 2)
            ss_tot = np.sum((Y - np.mean(Y)) ** 2)
            self.r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            self.r2 = max(0, min(self.r2, 1))  # Forzar entre 0 y 1
            
            if verbose:
                print(f"✅ Modelo entrenado - R²: {self.r2:.4f}")
                print(f"📊 MAE: ${self.mae:,.0f} USD")
                print(f"📈 RMSE: ${self.rmse:,.0f} USD")
            
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def predecir(self, X):
        if not self.entrenado:
            return np.zeros(len(X))
        
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        X_con_intercepto = np.column_stack([np.ones(len(X)), X])
        return X_con_intercepto @ self.coeficientes
    
    def predecir_instancia(self, m2, habitaciones, antiguedad, zona, tipo_propiedad):
        return self.predecir([[m2, habitaciones, antiguedad, zona, tipo_propiedad]])[0]
    
    def obtener_metricas(self):
        return {
            "R²": round(self.r2, 4),
            "MSE": round(self.mse, 2),
            "MAE (USD)": round(self.mae, 2),
            "RMSE (USD)": round(self.rmse, 2),
            "precision_porcentaje": round(self.r2 * 100, 2)
        }
    
    def obtener_coeficientes(self):
        if not self.entrenado:
            return {"error": "Modelo no entrenado"}
        
        if self.coeficientes is None:
            return {"error": "Coeficientes no calculados"}
            
        # Solo los coeficientes que necesitamos
        coef_dict = {
            "Intercepto (β₀)": round(self.coeficientes[0], 4),
            "m² (β₁)": round(self.coeficientes[1], 4),
            "Habitaciones (β₂)": round(self.coeficientes[2], 4),
            "Antigüedad (β₃)": round(self.coeficientes[3], 4),
            "Zona (β₄)": round(self.coeficientes[4], 4),
            "Tipo (β₅)": round(self.coeficientes[5], 4) if len(self.coeficientes) > 5 else 0
        }
        return coef_dict