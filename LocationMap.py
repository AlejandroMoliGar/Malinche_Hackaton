import streamlit as st
import googlemaps
import folium
from locations import locations, iconos, nombres
from streamlit_folium import folium_static
from folium.features import CustomIcon

# Obtener la clave de API de Google Maps
gmaps = googlemaps.Client(key='AIzaSyChU5WCul4HUz413FR4wVEMKmsElDm2DFk')

# Obtener la ubicación actual del usuario
location = [20.0410054,-90.2256905]


# Crear un mapa centrado en la región específica
m = folium.Map(location=[20.0410054,-90.2256905], zoom_start=13)
folium.Marker(location=[20.0410054,-90.2256905], tooltip='Tu ubicación').add_to(m)

for coord, icono_path in zip(locations, iconos):
    folium.Marker(
        location=coord,
        icon=folium.CustomIcon(
            icon_image=icono_path,
            icon_size=(25, 25)
        )
    ).add_to(m)

#Agrega las lineas de seguimiento
folium.PolyLine(
    locations=locations,
    color='red',
    weight=5,
    opacity=0.2,
).add_to(m)

# Mostrar el mapa en Streamlit
folium_static(m)