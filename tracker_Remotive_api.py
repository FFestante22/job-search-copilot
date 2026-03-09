import requests
import pandas as pd

print("--- Iniciando El Tracker v2.0 (Modo Anti-Autónomo) ---")
print("Descargando 100 ofertas frescas...")

url = "https://remotive.com/api/remote-jobs?limit=100"
respuesta = requests.get(url)
datos_empleo = respuesta.json()
lista_ofertas = datos_empleo['jobs']

df = pd.DataFrame(lista_ofertas)

# Añadimos 'job_type' a nuestras columnas para poder escanearlo
columnas_utiles = ['title', 'company_name', 'job_type', 'candidate_required_location', 'salary', 'url']
df_limpio = df[columnas_utiles]

print("¡Datos descargados! Aplicando filtros de negocio y legales...")

# 1. Lo que SÍ queremos
mis_roles = "support|help desk|analyst|product manager|python|it"
mis_zonas = "spain|europe|worldwide" # A veces empresas en Europa usan plataformas como Deel para contratarte legalmente en España.

# 2. Lo que NO queremos (Nuestra lista negra)
palabras_prohibidas = "freelance|contractor|independent|b2b"

# 3. Creamos las máscaras
filtro_roles = df_limpio['title'].str.contains(mis_roles, case=False, na=False)
filtro_zonas = df_limpio['candidate_required_location'].str.contains(mis_zonas, case=False, na=False)

# 4. EL FILTRO NEGATIVO: Usamos ~ para decir "Que NO contenga esto" en el título NI en el tipo de trabajo
filtro_legal = ~df_limpio['title'].str.contains(palabras_prohibidas, case=False, na=False) & \
               ~df_limpio['job_type'].str.contains('freelance|contractor', case=False, na=False)

# 5. Juntamos todo (Tiene que ser el rol correcto Y la zona correcta Y cumplir lo legal)
df_final = df_limpio[filtro_roles & filtro_zonas & filtro_legal]

df_final.to_csv("ofertas_tracker.csv", index=False)

print(f"De 100 ofertas analizadas, El Tracker encontró {len(df_final)} que encajan con tu perfil y estatus legal.")
print("¡Archivo 'ofertas_tracker.csv' actualizado con éxito!")