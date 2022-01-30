#set up notebook
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#load data
data_file="Visualisasi_data/flight_delays.csv"
data=pd.read_csv(data_file,index_col='Month')
print(data)
#plot
plt.figure(figsize=(10,6))
v_barchart=sns.barplot(x=data.index,y=data['NK'])
plt.title("Panjang Delay Penerbangan Dunia 2021")
plt.ylabel("Arrival Delay (in minutes)")
plt.show()