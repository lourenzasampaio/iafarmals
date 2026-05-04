import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Assistente de Atendimento Farmacêutico", page_icon="💊", layout="wide")

# --- BANCO DE DADOS DE SUPLEMENTOS ---
suplementos_db = [
    {"nome": "Magnésio Treonato", "info": "Único que entra no cérebro; Melhora memória e reduz ansiedade.", "tags": "ansiedade, memoria, alzheimer, cerebro", "obs": "300-400mg/dia. Não vender com óxido de magnésio."},
    {"nome": "Magnésio Malato", "info": "Produz energia, combate fadiga crônica e cansaço extremo.", "tags": "cansaco extremo, fadiga, energia", "obs": "Ideal para exaustão."},
    {"nome": "Magnésio Glicina", "info": "Relaxa músculos e sistema nervoso. Ótimo para insônia.", "tags": "insonia, tensao, sono", "obs": "Tomar antes de dormir."},
    {"nome": "Magnésio Citrato", "info": "Ajuda a soltar o intestino e melhorar a digestão.", "tags": "intestino preso, digestao, constipacao", "obs": "Atenção a pacientes renais."},
    {"nome": "Ômega 3", "info": "Anti-inflamatório, saúde vascular, foco, humor e gestação.", "tags": "anti-inflamatorio, circulacao, coracao, tpm, gravidez", "obs": "Melhora chances de ovulação."},
    {"nome": "Metilfolato", "info": "Ideal para quem quer engravidar (iniciar 4 meses antes).", "tags": "gravidez, gestacao, tentante", "obs": "Menor risco de defeitos no tubo neural."},
    {"nome": "Coenzima Q10", "info": "Antioxidante potente. Melhora qualidade dos óvulos e energia.", "tags": "antioxidante, energia, ovulos, coracao", "obs": ""},
    {"nome": "Targifor C", "info": "Vitamina C + Arginina. Bom para hematomas (roxos) e vasos.", "tags": "hematoma, vasos, cicatrizacao", "obs": ""},
    {"nome": "Creatina", "info": "Força muscular, energia celular e envelhecimento saudável.", "tags": "musculos, forca, idoso", "obs": "Manter boa hidratação."},
    {"nome": "Vitamina D (Addera)", "info": "Imunidade, saúde vascular e reprodutiva.", "tags": "imunidade, gravidez, ossos", "obs": "Baixa Vit D aumenta risco cardiovascular."},
    {"nome": "B12", "info": "Energia, sistema nervoso, foco e memória.", "tags": "energia, cerebro, foco", "obs": ""},
    {"nome": "Ferro", "info": "Combate anemia e fadiga. Essencial para engravidar.", "tags": "anemia, energia, gravidez", "obs": ""}
]

