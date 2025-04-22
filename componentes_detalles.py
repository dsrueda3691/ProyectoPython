import streamlit as st

def tarjeta_auto(auto):
    st.markdown(
        f"""
        <div style="color: black; border: 1px solid #ddd; border-radius: 12px; padding: 20px; margin-bottom: 20px; background-color: #ffffff; display: flex; flex-direction: row; align-items: center; justify-content: space-between; max-width: 800px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <div style="flex-shrink: 0;">
                <img src="{auto.imagen}" alt="Auto" style="width: 250px; height: auto; border-radius: 10px; object-fit: cover;">
            </div>
            <div style="flex-grow: 1; padding-left: 20px;">
                <h3 style="margin: 0; font-size: 1.3em; font-weight: 600; color: #333;">{auto.marca} {auto.modelo}</h3>
                <p style="margin: 5px 0; font-size: 1em; color: #555;"><strong>Año:</strong> {auto.año}</p>
                <p style="margin: 5px 0; font-size: 1.2em; font-weight: bold; color: #007BFF;"><strong>Precio:</strong> ${auto.precio:,.2f}</p>
            </div>
        </div>
        """,
        #esto me deja usar html
        unsafe_allow_html=True
    )

def mostrar_detalles_auto(auto):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(auto.imagen, use_container_width=True)
    
    with col2:
        st.title(f"{auto.marca} {auto.modelo}")
        st.subheader(f"Año: {auto.año}")
        st.subheader(f"Precio: ${auto.precio:,.2f}")
        st.write(
            f"""
            **Descripción:**

            El {auto.marca} {auto.modelo} es uno de los modelos más destacados de su categoría. 
            Ofrece una experiencia de conducción de primera calidad y un diseño que combina estilo y funcionalidad.
            """
        )