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

    # --- LÓGICA PARA ANTICONCEPCIONAL ---
    elif "6. Anticoncepcional" in categoria:
        st.subheader("💊 Protocolo de Anticoncepcionais")
        primeira_vez = st.radio("A cliente quer começar a tomar pela primeira vez?", ["Não", "Sim"])
        if primeira_vez == "Sim":
            st.error("❌ **ATENÇÃO:** Farmacêutico não deve indicar o primeiro anticoncepcional. Encaminhar ao Ginecologista.")
        else:
            esquecimento = st.radio("É dúvida sobre esquecimento?", ["Não", "Sim"])
            if esquecimento == "Sim":
                horas = st.number_input("Quanto tempo de atraso (em horas)?", min_value=0)
                if horas <= 12:
                    st.success("**ORIENTAÇÃO:** Tomar agora. Eficácia mantida.")
                else:
                    st.error("**ALERTA:** Eficácia reduzida! Usar CAMISINHA por 7 dias.")

    # --- LÓGICA PARA CORTICOIDE ---
    elif "7. Corticoide" in categoria:
        st.subheader("🚫 Protocolo de Ética e Segurança - Corticoides")
        possui_receita = st.radio("O paciente possui receita médica?", ["Não", "Sim"])
        if possui_receita == "Não":
            st.error("❌ **ATENÇÃO:** Corticoides não são MIPs. Não indicar.")
        else:
            st.success("✅ **OK:** Tomar pela MANHÃ e com ESTÔMAGO CHEIO.")

    # --- LÓGICA PARA COLÍRIOS ---
    elif "8. Colírios" in categoria:
        st.subheader("👁️ Avaliação Ética Ocular")
        vermelho = st.radio("O olho está muito vermelho ou com dor?", ["Não", "Sim"])
        secrecao = st.radio("Tem secreção amarelada (pus)?", ["Não", "Sim"])
        if secrecao == "Sim":
            st.error("❌ **NÃO INDICAR:** Suspeita de Infecção Bacteriana. Encaminhar ao Oftalmo.")
        else:
            st.success("✅ **AUTONOMIA:** Você pode indicar Lubrificantes (Lágrimas Artificiais).")

    # --- LÓGICA PARA FEBRE ---
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
        {"nome": "Magnésio Treonato", "info": "Único que entra no cérebro; Melhora a memória, reduz a ansiedade; ajuda na prevenção do Alzheimer.", "tags": "ansiedade, memoria, alzheimer, cerebro", "obs": "Média de 300 a 400mg/dia. Atenção a pacientes renais."},
        {"nome": "Magnésio Malato", "info": "Produz energia nas células, combate fadiga crônica e cansaço extremo.", "tags": "cansaco extremo, fadiga, energia, exausto", "obs": "Ideal para exaustão. Atenção a pacientes renais."},
        {"nome": "Magnésio Glicina", "info": "Relaxa os músculos e acalma o sistema nervoso, ótimo para insônia.", "tags": "insonia, tensao, sono, relaxante", "obs": "Toma antes de dormir. Atenção a pacientes renais."},
        {"nome": "Magnésio Citrato", "info": "Ajuda a soltar o intestino e melhorar a digestão.", "tags": "intestino preso, digestao, constipacao", "obs": "Atenção a pacientes renais."},
        {"nome": "Ômega 3", "info": "Ação anti-inflamatória, saúde vascular, foco e humor.", "tags": "anti-inflamatorio, circulacao, coracao, tpm, gravidez", "obs": "Verificar EPA/DHA."},
        {"nome": "Metilfolato", "info": "Forma ativa do ácido fólico. Ideal para quem quer engravidar.", "tags": "gravidez, gestacao, tentante", "obs": "Iniciar 4 meses antes."},
        {"nome": "Creatina", "info": "Força muscular, energia celular e envelhecimento saudável.", "tags": "musculos, forca, academia, idoso", "obs": "Beber bastante água."},
        {"nome": "Vitamina B12", "info": "Energia, sistema nervoso, foco e memória.", "tags": "energia, cerebro, foco, memoria", "obs": ""},
        {"nome": "Ferro", "info": "Reduz fadiga e anemia.", "tags": "gravidez, anemia, energia, cansaco", "obs": "Melhor com Vitamina C."}
    ]

    busca = st.text_input("🔍 Digite o nome ou sintoma (ex: 'sono', 'memória'):")

    if busca:
        encontrados = [s for s in suplementos if busca.lower() in s['nome'].lower() or busca.lower() in s['tags'].lower()]
        if encontrados:
            for item in encontrados:
                with st.expander(f"✨ {item['nome']}", expanded=True):
                    st.write(f"**Indicação:** {item['info']}")
                    if item['obs']: st.warning(f"**⚠️ Atenção:** {item['obs']}")
        else:
            st.error("Nenhum suplemento encontrado.")
    else:
        st.info("Aguardando busca...")

