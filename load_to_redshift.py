import psycopg2
from redshift_conecction import connect_redshift
from psycopg2.extras import execute_values

# Carga de datos a Redshift
def load_data(df):
    if df is None or df.empty:
        print("No hay datos que cargar, df vacio.")
        return

    conn = connect_redshift()
    try:
        with conn.cursor() as cursor:

              # Convertir tipos de datos a tipos estándar de Python
          

              # Crear la tabla stock_data en el esquema especificado
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS public.politicas_2050_na (
                pais VARCHAR(255),
                comisionado VARCHAR(255),
                reduccion_c02 VARCHAR(20),
                incrmento_p VARCHAR(20),
                inversion_arboles VARCHAR(20),
                fecha DATE,
                telefono VARCHAR(20)
            );
            """)
            print("Tabla en Redshift lista!")
            
            # Preparar datos para inserción en bloque
            block_size = 20  # Tamaño del bloque
            for start in range(0, len(df), block_size):
                end = start + block_size
                block_df = df.iloc[start:end]
                rows_to_insert = list(block_df.to_records(index=False))

                # Inserción en bloque
                insert_query = f"""
                INSERT INTO {'public'}.politicas_2050_NA (pais, comisionado, reduccion_c02, incrmento_p, inversion_arboles, fecha, telefono)
                VALUES %s
                """
                execute_values(cursor, insert_query, rows_to_insert)
                
                conn.commit()
                print(f"Se ha agregado un bloque de {len(rows_to_insert)} registros a Redshift.")

    except psycopg2.Error as e:
        print(f"Error cargando datos a Redshift: {e}")
    finally:
        conn.close()