import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="IA Farmals - Assistente Pro", page_icon="💊", layout="wide")

# 2. Banco de Dados de Suplementos (Dicionário Expandido)
suplementos_db = [
    {"nome": "Magnésio Treonato", "info": "Único que entra no cérebro; Melhora memória e reduz ansiedade.", "tags": "ansiedade, memoria, alzheimer, cerebro, mente", "obs": "300-400mg/dia. Não usar com óxido de magnésio."},
    {"nome": "Magnésio Malato", "info": "Energia celular, combate fadiga crônica e cansaço extremo.", "tags": "cansaco extremo, fadiga, energia, exausto", "obs": "Ideal para quem está sempre exausto."},
    {"nome": "Magnésio Glicina", "info": "Relaxa músculos e sistema nervoso. Ótimo para insônia e tensão.", "tags": "insonia, tensao, sono, relaxamento", "obs": "Tomar antes de dormir."},
    {"nome": "Magnésio Citrato", "info": "Ajuda a soltar o intestino e melhorar a digestão.", "tags": "intestino preso, digestao, constipacao", "obs": "Atenção a pacientes renais."},
    {"nome": "Ômega 3", "info": "Anti-inflamatório, saúde vascular, foco e gestação.", "tags": "anti-inflamatorio, circulacao, coracao, tpm, gravidez, gestacao", "obs": "Aumenta chances de ovulação."},
    {"nome": "Metilfolato", "info": "Ideal para quem quer engravidar (iniciar 4 meses antes).", "tags": "gravidez, gestacao, tentante, feto", "obs": "Menor risco de defeitos no tubo neural."},
    {"nome": "Coenzima Q10", "info": "Antioxidante potente. Melhora qualidade dos óvulos e energia.", "tags": "antioxidante, energia, ovulos, coracao", "obs": ""},
    {"nome": "Targifor C", "info": "Vitamina C + Arginina. Bom para hematomas (roxos) e vasos.", "tags": "hematoma, vasos, pele, cicatrizacao", "obs": ""},
    {"nome": "Creatina", "info": "Força muscular, energia celular e envelhecimento saudável.", "tags": "musculos, forca, idoso", "obs": "Manter boa hidratação."},
    {"nome": "Vitamina D (Addera)", "info": "Imunidade, saúde vascular e reprodutiva.", "tags": "imunidade, gravidez, ossos, vascular", "obs": "Baixa Vit D aumenta risco cardiovascular."},
    {"nome": "B12", "info": "Energia, sistema nervoso, foco e memória.", "tags": "energia, cerebro, foco, memoria", "obs": "Ajuda no humor e sistema nervoso."},
    {"nome": "Ferro", "info": "Combate anemia e fadiga. Essencial para engravidar.", "tags": "anemia, energia, gravidez, fadiga", "obs": "Melhor absorção com Vitamina C."},
    {"nome": "Inositol", "info": "Equilibra os ciclos de insulina. Essencial na SOP.", "tags": "sop, insulina, ovario, hormonio", "obs": ""},
    {"nome": "Zinco", "info": "Ajuda na acne, imunidade e ovulação.", "tags": "acne, imunidade, ovulacao, pele", "obs": ""},
    {"nome": "Berberina", "info": "Regula o açúcar no sangue (similar à metformina natural).", "tags": "sop, acucar, diabetes, insulina", "obs": ""},
    {"nome": "NAC", "info": "Antioxidante, melhora qualidade do óvulo e fadiga muscular.", "tags": "ovulo, musculo, antioxidante, sop, fibromialgia", "obs": ""}
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
    st.info("Bem-vinda, Lourenza! Este sistema contém protocolos atualizados para suporte no balcão.")
    st.write("Selecione uma categoria no menu lateral para visualizar os protocolos.")

# --- 1. TOSSE ---
elif "1. Tosse" in categoria:
    st.header("🗣️ Protocolo para Tosse")
    tipo = st.radio("Tipo de Tosse:", ["Seca", "Com catarro", "Alérgica"])
    
    if tipo == "Seca":
        st.success("✅ **INDICAÇÃO:** Dropropizina, Clobutinol, Levodropropizina.")
    elif tipo == "Com catarro":
        st.write("**Ativos:** Acetilcisteína, Ambroxol, Hedera Helix.")
    elif tipo == "Alérgica":
        st.warning("✅ **INDICAR:** Celerg, Celergin ou KOID D (Dexclorfeniramina + Betametasona).")

# --- 9. FEBRE E CÁLCULOS ---
elif "9. Febre" in categoria:
    st.header("🌡️ Protocolo de Febre e Cálculos de Gotas")
    peso = st.number_input("Peso do paciente (kg):", min_value=1.0, value=20.0, step=0.5)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Ibuprofeno")
        i50_max = min(int(peso * 2), 40)
        st.info(f"**50mg/ml:** {int(peso)} a {i50_max} gotas (Máx 40)")
        i100 = min(max(1, int(peso / 2)), 20)
        st.info(f"**100mg/ml:** {i100} gotas (Máx 20)")
    with c2:
        st.subheader("Paracetamol")
        st.success(f"**200mg/ml:** {int(peso)} a {int(peso * 1.5)} gotas")
    with c3:
        st.subheader("Dipirona")
        st.write(f"**Gotas:** {int(peso)} gts | **Xarope:** {peso * 0.5} ml")

# --- BUSCA DE SUPLEMENTOS ---
elif "🔍 Busca" in categoria:
    st.header("🔍 Busca de Suplementos")
    busca = st.text_input("Objetivo (ex: memória, gravidez, SOP, energia):")
    if busca:
        resultados = [s for s in suplementos_db if busca.lower() in s['tags'].lower() or busca.lower() in s['nome'].lower()]
        for item in resultados:
            with st.expander(f"✨ {item['nome']}"):
                st.write(f"**Indicação:** {item['info']}")
                if item['obs']: st.warning(item['obs'])

# --- GUIA DE PATOLOGIAS (AQUI ESTÃO OS DADOS QUE FALTAVAM) ---
elif "📋 Guia" in categoria:
    st.header("📋 Guia Completo de Condições")
    pat = st.selectbox("Selecione a Condição:", 
                       ["Fibromialgia", "Lipedema", "Hipotireoidismo", "SOP", 
                        "Gravidez", "Uso de GLP-1", "Dermatite Atópica", "Pomadas", 
                        "Desparasitação", "Corrimentos", "Resfriado/Imunidade"])

    if pat == "Fibromialgia":
        st.markdown("""
        - **Magnésio Dimalato:** Dor e relaxamento muscular.
        - **Ômega 3:** Modulação inflamatória e humor.
        - **NAC:** Reduz estresse oxidativo e fadiga.
        - **Coenzima Q10:** Produção de energia e dor.
        - **Melatonina:** Sono reparador e modulador da dor.
        - **Cúrcuma e Vitamina D:** Anti-inflamatório e correção de deficiência.
        """)

    elif pat == "Lipedema":
        st.markdown("""
        - **Ômega 3:** Redução da inflamação.
        - **Cúrcuma:** Potente anti-inflamatório.
        - **Resveratrol:** Melhora circulação e dor.
        - **Coenzima Q10:** Combate radicais livres.
        - **Magnésio e Melatonina:** Suporte nervoso e sono.
        """)

    elif pat == "Hipotireoidismo":
        st.info("🚀 **Conversão T4 -> T3:** Depende de Selênio, Zinco, Ferro, Vitamina D e Iodo.")

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

    elif pat == "Dermatite Atópica":
        st.subheader("Cuidados com a Pele")
        st.write("**Higiene:** Sabonete Baby Dove, Shampoo Johnsons Baby.")
        st.write("**Hidratação:** Vasenol (sem fragrância), Neutrogena Loção Intensiva.")
        st.write("**Crise:** Bepantriz (corpo/rosto), Vaselina Sólida.")

    elif pat == "Pomadas":
        st.markdown("""
        - **Diclofenaco Sódico:** Início lento (2-3h), efeito longo.
        - **Diclofenaco Potássico:** Início rápido (20-30min), efeito curto.
        - **Tretinoína:** Acne e manchas (Uso noturno).
        - **Clobetasol:** Psoríase/Dermatite severa.
        - **Mupirocina:** Infecção bacteriana (2x ao dia).
        - **Aciclovir:** Herpes simples.
        - **Óxido de Zinco:** Assaduras (2-4x ao dia).
        """)

    elif pat == "Desparasitação":
        st.write("**Nitazoxanida (Anitta):** Peso x 0,375ml (12/12h por 3 dias).")
        st.write("**Secnidazol:** Peso x 1ml (Dose única).")
        st.write("**Albendazol:** 1-2 anos (5ml/dia - 3 dias) | >3 anos (10ml/dia - 3 dias).")

    elif pat == "Corrimentos":
        st.markdown("""
        - **Fluconazol:** Candidíase (coceira intensa, branco, ardência).
        - **Secnidazol:** Bactérias/Protozoários (odor forte, amarelado).
        - **Pomadas:** Clotrimazol ou Miconazol.
        """)

    elif pat == "Resfriado/Imunidade":
        st.markdown("""
        - **Kaloba:** 1-5 anos (10 gts), 6-12 anos (20 gts), >12 anos (30 gts).
        - **Imunoflan:** Fitoterápico para imunidade.
        - **Gripe todo mês:** Suplementar Zinco + Vitamina D.
        - **Tosse com catarro:** Própolis aquoso + Mel (acima de 1 ano).
        """)

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("© 2026 - Desenvolvido por Lourenza Sampaio")
