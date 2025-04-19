import streamlit as st
from clases import Auto

def mostrar_admin(concesionario):
    st.subheader("Gestión de Inventario de Vehículos")

    # Formulario para agregar autos
    with st.form("Agregar Auto", clear_on_submit=True):
        marca = st.text_input("Marca")
        modelo = st.text_input("Modelo")
        año = st.number_input("Año", min_value=1900, max_value=2100, step=1)
        precio = st.number_input("Precio", min_value=0.0, step=1000.0)
        imagen= st.text_input("Imagen", value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPBzET7eg0wmQpGcOTWwRdolhOFJ9W-z96EQ&s")
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
        opciones = [f"{auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}" for auto in concesionario.inventario if not auto.vendido]
        
        seleccionado = st.selectbox("Selecciona un auto para gestionar:", opciones)
        
        if seleccionado:
            auto = next((auto for auto in concesionario.inventario if f"{auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}" == seleccionado), None)
            
            if auto:
                st.write(f"**Seleccionado:** {auto.marca} {auto.modelo} ({auto.año}) - ${auto.precio:,.2f}")
                # Botón para actualizar
                if st.button("Actualizar"):
                    
                    actualizar_auto(auto, concesionario)
                # Botón para eliminar
                if st.button("Eliminar"):
                    concesionario.inventario.remove(auto)
                    st.warning(f"Auto {auto.marca} {auto.modelo} eliminado del inventario.")
    else:
        st.info("No hay autos disponibles actualmente.")

def actualizar_auto(auto, concesionario):
    # Formulario para actualizar los datos de un auto
    with st.form(f"Actualizar {auto.marca} {auto.modelo}", clear_on_submit=True):
        marca = st.text_input("Marca", value=auto.marca)
        modelo = st.text_input("Modelo", value=auto.modelo)
        año = st.number_input("Año", min_value=1900, max_value=2100, step=1, value=auto.año)
        precio = st.number_input("Precio", min_value=0.0, step=1000.0, value=auto.precio)
        imagen =st.text_input("Imagen", value=auto.imagen)
        submit = st.form_submit_button("Guardar Cambios")

        if submit:
            if marca and modelo and año and precio and imagen:
                concesionario.inventario.remove(auto)
                nuevo_auto = Auto(marca, modelo, año, precio, imagen)
                concesionario.agregar_auto(nuevo_auto)
                st.success(f"Auto {marca} {modelo} agregado con éxito.")
                
            else:
                st.error("Por favor, completa todos los campos.")
