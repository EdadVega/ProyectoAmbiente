import pandas as pd

from data.generator.vehiculos import cantidadVehiculos

def contruiraguaDataFrame():
    datosCantidadVehiculos =  cantidadVehiculos()
    
    #generar dataframe
    cantidadVehiculosDataFrame = pd.DataFrame(datosCantidadVehiculos, columns= [ 'nombre', 'vDiesel', 'vCte', 'vElectrico', 'comuna', 'fecha', 'Correo' ])    
    print(cantidadVehiculosDataFrame)