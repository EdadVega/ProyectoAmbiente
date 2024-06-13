import pandas as pd

from data.generator.ruidoAmbiental import ruidoAmbiental

def contruirRuidoDataFrame():
    datosRuido = ruidoAmbiental()
    
    #generar dataframe
    ruidoDataFrame = pd.DataFrame(datosRuido, columns= ['nombre', 'comuna', 'dbDiurnos', 'dbNocturnos', 'fecha', 'direccion'] )    

    print(ruidoDataFrame)