import pandas as pd
import matplotlib.pyplot as plt

from data.generator.siembraArboles import siembraArboles

def contruirSiembraDataFrame():
    datosSiembra = siembraArboles()
    
    #generar dataframe
    siembraDataFrame = pd.DataFrame(datosSiembra, columns= [ 'nombre', 'correjimiento', 'Hectarea', 'especie', 'fecha', 'Correo' ])    
    
    
    
    # Limpiando el dataframe
    siembraDataFrame.replace('sin', pd.NA, inplace=True)
    
    filtroSiembraAlta = siembraDataFrame.query("(Hectarea>=1000) and (Hectarea<100000)").value_counts()
    filtroSiembraOptima= siembraDataFrame.query("(Hectarea>=500) and (Hectarea<1000)").value_counts()
    filtroSiembraBaja = siembraDataFrame.query("(Hectarea>=0) and (Hectarea<500)").value_counts()
    
    
    # Ordenando los datos para graficarlos
    datosOrdenadosSiembra = siembraDataFrame.groupby('correjimiento')['Hectarea'].mean() 
    
    
    # Grafico la info
    plt.figure(figsize=(20,20))
    datosOrdenadosSiembra.plot(kind='bar', color='green')
    plt.title("Indice de Siembra por Corregimiento")
    plt.xlabel("correjimiento")
    plt.ylabel("Hectarea")
    plt.grid(True)
    plt.savefig("./img/calidadSiembra.png", format='png', dpi=300)
    
contruirSiembraDataFrame()