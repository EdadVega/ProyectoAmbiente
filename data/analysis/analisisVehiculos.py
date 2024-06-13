import pandas as pd
import matplotlib.pyplot as plt

from data.generator.vehiculos import cantidadVehiculos

def contruiraguaDataFrame():
    datosCantidadVehiculos =  cantidadVehiculos()
    
    #generar dataframe
    cantidadVehiculosDataFrame = pd.DataFrame(datosCantidadVehiculos, columns= [ 'nombre', 'vDiesel', 'vCte', 'vElectrico', 'comuna', 'fecha', 'Correo' ])    
    
    # Limpiando el dataframe
    cantidadVehiculosDataFrame.replace('sin', pd.NA, inplace=True)
    
    filtroMuchosCarros = cantidadVehiculosDataFrame.query("(vElectrico>=0) and (vElectrico<1000)").value_counts()
    filtroCarrosoptimos= cantidadVehiculosDataFrame.query("(vElectrico>=0) and (vElectrico<1000)").value_counts()
    filtroCarrosPocosCarros = cantidadVehiculosDataFrame.query("(vElectrico>=0) and (vElectrico<500)").value_counts()
    
    
    # Ordenando los datos para graficarlos
    datosOrdenadosVehiculos= cantidadVehiculosDataFrame.groupby('comuna')['vElectrico'].mean() 
    
    
    # Grafico la info
    plt.figure(figsize=(20,20))
    datosOrdenadosVehiculos.plot(kind='bar', color='green')
    plt.title("Cantidad Vehiculos por comuna")
    plt.xlabel("comuna")
    plt.ylabel("vElectrico")
    plt.grid(True)
    plt.savefig("./img/vehiculos.png", format='png', dpi=300)
    
contruiraguaDataFrame()