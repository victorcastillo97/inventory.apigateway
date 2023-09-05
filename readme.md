# Inventory API Gateway

Este repositorio contiene el código para el API Gateway del proyecto de gestión de inventario. Actúa como una interfaz entre el frontend y diversos microservicios en el backend, como el servicio de gestión de inventario.

## Características

- Ruteo y redirección de solicitudes al microservicio adecuado.
- Simplifica la interfaz de cliente, ofreciendo un único punto de acceso para diferentes servicios.

## Tecnologías Utilizadas

- **FastAPI**: Un moderno framework web rápido de escribir y fácil de usar para construir APIs con Python 3.7+ basado en estándares para APIs.
- **Requests**: Una biblioteca HTTP para Python, para enviar solicitudes HTTP. Es abstracta y fácil de usar.

## Instalación y Uso

1. **Clonar el repositorio**
`git clone https://github.com/<tu-usuario>/inventory.apigateway.git`
`cd inventory.apigateway`

2.  **Instalar dependencias**
`pip install -r requirements.txt`

3. **Ejecutar la aplicación**
`uvicorn app:app --reload`


El API estará disponible en `http://localhost:8000`.

## Dockerización

El proyecto incluye un `Dockerfile` para construir una imagen y desplegarla en contenedores. Para construir y ejecutar el proyecto con Docker, sigue estos pasos:

1. **Construir la imagen**
`make build.image`

2. **Ejecutar el contenedor**
`make run.app`

De nuevo, el API estará disponible en `http://localhost:8000`.

## Contribución

Las Pull Requests son bienvenidas. Para cambios importantes, por favor, abre un issue primero para discutir lo que te gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)