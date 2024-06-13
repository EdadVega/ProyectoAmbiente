import random

def siembraArboles():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        corregimiento = random.choice(['San Antonio de Prado', 'altavista', 'San Cristobal', 'Santa Elena', 'San Sebastian' ])
        Hectarea = random.randint(0, 500)
        especie = random.choice(['Pino', 'Eucalipto', 'Manzano', 'roble', 'Palo de Mango'])
        fecha = random.choice(['2024-05-15', '2024-05-16', '2024-05-17'])
        correo = random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo4@correo.com'])
        
        encuesta = [nombre, corregimiento, Hectarea, especie, fecha ,correo]
        listaDatos.append(encuesta)
        
    return listaDatos
print(siembraArboles())