def aba_patologias():
    st.header("📋 Guia de Patologias e Indicações")
    
    categorias = [
        "Fibromialgia", "Lipedema", "Hipotireoidismo", "SOP", 
        "Gravidez", "Uso de GLP-1", "Dermatite Atópica", "Pomadas", 
        "Saúde Intestinal", "Desparasitação", "Corrimentos", 
        "Tosse e Resfriado", "Interações Médicas"
    ]
    
    escolha = st.selectbox("Selecione a condição:", categorias)

    if escolha == "Fibromialgia":
        st.markdown("""
        * **Magnésio dimalato:** Relaxamento muscular e energia.
        * **Ômega 3:** Modulação inflamatória e dor.
        * **NAC:** Reduz estresse oxidativo.
        * **Melatonina:** Regula o sono e modula a dor.
        """)

elif escolha == "Lipedema":
        st.subheader("Suplementos para Lipedema")
        st.write("- **Ômega 3:** Redução da inflamação e saúde vascular.")
        st.write("- **Cúrcuma:** Controle do lipedema e antioxidante.")
        st.write("- **Resveratrol:** Melhora circulação e reduz dor.")
        st.write("- **Vitamina D:** Imunidade e regulação do cálcio.")
        st.write("- **Melatonina e Calman:** Melhora do sono.")
    
    elif escolha == "SOP":
        st.markdown("""
        * **Inositol:** Sensibilidade à insulina.
        * **Zinco:** Acne e ovulação.
        * **Berberina:** Regula o açúcar no sangue.)
        
    elif escolha == "Gravidez":
        st.subheader("Planejamento e Gestação")
        st.write("- **Metilfolato:** Prevenção de defeitos no tubo neural.")
        st.write("- **Ferro:** Essencial para a ovulação.")
        st.write("- **Coenzima Q10:** Qualidade dos óvulos.")
            
    elif escolha == "Hipotireoidismo":
        st.info("A conversão T4 -> T3 depende de: Selênio, Zinco, Ferro, Vitamina D e Iodo.")

    elif escolha == "Uso de GLP-1":
        st.write("- **Cabelos:** Ferro e Zinco.")
        st.write("- **Massa Muscular:** Creatina e Proteína.")
        st.write("- **Energia:** Glucerna.")

    elif escolha == "Pomadas":
        st.markdown("""
        st.write("**Dor:** Diclofenaco")
            st.write("**Acne:** Tretinoína (Noite)")
            st.write("**Cortes:** Bacitracina + Neomicina")
            st.write("**Psoríase:** Clobetasol")
            st.write("**Herpes:** Aciclovir")
            st.write("**Candidíase:** Nistatina")
            st.write("**Picadas:** Hidrocortisona / Magic Balm")
            st.write("**Bacteriana:** Mupirocina (2x dia)")
            st.write("**Assadura:** Óxido de Zinco")
            st.write("**Micoses:** Clotrimazol")        
        """)
        elif escolha == "Dermatite Atópica":
        st.subheader("Cuidados com a Pele")
        st.write("**Higiene:** Baby Dove, Johnsons Baby.")
        st.write("**Hidratação:** Vasenol (sem fragrância), Neutrogena Loção Intensiva.")
        st.write("**Crise:** Bepantriz (corpo e rosto), Vaselina sólida.")

    elif escolha == "Desparasitação":
        st.write("**Anitta:** Peso x 0,375ml (12/12h por 3 dias).")
        st.write("**Albendazol:** 400mg dose única (repetir em 15 dias para alguns casos).")
    elif escolha == "Interações Médicas":
        st.warning("**Omeprazol X Clopidogrel:** Não usar juntos. Preferir Pantoprazol.")

# ==========================================
# 3. INTERFACE PRINCIPAL (SIDEBAR E NAVEGAÇÃO)
# ==========================================

st.sidebar.title("🩺 Menu Principal")
st.sidebar.markdown("---")
aba = st.sidebar.radio("Navegação:", ["Página Inicial", "Atendimento de Balcão", "Suplementos Individuais", "Guia de Patologias"])

if aba == "Página Inicial":
    st.info("### Bem-vinda!")
    st.write("Este é o seu sistema seguro para apoio em balcão. Navegue pelas opções ao lado para protocolos e suplementação.")
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022131.png", width=100)

elif aba == "Atendimento de Balcão":
    aba_atendimento_balcao()

elif aba == "Suplementos Individuais":
    aba_suplementos_individuais()

elif aba == "Guia de Patologias":
    aba_patologias()

# RODAPÉ
st.markdown("---")
st.caption("© 2026 - Desenvolvido com dedicação por Lourenza Sampaio. Sistema seguro para uso em balcão.")