# --- FUNÇÕES DAS ABAS ---
def aba_suplementos():
    st.title("📚 Guia de Suplementação Inteligente")
    st.markdown("---")
    
    suplementos = [
        {"nome": "Magnésio Treonato", "info": "É o único que entra no cérebro; Melhora a memória, reduz a ansiedade; ajuda na prevenção do Alzheimer.", "tags": "ansiedade, memoria, alzheimer, cerebro", "obs": "Média de 300 a 400mg/dia. Não vender com óxido de magnésio. Atenção a pacientes renais."},
        {"nome": "Magnésio Malato", "info": "Produz energia nas células, combate fadiga crônica e cansaço extremo, ideal para quem está sempre exausto.", "tags": "cansaco extremo, fadiga, energia, exausto", "obs": "Média de 300 a 400mg/dia. Não vender com óxido de magnésio. Atenção a pacientes renais."},
        {"nome": "Magnésio Glicina", "info": "Relaxa os músculos e acalma o sistema nervoso, ótimo para insônia e para quem acorda tenso (toma antes de dormir).", "tags": "insonia, tensao, sono, relaxante", "obs": "Média de 300 a 400mg/dia. Não vender com óxido de magnésio. Atenção a pacientes renais."},
        {"nome": "Magnésio Citrato", "info": "Ajuda a soltar o intestino e melhorar a digestão.", "tags": "intestino preso, digestao, constipacao", "obs": "Média de 300 a 400mg/dia. Não vender com óxido de magnésio. Atenção a pacientes renais."},
        {"nome": "Ômega 3", "info": "Ação anti-inflamatória, saúde vascular, melhora a circulação e protege o coração. Ajuda no foco, humor e TPM. Aumenta chances de gestação.", "tags": "anti-inflamatorio, circulacao, cognicao, coracao, tpm, gravidez, gestacao", "obs": "Consulte a concentração de EPA/DHA no rótulo."},
        {"nome": "Coenzima Q10", "info": "Poderoso antioxidante para as células.", "tags": "antioxidante, energia, coracao", "obs": ""},
        {"nome": "Metilfolato", "info": "Ideal para quem quer engravidar (iniciar 4 meses antes de tentar).", "tags": "gravidez, gestacao, tentante", "obs": "Forma ativa do ácido fólico."},
        {"nome": "Targifor C (Vit C + Arginina)", "info": "Auxilia em hematomas (roxinhos do nada), melhora a saúde dos vasos, pele e cicatrização.", "tags": "hematoma, vasos sanguineos, cicatrizacao, pele", "obs": ""},
        {"nome": "Magnésio Quelato (Puro)", "info": "Regula a contração dos vasos, ajuda na circulação e melhora a qualidade do sono.", "tags": "circulacao, sono, vasos", "obs": "Média de 300 a 400mg/dia. Atenção a pacientes renais."},
        {"nome": "Creatina", "info": "Auxilia na força muscular, energia celular e contribui para um envelhecimento saudável.", "tags": "musculos, forca, academia, idoso", "obs": "Beber bastante água durante o uso."},
        {"nome": "Vitamina D 2.000 U.I (Addera)", "info": "Imunidade e saúde vascular. Melhora chances de engravidar e reduz riscos cardiovasculares.", "tags": "imunidade, gravidez, vascular, coracao", "obs": ""},
        {"nome": "Whey Protein", "info": "Essencial para manutenção muscular, recuperação e suporte metabólico.", "tags": "proteinas, musculos, pos-treino", "obs": ""},
        {"nome": "Vitamina B12", "info": "Aumenta energia, melhora sistema nervoso, foco, memória e humor.", "tags": "energia, sistema nervoso, cerebro, foco, memoria", "obs": ""},
        {"nome": "Ferro", "info": "Reduz fadiga e aumenta energia. Essencial para quem quer engravidar ou tem anemia.", "tags": "gravidez, anemia, energia, cansaco", "obs": "Melhor absorvido se tomado com Vitamina C."}
    ]
    
    busca = st.text_input("🔍 Digite o nome do suplemento ou o que o paciente sente (ex: 'insônia', 'gravidez'):")
    
    if busca:
        encontrados = [s for s in suplementos if busca.lower() in s['nome'].lower() or busca.lower() in s['tags'].lower()]
        
        if encontrados:
            for item in encontrados:
                with st.expander(f"✨ {item['nome']}", expanded=True):
                    st.write(f"**Indicação:** {item['info']}")
                    if item['obs']:
                        st.warning(f"**⚠️ Atenção/Dica:** {item['obs']}")
                    st.caption(f"Tags: {item['tags']}")
        else:
            st.error("Nenhum suplemento encontrado para essa busca.")
    else:
        st.info("Aguardando busca... Digite algo acima para filtrar.")

