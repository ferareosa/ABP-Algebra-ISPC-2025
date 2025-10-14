# datos/database_manager.py
import sqlite3
import pandas as pd
import os

class DatabaseManager:
    def __init__(self, db_path="inmuebles_cordoba.db"):
        self.db_path = db_path
        
        if os.path.exists(db_path):
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inmuebles'")
                tabla_existe = cursor.fetchone()
                
                if tabla_existe:
                    cursor.execute("SELECT COUNT(*) FROM inmuebles WHERE activo = 1")
                    cantidad_registros = cursor.fetchone()[0]
                    conn.close()
                    
                    if cantidad_registros == 0:
                        os.remove(db_path)
                    else:
                        self._crear_tabla()
                        return
                else:
                    os.remove(db_path)
                    
            except sqlite3.Error:
                os.remove(db_path)
            except Exception:
                if os.path.exists(db_path):
                    os.remove(db_path)
        
        self._crear_tabla()
    
    def _crear_tabla(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inmuebles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    m2 REAL NOT NULL,
                    habitaciones INTEGER NOT NULL,
                    antiguedad INTEGER NOT NULL,
                    zona_categoria INTEGER NOT NULL,
                    tipo_propiedad INTEGER NOT NULL,
                    precio_usd REAL NOT NULL,
                    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    activo BOOLEAN DEFAULT 1
                )
            ''')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_inmuebles_activo ON inmuebles(activo)')
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error creando tabla: {e}")
    
    def insertar_inmueble(self, m2, habitaciones, antiguedad, zona_categoria, tipo_propiedad, precio_usd):
        try:
            m2 = float(m2)
            habitaciones = int(habitaciones)
            antiguedad = int(antiguedad)
            zona_categoria = int(zona_categoria)
            tipo_propiedad = int(tipo_propiedad)
            precio_usd = float(precio_usd)
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inmuebles 
                (m2, habitaciones, antiguedad, zona_categoria, tipo_propiedad, precio_usd)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (m2, habitaciones, antiguedad, zona_categoria, tipo_propiedad, precio_usd))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error insertando inmueble: {e}")
            return False
    
    def obtener_inmuebles(self, solo_activos=True):
        try:
            conn = sqlite3.connect(self.db_path)
            query = "SELECT * FROM inmuebles WHERE activo = 1" if solo_activos else "SELECT * FROM inmuebles"
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error obteniendo inmuebles: {e}")
            return pd.DataFrame()
    
    def poblar_datos_iniciales(self, dataset):
        df_existente = self.obtener_inmuebles()
        if len(df_existente) == 0:
            exitos = 0
            for _, fila in dataset.iterrows():
                if self.insertar_inmueble(fila['m2'], fila['habitaciones'], fila['antiguedad'],
                                        fila['zona_categoria'], fila['tipo_propiedad'], fila['precio_usd']):
                    exitos += 1
            print(f"Se insertaron {exitos}/{len(dataset)} registros iniciales")

if __name__ == "__main__":
    db = DatabaseManager()
    print("DatabaseManager funcionando correctamente")