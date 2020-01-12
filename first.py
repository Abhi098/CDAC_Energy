
import pandas as pd

building_meta=pd.read_csv(r"D:\project_energy\building_metadata.csv")
print("##################################")
print("BUILDING METADATA ",building_meta.shape)
for i in building_meta.columns:
    print(i," ",building_meta[i].isnull().sum())
    
train=pd.read_csv(r"D:\project_energy\train.csv")
print("##################################")
print(" ")
print("##################################")      
print("TRAIN ",train.shape)
for i in train.columns:
    print(i," ",train[i].isnull().sum())
print("##################################")
print(" ")

print("##################################")
      
weather=pd.read_csv(r"D:\project_energy\weather_train.csv")
print("WEATHER ",weather.shape)
for i in weather.columns:
    print(i," ",weather[i].isnull().sum())
print("##################################")
      

