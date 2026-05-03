import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="IA Farmals - Assistente Pro", page_icon="💊", layout="wide")

# 2. Banco de Dados de Suplementos (Dicionário para busca)
suplementos_db = [
    {"nome": "Magnésio Treonato", "info": "Único que entra no cérebro; Melhora memória e reduz ansiedade.", "tags": "ansiedade, memoria, alzheimer, cerebro", "obs": "300-400mg/dia. Não usar com óxido de magnésio."},
    {"nome": "Magnésio Malato", "info": "Energia celular, combate fadiga crônica e cansaço extremo.", "tags": "cansaco extremo, fadiga, energia, exausto", "obs": "Ideal para quem está sempre exausto."},
    {"nome": "Magnésio Glicina", "info": "Relaxa músculos e sistema nervoso. Ótimo para insônia e tensão.", "tags": "insonia, tensao, sono, relaxamento", "obs": "Tomar antes de dormir."},
    {"nome": "Magnésio Citrato", "info": "Ajuda a soltar o intestino e melhorar a digestão.", "tags": "intestino preso, digestao, constipacao", "obs": "Atenção a pacientes renais."},
    {"nome": "Ômega 3", "info": "Anti-inflamatório, saúde vascular e gestação. Ajuda no foco e TPM.", "tags": "anti-inflamatorio, circulacao, coracao, tpm, gravidez, gestacao", "obs": "Aumenta chances de ovulação."},
    {"nome": "Metilfolato", "info": "Ideal para quem quer engravidar (iniciar 4 meses antes).", "tags": "gravidez, gestacao, tentante", "obs": "Menor risco de defeitos no tubo neural."},
    {"nome": "Coenzima Q10", "info": "Antioxidante potente. Melhora qualidade dos óvulos e energia.", "tags": "antioxidante, energia, ovulos, coracao", "obs": ""},
    {"nome": "Targifor C", "info": "Vitamina C + Arginina. Bom para hematomas (roxos) e saúde dos vasos.", "tags": "hematoma, vasos, pele, cicatrizacao", "obs": ""},
    {"nome": "Creatina", "info": "Força muscular, energia celular e envelhecimento saudável.", "tags": "musculos, forca, idoso", "obs": "Manter boa hidratação."},
    {"nome": "Vitamina D (Addera)", "info": "Imunidade, saúde vascular e reprodutiva (ovulação).", "tags": "imunidade, gravidez, ossos, vascular", "obs": "Melhora chances de engravidar."},
    {"nome": "B12", "info": "Energia, sistema nervoso, foco e memória.", "tags": "energia, cerebro, foco, memoria", "obs": ""},
    {"nome": "Ferro", "info": "Combate anemia e fadiga. Essencial para engravidar.", "tags": "anemia, energia, gravidez, fadiga", "obs": "Melhor absorção com Vitamina C."}
]

# 3. Menu Lateral
st.sidebar.title("🩺 IA Farmals")
st.sidebar.markdown("---")
categoria = st.sidebar.selectbox(
    "Selecione o Atendimento:",
    ["Início", "1. Tosse", "2. Dor/Enxaqueca", "3. Alergia/Rinite", 
     "4. Digestivo", "5. Muscular", "6. Anticoncepcional", 
     "7. Corticoide", "8. Colírios", "9. Febre e Cálculos", 
     "🔍 Busca de Suplementos", "📋 Guia de Patologias"]
)

# --- 0. TELA INICIAL ---
if categoria == "Início":
    st.title("💊 Assistente de Atendimento Farmacêutico")
    st.info("Bem-vinda, Lourenza! Selecione uma categoria no menu lateral para iniciar o protocolo.")
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022131.png", width=100)

# --- 1. TOSSE ---
elif "1. Tosse" in categoria:
    st.header("🗣️ Protocolo para Tosse")
    tipo = st.radio("A tosse é:", ["Seca", "Com catarro"])
    if tipo == "Seca":
        st.success("✅ **INDICAÇÃO:** Dropropizina, Clobutinol, Levodropropizina.")
        st.warning("Não indicar para asmáticos ou menores de 2 anos.")
    else:
        st.write("**Ativos:** Acetilcisteína, Ambroxol, Hedera Helix, Guaco.")
        diabetes = st.radio("Paciente tem diabetes?", ["Não", "Sim"])
        if diabetes == "Sim":
            st.warning("⚠️ Usar versões DIET ou sachês sem açúcar.")

# --- 2. DOR / ENXAQUECA ---
elif "2. Dor/Enxaqueca" in categoria:
    st.header("🧠 Protocolo de Cefaleia")
    unilateral = st.radio("Dor unilateral e latejante?", ["Não", "Sim"])
    hipertensao = st.radio("Paciente tem pressão alta?", ["Não", "Sim"])
    if unilateral == "Sim":
        if hipertensao == "Sim":
            st.error("❌ Evitar Naratriptana. Indicar Dipirona 1g.")
        else:
            st.success("✅ Indicar Naratriptana (Naramig) ou Cefaliv.")

