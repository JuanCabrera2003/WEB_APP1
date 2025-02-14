import streamlit as st 

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Web_app/Me.jpg", width=600)

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

col3, col4 = st.columns(2)

with col3:
    st.subheader("Task List")
    st.image("/Users/yesus/Downloads/images/1.png")


with col4:
    st.subheader("Detector")