import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Assistente de Atendimento Farmacêutico", page_icon="💊", layout="wide")

# ==========================================
# 2. FUNÇÕES DE APOIO (LÓGICA DAS ABAS)
# ==========================================

def aba_atendimento_balcao():
    st.header("🏪 Protocolos de Atendimento ao Paciente")
    
    categoria = st.selectbox(
        "Selecione a queixa do paciente:",
        ["Selecione...", "1. Tosse", "2. Dor/Enxaqueca", "3. Alergia/Rinite", 
         "4. Digestivo", "5. Muscular", "6. Anticoncepcional", 
         "7. Corticoide", "8. Colírios", "9. Febre"]
    )

    if categoria == "Selecione...":
        st.info("Selecione uma categoria acima para visualizar o protocolo clínico.")

    # --- LÓGICA PARA TOSSE ---
    elif "1. Tosse" in categoria:
        st.subheader("🗣️ Protocolo para Tosse")
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
        st.subheader("🧠 Protocolo de Avaliação de Cefaleia")
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
        st.subheader("🤧 Protocolo de Avaliação de Alergia/Rinite")
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
                st.write("✅ **Opções:** Dexclorfeniramina (Polaramine), Histamin ou Hidroxizina.")

        if "2." in tipo_sintoma:
            if hipertenso == "Sim":
                st.error("⚠️ **ALERTA:** Evitar descongestionantes com Naftazolina (Neosoro/Sorine).")
                st.write("👉 **INDICAR:** Apenas Soro Fisiológico 0,9% em abundância.")
            else:
                st.success("👉 **INDICAR:** Descongestionantes tópicos por no MÁXIMO 3 a 5 dias.")

        if "2" in tempo:
            st.info("💡 **DICA DE TRATAMENTO:** O paciente precisa de Corticoide Nasal (Budesonida/Mometasona).")
            st.write("📢 **NOTA:** O efeito demora de 2 a 3 dias. Higienizar com soro antes de usar.")

    # --- LÓGICA PARA SAÚDE DIGESTIVA ---
    elif "4. Digestivo" in categoria:
        st.subheader("🤢 Protocolo de Avaliação Digestiva")
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
                st.write("👉 **ESSENCIAL:** Soro de Reidratação Oral (beber após cada evacuação).")
                if crianca == "Sim":
                    st.info("💡 **DICA:** Zinco (em gotas/xarope) ajuda na recuperação da mucosa infantil.")

        elif "3." in queixa:
            tempo = st.number_input("Há quantos dias sem ir ao banheiro?", min_value=0, value=1)
            if tempo > 7:
                st.error("⚠️ **ALERTA:** Risco de impactação fecal. Encaminhar para avaliação médica.")
            else:
                st.success("👉 **INDICAR:** Lactulose (Lactulona) ou Fibras. Bisacodil para efeito rápido.")

    # --- LÓGICA PARA SAÚDE MUSCULAR ---
    elif "5. Muscular" in categoria:
        st.subheader("💪 Protocolo de Avaliação Muscular")
        tipo_dor = st.selectbox("Qual o tipo da dor?", ["1. Torcicolo / Tensão", "2. Pancada / Trauma", "3. Dor Lombar / Nervo Ciático"])
        
        if "1" in tipo_dor:
            st.success("👉 **INDICAR:** Ciclobenzaprina (Miosan) ou Dorflex.")
        elif "2" in tipo_dor:
            st.success("👉 **INDICAR:** Anti-inflamatório (Ibuprofeno ou Cetoprofeno) e Gelo.")
        elif "3" in tipo_dor:
            st.write("👉 **INDICAR:** Paracetamol + Vitaminas do complexo B (Etna/Citoneurin).")

    # ---outras lógicas omitidas para brevidade, mas o peso segue o mesmo padrão---
    elif "9. Febre" in categoria:
        st.subheader("🌡️ Protocolo de Avaliação de Febre")
        peso = st.number_input("Qual o peso do paciente?", min_value=1.0, value=60.0)
        st.write(f"### **DOSAGEM ESTIMADA PARA DIPIRONA ({peso}kg):**")
        st.write(f"- **Dipirona GOTAS (500mg/mL):** {int(peso)} gotas.")
        st.write(f"- **Dipirona XAROPE (50mg/mL):** {peso * 0.5} mL.")

