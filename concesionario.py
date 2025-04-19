import streamlit as st
import Inicio as inicio
import autos as cliente
import admin
import perfil
import clases as cs
import detalles_auto

# Inicializar datos en session_state si no existen
if "concesionario" not in st.session_state:
    st.session_state.concesionario = cs.Concesionario("AutoShop")

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"  # Página principal por defecto

if "rol" not in st.session_state:
    st.session_state.rol = None

if "usuario" not in st.session_state:
    st.session_state.usuario = None

# Configurar barra de navegación
if st.session_state.usuario and st.session_state.rol == "admin":
    opciones = ["Inicio", "Autos", "Detalles del Auto","Admin", "Perfil", "Cerrar Sesión"]
elif st.session_state.usuario:
    opciones = ["Inicio", "Autos", "Detalles del Auto","Perfil", "Cerrar Sesión"]
else:
    opciones = ["Inicio", "Autos",  "Login"]

st.session_state.pagina = st.sidebar.radio("Selecciona una opción", opciones)

# Lógica para renderizar páginas
if st.session_state.pagina == "Inicio":
    inicio.mostrar_inicio(st.session_state.concesionario)

elif st.session_state.pagina == "Autos":
    cliente.mostrar_autos(st.session_state.concesionario)

elif st.session_state.pagina == "Admin":
    if st.session_state.rol == "admin":
        admin.mostrar_admin(st.session_state.concesionario)
    else:
        st.warning("Necesitas iniciar sesión como administrador para acceder a esta sección.")

elif st.session_state.pagina == "Detalles del Auto":
    detalles_auto.mostrar_detalles_auto()


elif st.session_state.pagina == "Perfil":
    perfil.mostrar_perfil(st.session_state.usuario, st.session_state.rol)

elif st.session_state.pagina == "Cerrar Sesión":
    st.session_state.usuario = None
    st.session_state.rol = None 
    st.success("Has cerrado sesión exitosamente.")
    st.session_state.pagina = "Login" 

elif st.session_state.pagina == "Login":
    st.subheader("Login")
    if not st.session_state.usuario:
        # Formulario de inicio de sesión
        usuario = st.text_input("Usuario:")
        contraseña = st.text_input("Contraseña:", type="password")

        if st.button("Iniciar Sesión"):
            if usuario in cs.usuarios and cs.usuarios[usuario]["password"] == contraseña:
                st.session_state.rol = cs.usuarios[usuario]["rol"]
                st.session_state.usuario = usuario
                st.success(f"Bienvenido {usuario}")
            else:
                st.error("Credenciales incorrectas")
