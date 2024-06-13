import pandas as pd

from data.generator.agua import accesoAgua

def contruiraguaDataFrame():
    datosconsumoAgua= accesoAgua()
    
    #generar dataframe
    consumoAguaDataFrame = pd.DataFrame(datosconsumoAgua, columns= [ 'nombre', 'consumoMes', 'accesoAlAlcantarillado', 'comuna', 'fecha', 'Correo' ])    
    print(consumoAguaDataFrame)
    
    #generamos html
    
    #crear tabla (consumoAguaDataFrame, "datosConsumoAgua")
    #limmpiando el dataframe
    
    consumoAguaDataFrame.replace('sin', pd.NA, inplace=True )
    
    #Filtrar datos
    filtroConsumoMuyAlto = consumoAguaDataFrame.query("(consumoMes>=900) and (consumoMEs<1000)").value_counts()
    filtroConsumoAlto = consumoAguaDataFrame.query("(consumoMes>=801) and (consumoMEs<890").value_counts()
    filtroConsumoOptimo = consumoAguaDataFrame.query("(consumoMes>=700) and (consumoMEs<800").value_counts()
    
    
    datosOrdenadosAgua = consumoAguaDataFrame.groupby('comunna')['consumoMes'].mean()