import streamlit as st
import Inicio as inicio
import autos as cliente
import admin
import perfil
import clases as cs


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
    opciones = ["Inicio", "Autos","Admin", "Perfil", "Cerrar Sesión"]
elif st.session_state.usuario:
    opciones = ["Inicio", "Autos","Perfil", "Cerrar Sesión"]
else:
    opciones = ["Inicio", "Autos",  "Login"]

st.session_state.pagina = st.sidebar.radio("Selecciona una opción", opciones) 


def cargar_autos_iniciales():
    if not st.session_state.concesionario.inventario:
        autos = [
            cs.Auto("Toyota", "Corolla", 2020, 17500, "https://cdn.pixabay.com/photo/2015/01/19/13/51/car-604019_1280.jpg"),
            cs.Auto("Honda", "Civic", 2021, 18900, "https://cdn.pixabay.com/photo/2017/01/06/19/15/honda-1957037_1280.jpg"),
            cs.Auto("Ford", "Mustang", 2019, 26000, "https://cdn.pixabay.com/photo/2015/01/19/13/51/car-604019_1280.jpg"),
            cs.Auto("Chevrolet", "Camaro", 2018, 24000, "https://th.bing.com/th/id/OIP.5YB3vP0GBoxHZPdgkg4wSgAAAA?rs=1&pid=ImgDetMain"),
            cs.Auto("Nissan", "Altima", 2022, 21000, "https://cdn.pixabay.com/photo/2016/06/17/06/24/auto-1468720_1280.jpg"),
        ]
        for auto in autos:
            st.session_state.concesionario.agregar_auto(auto)

cargar_autos_iniciales()

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




elif st.session_state.pagina == "Perfil":
    perfil.mostrar_perfil(st.session_state.usuario, st.session_state.rol, st.session_state.concesionario)


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
