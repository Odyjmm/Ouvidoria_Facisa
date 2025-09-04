opcao = 0
manifestacoes = []

while opcao != 6:
    print("\n" + "--- Ouvidoria 24h ---" + "\n")
    print(
        "1) Listar Manifestações \n2) Adicionar Nova Manifestação \n3) Pesquisar por Código \n4) Remover por Código \n5) Editar Manifestação \n6) Encerrar")
    opcao = int(input("\n" + "Escolha sua opção: "))

    if opcao == 1:
        if len(manifestacoes) == 0:
            print("Não existem manifestações registradas na base de dados.")

        else:
            print("\n" + "--- Listagem de Manifestações ---" + "\n")
            for n in range(len(manifestacoes)):
                print(f'- Manifestação nº {n + 1}: "{manifestacoes[n]}".')

    elif opcao == 2:
        novaManifestacao = input("Por favor, digite sua reclamação, sugestão ou elogio: ")
        manifestacoes.append(novaManifestacao)
        print("Sua manifestação foi adicionada com sucesso!")

    elif opcao == 3:
        codigo = int(input("\n" + "Digite o código da manifestação a ser pesquisada: "))

        if 1 <= codigo <= len(manifestacoes):
            manifestacaoPesquisada = manifestacoes[codigo - 1]
            print(f'A manifestação de código {codigo} diz o seguinte: "{manifestacaoPesquisada}".')

        else:
            print("O código informado é inválido.")

    elif opcao == 4:
        codigo = int(input("\n" + "Digite o código da manifestação a ser removida: "))

        if 1 <= codigo <= len(manifestacoes):
            manifestacoes.pop(codigo - 1)
            print(f"A manifestação de código {codigo} foi removida com sucesso!")

        else:
            print("O código informado é inválido.")

    elif opcao == 5:
        codigo = int(input("\n" + "Digite o código da manifestação a ser editada: "))

        if 1 <= codigo <= len(manifestacoes):
            novaManifestacao = input("Por favor, digite sua reclamação, sugestão ou elogio: ")
            manifestacoes[codigo - 1] = novaManifestacao
            print("Manifestação editada com sucesso!")

        else:
            print("O código informado é inválido.")

    elif opcao != 6:
        print("Opção Inválida")

print("\n" + "Obrigado por usar a Ouvidoria 24h!")