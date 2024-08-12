# Microdesafio Anonimizacion

## Configuración del Entorno

### Para Entornos Locales

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

### Para GitHub Codespaces

Si estás utilizando GitHub Codespaces, el entorno se configurará automáticamente para ti. Solo necesitas realizar los siguientes pasos:

1. **Abrir el Codespace**:

   Abre el Codespace desde GitHub. El entorno se configurará automáticamente según la configuración en el archivo `.devcontainer`.

2. **Llenar el Archivo `.env`**:

   Completa el archivo `.env` con las credenciales y configuraciones necesarias. Aquí tienes un ejemplo de cómo debería lucir el archivo `.env`:

    ```plaintext
    DATABASE_URL=postgres://user:password@localhost/dbname
    SECRET_KEY=your_secret_key_here
    ```

   Asegúrate de reemplazar los valores con las credenciales reales y las configuraciones específicas de tu entorno.

### Configuración Automática en GitHub Codespaces

Cuando se crea o se reinicia el Codespace, GitHub Codespaces realiza automáticamente las siguientes acciones:

1. **Crear el Entorno Virtual**: Utiliza el comando `python -m venv venv` definido en el archivo `.devcontainer/devcontainer.json`.

2. **Activar el Entorno Virtual**: El entorno virtual se activa automáticamente para ti.

3. **Instalar las Dependencias**: Instala las librerías necesarias usando el comando `pip install -r requirements.txt`, también definido en el archivo `.devcontainer/devcontainer.json`.

Así que, en GitHub Codespaces, el único paso que debes realizar es configurar el archivo `.env`. El entorno y las dependencias se configurarán automáticamente al iniciar o reiniciar el Codespace.
