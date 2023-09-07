import folium
from locations import locations, iconos
from streamlit_folium import folium_static
from folium.features import CustomIcon

def create_map():
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
