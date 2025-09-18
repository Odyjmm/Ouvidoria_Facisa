def tradutor_silabas(silaba):
    if silaba == "R":
        return "Reclamação"
    elif silaba == "E":
        return "Elogio"
    elif silaba == "S":
        return "Sugestão"

    return None

def entrada_titulo_valido():
    while True:
        titulo = input("Digite o titulo da manifestação: ")

        if len(titulo) < 3:
            print("Titulo muito curto, seu titulo deve ser descritivo e conter pelo menos 3 caracteres." + "\n")
            continue

        elif len(titulo) > 100:
            print("Titulo muito longo, seu titulo deve ser conciso e conter no máximo 100 caracteres." + "\n")
            continue

        return titulo

def entrada_descricao_valido():
    while True:
        descricao = input("Descreva sua manifestação: ")

        if len(descricao) < 15:
            print("Descrição muito curta, sua descrição deve ser descritivo e conter pelo menos 15 caracteres." + "\n")
            continue

        elif len(descricao) > 300:
            print("Descrição muito longa, sua descrição deve ser conciso e conter no máximo 300 caracteres." + "\n")
            continue

        return descricao

def entrada_autor_valido():
    while True:
        autor = input("Insira seu nome: ")

        if len(autor) < 3:
            print("Nome do autor muito curto, precisamos ser capazer de indenfica-lô, "
                  "seu nome deve conter pelo menos 3 caracteres." + "\n")
            continue

        elif len(autor) > 50:
            print("Nome do autor muito longo, insira apenas seus dois ou três primeiros nomes, de modo que"
                  "seu nome não ultrapasse 50 caracteres." + "\n")
            continue

        return autor

def entrada_respondente_valido():
    while True:
        respondente = input("Insira nome do respondente: ")

        if len(respondente) < 3:
            print("Nome do respondente muito curto, precisamos ser capazer de indenfica-lô, "
                  "o nome do respondente deve conter pelo menos 3 caracteres." + "\n")
            continue

        elif len(respondente) > 50:
            print("Nome do respondente muito longo, insira apenas seus dois ou três primeiros nomes, de modo que"
                  "o nome do respondente não ultrapasse 50 caracteres." + "\n")
            continue

        return respondente

def entrada_tipo_valido(situacao):
    while True:
        tipo = ""
        if situacao == "NEW":
            tipo = input("Qual o tipo da sua manifestação? "
                     "Use 'R' para reclamações, 'E' para elogios e 'S' para sugestões ").upper()

        elif situacao == "LIST":
            tipo = input("Qual o tipo de manifestação que você deseja ver? "
                         "Use 'R' para reclamações, 'E' para elogios e 'S' para sugestões ").upper()


        if tipo not in ["R", "S", "E"]:
            print("Você não selecionou um tipo válido, Use apenas 'R' para reclamações,"
                  " 'E' para elogios e 'S' para sugestões" + "\n")
            continue

        return tradutor_silabas(tipo)

def entrada_id(situacao):
    while True:
        n = 0
        if situacao == "REMOVE":
            n = int(input("Digite o código da manifestação a ser removida: "))
        elif situacao == "SEARCH":
            n = int(input("Digite o código da manifestação que você deseja consultar: "))

        if n <= 0:
            print("Código digitado é inválido." + "\n")
            continue

        return n