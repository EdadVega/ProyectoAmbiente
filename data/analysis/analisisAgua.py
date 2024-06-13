import pandas as pd
import matplotlib.pyplot as plt

from data.generator.agua import accesoAgua

def contruiraguaDataFrame():
    datosconsumoAgua= accesoAgua()
    
    #generar dataframe
    consumoAguaDataFrame = pd.DataFrame(datosconsumoAgua, columns= [ 'nombre', 'consumoMes', 'accesoAlAlcantarillado', 'comuna', 'fecha', 'Correo' ])    
    
    
    #generamos html
    
    #crear tabla (consumoAguaDataFrame, "datosConsumoAgua")
    #limmpiando el dataframe
    
    consumoAguaDataFrame.replace('sin', pd.NA, inplace=True )
    
    #Filtrar datos
    filtroConsumoMuyAlto = consumoAguaDataFrame.query("(consumoMes>=900) and (consumoMes<1000)").value_counts()
    filtroConsumoAlto = consumoAguaDataFrame.query("(consumoMes>=801) and (consumoMes<890)").value_counts()
    filtroConsumoOptimo = consumoAguaDataFrame.query("(consumoMes>=700) and (consumoMes<800)").value_counts()
    
    
    datosOrdenadosAgua = consumoAguaDataFrame.groupby('comuna')['consumoMes'].mean()
    print(datosOrdenadosAgua)
   
    plt.figure(figsize=(20,20))
    datosOrdenadosAgua.plot(kind='bar', color='green')
    plt.title("Indice de consumo de Agua")
    plt.xlabel("comuna")
    plt.ylabel("consumoMes")
    plt.grid(True)
    plt.savefig("./img/consumoAgua.png", format='png', dpi=300)
    
contruiraguaDataFrame()
    