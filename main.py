import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Assistente de Atendimento Farmacêutico", page_icon="💊", layout="wide")

# Título Principal e Autoria
st.title("💊 Assistente de Atendimento Farmacêutico")
st.markdown(f"### Desenvolvido por: **Lourenza Sampaio**")
st.markdown("---")

# Menu Principal de Categorias (Lateral)
st.sidebar.header("Menu de Navegação")
categoria = st.sidebar.selectbox(
    "Selecione a categoria:",
    ["Selecione...", "1. Tosse", "2. Dor/Enxaqueca", "3. Alergia/Rinite", 
     "4. Digestivo", "5. Muscular", "6. Anticoncepcional", 
     "7. Corticoide", "8. Colírios", "9. Febre"]
)

# --- TELA INICIAL ---
if categoria == "Selecione...":
    st.info("### Bem-vindo!")
    st.write("Selecione uma categoria no menu à esquerda para iniciar o protocolo de atendimento.")
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022131.png", width=100)

# --- LÓGICA PARA TOSSE ---
elif "1. Tosse" in categoria:
    st.header("🗣️ Protocolo para Tosse")
    tipo_tosse = st.radio("A tosse é seca ou com catarro?", ["Seca", "Com catarro"])
    
    if tipo_tosse == "Seca":
        st.success("""**INDICAÇÃO:** Sugerir Hidratação e Antitussígenos: Dropropizina, Clobutinol, Levodropropizina e o Dextrometorfano.""")
        st.warning("""**OBSERVAÇÃO:** Não indicar para tosse com catarro, menores de 2 anos, Asmáticos e Pacientes com DPOC, Insuficiência Renal ou Hepática Grave e Gravidez ou amamentação (sem receita médica).""")
        st.info("""**AVISO:** Pode causar sonolência (avise quem dirige) e hipotensão (queda de pressão) em pessoas sensíveis.""")
        
    elif tipo_tosse == "Com catarro":
        st.write("### **Opções de Ativos:**")
        st.write("- **Mucolíticos:** Acetilcisteína, Ambroxol, Bromexina, Carbocisteína")
        st.write("- **Expectorantes:** Guaifenesina")
        st.write("- **Fitoterápicos:** Hedera Helix, Guaco")
        st.write("- **Com Broncodilatador:** Acebrofilina")

        diabetes = st.radio("O paciente tem diabetes?", ["Não", "Sim"])
        if diabetes == "Sim":
            st.warning("⚠️ **INDICAR:** Acetilcisteína (sachê sem açúcar) ou versões DIET de Ambroxol/Acebrofilina.")

        st.markdown("---")
        st.write("**Verificando indicação de Acebrofilina...**")
        cardiaco = st.radio("O paciente tem problemas de coração ou pressão muito alta?", ["Não", "Sim"])
        epilepsia = st.radio("O paciente tem histórico de convulsões?", ["Não", "Sim"])
        idade = st.number_input("Qual a idade do paciente?", min_value=0, value=10)

        if cardiaco == "Sim" or epilepsia == "Sim" or idade < 2:
            st.error("❌ **EVITAR ACEBROFILINA.** Risco de taquicardia ou crises.")
            st.write("✅ **PREFERIR:** Acetilcisteína ou Ambroxol (são mais seguros para o coração).")
        else:
            st.success("✅ **ACEBROFILINA LIBERADA.** (Excelente para peito chiando).")

# --- LÓGICA PARA DOR / ENXAQUECA ---
elif "2. Dor/Enxaqueca" in categoria:
    st.header("🧠 Protocolo de Avaliação de Cefaleia")
    
    unilateral = st.radio("A dor é de um lado só e latejante?", ["Não", "Sim"])
    sintomas_extras = st.radio("Tem náusea, vômito ou incômodo com a luz?", ["Não", "Sim"])
    frequencia = st.radio("Isso acontece com frequência (crônico)?", ["Não", "Sim"])
    hipertensao = st.radio("O paciente tem pressão alta ou problema no coração?", ["Não", "Sim"])
    estomago = st.radio("Tem histórico de gastrite ou úlcera?", ["Não", "Sim"])

    st.subheader("--- Resultado da Análise ---")
    if unilateral == "Sim" or sintomas_extras == "Sim":
        st.warning("**SUSPEITA:** Crise de Enxaqueca (Migrânea).")
        if hipertensao == "Sim":
            st.error("⚠️ **ALERTA:** Evitar Triptanos (Naratriptana) e Ergotamina.")
            st.write("👉 **INDICAR:** Dipirona 1g ou Paracetamol 750mg.")
            st.info("💡 **DICA:** Se houver náusea, associar Metoclopramida (Plasil).")
        else:
            st.success("👉 **INDICAR:** Naratriptana (Naramig) ou Cefaliv/Cefalium.")
            st.write("💡 **ORIENTAÇÃO:** Tomar o mais rápido possível no início da dor.")
    else:
        st.write("**SUSPEITA:** Cefaleia Tensional ou Dor Comum.")
        if estomago == "Sim":
            st.write("👉 **INDICAR:** Paracetamol (mais seguro para o estômago). Evitar Ibuprofeno/Aspirina.")
        else:
            st.write("👉 **INDICAR:** Dipirona ou associações com Cafeína (Neosaldina, Dorflex).")

    if frequencia == "Sim":
        st.error("📢 **NOTA:** Uso de analgésicos >3x na semana causa efeito rebote. Encaminhar para profilaxia.")

