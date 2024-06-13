import random

def ruidoAmbiental():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        comuna = random.randint(1,14)
        dbDiurnos= random.randint(0, 100)
        dbNocturnos= random.randint(0, 100)
        fecha = random.choice(['2024-05-15', '2024-05-16', '2024-05-17'])
        direccion = random.choice(['car 75 # 45 - 89','car 75 # 45 - 7','car 75 # 45 - 82','car 75 # 45 - 87','car 75 # 45 - 50'])
        
        encuesta = [nombre, comuna, dbDiurnos, dbNocturnos, fecha ,direccion]
        listaDatos.append(encuesta)
        
    return listaDatos
print(ruidoAmbiental())