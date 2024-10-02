def explorar_datos(frecuencia: str, data):
    if frecuencia == "diaria":
        print('\nNúmero de valores perdidos:\n', data.isnull().sum())
        print('\nNúmero de valores perdidos por año:\n', data.groupby('year')['null'].sum())
        print('\nNumero de valores perdidos por mes:\n', data.groupby('month')['null'].sum())
        print('\nNumero de valores perdidos por días de la semana:\n', data.groupby('value_day_week')['null'].sum())
        print(data.groupby('year')['value'].describe().round(2).T.to_string())
        
    elif frecuencia == "mensual":
        print('\nNúmero de valores perdidos:\n', data.isnull().sum())
        print('\nNúmero de valores perdidos por año:\n', data.groupby('year')['null'].sum())
        print('\nNumero de valores perdidos por mes:\n', data.groupby('month')['null'].sum())
        print(data.groupby('year')['value'].describe().round(2).T.to_string())

