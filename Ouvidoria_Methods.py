from Entrega_2.operacoesbd import *
from Entrega_2.Ouvidoria_Utils import *

def listar_todas_manifestacoes(connection):
    querry = "select * from feedback"
    manifestacoes = listarBancoDados(connection, querry)

    if len(manifestacoes) == 0:
        print("Não existe nenhuma manifestação cadastrada")
    else:
        for m in manifestacoes:
            print(
                f"Manifestação nº{m[0]}: Titulo - {m[1]}; {m[2]} | Autor - {m[3]} | Respondente - {m[4]} | Tipo - {m[5]}")

def listar_manifestacoes_tipo(connection):
    tipo = entrada_tipo_valido("LIST")
    querry = f"select * from feedback where tipo = '{tipo}'"
    manifestacoes = listarBancoDados(connection, querry)

    if len(manifestacoes) == 0:
        print("Não existe nenhuma manifestação desse tipo cadastrada")
    else:
        for m in manifestacoes:
            print(
                f"Manifestação nº{m[0]}: Titulo - {m[1]}; {m[2]} | Autor - {m[3]} | Respondente - {m[4]} | Tipo - {m[5]}")

def listar_numero_manifestacoes(connection):
    querry = "select count(*) from feedback"
    quantidade_manifestacoes = listarBancoDados(connection, querry)

    print(f"Atualmente, temos {quantidade_manifestacoes[0][0]} manifestações registradas.")

def adicionar_manifestacoes_tipo(connection):
    titulo = entrada_titulo_valido()
    descricao = entrada_descricao_valido()
    autor = entrada_autor_valido()
    respondente = entrada_respondente_valido()
    tipo = entrada_tipo_valido("NEW")

    querry = 'insert into feedback (titulo, descricao, autor, respondente, tipo) values (%s, %s, %s, %s, %s)'
    valores = [titulo, descricao, autor, respondente, tipo]

    codigo_manifestacao = insertNoBancoDados(connection, querry, valores)
    print("Manifestação adicionada com sucesso! O código é", codigo_manifestacao)

def pesquisa_manifestacao(connection):
    codigo_manifestacao = entrada_id("SEARCH")
    querry = "select * from feedback where id = %s "
    valor = [codigo_manifestacao]
    manifestacao = listarBancoDados(connection, querry, valor)

    if len(manifestacao) == 0:
        print("Nao existe uma manifestação cadastrada com o código informado")
    else:
        for m in manifestacao:
            print(
                f"Manifestação nº{m[0]}: Titulo - {m[1]}; {m[2]} | Autor - {m[3]} | Respondente - {m[4]} | Tipo - {m[5]}")

def remover_manifestacao(connection):
    codigo_manifestacao = entrada_id("REMOVE")
    querry = 'delete from feedback where id  = %s'
    valores = [codigo_manifestacao]

    manifestacoes_removidas = excluirBancoDados(connection, querry, valores)

    if manifestacoes_removidas == 1:
        print("Manifestação removida com sucesso!")
    else:
        print("Não existe uma manifestação com esse código.")