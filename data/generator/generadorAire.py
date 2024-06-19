import random

def generarDatosCalidadAire():
    listaDatos = []
    for i in range(10):  # Modifica el rango según sea necesario
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
                    <th class="table-header">Comuna Mes</th>
                    <th class="table-header">ICA</th>
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
        <img class="img-generada" src="../img/calidadaire.png" alt="aire">
    </body>
    </html>
    """

    # Escribir el contenido en un archivo HTML
    with open("./tablasGeneradas/calidad_del_aire.html", "w") as file:
        file.write(html_content)

# Generar el archivo HTML
generar_html()
