import streamlit as st

st.title ("Dell Global Busyness Centre")
st.image ("dell_logo.jpg", width = 300)
st.camera_input ("Case Input:")
st.date_input ("Transactional Date")
st.radio ("Department:", ['AI', 'CFI', 'ISG NPI', 'CSG NPI'])


###

