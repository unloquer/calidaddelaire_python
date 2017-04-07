# calidaddelaire_python
Repositorio para código de python relacionado con el análisis de los datos del aire.
La idea es usar datos extraídos de los sensores móviles ciudadanos y analizarlos.
Este código va en respuesta a un thread en la lista de correo de unloquer en la cual se discutía la manera de usar los datos ciudadanos y extraer buenas métricas de los sensores que estan distribuidos y en movimiento.

probablemente no sea usado para la visualización, pero si para hacer el análisis de las bases de datos de diferentes maneras posibles que se han discutido: desde aplanar todos los datos sobre las coordenadas hasta filtrar los datos deacuerdo a su periodicidad (i.e. todos los martes) y en ciertas franjas horarias(i.e. de 4 pm a 7pm).

Tamnbién debe resolverse un asunto sobre la calibración de los sensores y el tipo de medidas que arroja y tratar de independizarlas de otros factores como tiempo de exposición, etc. Esto se ha discutido con la Doctora Eliette Restrepo que está encargada de optimizar las mediciones de los sensores.

Estas funcionalidades del análisis se irán implementando poco a poco. Por el momento solo aplana los datos.

Acepta Json y txt en csv. revisar los datasets adjuntos para entender el formato.
