def assistente_farmacia_pro():
    print("--- Assistente de Atendimento Farmacêutico (Lourenza) ---")
    print("Selecione a categoria:")
    print("1. Tosse\n2. Dor/Enxaqueca\n3. Alergia/Rinite\n4. Digestivo\n5. Muscular\n6. Anticoncepcional\n7. Corticoide\n8. Colírios\n9. Febre")

    categoria = input("Opção (digite o número): ")

    # --- LÓGICA PARA TOSSE ---
    if categoria == "1":
        tipo_tosse = input("A tosse é seca ou com catarro? (S/C) ").upper()
        if tipo_tosse == "S":
            print("""INDICAÇÃO: Sugerir Hidratação e Antitussígenos : Dropropizina, Clobutinol, Levodropropizina e o Dextrometorfano.
            OBSERVAÇÃO: Não indicar para tosse com catarro, menores de 2 anos, Asmáticos e Pacientes com DPOC, Insuficiência Renal ou Hepática Grave e Gravidez o amamentaçãO (sem receita médica)
            AVISO: Pode causar sonolência (avise quem dirige) e hipotensão (queda de pressão) em pessoas sensíveis""")
        elif tipo_tosse == "C":
            print("Opções de Ativos:")
            print("- Mucolíticos: Acetilcisteína, Ambroxol, Bromexina, Carbocisteína")
            print("- Expectorantes: Guaifenesina")
            print("- Fitoterápicos: Hedera Helix, Guaco")
            print("- Com Broncodilatador: Acebrofilina")

            diabetes = input("O paciente tem diabetes? (S/N) ").upper()
            if diabetes == "S":
                print("⚠️ INDICAR: Acetilcisteína (sachê sem açúcar) ou versões DIET de Ambroxol/Acebrofilina.")

            # Nova lógica para Acebrofilina
            print("Verificando indicação de Acebrofilina...")
            cardiaco = input("O paciente tem problemas de coração ou pressão muito alta? (S/N) ").upper()
            epilepsia = input("O paciente tem histórico de convulsões? (S/N) ").upper()
            idade = int(input("Qual a idade do paciente? ")) # Adicionando a solicitação de idade

            if cardiaco == "S" or epilepsia == "S" or idade < 2:
                print("❌ EVITAR ACEBROFILINA. Risco de taquicardia ou crises.")
                print("✅ PREFERIR: Acetilcisteína ou Ambroxol (são mais seguros para o coração).")
            else:
                print("✅ ACEBROFILINA LIBERADA. (Excelente para peito chiando).")
        else:
            print("Tipo de tosse inválido.")

    # --- LÓGICA PARA DOR / ENXAQUECA ---
    elif categoria == "2":
        print("\n--- Protocolo de Avaliação de Cefaleia ---")

        # 1. Identificação do Tipo de Dor
        unilateral = input("A dor é de um lado só e latejante? (S/N): ").upper()
        sintomas_extras = input("Tem náusea, vômito ou incômodo com a luz? (S/N): ").upper()
        frequencia = input("Isso acontece com frequência (crônico)? (S/N): ").upper()

        # 2. Filtro de Segurança Cardiovascular
        hipertensao = input("O paciente tem pressão alta ou problema no coração? (S/N): ").upper()
        estomago = input("Tem histórico de gastrite ou úlcera? (S/N): ").upper()

        print("\n--- Resultado da Análise ---")

        # Lógica de Decisão
        if unilateral == "S" or sintomas_extras == "S":
            print("SUSPEITA: Crise de Enxaqueca (Migrânea).")

            if hipertensao == "S":
                print("⚠️ ALERTA: Evitar Triptanos (Naratriptana) e Ergotamina.")
                print("👉 INDICAR: Dipirona 1g ou Paracetamol 750mg.")
                print("💡 DICA: Se houver náusea, associar Metoclopramida (Plasil).")
            else:
                print("👉 INDICAR: Naratriptana (Naramig) ou Cefaliv/Cefalium.")
                print("💡 ORIENTAÇÃO: Tomar o mais rápido possível no início da dor.")

        else:
            print("SUSPEITA: Cefaleia Tensional ou Dor Comum.")
            if estomago == "S":
                print("👉 INDICAR: Paracetamol (mais seguro para o estômago). Evitar Ibuprofeno/Aspirina.")
            else:
                print("👉 INDICAR: Dipirona ou associações com Cafeína (Neosaldina, Dorflex).")

        if frequencia == "S":
            print("\n📢 NOTA: Uso de analgésicos >3x na semana causa efeito rebote. Encaminhar para profilaxia.")

    # --- LÓGICA PARA ALERGIA / RINITE ---
    elif categoria == "3":
        print("\n--- Protocolo de Avaliação de Alergia/Rinite ---")

        # 1. Identificação dos Sintomas
        tipo_sintoma = input("Sintomas: (1) Espirro/Coriza/Coceira ou (2) Nariz Entupido apenas? ")
        tempo = input("É uma crise aguda (agora) ou persistente (todo dia)? (1/2) ")

        # 2. Filtro de Segurança e Estilo de Vida
        atividade = input("Vai dirigir, estudar ou operar máquinas hoje? (S/N): ").upper()
        idoso = input("O paciente é idoso? (S/N): ").upper()
        hipertenso = input("O paciente tem pressão alta? (S/N): ").upper()

        print("\n--- Resultado da Análise ---")

        # Lógica para Anti-histamínicos (Espirro/Coceira)
        if tipo_sintoma == "1":
            if atividade == "S" or idoso == "S":
                print("👉 INDICAR: Antialérgicos de 2ª Geração (Não dão sono).")
                print("✅ Opções: Loratadina, Desloratadina ou Fexofenadina (Allegra).")
            else:
                print("👉 INDICAR: Antialérgicos de 1ª Geração (Ação rápida, mas dá SONO).")
                print("✅ Opções: Dexclorfeniramina (Polaramine, é REFERÊNCIA), Histamin (é SIMILAR) ou Hidroxizina.")

        # Lógica para Nariz Entupido (Congestão)
        if tipo_sintoma == "2": 
            if hipertenso == "S":
                print("⚠️ ALERTA: Evitar descongestionantes com Naftazolina (Neosoro/Sorine).")
                print("👉 INDICAR: Apenas Soro Fisiológico 0,9% em abundância.")
            else:
                print("👉 INDICAR: Descongestionantes tópicos por no MÁXIMO 3 a 5 dias.")

        # Lógica para Uso Persistente (Tratamento)
        if tempo == "2":
            print("💡 DICA DE TRATAMENTO: O paciente precisa de Corticoide Nasal (Budesonida/Mometasona).")
            print("📢 NOTA: O efeito demora de 2 a 3 dias. Higienizar com soro antes de usar.")

        if idoso == "S" and atividade == "N":
            print("❗ AVISO: Mesmo que não dirija, antialérgicos que dão sono aumentam risco de QUEDAS em idosos.")


    # --- LÓGICA PARA SAÚDE DIGESTIVA ---
    elif categoria == "4":
        print("\n--- Protocolo de Avaliação Digestiva ---")

        print("Qual o principal sintoma?")
        print("1. Azia / Queimação / Má digestão")
        print("2. Diarreia")
        print("3. Intestino Preso (Constipação)")
        queixa = input("Opção: ")

        # 1. AZIA E QUEIMAÇÃO
        if queixa == "1":
            gravida = input("A paciente está grávida? (S/N): ").upper()
            uso_frequente = input("Usa remédio para azia quase todo dia? (S/N): ").upper()

            if gravida == "S":
                print("👉 INDICAR: Carbonato de Cálcio ou Magnésio (Mylanta/Pepsamar). Mais seguro.")
            else:
                print("👉 ALÍVIO RÁPIDO: Hidróxido de Alumínio ou Sais de Fruta.")
                print("👉 TRATAMENTO: Omeprazol ou Pantoprazol (Tomar em jejum).")

            if uso_frequente == "S":
                print("⚠️ ALERTA: Uso crônico pode esconder úlceras ou H. Pylori. Indicar médico.")

        # 2. DIARREIA
        elif queixa == "2":
            febre = input("Tem febre ou sangue/pus nas fezes? (S/N): ").upper()
            crianca = input("É para criança pequena? (S/N): ").upper()

            if febre == "S":
                print("❌ ALERTA CRÍTICO: NÃO usar Imosec (Loperamida). Risco de infecção generalizada.")
                print("👉 ORIENTAÇÃO: Encaminhar ao Pronto Socorro imediatamente.")
            else:
                print("👉 INDICAR: Floratil (Saccharomyces boulardii) ou Enterogermina.")
                print("👉 ESSENCIAL: Soro de Reidratação Oral (beber após cada evacuação).")
                if crianca == "S":
                    print("💡 DICA: Zinco (em gotas/xarope) ajuda na recuperação da mucosa infantil.")

        # 3. INTESTINO PRESO
        elif queixa == "3":
            tempo = int(input("Há quantos dias sem ir ao banheiro? "))
            idoso = input("O paciente é idoso? (S/N): ").upper()

            if tempo > 7:
                print("⚠️ ALERTA: Risco de impactação fecal. Encaminhar para avaliação médica.")
            elif idoso == "S":
                print("👉 INDICAR: Lactulose (Lactulona) ou Fibras. Evitar laxantes estimulantes fortes.")
            else:
                print("👉 INDICAR: Bisacodil (Dulcolax) para efeito rápido ou Almeida Prado 46.")

            print("📢 ORIENTAÇÃO: Aumentar ingestão de água e fibras (mamão, aveia).")

    # --- LÓGICA PARA SAÚDE MUSCULAR ---
    elif categoria == "5":
        print("\n--- Protocolo de Avaliação Muscular ---")
        print("Qual o tipo da dor?")
        print("1. Torcicolo / Tensão no pescoço e ombros")
        print("2. Pancada / Trauma recente (Inchaço)")
        print("3. Dor Lombar / Nervo Ciático")
        tipo_dor = input("Opção: ")

        # 1. Filtros de Segurança
        idoso = input("O paciente é idoso? (S/N): ").upper()
        dirigir = input("Vai dirigir ou operar máquinas hoje? (S/N): ").upper()
        estomago = input("Tem histórico de gastrite ou úlcera? (S/N): ").upper()

        print("\n--- Resultado da Análise ---")

        # Lógica de Decisão
        if tipo_dor == "1": # Tensão / Torcicolo
            if idoso == "S" or dirigir == "S":
                print("👉 INDICAR: Dipirona 1g + Compressas quentes + Pomada (Diclofenaco).")
                print("⚠️ ALERTA: Evitar Ciclobenzaprina pelo risco de sono e quedas.")
            else:
                print("👉 INDICAR: Ciclobenzaprina (Miosan) ou Dorflex.")
                print("💡 DICA: Tomar preferencialmente à noite.")

        elif tipo_dor == "2": # Pancada / Inflamação
            print("👉 INDICAR: Gelo nas primeiras 48h.")
            if estomago == "S":
                print("👉 INDICAR: Paracetamol + Gel de Arnica ou Diclofenaco Tópico.")
            else:
                print("👉 INDICAR: Anti-inflamatório (Ibuprofeno ou Cetoprofeno).")

        elif tipo_dor == "3": # Lombar / Ciático
            print("⚠️ ALERTA: Se houver perda de força nas pernas, ir ao médico.")
            if idoso == "S":
                print("👉 INDICAR: Paracetamol + Vitaminas do complexo B (Etna/Citoneurin).")
            else:
                print("👉 INDICAR: Associações potentes (Tandrilax / Torsilax / Bioflex).")

        # Dica Geral
        print("\n📢 ORIENTAÇÃO: Pomadas e géis ajudam muito sem agredir o estômago.")

    # --- LÓGICA PARA ANTICONCEPCIONAL ---
    elif categoria == "6":
        primeira_vez = input("A cliente quer começar a tomar pela primeira vez? (S/N) ").upper()

        if primeira_vez == "S":
            print("❌ ATENÇÃO: Farmacêutico não deve indicar o primeiro anticoncepcional.")
            print("👉 ORIENTAÇÃO: Encaminhar ao Ginecologista para exames de risco de Trombose.")
        else:
            print("✅ OK: Verificar se ela já tem o nome do remédio ou se deseja o Genérico/Intercambiável.")
            esquecimento = input("É dúvida sobre esquecimento? (S/N) ").upper()
            if esquecimento == "S":
                horas = int(input("Quanto tempo de atraso (em horas)? "))
                if horas <= 12:
                    print("ORIENTAÇÃO: Tomar agora. Eficácia mantida. Continuar cartela normalmente.")
                else:
                    print("ALERTA: Eficácia reduzida! Tomar o esquecido e usar CAMISINHA por 7 dias.")

            interacao = input("Está tomando antibiótico ou remédio para convulsão? (S/N) ").upper()
            if interacao == "S":
                print("ALERTA CRÍTICO: Esses remédios podem cortar o efeito. Usar método de barreira (camisinha).")

            fuma = input("Paciente fuma e tem mais de 35 anos? (S/N) ").upper()
            if fuma == "S":
                print("AVISO MÉDICO: Risco aumentado de Trombose. Sugerir consulta para avaliar métodos sem estrogênio.")

    # --- LÓGICA PARA CORTICOIDE ---
    elif categoria == "7":
        print("\n--- Protocolo de Ética e Segurança ---")
        possui_receita = input("O paciente possui receita médica? (S/N): ").upper()

        if possui_receita == "N":
            print("❌ ATENÇÃO: Corticoides não são MIPs (Medicamentos Isentos de Prescrição).")
            print("👉 CONDUTA: Não indicar. Encaminhar ao médico para diagnóstico.")
            print("💡 DICA: Se for inflamação leve, sugerir Anti-inflamatório (AINE) ou Tópico (Pomada).")
        else:
            print("✅ OK: Proceder com a DISPENSAÇÃO e as orientações de segurança...")
            diabetes = input("O paciente é diabético? (S/N) ").upper()
            pressao = input("Tem pressão alta? (S/N) ").upper()
            tempo = int(input("Uso por quantos dias? "))

            if diabetes == "S":
                print("ALERTA: Monitorar glicemia! Corticoides sobem o açúcar no sangue.")
            if pressao == "S":
                print("ALERTA: Pode reter líquido e subir a pressão arterial.")

            print("REGRAS DE OURO:")
            print("- Tomar preferencialmente pela MANHÃ (até as 9h).")
            print("- Tomar sempre com o ESTÔMAGO CHEIO.")

            if tempo > 10:
                print("- AVISO: Não parar o uso de vez. O desmame deve ser gradual (conforme médico).")
    
    # --- LÓGICA PARA COLÍRIOS ---
    elif categoria == "8": # Colírios
        print("\n--- Avaliação Ética Ocular ---")
        vermelho = input("O olho está muito vermelho ou com dor? (S/N): ").upper()
        secrecao = input("Tem secreção amarelada (pus)? (S/N): ").upper()

        if secrecao == "S":
            print("❌ NÃO INDICAR: Suspeita de Infecção Bacteriana.")
            print("👉 CONDUTA: Encaminhar ao Oftalmologista. Precisa de antibiótico com receita.")
        
        elif vermelho == "S":
            print("⚠️ CUIDADO: Se houver dor forte ou visão turva, não indique nada.")
            print("👉 CONDUTA: Sugerir apenas compressas geladas e encaminhar ao médico.")
        
        else:
            print("✅ AUTONOMIA: Você pode indicar Lubrificantes (Lágrimas Artificiais).")
            print("👉 Sugestão: Carmulose Sódica ou Hialuronato de Sódio.")

    # --- LÓGICA PARA FEBRE (ADULTOS E CRIANÇAS) ---
    elif categoria == "9":
        print("\n--- Protocolo de Avaliação de Febre ---")
        
        idade = float(input("Qual a idade do paciente? (Ex: 0.5 para 6 meses): "))
        temperatura = float(input("Qual a temperatura medida? (Ex: 38.5): "))
        peso = float(input("Qual o peso do paciente? (Essencial para crianças): "))

        # 1. Filtro de Segurança (Dengue e Alertas)
        print("\nSinais de Alerta:")
        manchas = input("- Tem manchas vermelhas no corpo ou dor atrás dos olhos? (S/N): ").upper()
        vmito = input("- Tem vômito persistente ou dor abdominal forte? (S/N): ").upper()
        pescoco = input("- Tem rigidez na nuca (dor ao tentar encostar o queixo no peito)? (S/N): ").upper()

        print("\n--- Resultado da Análise ---")

        # Alertas de Emergência
        if pescoco == "S":
            print("❌ ALERTA CRÍTICO: Suspeita de Meningite. Ir ao Pronto Socorro AGORA!")
        elif manchas == "S" or vmito == "S":
            print("⚠️ ALERTA: Suspeita de Dengue/Zika/Chikungunya.")
            print("👉 CONDUTA: Hidratação intensa. NÃO usar Ibuprofeno ou Aspirina.")
            print("👉 INDICAR: Apenas Paracetamol ou Dipirona.")

        # Lógica por Idade
        elif idade < 0.25: # Menores de 3 meses
            print("❌ ALERTA: Bebês menores de 3 meses com febre devem ir ao Pediatra imediatamente.")
        
        else:
            if temperatura < 37.8:
                print("👉 ESTADO: Febrícula. Sugerir banho morno e hidratação antes de medicar.")
            else:
                print(f"👉 INDICAR: Dipirona ou Paracetamol.")
                if idade >= 0.5: # Acima de 6 meses
                    print("✅ OPCIONAL: Ibuprofeno (Se não houver suspeita de Dengue).")
                
                # --- CÁLCULO DE DOSAGEM ---
                print(f"\n💡 DOSAGEM ESTIMADA PARA DIPIRONA ({peso}kg):")
                
                # 1. Gotas (500mg/mL) -> 1 gota por kg
                print(f"- Dipirona GOTAS (500mg/mL): {int(peso)} gotas.")
                
                # 2. Xarope/Solução (50mg/mL) -> 0,5 mL por kg
                print(f"- Dipirona XAROPE (50mg/mL): {peso * 0.5} mL.")
                
                print("\n⚠️ IMPORTANTE: Intervalo recomendado de 6 em 6 horas.")

    else:
        print("Verificando categoria ou opção inválida. Por favor, digite o número da categoria (1-9).")

# Executar
assistente_farmacia_pro()