def aba_patologias():
    st.header("📋 Guia de Patologias e Indicações")
    
    categorias = [
        "Fibromialgia", "Lipedema", "Hipotireoidismo", "SOP", 
        "Gravidez", "Uso de GLP-1", "Dermatite Atópica", "Pomadas", 
        "Desparasitação", "Interações Médicas"
    ]
    
    escolha = st.selectbox("Selecione a patologia ou condição:", categorias)

    if escolha == "Fibromialgia":
        st.subheader("Suplementos para Fibromialgia")
        st.markdown("""
        * **Magnésio dimalato:** Para dor, causa relaxamento muscular e produção de energia.
        * **Ômega 3:** Modulação inflamatória, sensibilidade à dor e humor.
        * **NAC:** Precursor de glutationa, reduz estresse oxidativo e fadiga.
        * **Complexo B:** Suporte neurometabólico e cognição.
        * **Melatonina:** Regula o sono e modula a dor (insônia).
        * **Coenzima Q-10:** Energia celular e antioxidante.
        * **Cúrcuma:** Propriedades anti-inflamatórias.
        * **Vitamina D:** Redução de dor musculoesquelética.
        """)

    elif escolha == "Lipedema":
        st.subheader("Suplementos para Lipedema")
        st.markdown("""
        * **Ômega 3:** Redução da inflamação, melhora o colesterol, saúde celular.
        * **Cúrcuma:** Potente ação anti-inflamatória, antioxidante.
        * **Coenzima Q10:** Combate radicais livres, efeito anti-inflamatório.
        * **Resveratrol:** Antioxidante, melhora a circulação e auxilia na redução da dor.
        * **Vitamina D:** Fortalece a imunidade, saúde óssea.
        * **Magnésio:** Funcionamento muscular e vascular, melhora o sono.
        * **Melatonina e Calman:** Para melhorar o sono.
        """)

    elif escolha == "Hipotireoidismo":
        st.subheader("Conversão T4 -> T3")
        st.info("A conversão depende de: Selênio, Zinco, Ferro, Vitamina D e Iodo.")

    elif escolha == "SOP":
        st.subheader("Suplementos para SOP")
        st.markdown("""
        * **Inositol:** Equilibra os ciclos de insulina
        * **Vitamina D3:** Auxilia os hormônios
        * **Magnésio:** Reduz a TPM e estresse
        * **Ômega 3:** Combate cistos e inflamações
        * **Zinco:** Ajuda na acne e ovulação
        * **Hortelã:** Reduz os hormônios masculinos
        * **Berberina:** Regula o açúcar no sangue
        * **Cromo:** Auxilia o metabolismo
        * **Probióticos:** Melhora a saúde intestinal e hormonal
        * **NAC:** Aumenta a qualidade do óvulo
        """)

    elif escolha == "Gravidez":
        st.subheader("Planejamento e Gestação")
        st.write("- **Metilfolato:** Prevenção de defeitos no tubo neural.")
        st.write("- **Ferro:** Essencial para a ovulação.")
        st.write("- **Coenzima Q10:** Qualidade dos óvulos.")
        st.write("- **Vitamina D:** Ajuda na ovulação, melhora a capacidade reprodutiva.")
        st.write("- **Ômega 3:** Maiores chances de ovulação.")

    elif escolha == "Uso de GLP-1":
        st.subheader("Suporte para usuários de GLP-1 (ex: Ozempic)")
        st.write("- **Cabelos:** Ferro e Zinco.")
        st.write("- **Massa Muscular:** Creatina e Proteína.")
        st.write("- **Energia:** Glucerna (carboidrato de liberação prolongada).")
        st.write("- **B12 e Magnésio:** Para o cansaço.")
        st.write("- **Fibras:** Para quando o intestino não está funcionando.")
        st.write("- **Macrogol ou Lactulose:** Quando está com muitos dias de diferença.")
        st.write("- **Probióticos:** Restaura a flora intestinal, ajuda na diarreia.")

    elif escolha == "Dermatite Atópica":
        st.subheader("Cuidados com a Pele")
        st.write("**Higiene:** Baby Dove, Johnsons Baby.")
        st.write("**Hidratação:** Vasenol (sem fragrância), Neutrogena Loção Intensiva.")
        st.write("**Crise:** Bepantriz (corpo e rosto), Vaselina sólida.")

    elif escolha == "Pomadas":
        st.subheader("Guia Rápido de Pomadas")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Dor:** Diclofenaco")
            st.write("**Acne:** Tretinoína (Noite)")
            st.write("**Cortes:** Bacitracina + Neomicina")
            st.write("**Psoríase:** Clobetasol")
            st.write("**Herpes:** Aciclovir")
        with col2:
            st.write("**Candidíase:** Nistatina")
            st.write("**Picadas:** Hidrocortisona / Magic Balm")
            st.write("**Bacteriana:** Mupirocina (2x dia)")
            st.write("**Assadura:** Óxido de Zinco")
            st.write("**Micoses:** Clotrimazol")

    elif escolha == "Desparasitação":
        st.subheader("Protocolos de Desparasitação")
        st.write("**Nitazoxanida (Anitta):** Peso x 0,375ml (12/12h por 3 dias).")
        st.write("**Secnidazol:** Peso x 1ml (Dose única).")
        st.write("**Albendazol:** 1-2 anos (5ml/3 dias) | >3 anos (10ml/3 dias).")

    elif escolha == "Interações Médicas":
        st.subheader("Alertas Importantes")
        st.warning("**Omeprazol X Clopidogrel:** Não devem ser usados juntos.")
        st.success("**Dica:** Em pacientes polimedicados, preferir o **Pantoprazol** para evitar interações.")

