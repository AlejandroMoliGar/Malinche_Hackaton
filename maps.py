import folium
from locations import locations, iconos
from streamlit_folium import folium_static
from folium.features import CustomIcon
#import googlemaps

def create_map():

    m = folium.Map(location=[20.0410054,-90.2256905], zoom_start=13)
    folium.Marker(location=[20.0410054,-90.2256905], tooltip='Tu ubicación').add_to(m)

    #m = folium.Map(location=[location['location']['lat'], location['location']['lng']], zoom_start=13)
    #folium.Marker(location=[location['location']['lat'], location['location']['lng']], tooltip='Tu ubicación').add_to(m)

    #gmaps = googlemaps.Client(key='AIzaSyChU5WCul4HUz413FR4wVEMKmsElDm2DFk')
    
    #location = gmaps.geolocate()

    for coord, icono_path in zip(locations, iconos):
        folium.Marker(
            location=coord,
            icon=folium.CustomIcon(
                icon_image=icono_path,
                icon_size=(25, 25)
            )
        ).add_to(m)

    folium.PolyLine(
        locations=locations,
        color='red',
        weight=5,
        opacity=0.2,
    ).add_to(m)

    return m

def display_map():
    m = create_map()
    folium_static(m)
