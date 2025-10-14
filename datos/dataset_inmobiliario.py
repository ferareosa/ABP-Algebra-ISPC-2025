# datos/dataset_inmobiliario.py
import pandas as pd
import numpy as np
import sqlite3

try:
    from database_manager import DatabaseManager
except ImportError:
    from .database_manager import DatabaseManager

class DatasetInmobiliario:
    def __init__(self, db_path="inmuebles_cordoba.db"):
        self.db = DatabaseManager(db_path)
        self.df = None
        
        self.categorias_zona = {
            1: "Centro - Alta demanda",
            2: "Zona Céntrica - Excelente ubicación", 
            3: "Barrio Residencial - Tranquilo",
            4: "Área Suburbana - Espacios verdes",
            5: "Periferia - Precios accesibles"
        }
        
        self.tipos_propiedad = {
            1: "Casa",
            2: "Departamento"
        }
    
    def crear_dataset(self, usar_base_datos=True):
        if usar_base_datos:
            df_db = self.db.obtener_inmuebles()
            if len(df_db) > 0:
                self.df = df_db
                return self.df
            else:
                return self.cargar_datos_ejemplo()
        
        self.df = pd.DataFrame(columns=['m2', 'habitaciones', 'antiguedad', 'zona_categoria', 'tipo_propiedad', 'precio_usd'])
        return self.df
    
    def cargar_datos_ejemplo(self):
        data = {
            'm2': [85, 220, 180, 150, 120, 95, 250, 70, 200, 130, 140, 160, 90, 300, 120, 180, 150, 110, 100, 125, 280, 200, 170, 140, 190, 160, 135, 115, 155, 175],
            'habitaciones': [2, 4, 3, 3, 3, 2, 4, 1, 3, 3, 3, 3, 2, 5, 2, 3, 3, 2, 2, 3, 4, 3, 3, 2, 3, 3, 3, 2, 3, 3],
            'antiguedad': [5, 2, 8, 12, 15, 20, 3, 3, 10, 18, 8, 5, 25, 1, 6, 7, 9, 22, 20, 28, 4, 6, 11, 16, 8, 12, 14, 19, 13, 10],
            'zona_categoria': [1, 1, 2, 2, 3, 3, 1, 1, 2, 3, 4, 4, 5, 1, 1, 2, 3, 5, 5, 5, 2, 3, 4, 4, 2, 3, 4, 5, 3, 2],
            'tipo_propiedad': [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
            'precio_usd': [320000, 850000, 580000, 420000, 350000, 220000, 950000, 250000, 520000, 380000, 320000, 340000, 180000, 1200000, 280000, 450000, 380000, 240000, 210000, 260000, 620000, 440000, 360000, 290000, 480000, 400000, 330000, 250000, 410000, 470000]
        }
        
        df_ejemplo = pd.DataFrame(data)
        self.db.poblar_datos_iniciales(df_ejemplo)
        self.df = self.db.obtener_inmuebles()
        return self.df
    
    def obtener_matrices_entrenamiento(self):
        if self.df is None or len(self.df) == 0:
            self.crear_dataset()
        
        caracteristicas = ['m2', 'habitaciones', 'antiguedad', 'zona_categoria', 'tipo_propiedad']
        X = self.df[caracteristicas].values
        Y = self.df['precio_usd'].values
        return X, Y
    
    def agregar_propiedad(self, m2, habitaciones, antiguedad, zona_categoria, tipo_propiedad, precio_usd):
        success = self.db.insertar_inmueble(m2, habitaciones, antiguedad, zona_categoria, tipo_propiedad, precio_usd)
        if success:
            self.df = self.db.obtener_inmuebles()
        return success
    
    def actualizar_propiedad(self, id_inmueble, **kwargs):
        try:
            df_existente = self.db.obtener_inmuebles()
            if id_inmueble not in df_existente['id'].values:
                return False
            
            campos_permitidos = ['m2', 'habitaciones', 'antiguedad', 'zona_categoria', 'tipo_propiedad', 'precio_usd', 'activo']
            set_clause = []
            valores = []
            
            for campo, valor in kwargs.items():
                if campo in campos_permitidos:
                    set_clause.append(f"{campo} = ?")
                    valores.append(valor)
            
            if not set_clause:
                return False
            
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            query = f"UPDATE inmuebles SET {', '.join(set_clause)} WHERE id = ?"
            valores.append(id_inmueble)
            cursor.execute(query, valores)
            conn.commit()
            conn.close()
            
            self.df = self.db.obtener_inmuebles()
            return True
            
        except Exception as e:
            print(f"Error actualizando propiedad: {e}")
            return False
    
    def eliminar_propiedad(self, id_inmueble):
        try:
            df_existente = self.db.obtener_inmuebles()
            if id_inmueble not in df_existente['id'].values:
                return False
            
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE inmuebles SET activo = 0 WHERE id = ?", (id_inmueble,))
            conn.commit()
            conn.close()
            
            self.df = self.db.obtener_inmuebles()
            return True
            
        except Exception as e:
            print(f"Error eliminando propiedad: {e}")
            return False
    
    def limpiar_base_datos(self):
        try:
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inmuebles")
            conn.commit()
            conn.close()
            self.df = pd.DataFrame()
            return True
        except Exception as e:
            print(f"Error limpiando base de datos: {e}")
            return False
    
    def obtener_estadisticas(self):
        if self.df is None or len(self.df) == 0:
            return {"error": "Dataset vacío"}
        
        return {
            'total_propiedades': len(self.df),
            'precio_promedio': self.df['precio_usd'].mean(),
            'precio_minimo': self.df['precio_usd'].min(),
            'precio_maximo': self.df['precio_usd'].max(),
            'm2_promedio': self.df['m2'].mean(),
            'habitaciones_promedio': self.df['habitaciones'].mean(),
            'antiguedad_promedio': self.df['antiguedad'].mean()
        }
    
    def obtener_info_dataset(self):
        if self.df is None:
            return "Dataset no cargado"
        
        stats = self.obtener_estadisticas()
        if 'error' in stats:
            return stats['error']
        
        info = f"""
INFORMACIÓN DEL DATASET:
Propiedades registradas: {stats['total_propiedades']}
Precio promedio: ${stats['precio_promedio']:,.0f} USD
Rango de precios: ${stats['precio_minimo']:,.0f} - ${stats['precio_maximo']:,.0f} USD
Metros cuadrados promedio: {stats['m2_promedio']:.1f} m²
Habitaciones promedio: {stats['habitaciones_promedio']:.1f}
Antigüedad promedio: {stats['antiguedad_promedio']:.1f} años
        """
        return info

if __name__ == "__main__":
    dataset = DatasetInmobiliario()
    df = dataset.crear_dataset()
    X, Y = dataset.obtener_matrices_entrenamiento()
    print(f"Dataset creado: {len(df)} propiedades")
    print(f"Matriz X: {X.shape}, Vector Y: {Y.shape}")
    print(dataset.obtener_info_dataset())