# --- 4. DIGESTIVO ---
elif "4. Digestivo" in categoria:
    st.header("🤢 Saúde Digestiva")
    queixa = st.selectbox("Sintoma:", ["Azia/Queimação", "Diarreia", "Constipação"])
    if "Diarreia" in queixa:
        st.write("**Indicar:** Floratil ou Enterogermina.")
        st.info("Probióticos restauram a flora intestinal.")
    elif "Azia" in queixa:
        st.write("**Opções:** Omeprazol (jejum) ou Mylanta Plus.")

# --- 9. FEBRE E CÁLCULOS (COM SEUS NOVOS DADOS) ---
elif "9. Febre" in categoria:
    st.header("🌡️ Protocolo de Febre e Cálculos de Gotas")
    peso = st.number_input("Peso do paciente (kg):", min_value=1.0, value=20.0, step=0.5)
    
    st.subheader("📏 Cálculos Automáticos")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**IBUPROFENO**")
        # Ibu 50mg: 1 a 2 gotas por kg (Dose Máxima: 40 gotas)
        i50_min = min(int(peso * 1), 40)
        i50_max = min(int(peso * 2), 40)
        st.info(f"50mg/ml: **{i50_min} a {i50_max} gotas**")
        # Ibu 100mg: 1 gota a cada 2 kg (Dose Máxima: 20 gotas)
        i100 = min(max(1, int(peso / 2)), 20)
        st.info(f"100mg/ml: **{i100} gotas**")

    with c2:
        st.markdown("**PARACETAMOL**")
        # 10 a 15mg/kg (Considerando 200mg/ml onde 1 gota = 10mg)
        p_min = int(peso)
        p_max = int(peso * 1.5)
        st.success(f"200mg/ml: **{p_min} a {p_max} gotas**")
        st.caption("Dose máxima: 150mg/kg/dia")

    with c3:
        st.markdown("**DIPIRONA**")
        st.write(f"Gotas: **{int(peso)} gotas**")
        st.write(f"Xarope: **{peso * 0.5} ml**")

# --- BUSCA DE SUPLEMENTOS ---
elif "🔍 Busca" in categoria:
    st.header("🔍 Busca Inteligente de Suplementos")
    busca = st.text_input("Para que você quer o suplemento? (Ex: menopausa, memória, energia)")
    if busca:
        resultados = [s for s in suplementos_db if busca.lower() in s['tags'].lower() or busca.lower() in s['nome'].lower()]
        if resultados:
            for item in resultados:
                with st.expander(f"✨ {item['nome']}", expanded=True):
                    st.write(f"**Indicação:** {item['info']}")
                    if item['obs']: st.warning(f"⚠️ {item['obs']}")
        else:
            st.error("Nenhum suplemento encontrado para essa finalidade.")

# --- GUIA DE PATOLOGIAS (MAIS DE 100 LINHAS DE DADOS AQUI) ---
elif "📋 Guia" in categoria:
    st.header("📋 Guia de Patologias e Condições")
    pat = st.selectbox("Selecione a Condição:", 
                       ["Fibromialgia", "Lipedema", "Hipotireoidismo", "SOP", 
                        "Gravidez", "Uso de GLP-1", "Dermatite/Pele", "Pomadas", 
                        "Desparasitação", "Corrimentos", "Tosse Alérgica/Resfriado", "Interações"])

    if pat == "Fibromialgia":
        st.write("✅ **Suplementos:** Magnésio Dimalato, Ômega 3, NAC, Complexo B, Melatonina, Coenzima Q10, Cúrcuma, Vitamina D.")
    
    elif pat == "Lipedema":
        st.write("✅ **Suplementos:** Ômega 3, Cúrcuma, Coenzima Q10, Resveratrol, Vitamina D, Magnésio, Melatonina.")

    elif pat == "SOP":
        st.markdown("""
        - **Inositol:** Equilibra insulina.
        - **Zinco:** Ajuda na acne e ovulação.
        - **Berberina:** Regula açúcar no sangue.
        - **Hortelã:** Reduz hormônios masculinos.
        - **NAC:** Qualidade do óvulo.
        """)

    elif pat == "Pomadas":
        st.subheader("Guia de Balcão - Pomadas")
        st.markdown("""
        * **Acne:** Tretinoína (Uso noturno)
        * **Candidíase:** Nistatina ou Clotrimazol
        * **Infeções:** Mupirocina (2x ao dia)
        * **Cortes:** Bacitracina + Neomicina
        * **Herpes:** Aciclovir
        * **Diclofenaco Sódico:** Início lento, efeito duradouro.
        * **Diclofenaco Potássico:** Início rápido, efeito curto.
        """)

    elif pat == "Desparasitação":
        st.write("**Nitazoxanida (Anitta):** Peso x 0,375 (12/12h por 3 dias).")
        st.write("**Albendazol:** 1-2 anos (5ml/3 dias) | >3 anos (10ml/3 dias).")

    elif pat == "Interações":
        st.error("🚫 **Omeprazol X Clopidogrel:** NÃO PODEM SER USADOS JUNTOS.")
        st.success("✅ **Preferir:** Pantoprazol para evitar interações.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("© 2026 - Lourenza Sampaio")