# --- MENU LATERAL PRINCIPAL ---
st.sidebar.title("Navegação")
menu_principal = st.sidebar.radio("Escolha o módulo:", ["Protocolos de Atendimento", "Guia de Suplementos", "Patologias"])

if menu_principal == "Protocolos de Atendimento":
    st.title("💊 Assistente de Atendimento Farmacêutico")
    
    # Menu de Categorias
    st.sidebar.header("Menu de Navegação")
    categoria = st.sidebar.selectbox(
        "Selecione a categoria:",
        ["Selecione...", "1. Tosse", "2. Dor/Enxaqueca", "3. Alergia/Rinite", 
         "4. Digestivo", "5. Muscular", "6. Anticoncepcional", 
         "7. Corticoide", "8. Colírios", "9. Febre"]
    )
    
    # TELA INICIAL
    if categoria == "Selecione...":
        st.info("### Bem-vindo!")
        st.write("Selecione uma categoria no menu à esquerda para iniciar o protocolo de atendimento.")
        st.image("https://cdn-icons-png.flaticon.com/512/3022/3022131.png", width=100)
    
    # TOSSE
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
    
    # DOR / ENXAQUECA
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
    
    # ALERGIA / RINITE
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
    
    # DIGESTIVO
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
                st.write("👉 **ESSENCIAL:** Soro de Reidratação Oral (beber após cada evacuação).")
                if crianca == "Sim":
                    st.info("💡 **DICA:** Zinco (em gotas/xarope) ajuda na recuperação da mucosa infantil.")
        
        elif "3." in queixa:
            tempo = st.number_input("Há quantos dias sem ir ao banheiro?", min_value=0, value=1)
            idoso = st.radio("O paciente é idoso?", ["Não", "Sim"])
            if tempo > 7:
                st.error("⚠️ **ALERTA:** Risco de impactação fecal. Encaminhar para avaliação médica.")
            elif idoso == "Sim":
                st.success("👉 **INDICAR:** Lactulose (Lactulona) ou Fibras. Evitar laxantes estimulantes fortes.")
            else:
                st.success("👉 **INDICAR:** Bisacodil (Dulcolax) para efeito rápido ou Almeida Prado 46.")
            st.write("📢 **ORIENTAÇÃO:** Aumentar ingestão de água e fibras (mamão, aveia).")
    
    # MUSCULAR
    elif "5. Muscular" in categoria:
        st.header("💪 Protocolo de Avaliação Muscular")
        tipo_dor = st.selectbox("Qual o tipo da dor?", ["1. Torcicolo / Tensão", "2. Pancada / Trauma", "3. Dor Lombar / Nervo Ciático"])
        idoso = st.radio("O paciente é idoso?", ["Não", "Sim"])
        dirigir = st.radio("Vai dirigir ou operar máquinas hoje?", ["Não", "Sim"])
        estomago = st.radio("Tem histórico de gastrite ou úlcera?", ["Não", "Sim"])
        
        if "1" in tipo_dor:
            if idoso == "Sim" or dirigir == "Sim":
                st.write("👉 **INDICAR:** Dipirona 1g + Compressas quentes + Pomada (Diclofenaco).")
                st.error("⚠️ **ALERTA:** Evitar Ciclobenzaprina pelo risco de sono e quedas.")
            else:
                st.success("👉 **INDICAR:** Ciclobenzaprina (Miosan) ou Dorflex.")
                st.info("💡 **DICA:** Tomar preferencialmente à noite.")
        elif "2" in tipo_dor:
            st.write("👉 **INDICAR:** Gelo nas primeiras 48h.")
            if estomago == "Sim":
                st.write("👉 **INDICAR:** Paracetamol + Gel de Arnica ou Diclofenaco Tópico.")
            else:
                st.success("👉 **INDICAR:** Anti-inflamatório (Ibuprofeno ou Cetoprofeno).")
        elif "3" in tipo_dor:
            st.warning("⚠️ **ALERTA:** Se houver perda de força nas pernas, ir ao médico.")
            if idoso == "Sim":
                st.write("👉 **INDICAR:** Paracetamol + Vitaminas do complexo B (Etna/Citoneurin).")
            else:
                st.success("👉 **INDICAR:** Associações potentes (Tandrilax / Torsilax / Bioflex).")
    
    # ANTICONCEPCIONAL
    elif "6. Anticoncepcional" in categoria:
        st.header("💊 Protocolo de Anticoncepcionais")
        primeira_vez = st.radio("A cliente quer começar a tomar pela primeira vez?", ["Não", "Sim"])
        if primeira_vez == "Sim":
            st.error("❌ **ATENÇÃO:** Farmacêutico não deve indicar o primeiro anticoncepcional.")
            st.write("👉 **ORIENTAÇÃO:** Encaminhar ao Ginecologista para exames de risco de Trombose.")
        else:
            st.write("✅ **OK:** Verificar se ela já tem o nome do remédio ou se deseja o Genérico/Intercambiável.")
            esquecimento = st.radio("É dúvida sobre esquecimento?", ["Não", "Sim"])
            if esquecimento == "Sim":
                horas = st.number_input("Quanto tempo de atraso (em horas)?", min_value=0)
                if horas <= 12:
                    st.success("**ORIENTAÇÃO:** Tomar agora. Eficácia mantida. Continuar cartela normalmente.")
                else:
                    st.error("**ALERTA:** Eficácia reduzida! Tomar o esquecido e usar CAMISINHA por 7 dias.")
            
            interacao = st.radio("Está tomando antibiótico ou remédio para convulsão?", ["Não", "Sim"])
            if interacao == "Sim":
                st.error("**ALERTA CRÍTICO:** Esses remédios podem cortar o efeito. Usar método de barreira (camisinha).")
            
            fuma = st.radio("Paciente fuma e tem mais de 35 anos?", ["Não", "Sim"])
            if fuma == "Sim":
                st.warning("**AVISO MÉDICO:** Risco aumentado de Trombose. Sugerir consulta para avaliar métodos sem estrogênio.")
    
    # CORTICOIDE
    elif "7. Corticoide" in categoria:
        st.header("🚫 Protocolo de Ética e Segurança - Corticoides")
        possui_receita = st.radio("O paciente possui receita médica?", ["Não", "Sim"])
        if possui_receita == "Não":
            st.error("❌ **ATENÇÃO:** Corticoides não são MIPs.")
            st.write("👉 **CONDUTA:** Não indicar. Encaminhar ao médico para diagnóstico.")
        else:
            st.success("✅ **OK:** Proceder com a DISPENSAÇÃO...")
            diabetes = st.radio("O paciente é diabético?", ["Não", "Sim"])
            pressao = st.radio("Tem pressão alta?", ["Não", "Sim"])
            tempo = st.number_input("Uso por quantos dias?", min_value=1, value=1)
            if diabetes == "Sim": st.error("ALERTA: Monitorar glicemia!")
            if pressao == "Sim": st.error("ALERTA: Pode subir a pressão arterial.")
            st.info("**REGRAS DE OURO:** Tomar pela MANHÃ e com ESTÔMAGO CHEIO.")
            if tempo > 10: st.warning("- AVISO: Não parar o uso de vez. O desmame deve ser gradual.")
    
    # COLÍRIOS
    elif "8. Colírios" in categoria:
        st.header("👁️ Avaliação Ética Ocular")
        vermelho = st.radio("O olho está muito vermelho ou com dor?", ["Não", "Sim"])
        secrecao = st.radio("Tem secreção amarelada (pus)?", ["Não", "Sim"])
        if secrecao == "Sim":
            st.error("❌ **NÃO INDICAR:** Suspeita de Infecção Bacteriana. Encaminhar ao Oftalmo.")
        elif vermelho == "Sim":
            st.warning("⚠️ **CUIDADO:** Se houver dor forte ou visão turva, não indique nada. Compressas geladas e médico.")
        else:
            st.success("✅ **AUTONOMIA:** Você pode indicar Lubrificantes (Lágrimas Artificiais).")
    
    # FEBRE
    elif "9. Febre" in categoria:
        st.header("🌡️ Protocolo de Avaliação de Febre")
        idade = st.number_input("Qual a idade do paciente? (Ex: 0.5 para 6 meses)", min_value=0.0, value=20.0, step=0.1)
        temperatura = st.number_input("Qual a temperatura medida? (Ex: 38.5)", min_value=30.0, value=37.0, step=0.1)
        peso = st.number_input("Qual o peso do paciente?", min_value=1.0, value=60.0)
        
        manchas = st.radio("- Tem manchas vermelhas ou dor atrás dos olhos?", ["Não", "Sim"])
        vmito = st.radio("- Tem vômito persistente ou dor abdominal forte?", ["Não", "Sim"])
        pescoco = st.radio("- Tem rigidez na nuca?", ["Não", "Sim"])
        
        if pescoco == "Sim":
            st.error("❌ **ALERTA CRÍTICO:** Suspeita de Meningite. Ir ao Pronto Socorro AGORA!")
        elif manchas == "Sim" or vmito == "Sim":
            st.error("⚠️ **ALERTA:** Suspeita de Dengue/Zika/Chikungunya. Hidratação intensa. NÃO usar Ibuprofeno/Aspirina.")
        elif idade < 0.25:
            st.error("❌ **ALERTA:** Bebês menores de 3 meses com febre devem ir ao Pediatra imediatamente.")
        else:
            if temperatura < 37.8:
                st.info("👉 **ESTADO:** Febrícula. Banho morno e hidratação.")
            else:
                st.success(f"👉 **INDICAR:** Dipirona ou Paracetamol.")
                st.write(f"### **DOSAGEM ESTIMADA PARA DIPIRONA ({peso}kg):**")
                st.write(f"- **Dipirona GOTAS (500mg/mL):** {int(peso)} gotas.")
                st.write(f"- **Dipirona XAROPE (50mg/mL):** {peso * 0.5} mL.")

elif menu_principal == "Guia de Suplementos":
    aba_suplementos()

elif menu_principal == "Patologias":
    aba_patologias()

# RODAPÉ
st.markdown("---")
st.caption("© 2026 - Desenvolvido com dedicação por Lourenza Sampaio.")
st.sidebar.markdown("---")
st.sidebar.write("Sistema seguro para uso em balcão.")
