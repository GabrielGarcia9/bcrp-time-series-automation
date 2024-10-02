import requests
from datetime import datetime

def descargar_datos(frecuencia: str, codigos_series: str, periodo_inicial: str):
 
    url_base = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api'
    formato_salida = 'csv'
    idioma = 'esp'

    if frecuencia == "diaria":   
        periodo_inicial = datetime.strptime(periodo_inicial, "%d-%m-%Y").strftime("%Y-%m-%d")
        periodo_final = str(datetime.now().strftime('%Y-%m-%d'))

    elif frecuencia == "mensual":
        periodo_inicial = datetime.strptime(periodo_inicial, "%m-%Y").strftime("%Y-%m")
        periodo_final = str(datetime.now().strftime('%Y-%m'))
        
    url = f"{url_base}/{codigos_series}/{formato_salida}/{periodo_inicial}/{periodo_final}/{idioma}"
    response = requests.get(url)

    if response.status_code == 200:
        contenido_respuesta = response.text
        lineas = contenido_respuesta.split('<br>')
        return lineas
    
    else:
        print("La solicitud no fue exitosa. Código de estado:", response.status_code)
        return None
        
# PD04649MD  #04-01-1999
# PN00001MM #mensuales #Ene-1992

# lineas = descargar_datos_diarias('diaria', 'PD04649MD', '04-01-2024')
# for linea in lineas:
#     print(linea)