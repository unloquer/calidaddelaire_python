# calidad del aire (python)
Repositorio para el análisis de los datos de la calidad del aire en Medellín.
La idea es usar datos extraídos de los sensores móviles ciudadanos construidos por Unloquer para luego analizarlos en relación al mapa de la ciudad ya sí contribuir a la exposición de la contaminación en la ciudad. Creemos que exponer estos datos de manera abierta y comunitaria aporta a la discusión del tema, a comprender su realidad, a tener un punto de vista independiente y en el futuro a la toma de decisiones sobre la calidad del aire y en general del impacto ambiental generado por la emisión de partículas y gases.

Este código va en respuesta a un thread en la lista de correo de unloquer en el cual se discutía la manera de usar los datos ciudadanos y extraer buenas métricas de los sensores que estan distribuidos y en movimiento.

probablemente no sea usado para la visualización, pero si para hacer el análisis de las bases de datos de diferentes maneras posibles que se han discutido: desde aplanar todos los datos sobre las coordenadas hasta filtrar los datos deacuerdo a su periodicidad (i.e. todos los martes) y en ciertas franjas horarias(i.e. de 4 pm a 7pm).

También debe resolverse un asunto sobre la calibración de los sensores y el tipo de medidas que arroja y tratar de independizarlas de otros factores como el tiempo de exposición, etc. Esto se ha discutido con la Doctora Eliette Restrepo que está encargada de optimizar las mediciones de los sensores.

Estas funcionalidades del análisis se irán implementando poco a poco. Por el momento solo aplana los datos.

Acepta Json y txt en csv. revisar los datasets adjuntos para entender el formato.
