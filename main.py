import pandas as pd
from anonymizedf.anonymizedf import anonymize
from load_to_redshift import load_data


# Extraer los datos
df = pd.read_csv('https://raw.githubusercontent.com/CoderContenidos/Data.Engineering/main/Semana%208/Datos_Microdesafio_Semana8_DE.csv',  sep=';')
df.columns = df.columns.str.strip()

# Mostrar df original
#print(df)

# Generar datos falsos usando anonymizedf
an = anonymize(df) 

fake_df = (
    an
    .fake_names("Comisionado", chaining=True)
    .fake_dates("Fecha", chaining=True)
    .fake_whole_numbers("Telefono", chaining=True)
    .show_data_frame()
)

# Mostrar el DataFrame generado
#print(fake_df)

# Seleccionar columnas'
df_selected = df[['Pais', 'Fake_Comisionado', 'Reduccion_CO2', 'Incrmento_P', 'Inversion_arboles', 'Fake_Fecha', 'Fake_Telefono']]

# Cambiar el nombre de las columnas seleccionadas
df_selected = df_selected.rename(columns={
    'Fake_Comisionado': 'Comisionado',
    'Fake_Fecha': 'Fecha',
    'Fake_Telefono': 'Telefono'
})

# Mostrar el DataFrame anonimizado
#print(df_selected)

# Cargar los datos a Redshift
load_data(df = df_selected)
