# from extract_with_api_bcrp import descargar_datos
# from processing_data import procesar_datos_diarios, procesar_datos_mensuales
# from vizualization import visualizar_box_plot, visualizar_line_plot, visualizar_comparacion_anual
# from descriptive_and_groupby import explorar_datos

# def main():
#     print("Encuentre el codigo y fecha de inicio disponible en: https://estadisticas.bcrp.gob.pe/estadisticas/series/index")
#     frecuencia_serie = input("\nIngrese el la frecuencia (diaria, mensual, trimestral o anual) de serie (o 'q' para salir): ")
#     if frecuencia_serie == 'q': return

#     codigos_series = input("Ingrese el código de serie (o 'q' para salir): ")
#     if codigos_series.lower() == 'q':return
        
#     if frecuencia_serie == 'diaria':
#         periodo_inicial = input("Ingrese la fecha de inicio (en formato %d-%m-%Y por ejemplo 27-04-1998) (o 'q' para salir): ")
#         if periodo_inicial.lower() == 'q': return

#         lineas = descargar_datos(frecuencia_serie, codigos_series, periodo_inicial)
#         if lineas:
#             data, titulo = procesar_datos_diarios(lineas)
#             explorar_datos(data)
#             visualizar_box_plot(data, titulo)
#             visualizar_line_plot(data, titulo)
#             visualizar_comparacion_anual(data)

#         salir = input("¿Desea salir del programa? (si/no): ")
#         if salir.lower() == "si":
#             return
#         else:
#             main()
# ##########################################################
#     elif frecuencia_serie == 'mensual':
#         periodo_inicial = input("Ingrese la fecha de inicio (En formato %m-%Y por ejemplo 04-2004) (o 'q' para salir): ")
#         if periodo_inicial.lower() == 'q': return
#         lineas = descargar_datos(frecuencia_serie, codigos_series, periodo_inicial)
#         if lineas:
#             data, titulo = procesar_datos_mensuales(lineas)
#             # explorar_datos(data)
#             visualizar_box_plot(data, titulo)
#             visualizar_line_plot(data, titulo)
#             visualizar_comparacion_anual(data)

#         salir = input("¿Desea salir del programa? (si/no): ")
#         if salir.lower() == "si":
#             return
#         else:
#             main()



from extract_with_api_bcrp import descargar_datos
from processing_data import procesar_datos_diarios, procesar_datos_mensuales
from vizualization import visualizar_box_plot, visualizar_line_plot, visualizar_comparacion_anual
from descriptive_and_groupby import explorar_datos

# Función auxiliar para procesar entradas
def solicitar_entrada(mensaje, opcion_salir='q'):
    entrada = input(mensaje)
    if entrada.lower() == opcion_salir:
        return None
    return entrada

# Función principal para descargar y procesar los datos
def procesar_serie(frecuencia_serie, codigos_series, periodo_inicial):
    lineas = descargar_datos(frecuencia_serie, codigos_series, periodo_inicial)
    if not lineas:
        print("No se encontraron datos.")
        return
    
    if frecuencia_serie == 'diaria':
        data, titulo = procesar_datos_diarios(lineas)
    elif frecuencia_serie == 'mensual':
        data, titulo = procesar_datos_mensuales(lineas)
    else:
        print("Frecuencia no soportada en este momento.")
        return
    
    explorar_datos(frecuencia_serie, data)
    visualizar_box_plot(data, titulo)
    visualizar_line_plot(data, titulo)
    visualizar_comparacion_anual(data)

# Función principal
def main():
    print("\nEncuentre el código y fecha de inicio disponible en: https://estadisticas.bcrp.gob.pe/estadisticas/series/index")
    
    while True:
        frecuencia_serie = solicitar_entrada("\nIngrese la frecuencia (diaria, mensual, trimestral o anual) de la serie (o 'q' para salir): ")
        if not frecuencia_serie: break
        
        codigos_series = solicitar_entrada("Ingrese el código de serie (o 'q' para salir): ")
        if not codigos_series: break

        if frecuencia_serie == 'diaria':
            periodo_inicial = solicitar_entrada("Ingrese la fecha de inicio (en formato %d-%m-%Y, por ejemplo, 27-04-1998) (o 'q' para salir): ")
            if not periodo_inicial: break
        elif frecuencia_serie == 'mensual':
            periodo_inicial = solicitar_entrada("Ingrese la fecha de inicio (en formato %m-%Y, por ejemplo, 04-2004) (o 'q' para salir): ")
            if not periodo_inicial: break
        else:
            print("Frecuencia no soportada.")
            continue

        procesar_serie(frecuencia_serie, codigos_series, periodo_inicial)
        
        salir = solicitar_entrada("¿Desea salir del programa? (si/no): ", opcion_salir="si")
        if salir is None:
            break

if __name__ == "__main__":
    main()


# if __name__ == "__main__":
#     main()
# PD04649MD  #04-01-1999
# PN00001MM #mensuales #Ene-1992

# PD38026MD #diaria #02-01-2006