import pandas as pd

from data.generator.siembraArboles import siembraArboles

def contruirSiembraDataFrame():
    datosSiembra = siembraArboles()
    
    #generar dataframe
    siembraDataFrame = pd.DataFrame(datosSiembra, columns= [ 'nombre', 'correjimiento', 'Hectarea', 'especie', 'fecha', 'Correo' ])    
    print(siembraDataFrame)