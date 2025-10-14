#### lanzador.py

import os
import webbrowser
import threading
import time

def abrir_navegador():
    """Abre el navegador automáticamente"""
    time.sleep(3)
    webbrowser.open("http://localhost:8501")

def main():
    print("🚀 Iniciando Sistema de Valuación Inmobiliaria...")
    print("📊 Cargando modelo predictivo...")
    print("🌐 La aplicación se abrirá automáticamente en tu navegador")
    
    # Abrir navegador en segundo plano
    threading.Thread(target=abrir_navegador, daemon=True).start()
    
    # Ejecutar Streamlit
    os.system("streamlit run interfaz/app_streamlit.py --server.headless true --browser.gatherUsageStats false")

if __name__ == "__main__":
    main()