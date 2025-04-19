import streamlit as st
from streamlit.components.v1 import html

def mostrar_inicio(concesionario):
    st.markdown("""
    <style>
    
    .hero-section {
        
        padding: 30px;
        text-align: center;
        border-radius: 10px;
        
    }
    .section {
        margin-top: 20px;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        
    }
    .section h2 {
        margin-bottom: 15px;
        font-size: 1.5rem;
        color: #007BFF;
        
    }
    .card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
        background-color: #fff;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        
    }
    .card img {
        max-width: 100%;
        border-radius: 10px;
        margin-bottom: 10px;
        
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown(
        """
        <div class="hero-section">
            <h1>Bienvenido a AutoShop</h1>
            <p>Encuentra los mejores vehículos para tus necesidades. Autos confiables, modernos y al mejor precio.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

   