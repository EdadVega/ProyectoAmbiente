import pandas as pd
import matplotlib.pyplot as plt

from data.generator.generadorAire import generarDatosCalidadAire
from helpers.tablaHtml import crearTabla

def construirAireDataFrame():
    datosAire = generarDatosCalidadAire()
    
    # Generamos el dataframe
    aireDataFrame = pd.DataFrame(datosAire, columns=['nombre', 'comuna', 'ICA', 'fecha', 'correo'])
    
    # Limpiando el dataframe
    aireDataFrame.replace('sin', pd.NA, inplace=True)
    
    # Filtrar Datos
    filtroCalidadAireBueno = aireDataFrame.query("(ICA>=10) and (ICA<40)").value_counts()
    filtroCalidadAireAceptable = aireDataFrame.query("(ICA>=40) and (ICA<50)").value_counts()
    filtroCalidadAireMala = aireDataFrame.query("(ICA>=50) and (ICA<100)").value_counts()
    
    # Ordenando los datos para graficarlos
    datosOrdenadosAire = aireDataFrame.groupby('comuna')['ICA'].mean()  # El error estaba aquí, corregido de 'comunna' a 'comuna'
    print(datosOrdenadosAire)
   
    # Grafico la info
    plt.figure(figsize=(20,20))
    datosOrdenadosAire.plot(kind='bar', color='green')
    plt.title("Indice de contaminacion del Aire por comuna en Medellin")
    plt.xlabel("comuna")
    plt.ylabel("ICA")
    plt.grid(True)
    plt.savefig("./img/calidadaire.png", format='png', dpi=300)
    
construirAireDataFrame()
