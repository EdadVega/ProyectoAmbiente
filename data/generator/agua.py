import random

def accesoAgua():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        consumoMes = random.randint(1, 999)
        accesoalcantarillado= random.choice(["si", "No"])        
        comuna = random.randint(1, 14)        
        fecha = random.choice(['2024-05-15', '2024-05-16', '2024-05-17'])
        correo = random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo4@correo.com'])
        
        encuesta = [nombre, consumoMes, accesoalcantarillado, fecha ,correo, comuna]
        listaDatos.append(encuesta)
        
    return listaDatos
print(accesoAgua())