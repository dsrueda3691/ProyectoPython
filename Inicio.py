import streamlit as st

def mostrar_inicio(concesionario):
    st.markdown("<h1 style='color: #2E86C1; font-family: Arial, sans-serif;'>Bienvenido a AutoShop 🚘</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px; font-family: Arial, sans-serif; color: #555;'>¡Bienvenido a AutoShop! Somos un concesionario de confianza con una amplia variedad de vehículos nuevos y usados.</p>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/?size=100&id=Fmaz1iZbHetE&format=png&color=000000", width=150)
    st.markdown("---")
    st.markdown("<p style='font-size:16px; font-family: Arial, sans-serif; color: #333;'>Explora nuestro catálogo y encuentra el auto perfecto para ti.</p>", unsafe_allow_html=True)
    
