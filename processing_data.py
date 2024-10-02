from io import StringIO
from datetime import datetime
import pandas as pd
from numpy import nan

def procesar_datos_diarios(lineas):
    titulo = lineas.pop(0).split(',')[1]

    buffer = StringIO('\n'.join(lineas))
    df = pd.read_csv(buffer)
    df.columns = ['fecha', 'valor']

    # df['valor'].replace('n.d.', nan, inplace=True)
    df['valor'] = df['valor'].replace('n.d.', nan)
    df['valor'] = df['valor'].astype(float)

    date = []
    for cadena in df['fecha']:
        if cadena[3:6] in ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']:
            cadena = cadena.replace('Ene', '01').replace('Feb', '02').replace('Mar', '03').replace('Abr', '04').replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Ago', '08').replace('Set', '09').replace('Oct', '10').replace('Nov', '11').replace('Dic', '12')
            date.append(cadena)
        else:
            continue

    df['fecha'] = [datetime.strptime(d, '%d.%m.%y') for d in date]
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d.%b.%y')

    data = pd.DataFrame({
        'date': df['fecha'],
        'year': df['fecha'].dt.strftime('%Y'),
        'month': df['fecha'].dt.strftime('%B'),
        'value_month': df['fecha'].dt.strftime('%m'),
        'value_day_week': df['fecha'].dt.strftime('%u'),
        'value': df['valor'],
        'null': df['valor'].isnull()
    })

    return data.set_index('date'), titulo

def procesar_datos_mensuales(lineas):
    titulo = lineas.pop(0).split(',')[1]

    buffer = StringIO('\n'.join(lineas))
    df = pd.read_csv(buffer)
    df.columns = ['fecha', 'valor']

    # df['valor'].replace('n.d.', nan, inplace=True)
    df['valor'] = df['valor'].replace('n.d.', nan)
    df['valor'] = df['valor'].astype(float)

    date = []
    for cadena in df['fecha']:
        
        if cadena[0:3] in ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']:
            cadena = cadena.replace('Ene', '01').replace('Feb', '02').replace('Mar', '03').replace('Abr', '04').replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Ago', '08').replace('Sep', '09').replace('Oct', '10').replace('Nov', '11').replace('Dic', '12')
            date.append(cadena)
        else:
            continue

    df['fecha'] = [datetime.strptime(d, '%m.%Y') for d in date]
    df['fecha'] = pd.to_datetime(df['fecha'], format='%m.%y')

    data = pd.DataFrame({
        'date': df['fecha'],
        'year': df['fecha'].dt.strftime('%Y'),
        'month': df['fecha'].dt.strftime('%B'),
        'value_month': df['fecha'].dt.strftime('%m'),
        'value': df['valor'],
        'null': df['valor'].isnull()
    })

    return data.set_index('date'), titulo



def procesar_datos_trimestrales(lineas):
    titulo = lineas.pop(0).split(',')[1]

    buffer = StringIO('\n'.join(lineas))
    df = pd.read_csv(buffer)
    df.columns = ['fecha', 'valor']

    df['valor'].replace('n.d.', nan, inplace=True)
    df['valor'] = df['valor'].astype(float)

    date = []
    for cadena in df['fecha']:
        
        if cadena[0:3] in ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']:
            cadena = cadena.replace('Ene', '01').replace('Feb', '02').replace('Mar', '03').replace('Abr', '04').replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Ago', '08').replace('Sep', '09').replace('Oct', '10').replace('Nov', '11').replace('Dic', '12')
            date.append(cadena)
        else:
            continue

    print("df['fecha']: ", df['fecha'].head(10))
    print("tamaño de df:", len(df))
    print("date : ", date)
    print("tamaño de date :", len(date))


    df['fecha'] = [datetime.strptime(d, '%m.%Y') for d in date]
    df['fecha'] = pd.to_datetime(df['fecha'], format='%m.%y')

    data = pd.DataFrame({
        'date': df['fecha'],
        'year': df['fecha'].dt.strftime('%Y'),
        'month': df['fecha'].dt.strftime('%B'),
        'value_month': df['fecha'].dt.strftime('%m'),
        'value': df['valor'],
        'null': df['valor'].isnull()
    })

    return data.set_index('date'), titulo





# from extract_with_api_bcrp import descargar_datos

# lineas = descargar_datos('PN00001MM', '2016-04-12')
# data, titulo = procesar_datos_mensuales(lineas)
# print("titulo:", titulo)
# print(data.head())

