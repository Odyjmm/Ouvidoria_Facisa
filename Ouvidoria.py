from Entrega_2.Ouvidoria_Methods import *
from Entrega_2.operacoesbd import *

opt = 0
connection = criarConexao("localhost", "root", "admin", "ouvidoria")

while opt != 7:
    print("\n" + "--- Ouvidoria 24h ---" + "\n")
    print("1) Listar Todas as Manifestações \n"
          "2) Listar Manifestações por Tipo \n"
          "3) Listar Números de Manifetações \n"
          "4) Adicionar Nova Manifestação \n"
          "5) Pesquisar Manifestação por Código \n"
          "6) Remover Manifestação por Código \n"
          "7) Encerrar")
    opt = int(input("\n" + "Escolha sua opção: "))

# Opção 1 - Listar Todas as manifestações
    if opt == 1:
        listar_todas_manifestacoes(connection)

# Opção 2 - Listar Manifestações por Tipo
    elif opt == 2:
        listar_manifestacoes_tipo(connection)

# Opção 3 - Listar Números de Manifetações
    elif opt == 3:
        listar_numero_manifestacoes(connection)

# Opção 4 - Adicionar Nova Manifestação
    elif opt == 4:
        adicionar_manifestacoes_tipo(connection)

# Opção 5 -  Pesquisar Manifestação por Código
    elif opt == 5:
        pesquisa_manifestacao(connection)

# Opção 5 -  Remover Manifestação por Código
    elif opt == 6:
        remover_manifestacao(connection)

    elif opt != 7:
        print("Opção Inválida")

print("\n" + "Obrigado por usar a Ouvidoria 24h!")