def aba_suplementos_individuais():
    st.header("📚 Guia de Suplementação Inteligente")
    st.markdown("---")
    suplementos = [
        {"nome": "Magnésio Treonato", "info": "Melhora a memória e ansiedade.", "tags": "sono, memoria", "obs": ""},
        {"nome": "Ômega 3", "info": "Ação anti-inflamatória.", "tags": "coracao, inflamacao", "obs": "Verificar EPA/DHA."}
    ]
    busca = st.text_input("🔍 Digite o nome ou sintoma:")
    if busca:
        encontrados = [s for s in suplementos if busca.lower() in s['nome'].lower() or busca.lower() in s['tags'].lower()]
        for item in encontrados:
            with st.expander(f"✨ {item['nome']}", expanded=True):
                st.write(item['info'])

def aba_patologias():
    st.header("📋 Guia de Patologias e Indicações")
    categorias = ["Fibromialgia", "Lipedema", "Hipotireoidismo", "SOP", "Gravidez", "Uso de GLP-1", "Pomadas", "Dermatite Atópica"]
    escolha = st.selectbox("Selecione a condição:", categorias)

    if escolha == "Fibromialgia":
        st.markdown("""
        * **Magnésio dimalato:** Relaxamento muscular.
        * **Ômega 3:** Modulação inflamatória.
        """)    
    elif escolha == "Lipedema":
        st.subheader("Suplementos para Lipedema")
        st.markdown("""
        * **Ômega 3:** Redução da inflamação e saúde vascular.
        * **Cúrcuma:** Controle do lipedema e antioxidante.
        * **Resveratrol:** Melhora circulação e reduz dor.
        * **Vitamina D:** Imunidade e regulação do cálcio.
        * **Melatonina:** Suporte para o sono.
        """)
    elif escolha == "Hipotireoidismo":
        st.subheader("Conversão T4 -> T3")
        st.info("A conversão depende de: Selênio, Zinco, Ferro, Vitamina D e Iodo.")

    elif pat == "SOP":
        st.markdown("""
        - **Inositol:** Ciclos de insulina.
        - **Zinco:** Acne e ovulação.
        - **Hortelã:** Reduz hormônios masculinos.
        - **Berberina:** Regula açúcar no sangue.
        - **NAC:** Qualidade do óvulo.
        """)

    elif pat == "Gravidez":
        st.markdown("""
        - **Metilfolato:** Prevenção de defeitos neurais (iniciar 4 meses antes).
        - **Ferro:** Essencial para ovulação.
        - **Coenzima Q10:** Qualidade dos óvulos.
        - **Vitamina D e Ômega 3:** Melhora capacidade reprodutiva.
        """) 

    elif pat == "Uso de GLP-1":
        st.subheader("Suporte Ozempic/Wegovy/Mounjaro")
        st.markdown("""
        - **Cabelos:** Ferro e Zinco.
        - **Massa Muscular:** Creatina e Proteína (Whey).
        - **Energia e Saciedade:** Glucerna (carboidrato lento).
        """)
        
        
    elif escolha == "Pomadas":
        st.subheader("Guia Rápido de Pomadas")
        st.write("- **Dor:** Diclofenaco")
        st.write("- **Acne:** Tretinoína (Noite)")
        st.write("- **Cortes:** Bacitracina + Neomicina")
        st.write("- **Psoríase:** Clobetasol")
        st.write("- **Herpes:** Aciclovir")
        st.write("- **Candidíase:** Nistatina")
        st.write("- **Picadas:** Hidrocortisona / Magic Balm")
        st.write("- **Bacteriana:** Mupirocina (2x dia)")
        st.write("- **Assadura:** Óxido de Zinco")
        st.write("- **Micoses:** Clotrimazol")
        

    elif escolha == "Dermatite Atópica": # Corrigido: Ajustei a identação (espaços à esquerda)
        st.subheader("Cuidados com a Pele")
        st.write("**Higiene:** Baby Dove, Johnsons Baby.")
        st.write("**Hidratação:** Vasenol (sem fragrância).")

# ==========================================
# 3. INTERFACE PRINCIPAL
# ==========================================
st.sidebar.title("🩺 Menu Principal")
aba = st.sidebar.radio("Navegação:", ["Página Inicial", "Atendimento de Balcão", "Suplementos Individuais", "Guia de Patologias"])

if aba == "Página Inicial":
    st.info("### Bem-vinda!")
    st.write("Sistema seguro para apoio em balcão.")

elif aba == "Atendimento de Balcão":
    aba_atendimento_balcao()

elif aba == "Suplementos Individuais":
    aba_suplementos_individuais()

elif aba == "Guia de Patologias":
    aba_patologias()

st.markdown("---")
st.caption("© 2026 - Desenvolvido por Lourenza Sampaio.")
