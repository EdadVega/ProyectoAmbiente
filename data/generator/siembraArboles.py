import random

def siembraArboles():
    listaDatos = []
    for i in range(10):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        corregimiento = random.choice(['San Antonio de Prado', 'altavista', 'San Cristobal', 'Santa Elena', 'San Sebastian' ])
        hectarea = random.randint(0, 500)
        especie = random.choice(['Pino', 'Eucalipto', 'Manzano', 'roble', 'Palo de Mango'])
        fecha = random.choice(['2024-05-15', '2024-05-16', '2024-05-17'])
        correo = random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo4@correo.com'])
        
        encuesta = [nombre, corregimiento, hectarea, especie, fecha, correo]
        listaDatos.append(encuesta)
        
    return listaDatos

def generar_html():
    # Generar los datos
    datos = siembraArboles()

    # Generar el contenido HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Siembra de Arboles</title>
        <link rel="stylesheet" href="../styles.css">
    </head>
      <header>
  <div class="icon1">
    <img src="../img/icon1.png" alt="">
  </div>
  <nav>
    <ul>
      <li><a href="../index.html">Home</a></li>
      <li><a href="../dashboard.html">Dashboard</a></li>
    </ul>
  </nav>
</header> 

    <body class="body">
        <div class="table-container">
            <h1 class="table-title">Tabla de Calidad del Agua</h1>
            <table class="styled-table">
                <tr>
                    <th class="table-header">Nombre</th>
                    <th class="table-header">Corregimiento</th>
                    <th class="table-header">Hectarea</th>
                    <th class="table-header">Especie</th>
                    <th class="table-header">Fecha</th>
                    <th class="table-header">Correo</th>
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
        </div>
        <h1 class="titulo-img-generada">TABLA GRAFICAMENTE</h1>
        <img class="img-generada" src="../img/calidadSiembra.png" alt="siembra">
    </body>
    </html>
    """

    # Escribir el contenido en un archivo HTML
    with open("./tablasGeneradas/siembra_arboles.html", "w") as file:
        file.write(html_content)

# Generar el archivo HTML
generar_html()
