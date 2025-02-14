import streamlit as st 
import pandas

#diseno de la pagina
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Web_app/Me.jpg", width=400)

with col2:
    st.title("Juan Cabrera")
    text = """
    Hello this my first porfolio.

    """
    st.info(text)

text2 = """Below you can find some of the apps
        I have built in python. Feel free to contact me
        """
st.write(text2)

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])
  # usamos pandas para leer el contenido del archivo csv se agrega el 
 # parametro sep para que pandas sepa como esta separada la informacion
   
data = pandas.read_csv("data.csv", sep=";")

with col3:
 
 #recorre las primeras 10 filas de un DataFrame de pandas (data) y muestra 
 # el contenido de la columna "title" como un encabezado en Streamlit.
 
 for index, row in data[0:10].iterrows():
    st.subheader(row["title"])
    st.write(row["description"])
    st.image("images/" + row["image"])
    st.write(f"[Source code]({row['url']})")

with col4:
   for index, row in data[10:20].iterrows():
    st.subheader(row["title"])
    st.write(row["description"])
    st.image("images/" + row["image"])
    st.write(f"[Source code]({row['url']})")