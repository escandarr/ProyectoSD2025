-- Cargar los eventos desde CSV
events = LOAD 'eventos_filtrados.csv'
    USING PigStorage('\t')
    AS (uuid:chararray, type:chararray, city:chararray, street:chararray, date:chararray, severity:int);

-- Ignorar la cabecera
filtered = FILTER events BY uuid != 'uuid';

-- Agrupar por ciudad
grouped = GROUP filtered BY city;

-- Contar por ciudad
counts = FOREACH grouped GENERATE group AS city, COUNT(filtered) AS total;

-- Guardar resultado en salida_pig/
STORE counts INTO 'salida_pig' USING PigStorage(',');
