import streamlit as st

# Configuración de la página para dispositivos móviles
st.set_page_config(
    page_title="Mi Closet & Lookbook",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo visual moderno estilo App Móvil
st.markdown("""
    <style>
    .stApp { max-width: 800px; margin: 0 auto; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #2e4053; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Mi Closet & Lookbook Digital")

# Navegación por pestañas fluidas
tab1, tab2, tab3 = st.tabs(["📸 Lookbook Continuo", "👗 Mi Armario", "🤖 Asistente de Moda"])

with tab1:
    st.header("Álbum de Outfits Aprobados")
    st.caption("Desliza suavemente hacia abajo para explorar todos tus conjuntos en formato de álbum continuo.")
    
    # Galería continua de Outfits Aprobados
    outfits = [
        {
            "titulo": "Look 1: Vestido Escocés y Botas de Gamuza", 
            "url": "https://drive.google.com/uc?export=view&id=1EEGB35H_f2c-WhW1RLGV9vaYkPzgQHjF", 
            "desc": "Vestido escocés con mangas largas, cuello tortuga y botas altas de gamuza café."
        },
        # Aquí iremos sumando las siguientes combinaciones aprobadas de tu bitácora
    ]
    
    for outfit in outfits:
        st.markdown(f"### {outfit['titulo']}")
        st.image(outfit["url"], use_column_width=True)
        st.write(outfit["desc"])
        st.divider()

with tab2:
    st.header("Inventario de Armario")
    categoria = st.selectbox("Filtrar por categoría:", ["Todas", "Tops y Camisas", "Pantalones y Faldas", "Vestidos", "Abrigos", "Calzado"])
    st.info("Aquí tienes el catálogo detallado de tus prendas reales verificadas (VST, PNT, TOP, CLZ).")

with tab3:
    st.header("Asistente Virtual de Estilo")
    st.write("¿Qué quieres vestir hoy? Escribe abajo para pedirme nuevas combinaciones con la ropa de tu armario.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ej: Armame un look casual con la biker negra..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = f"¡Excelente elección! Para tu consulta: '{prompt}', te sugiero combinar tus prendas verificadas de la bitácora."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
