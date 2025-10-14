## Utils Visualizador
# utils-visualizador.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class VisualizadorResultados:
    def __init__(self, estilo='seaborn'):
        plt.style.use(estilo)
        self.figsize = (12, 8)
    
    def grafico_real_vs_predicho(self, Y_real, Y_predicho, r2):
        """Grafica valores reales vs predichos"""
        fig, ax = plt.subplots(figsize=self.figsize)
        
        ax.scatter(Y_real, Y_predicho, alpha=0.7, s=60, color='blue')
        ax.plot([Y_real.min(), Y_real.max()], [Y_real.min(), Y_real.max()], 
                'r--', lw=2, label='Predicción Perfecta')
        
        ax.set_xlabel('Precio Real (USD)', fontsize=12)
        ax.set_ylabel('Precio Predicho (USD)', fontsize=12)
        ax.set_title(f'Validación: Real vs Predicho\n(R² = {r2:.4f})', fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def grafico_residuos(self, Y_predicho, residuos):
        """Grafica análisis de residuos"""
        fig, ax = plt.subplots(figsize=self.figsize)
        
        ax.scatter(Y_predicho, residuos, alpha=0.7, s=60, color='green')
        ax.axhline(y=0, color='red', linestyle='--', linewidth=2)
        
        ax.set_xlabel('Precio Predicho (USD)', fontsize=12)
        ax.set_ylabel('Residuos (USD)', fontsize=12)
        ax.set_title('Análisis de Residuos del Modelo', fontsize=14)
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def grafico_importancia_variables(self, coeficientes, nombres_variables):
        """Grafica la importancia de las variables"""
        # Excluir el intercepto
        coef_importancia = np.abs(coeficientes[1:])
        variables = nombres_variables[1:]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        y_pos = np.arange(len(variables))
        ax.barh(y_pos, coef_importancia)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(variables)
        ax.set_xlabel('Importancia (Valor Absoluto del Coeficiente)')
        ax.set_title('Importancia Relativa de Variables en el Modelo')
        ax.grid(True, alpha=0.3, axis='x')
        
        return fig
    
    def grafico_error_porcentual(self, Y_real, Y_predicho):
        """Grafica la distribución del error porcentual"""
        error_porcentual = np.abs((Y_real - Y_predicho) / Y_real) * 100
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.hist(error_porcentual, bins=15, alpha=0.7, edgecolor='black', color='orange')
        ax.axvline(np.mean(error_porcentual), color='red', linestyle='--', 
                  label=f'Promedio: {np.mean(error_porcentual):.1f}%')
        
        ax.set_xlabel('Error Porcentual (%)')
        ax.set_ylabel('Frecuencia')
        ax.set_title('Distribución del Error Porcentual de Predicción')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return fig
    

