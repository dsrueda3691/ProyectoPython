import streamlit as st

def mostrar_perfil(usuario, rol, concesionario):
    st.subheader("Perfil de Usuario")
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; display: flex; border-radius: 10px; padding: 20px; margin-bottom: 20px; align-items: center; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); width: 600px; height: 500px;">
        <div style="display: flex; flex-direction: column; align-items: center;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAEbo912SNlE28OayU-KnDZqjV5-KU3XqY-A&s" alt="" style="width: 250px; height: 200px; border-radius: 8px; object-fit: cover; margin-bottom: 10px;">

        </div>

        <div style="display: flex; flex-direction: column; margin-left: 20px;">
            <h3 style="margin: 0; font-size: 1.2em; font-weight: 600;">
                <strong>Rol:</strong> {rol} 
            </h3>
            <h3 style="margin: 0; font-size: 1.2em; font-weight: 600;">
                <strong>Usuario::</strong> {usuario}
            </h3>
            <h2 style="margin: 5px 0; font-size: 0.9em;">Descripción:----</h2>
            <p style="margin: 5px 0; font-size: 1em; font-weight: bold; color: #007BFF;"></p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # Mostrar autos vendidos según el rol
    if rol == "admin":
            
        st.subheader("Autos Vendidos")
        autos_vendidos = [auto for auto in st.session_state.concesionario.inventario if auto.vendido]
    else:
        st.subheader("Autos Comprados")
        autos_vendidos = [auto for auto in st.session_state.concesionario.inventario if auto.vendido and auto.comprador == usuario]

    if autos_vendidos:
        
        for auto in autos_vendidos:
            st.markdown(f"**{auto.marca} {auto.modelo} ({auto.año})** - ${auto.precio:,.2f}")
            st.image(auto.imagen, width=250)
            st.markdown("---")
    else:
        st.info("No has comprado ningún auto todavía." if rol != "admin" else "No hay autos vendidos aún.")