# --- LÓGICA PARA ALERGIA / RINITE ---
elif "3. Alergia/Rinite" in categoria:
    st.header("🤧 Protocolo de Avaliação de Alergia/Rinite")
    
    tipo_sintoma = st.selectbox("Sintomas:", ["1. Espirro/Coriza/Coceira", "2. Nariz Entupido apenas"])
    tempo = st.selectbox("Frequência:", ["1. Crise aguda (agora)", "2. Persistente (todo dia)"])
    atividade = st.radio("Vai dirigir, estudar ou operar máquinas hoje?", ["Não", "Sim"])
    idoso = st.radio("O paciente é idoso?", ["Não", "Sim"])
    hipertenso = st.radio("O paciente tem pressão alta?", ["Não", "Sim"])

    st.subheader("--- Resultado da Análise ---")
    if "1." in tipo_sintoma:
        if atividade == "Sim" or idoso == "Sim":
            st.success("👉 **INDICAR:** Antialérgicos de 2ª Geração (Não dão sono).")
            st.write("✅ **Opções:** Loratadina, Desloratadina ou Fexofenadina (Allegra).")
        else:
            st.warning("👉 **INDICAR:** Antialérgicos de 1ª Geração (Ação rápida, mas dá SONO).")
            st.write("✅ **Opções:** Dexclorfeniramina (Polaramine, é REFERÊNCIA), Histamin (é SIMILAR) ou Hidroxizina.")

    if "2." in tipo_sintoma:
        if hipertenso == "Sim":
            st.error("⚠️ **ALERTA:** Evitar descongestionantes com Naftazolina (Neosoro/Sorine).")
            st.write("👉 **INDICAR:** Apenas Soro Fisiológico 0,9% em abundância.")
        else:
            st.success("👉 **INDICAR:** Descongestionantes tópicos por no MÁXIMO 3 a 5 dias.")

    if "2" in tempo:
        st.info("💡 **DICA DE TRATAMENTO:** O paciente precisa de Corticoide Nasal (Budesonida/Mometasona).")
        st.write("📢 **NOTA:** O efeito demora de 2 a 3 dias. Higienizar com soro antes de usar.")

    if idoso == "Sim" and atividade == "Não":
        st.error("❗ **AVISO:** Mesmo que não dirija, antialérgicos que dão sono aumentam risco de QUEDAS em idosos.")

# --- LÓGICA PARA SAÚDE DIGESTIVA ---
elif "4. Digestivo" in categoria:
    st.header("🤢 Protocolo de Avaliação Digestiva")
    queixa = st.selectbox("Qual o principal sintoma?", ["1. Azia / Queimação / Má digestão", "2. Diarreia", "3. Intestino Preso (Constipação)"])

    if "1." in queixa:
        gravida = st.radio("A paciente está grávida?", ["Não", "Sim"])
        uso_frequente = st.radio("Usa remédio para azia quase todo dia?", ["Não", "Sim"])
        if gravida == "Sim":
            st.success("👉 **INDICAR:** Carbonato de Cálcio ou Magnésio (Mylanta/Pepsamar). Mais seguro.")
        else:
            st.write("👉 **ALÍVIO RÁPIDO:** Hidróxido de Alumínio ou Sais de Fruta.")
            st.write("👉 **TRATAMENTO:** Omeprazol ou Pantoprazol (Tomar em jejum).")
        if uso_frequente == "Sim":
            st.error("⚠️ **ALERTA:** Uso crônico pode esconder úlceras ou H. Pylori. Indicar médico.")

    elif "2." in queixa:
        febre = st.radio("Tem febre ou sangue/pus nas fezes?", ["Não", "Sim"])
        crianca = st.radio("É para criança pequena?", ["Não", "Sim"])
        if febre == "Sim":
            st.error("❌ **ALERTA CRÍTICO:** NÃO usar Imosec (Loperamida). Risco de infecção generalizada.")
            st.write("👉 **ORIENTAÇÃO:** Encaminhar ao Pronto Socorro imediatamente.")
        else:
            st.success("👉 **INDICAR:** Floratil (Saccharomyces boulardii) ou Enterogermina.")
            st.write("👉 **ESSENCIAL:** S")
