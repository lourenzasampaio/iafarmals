import streamlit as st

# Configuração visual da página
st.set_page_config(page_title="IA Farmacêutica - Lourenza", page_icon="💊", layout="wide")

st.title("💊 Assistente de Atendimento no Balcão")
st.write("### Olá, Lourenza! Sistema de Apoio à Decisão Farmacêutica.")
st.markdown("---")

# Menu Lateral Organizado
categoria = st.sidebar.selectbox(
    "Escolha a Categoria de Medicamento:",
    ["Início", "1. Tosse", "2. Dor/Enxaqueca", "3. Alergia/Rinite", "4. Digestivo", 
     "5. Muscular", "6. Anticoncepcional", "7. Corticoide", "8. Colírios", "9. Febre (Gotas)"]
)

# --- ABA INICIAL ---
if categoria == "Início":
    st.info("Selecione uma categoria no menu à esquerda para iniciar o protocolo de segurança.")
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022131.png", width=100)
    st.write("Este sistema ajuda a garantir que a indicação seja ética e segura, seguindo as RDCs da ANVISA.")

# --- 1. TOSSE ---
elif categoria == "1. Tosse":
    st.header("🗣️ Protocolo de Tosse")
    tipo_tosse = st.radio("Qual o tipo de tosse?", ["Seca", "Com catarro (Cheia)"])
    idade = st.number_input("Idade do paciente:", min_value=0, value=5)
    
    if tipo_tosse == "Com catarro (Cheia)":
        st.error("🚫 NÃO INDICAR Dropropizina ou Levodropropizina (Antitussígenos).")
        st.success("✅ INDICAR: Expectorantes ou Mucolíticos (Ambroxol, Acetilcisteína, Acebrofilina).")
    else:
        if idade < 2:
            st.error("⚠️ Menores de 2 anos: NÃO indicar. Encaminhar ao pediatra.")
        else:
            st.success("✅ Pode indicar Dropropizina (Vibral/Notuss).")

# --- 7. CORTICOIDE ---
elif categoria == "7. Corticoide":
    st.header("🚫 Protocolo de Corticoides (Hormônios)")
    st.warning("Lembrete: Corticoides orais NÃO são MIPs.")
    tem_receita = st.radio("O paciente possui receita médica válida?", ["Não", "Sim"])
    
    if tem_receita == "Não":
        st.error("❌ CONDUTA: NÃO INDICAR. O uso indevido pode mascarar infecções graves.")
        st.info("💡 Sugestão: Se for inflamação leve, oferecer um AINE (Ibuprofeno/Nimesulida) ou tópico.")
    else:
        st.success("✅ DISPENSAÇÃO AUTORIZADA. Orientar uso após refeições para proteger o estômago.")

# --- 8. COLÍRIOS ---
elif categoria == "8. Colírios":
    st.header("👁️ Atendimento Ocular")
    sintomas = st.multiselect("Sintomas relatados:", ["Olho Seco", "Vermelhidão leve", "Secreção/Pus", "Dor intensa"])
    
    if "Secreção/Pus" in sintomas or "Dor intensa" in sintomas:
        st.error("❌ RISCO DE INFECÇÃO/GLAUCOMA. Não indicar. Encaminhar ao Oftalmologista.")
    elif "Olho Seco" in sintomas:
        st.success("✅ INDICAÇÃO: Lubrificantes (Lágrimas Artificiais).")
    elif "Vermelhidão leve" in sintomas:
        st.warning("⚠️ Pode indicar Vasoconstritor (Nafazolina), mas orientar uso por no máximo 3 dias.")

# --- 9. FEBRE / GOTAS ---
elif categoria == "9. Febre (Gotas)":
    st.header("⚖️ Cálculo Preciso de Dosagem")
    med = st.selectbox("Medicamento:", ["Dipirona 500mg/mL", "Ibuprofeno 50mg/mL", "Ibuprofeno 100mg/mL"])
    peso = st.number_input("Peso do paciente (kg):", min_value=1.0, value=10.0)
    
    if med == "Dipirona 500mg/mL":
        gotas = round(peso * 0.6)
        limite = 40
    elif med == "Ibuprofeno 50mg/mL":
        gotas = round(peso * 2) # Regra padrão 2 gotas/kg
        limite = 40
    else: # 100mg/mL
        gotas = round(peso * 1)
        limite = 20

    if gotas > limite:
        st.warning(f"⚠️ Cálculo excedeu o teto. Indicar apenas {limite} gotas.")
    else:
        st.success(f"✅ Dose Recomendada: **{gotas} gotas**.")

# --- OUTRAS CATEGORIAS (Espaço para você completar) ---
else:
    st.header(f"🔧 Módulo {categoria}")
    st.write("Este módulo está sendo atualizado com seus protocolos originais.")
    st.info("Você pode editar o código no GitHub para adicionar os textos específicos aqui.")
