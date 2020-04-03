import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

# Read data
df = pd.read_csv('http://www.cedriccourtois.be/files/fs-data.csv', delimiter = ";")

df = df.dropna(subset = ['lat', 'lng'])
some_map = folium.Map(location=[-25.609138,134.361954],tiles = "Stamen Toner",zoom_start=5)

for row in df.itertuples():

  if row.restaurant == 'McDonalds':
        some_map.add_child(folium.CircleMarker(location=[row.lat,row.lng],radius=10,color="red",fill=True,fill_opacity=0.9))
  if row.restaurant == 'KFC':
        some_map.add_child(folium.CircleMarker(location=[row.lat,row.lng],radius=10,color="blue",fill=True,fill_opacity=0.9))
  if row.restaurant == 'Domino\'s':
        some_map.add_child(folium.CircleMarker(location=[row.lat,row.lng],radius=10,color="green",fill=True,fill_opacity=0.9))
  if row.restaurant == 'Hungry Jack\'s':
        some_map.add_child(folium.CircleMarker(location=[row.lat,row.lng],radius=10,color="orange",fill=True,fill_opacity=0.9))
  if row.restaurant == 'Pizza Hut':
        some_map.add_child(folium.CircleMarker(location=[row.lat,row.lng],radius=10,color="purple",fill=True,fill_opacity=0.9))

some_map.save("interactivemap.html")
