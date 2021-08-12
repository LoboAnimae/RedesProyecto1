# Proyecto 1

## ATENCIÓN

    Mi computadora no permite grabar lo que es la pantalla. Por lo mismo, se han adjuntado pruebas en la entrega en formato PNG.
    Por fallos en el internet de Tigo, no se puede usar el servidor XMPP de mi lado, por lo que no todos los métodos tienen pruebas
    de funcionamiento. Se tratarán de añadir cuando se pueda.

## Metadata

    Andrés Quan-Littow
    17652
    qua17652@uvg.edu.gt

## Project

Hello! Welcome to my XMPP project.

### Antecedentes

La mensajería instantánea es una de las invenciones de nuestra época que han revolucionado la forma de comunicación de persona a persona. Muchos servicios requieren el uso de protocolos privativos que limitan y obligan al usuario a usar únicamente las aplicaciones desarrolladas por el proveedor.

XMPP es un protocolo abierto con más de 10 años de desarrollo, que permite la interconexión entre distintos proveedores de mensajería instantánea.

### Objetivos

-   Apegarse a los estándares de un protocolo conocido y abierto
-   Comprender las bases de programación asíncrona requeridas para apegarse a las necesidades de desarrollo en redes.

### Desarrollo

Implementar un cliente que soporte el protocolo XMPP. Debe de soportar como mínimo las siguientes características:

#### Administración de la cuenta (25% del funcionamiento)

-   [x] Registrar una cuenta nueva en el servidor
-   [x] Iniciar sesión con una cuenta
-   [x] Cerrar sesión con una cuenta
-   [x] Eliminar la cuenta del servidor

#### Comunicación (75% del funcionamiento)

-   [x] Mostrar todos los usuarios/contactos y su estado
-   [x] Agregar un usuario a los contactos
-   [x] Mostrar detalles de contacto de un usuario
-   [x] Comunicación 1 a 1 con cualquier usuario/contacto
-   [x] Participar en conversaciones grupales
-   [x] Definir mensaje de presencia
-   [x] Enviar/recibir notificaciones
-   [ ] Enviar/recibir archivos

El proyecto debe estar definido con una `interfaz de consola`, no usando librerías de interfaces de gráficas (GUI). Puede utilizar cualquier lenguaje de programación, siempre y cuando este permita compatibilidad con distintos sistemas operativos y no requiera de herramientas externas.

Puede utilizar librerías que faciliten la comunicación con el protocolo XMPP, como `SliXMPP` para Python.

El dominio del servidor es

    alumchat.xyz

Todas las funcionalidades (excepto el enviar y recibir archivos) implementadas!

Funcionalidades a partir de métodos reaccionarios. Recomendado el usar otro cliente para ello.
