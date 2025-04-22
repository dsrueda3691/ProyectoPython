import streamlit as st
from clases import Auto

def mostrar_admin(concesionario):
    st.subheader("Gestión de Inventario de Vehículos")

    # Formulario para agregar autos
    with st.form("Agregar Auto", clear_on_submit=True):
        st.markdown("### Agregar un Nuevo Auto")
        
        col1, col2 = st.columns(2)  # Dos columnas para los campos de entrada
        with col1:
            marca = st.text_input("Marca")
            modelo = st.text_input("Modelo")
            año = st.number_input("Año", min_value=1900, max_value=2100, step=1)
        with col2:
            precio = st.number_input("Precio", min_value=0.0, step=1000.0)
            imagen = st.text_input("Imagen", value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPBzET7eg0wmQpGcOTWwRdolhOFJ9W-z96EQ&s")
        
        submit = st.form_submit_button("Agregar Auto")
        if submit:
            if marca and modelo and año and precio and imagen:
                nuevo_auto = Auto(marca, modelo, año, precio, imagen)
                concesionario.agregar_auto(nuevo_auto)
                st.success(f"Auto {marca} {modelo} agregado con éxito.")
            else:
                st.error("Por favor, completa todos los campos.")

    # Mostrar y gestionar autos en un combobox
    if concesionario.inventario:
        st.subheader("Lista de Autos en el Inventario")
        st.markdown("### Selecciona un auto para gestionar:")
        opciones = [f"{auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}" for auto in concesionario.inventario if not auto.vendido]
        
        seleccionado = st.selectbox("Selecciona un auto para gestionar:", opciones)
        
        auto = next((auto for auto in concesionario.inventario if f"{auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}" == seleccionado), None)

        if auto:
            st.write(f"**Seleccionado:** {auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}")

            col1, col2 = st.columns(2)  # Dos columnas para botones
            with col1:
                if st.button("Actualizar", key=f"actualizar_{auto.marca}_{auto.modelo}"):
                    st.session_state.auto_a_actualizar = auto
                with col2:
                    if st.button("Eliminar", key=f"eliminar_{auto.marca}_{auto.modelo}"):
                        concesionario.inventario.remove(auto)
                        st.warning(f"Auto {auto.marca} {auto.modelo} eliminado del inventario.")

    else:
        st.info("No hay autos disponibles actualmente.")

    # Mostrar formulario de actualización si hay un auto en session_state
    if "auto_a_actualizar" in st.session_state:
        auto = st.session_state.auto_a_actualizar
        st.subheader(f"Actualizar Auto: {auto.marca} {auto.modelo}")
        st.markdown("### Edita los campos que desees actualizar")

        with st.form(f"Actualizar {auto.marca} {auto.modelo}", clear_on_submit=True):
            col1, col2 = st.columns(2)  # Dos columnas para el formulario
            with col1:
                marca = st.text_input("Marca", value=auto.marca)
                modelo = st.text_input("Modelo", value=auto.modelo)
                año = st.number_input("Año", min_value=1900, max_value=2100, step=1, value=auto.año)
            with col2:
                precio = st.number_input("Precio", min_value=0.0, step=1000.0, value=float(auto.precio))
                imagen = st.text_input("Imagen", value=auto.imagen)
            
            submit = st.form_submit_button("Guardar Cambios")
            if submit:
                if marca and modelo and año and precio and imagen:
                    # Actualizar el objeto directamente
                    auto.marca = marca
                    auto.modelo = modelo
                    auto.año = año
                    auto.precio = precio
                    auto.imagen = imagen

                    st.success(f"Auto {auto.marca} {auto.modelo} actualizado con éxito.")
                    # Limpiamos el auto en edición
                    del st.session_state.auto_a_actualizar
                else:
                    st.error("Por favor, completa todos los campos.")