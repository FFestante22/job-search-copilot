import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# 1. Configuración Inicial
PALABRAS_PROHIBIDAS = ['autónomo', 'freelance', 'b2b', 'facturar', 'alta en el reta', 'cuenta propia']
ARCHIVO_CSV = "tracker_ofertas_aprobadas.csv"

def analizar_oferta(url):
    """Extrae el texto y aplica el filtro legal."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            texto_oferta = BeautifulSoup(respuesta.text, 'html.parser').get_text(separator=' ', strip=True).lower()
            
            for palabra in PALABRAS_PROHIBIDAS:
                if palabra in texto_oferta:
                    return False, f"Descartada (Contiene: '{palabra}')"
            return True, "Aprobada"
        else:
            return False, f"Error de conexión ({respuesta.status_code})"
    except Exception as e:
        return False, f"Error: {e}"

def procesar_y_guardar(url, empresa, puesto, plataforma):
    """Orquesta el análisis y guarda en CSV si es apta."""
    print(f"\n⏳ Analizando: {puesto} en {empresa}...")
    
    es_apta, mensaje = analizar_oferta(url)
    
    if not es_apta:
        print(f"❌ {mensaje}")
        return

    # Si es apta, preparamos los datos para Pandas
    print(f"✅ LUZ VERDE: Guardando en tu base de datos...")
    nueva_fila = pd.DataFrame([{
        'Fecha': datetime.now().strftime("%Y-%m-%d"),
        'Empresa': empresa,
        'Puesto': puesto,
        'Plataforma': plataforma,
        'Estado': '0 - Pendiente de Aplicar',
        'URL': url
    }])
    
    # Guardamos en el archivo CSV (si no existe, lo crea; si existe, añade abajo)
    if not os.path.isfile(ARCHIVO_CSV):
        nueva_fila.to_csv(ARCHIVO_CSV, index=False, encoding='utf-8-sig')
    else:
        nueva_fila.to_csv(ARCHIVO_CSV, mode='a', header=False, index=False, encoding='utf-8-sig')
        
    print(f"💾 ¡Guardado exitoso en {ARCHIVO_CSV}!")

# ==========================================
# EJECUCIÓN DEL COPILOTO (Ejemplos de demostración)
# ==========================================
print("🚀 Iniciando Job Search Copilot v2.0...")

# Ejemplo 1: Oferta simulada válida (Luz Verde)
procesar_y_guardar(
    url="https://www.getonbrd.com/empleos/project-management/it-project-manager-techflow-madrid", 
    empresa="TechFlow Solutions", 
    puesto="IT Project Manager", 
    plataforma="GetOnBoard"
)

# Ejemplo 2: Oferta real que falla el filtro (Alerta Roja por B2B)
procesar_y_guardar(
    url="https://www.getonbrd.com/empleos/comercial-ventas/kam-e-commerce-tw-logistica-santiago", 
    empresa="TW Logística", 
    puesto="KAM E-commerce", 
    plataforma="GetOnBoard"
)