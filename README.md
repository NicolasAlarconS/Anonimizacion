# Microdesafio Anonimizacion

## Configuración del Entorno

1. **Crear un Entorno Virtual**:

    ```bash
    python -m venv venv
    ```

2. **Activar el Entorno Virtual**:

    - **En Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **En macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

3. **Instalar las Dependencias**:

    Con el entorno virtual activado, instala las librerías necesarias ejecutando:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar el Archivo `.env`**:

    Completa con las credenciales y configuraciones necesarias en el archivo `.env`. Aquí tienes un ejemplo de cómo debería lucir el archivo `.env`:

    ```plaintext
    DATABASE_URL=postgres://user:password@localhost/dbname
    SECRET_KEY=your_secret_key_here
    ```

    Asegúrate de reemplazar los valores con las credenciales reales y las configuraciones específicas de tu entorno.
