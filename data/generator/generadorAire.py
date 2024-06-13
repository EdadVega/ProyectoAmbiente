import random

def generarDatosCalidadAire():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        comuna = random.randint(1,14)
        ICA = random.randint(10, 80)
        fecha = random.choice(['2024-05-15', '2024-05-16', 'sin'])
        correo = random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo4@correo.com'])
        
        encuesta = [nombre, comuna, ICA, fecha, correo]
        listaDatos.append(encuesta)
        
    return listaDatos
