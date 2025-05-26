import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(layout="wide")

st.title("Карта Folium у Streamlit")
st.write("Інтерактивна карта з центром у місті Сторожинець, Чернівецька область.")

# Створення карти
storozhynets_coords = [48.1617, 25.7096]
m = folium.Map(location=storozhynets_coords, zoom_start=13)

# Додавання маркера
folium.Marker(
    location=storozhynets_coords,
    popup="Сторожинець, Чернівецька область",
    tooltip="Клікни для підпису"
).add_to(m)

# Збереження карти в HTML
m.save("map.html")

# Відображення HTML в Streamlit
with open("map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

html(map_html, height=600)
