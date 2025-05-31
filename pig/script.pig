-- Cargar CSV sin encabezado desde /data
raw = LOAD 'eventos_sin_filtrar.csv' 
      USING PigStorage(',') 
      AS (uuid:chararray, type:chararray, city:chararray, street:chararray, pubMillis:chararray, severity:int);

-- Filtrar entradas inválidas
valid = FILTER raw BY 
    (type IS NOT NULL AND type != '') AND 
    (city IS NOT NULL AND city != '') AND 
    (severity IS NOT NULL);

-- Normalizar texto y convertir timestamps
processed = FOREACH valid GENERATE 
    uuid, 
    LOWER(type) AS type, 
    LOWER(city) AS city, 
    LOWER(street) AS street,
    ToDate((long)pubMillis, 'yyyy-MM-dd HH:mm:ss') AS date,
    severity;

-- Guardar CSV limpio (eventos_filtrados.csv)
STORE processed INTO 'eventos_filtrados' USING PigStorage(',');
