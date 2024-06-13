import pandas as pd
import matplotlib.pyplot as plt
from data.generator.ruidoAmbiental import ruidoAmbiental

def contruirRuidoDataFrame():
    datosRuido = ruidoAmbiental()
    
    #generar dataframe
    ruidoDataFrame = pd.DataFrame(datosRuido, columns= ['nombre', 'comuna', 'dbDiurnos', 'dbNocturnos', 'fecha', 'direccion'] )    

    # Limpiando el dataframe
    ruidoDataFrame.replace('sin', pd.NA, inplace=True)
    
    filtroRuidoAlto = ruidoDataFrame.query("(dbDiurnos>=60) and (dbDiurnos<100)").value_counts()
    filtroRuidoNormal= ruidoDataFrame.query("(dbDiurnos>=40) and (dbDiurnos<50)").value_counts()
    filtroRuidoBajo = ruidoDataFrame.query("(dbDiurnos>=0) and (dbDiurnos<400)").value_counts()
    
    
    # Ordenando los datos para graficarlos
    datosOrdenadosRuido = ruidoDataFrame.groupby('comuna')['dbDiurnos'].mean() 
    
    
    # Grafico la info
    plt.figure(figsize=(20,20))
    datosOrdenadosRuido.plot(kind='bar', color='green')
    plt.title("Indice de contaminacion auditiva")
    plt.xlabel("comuna")
    plt.ylabel("dbDiurno")
    plt.grid(True)
    plt.savefig("./img/calidadRuido.png", format='png', dpi=300)
    
contruirRuidoDataFrame()