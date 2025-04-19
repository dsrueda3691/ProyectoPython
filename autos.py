import streamlit as st
import detalles_auto as de

boton=False
def mostrar_autos(concesionario):
    st.subheader("Autos disponibles para la venta")

    # Mostrar autos disponibles
    if concesionario.inventario:
        for auto in concesionario.inventario:
            if not auto.vendido:
                st.markdown(
                    f"""
                    <div style="color: black; border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; display: flex; align-items: center; max-width: 400px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <!-- Imagen del auto -->
                    <img src="{auto.imagen}" alt="Auto" style="width: 50%; height: 50%; border-radius: 8px; object-fit: cover; margin-right: 20px;">
                    
                    <!-- Contenido de la tarjeta -->
                    <div>
                        <h3 style="margin: 0; font-size: 1.2em; font-weight: 600;">{auto.marca} {auto.modelo}</h3>
                        <p style="margin: 5px 0; font-size: 0.9em; color: #555;"><strong>Año:</strong> {auto.año}</p>
                        <p style="margin: 5px 0; font-size: 1em; font-weight: bold; color: #007BFF;"><strong>Precio:</strong> $ {auto.precio:,.2f}</p>
                        
                    </div>
                    </div>

                    """,
                    unsafe_allow_html=True
                )
                if st.button(f"Comprar", key=f"comprar_{auto.marca}_{auto.modelo}"):
                    st.session_state.auto_seleccionado = auto
                    de.mostrar_detalles_auto()
                    
    else:
        st.info("No hay autos disponibles actualmente.")
