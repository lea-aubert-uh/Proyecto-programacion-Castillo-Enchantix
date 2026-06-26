Castillo Enchantix es una aplicación de planificación de eventos desarrollada en Python con Streamlit, diseñada para gestionar las celebraciones más importantes de un castillo medieval. El sistema permite planificar, guardar y eliminar eventos, asegurando que se respeten estrictamente las tradiciones y protocolos del reino.

El proyecto se ambienta en un castillo medieval. Se eligió este dominio porque ofrece un escenario rico en tradiciones y jerarquías, lo que permite crear restricciones interesantes y lógicas para la planificación de eventos. Cada ceremonia sigue reglas estrictas que deben ser respetadas para mantener el orden y la majestuosidad del reino.

El sistema gestiona tres tipos de eventos principales:

Boda Real: Ceremonia de unión entre dos nobles. Requiere solemnidad, belleza floral y la bendición divina.

Coronación: Investidura del nuevo monarca. Es el evento más importante del reino y el que mayor simbolismo posee.

Nombramiento de Caballeros: Ceremonia de ascenso a la caballería, donde se otorgan títulos y honores a los guerreros más destacados.

El castillo cuenta con un inventario de recursos, Los disponibles son:

Para la Boda Real se utilizan el Arco de Flores, el Arco de Laureles, el Sacerdote, la Música y los Bardos.

Para la Coronación se utilizan la Corona, la Música, los Bardos y las Palomas.

Para el Nombramiento de Caballeros se utilizan la Espada, el Rey, la Reina, las Trompetas y las Palomas.

El sistema implementa un conjunto de reglas tradicionales que deben cumplirse para que un evento sea válido. Estas restricciones son el núcleo de la lógica del proyecto.

En la Boda Real, si hay Música deben estar los Bardos, no puede haber Arco de Flores y Arco de Laureles a la vez, y sin Sacerdote no hay Boda.

En la Coronación, sin Corona no hay Coronación, no se puede tener Música sin Bardos, y no puede haber Música y Palomas a la vez.

En el Nombramiento de Caballeros, no hay nombramiento sin la Espada, el Rey no puede estar sin la Reina, y no pueden haber Trompetas y Palomas a la vez.

La aplicación permite planificar nuevos eventos, verificando automáticamente que la combinación de recursos no viole ninguna restricción.

Si el usuario intenta planificar un evento que viola alguna restricción o tiene conflictos de recursos, el sistema muestra un mensaje de error claro y descriptivo sin fallar.

La aplicación utiliza un archivo JSON para guardar toda la información de los eventos planificados. Esto permite mantener el estado del castillo entre diferentes sesiones de uso y cargar automáticamente los eventos guardados al iniciar la aplicación.

El proyecto está desarrollado en Python con el framework Streamlit para la interfaz de usuario. Se utiliza JSON como formato de persistencia de datos y la librería datetime para la gestión de intervalos de tiempo.
