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
    .card { background-color: #f8f9f9; padding: 15px; border-radius: 15px; margin-bottom: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Mi Closet & Lookbook Digital")

# Navegación por pestañas
tab1, tab2, tab3 = st.tabs(["📸 Lookbook Continuo", "👗 Mi Armario", "🤖 Asistente de Moda"])

with tab1:
    st.header("Álbum de Outfits Aprobados")
    st.caption("Desliza suavemente hacia abajo para explorar todos tus conjuntos.")
    
    # Galería continua de Outfits
    outfits = [
        {"titulo": "Look 1: Vestido Escocés y Botas Largas", "url": "https://drive.google.com/uc?id=1EEGB35H_f2c-WhW1RLGV9vaYkPzgQHjF", "desc": "Vestido escocés con mangas largas y botas altas de gamuza café."},
    ]
    
    for outfit in outfits:
        st.markdown(f"### {outfit['titulo']}")
        st.image(outfit["url"], use_column_width=True)
        st.write(outfit["desc"])
        st.divider()

with tab2:
    st.header("Inventario de Armario")
    categoria = st.selectbox("Filtrar por categoría:", ["Todas", "Tops y Camisas", "Pantalones y Faldas", "Vestidos", "Abrigos", "Calzado"])
    st.info("Aquí se mostrarán las fichas individuales de cada una de tus prendas reales.")

with tab3:
    st.header("Asistente Virtual de Estilo")
    st.write("¿Qué quieres vestir hoy? Pídeme combinaciones o sugerencias según el clima de Montreal.")
    
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
