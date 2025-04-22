import streamlit as st
from componentes_detalles import tarjeta_auto, mostrar_detalles_auto

def mostrar_autos(concesionario):
    if "mostrar_detalles" not in st.session_state:
        st.session_state.mostrar_detalles = False
    if "auto_seleccionado" not in st.session_state:
        st.session_state.auto_seleccionado = None

    if st.session_state.mostrar_detalles and st.session_state.auto_seleccionado:
        auto = st.session_state.auto_seleccionado
        mostrar_detalles_auto(auto)

        if st.button("Volver a la lista de autos"):
            st.session_state.mostrar_detalles = False
            st.session_state.auto_seleccionado = None

        if st.button("Confirmar Compra"):
            auto.vender(st.session_state.usuario)  # Guardamos el comprador
            st.success(f"¡Felicidades! Has comprado el {auto.marca} {auto.modelo}.")
            st.session_state.auto_seleccionado = None
            st.session_state.mostrar_detalles = False
            st.rerun()


    else:
        st.subheader("Autos disponibles para la venta")
        if concesionario.inventario:
            for auto in concesionario.inventario:
                if not auto.vendido:
                    tarjeta_auto(auto)
                    if st.button(f"Detalles de {auto.marca} {auto.modelo}", key=f"detalles_{auto.marca}_{auto.modelo}"):
                        st.session_state.mostrar_detalles = True
                        st.session_state.auto_seleccionado = auto
                        st.rerun()
        else:
            st.info("No hay autos disponibles actualmente.")

