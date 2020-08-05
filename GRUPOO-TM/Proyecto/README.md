# PROYECTO-O-TM

## Descripción
Este README explica como instalar el proyecto en un sistema operativo Linux, como dejarlo preparado y las [funcionalidades básicas](#funcionalidades-básicas) de la página en sí.

## IMPORTANTE
Este proyecto fue realizado con Python 3.6.9. Si no se tiene instalada esta versión, no podemos asegurar que el proyecto funcione de forma correcta. A su vez 
es de vital importancia que instale Django a través de un entorno virtual como es explicado a continuación.

# Setup del proyecto
- Primero clone el proyecto en su directorio de preferencia con el comando `git clone https://github.com/Grupo-O-Desarrolladores/PROYECTO-O-TM.git`
- Luego diríjase a la carpeta del proyecto en `../PROYECTO-O-TM/GRUPOO-TM/Proyecto/comedor` y abra el terminal en esta ruta.

Una vez con el terminal abierto en esa ruta, lo siguiente es crear el entorno virtual:
- Utilice el comando `python3 -m venv entorno`, el cual le creará dentro de la misma ruta una carpeta llamada entorno.
- Una vez creado el entorno, utilice `source entorno/bin/activate` para activar el mismo. Si lo ha realizado de forma correcta, se le antepondrá en el comando de la consola (entorno).
Esto quiere decir que ha activado el entorno correctamente.
- Por último ingrese `python3 -m pip install django` para instalar la versión correspondiente de Django en su nuevo entorno virtual a traveś de pip, que es un gestor de paquetes.

Una vez instalado Django con éxito hay que proceder a ejecutar las migraciones, crear un super usuario para utilizar el administrador de la página y correr el servidor.
- Lo primero que hay que hacer son las migraciones. Para eso ejecute en la consola `python manage.py migrate`, y 
Django realizará todas las migraciones de base de datos correspondientes. Por favor, asegúrese de seguir en la ruta `../PROYECTO-O-TM/GRUPOO-TM/Proyecto/comedor`.
Una forma de saber que es la ruta correcta, es porque dentro de esta existe un archivo único llamado manage.py.
- Una vez realizadas las migraciones, procederemos a crear un super usuario para poder utilizar el administrador. Ejecute por favor `python manage.py createsuperuser`,
donde se le pedirá un nombre de usuario, un mail(no es requerimiento) y una contraseña.
- Teniendo ya listas las migraciones y el super usuario registrado, proceda a ejecutar `python manage.py runserver` y diríjase en su navegador a la dirección `127.0.0.1:8000`, o bien
`localhost:8000`. Debería poder ver la página de inicio del proyecto.

# Funcionalidades básicas
Para esta sección se recomienda que tenga abierta en una pestaña la página en sí y en otra pestaña la página del administrador. Para acceder al administrador,
debe agregar al final un `/admin` a la dirección de inicio, de esta forma `127.0.0.1:8000/admin`. Cuando entre por primera vez al administrador se va a encontrar con un registro. 
Ingrese ahí el usuario y contraseña que utilizó en la creación del super usuario.

## Registrar un comedor
Si explora la página en estos momentos, no encontrará ningún comedor registrado. Eso es porque debe registrarlos primero en el administrador. Una vez ingresado
con su usuario y contraseña al administrador, verá a la izquierda tres bloques. Agregue un Comedor donde dice +Add en el campo correspondiente. Ahí deberá llenar
los siguientes campos obligatorios: nombre, dirección y descripción. Por último puede agregar si desea los productos que necesita
el comedor que está creando. Recomendamos que siga este procedimiento porque lo consideramos el más práctico. Donde dice Productos al final de los
campos, tiene un cuadro vacío y un +. Haga click en el más para agregar un producto. Una vez agregada la demanda necesaria, debe guardar el comedor
abajo a la derecha.

## Agregar un producto
Si siguió los pasos anteriores, entonces una ventana debería aparecer para poder agregar un nuevo Producto. Si no, puede agregar un producto
desde la página de inicio del administrador, pero no lo recomendamos. Tiene tres campos obligatorios: nombre, 
tipo cantidad(kilos, litros, unidades, etc) y cantidad(número entero). Una vez completados simplemente tiene que guardarlo abajo a la derecha.

## Explorando la página
Si ahora se dirige a la página de inicio y hace click en Comedores, podrá seleccionar de una lista los comedores que se encuentren registrados
en la base de datos. Y si ingresa a uno de ellos, podrá ver dos tablas: una mostrando la información de los campos y otra con los productos que requieren.

## Haciendo una donación
Desde inicio, haga click en Donaciones. Ahí seleccione un comedor para el que desee realizar una donación y a continuación se le mostrará
un cuadro con los productos requeridos y su cantidad. Haga click en DONAR para alguno de esos productos. Se le mostrará un formulario donde se le
pedirá un nombre y una dirección de contacto. Esta puede ser un teléfono fijo o celular, e incluso una dirección de correo electrónico.
Por último haga click en enviar y volverá a la página de donaciones donde puede seleccionar otro comedor si lo desea.

## Gestionando las donaciones
Una vez tenga hecha una o varias donaciones, si vuelve a la página del administrador e ingresa en el último bloque de la izquierda en Donaciones,
podrá ver dentro del mismo que la o las donaciones que haya hecho hace un momento se habrán agregado a una lista, encabezados por el nombre del donante.
El administrador de Django pondrá primero por defecto a las donaciones mas recientes. El último campo donde sale una cruz roja se añade por defecto,
para ayudar al administrador o grupo de administradores, a saber cuál es el estado de las donaciones, y si han sido aceptadas o no por los comedores.
Por último se puede conservar el registro de las donaciones hechas(que no son visibles al público) y dirigiéndose desde el inicio del administrador a 
el producto que tenga un pedido de donación, se lo puede modificar y/o eliminar de acuerdo a si la demanda ha sido satisfecha o no.
Al ser esta página sólo un nexo entre los comedores y el voluntariado, y al no encargarse de la gestión específica de los movimientos reales de la mercadería,
la administración está enfocada en recibir los datos de donación, la alta y baja de Comedores y sus respectivas demandas.
