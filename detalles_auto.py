import streamlit as st

def mostrar_detalles_auto():
    if "auto_seleccionado" in st.session_state and st.session_state.auto_seleccionado:
        auto = st.session_state.auto_seleccionado
        st.image(auto.imagen, width=500)
        st.title(f"{auto.marca} {auto.modelo}")
        st.write(f"**Año:** {auto.año}")
        st.write(f"**Precio:** ${auto.precio:,.2f}")
        st.write(
            f"""
            El {auto.marca} {auto.modelo} es uno de los modelos más destacados de su categoría. 
            Ofrece una experiencia de conducción de primera calidad y un diseño que combina 
            estilo y funcionalidad. Es perfecto para quienes buscan un vehículo confiable con tecnología avanzada.
            """
        )
        if st.button("Volver"):
            st.session_state.pagina = "Autos"

        if st.button("Confirmar Compra"):
            auto.vender()
            st.success(f"¡Felicidades! Has comprado el {auto.marca} {auto.modelo}.")
            st.session_state.auto_seleccionado = None
            st.session_state.pagina = "Cliente"
    else:
        st.error("No hay auto seleccionado.")
