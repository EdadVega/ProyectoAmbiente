import random

def generarDatosCalidadAire():
    listaDatos = []
    for i in range(5):  # Modifica el rango según sea necesario
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        comuna = random.randint(1, 14)
        ICA = random.randint(10, 80)
        fecha = random.choice(['2024-05-15', '2024-05-16', 'sin'])
        correo = random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo4@correo.com'])
        
        encuesta = [nombre, comuna, ICA, fecha, correo]
        listaDatos.append(encuesta)
        
    return listaDatos

def generar_html():
    # Generar los datos
    datos = generarDatosCalidadAire()

    # Generar el contenido HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calidad del Aire</title>
    </head>
    <body>
        <h1>Tabla de Calidad del Aire</h1>
        <table border="1">
            <tr>
                <th>Nombre</th>
                <th>Comuna</th>
                <th>ICA</th>
                <th>Fecha</th>
                <th>Correo</th>
            </tr>
    """

    # Agregar filas de datos a la tabla
    for dato in datos:
        html_content += "<tr>"
        for item in dato:
            html_content += f"<td>{item}</td>"
        html_content += "</tr>"
    
    # Cerrar el contenido HTML
    html_content += """
        </table>
    </body>
    </html>
    """

    # Escribir el contenido en un archivo HTML
    with open("calidad_del_aire.html", "w") as file:
        file.write(html_content)

# Generar el archivo HTML
generar_html()
