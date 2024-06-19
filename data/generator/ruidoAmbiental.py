import random

def ruidoAmbiental():
    listaDatos = []
    for i in range(10):
        nombre = random.choice(['lina castro', 'eddy vega', 'camilo garces', 'bella builes', 'victor aristizabal'])
        comuna = random.randint(1, 14)
        dbDiurnos = random.randint(0, 100)
        dbNocturnos = random.randint(0, 100)
        fecha = random.choice(['2024-05-15', '2024-05-16', '2024-05-17'])
        direccion = random.choice(['car 75 # 45 - 89', 'car 75 # 45 - 7', 'car 75 # 45 - 82', 'car 75 # 45 - 87', 'car 75 # 45 - 50'])
        
        encuesta = [nombre, comuna, dbDiurnos, dbNocturnos, fecha, direccion]
        listaDatos.append(encuesta)
        
    return listaDatos

def generar_html():
    # Generar los datos
    datos = ruidoAmbiental()

    # Generar el contenido HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ruido Ambiental</title>
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
                    <th class="table-header">Comuna</th>
                    <th class="table-header">dbDiurnos</th>
                    <th class="table-header">dbNocturnos</th>
                    <th class="table-header">Fecha</th>
                    <th class="table-header">Direccion</th>
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
        <img class="img-generada" src="../img/calidadRuido.png" alt="ruido">
    </body>
    </html>
    """

    # Escribir el contenido en un archivo HTML
    with open("./tablasGeneradas/ruido_ambiental.html", "w") as file:
        file.write(html_content)

# Generar el archivo HTML
generar_html()
