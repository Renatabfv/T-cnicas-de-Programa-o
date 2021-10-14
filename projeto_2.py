#cadastrar novos usuários pelo seu nome completo e e-mail
#exibir todos os usuários cadastrados, listando-os por ordem de cadastro.
#exibir todos os usuários cadastros, listando-os por ordem alfabética.
#um usuário faz parte da lista de participantes, buscando-o pelo seu nome.
#remover um usuário cadastrado, buscando-o por seu e-mail.
#poder alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.

def criarEstudante():
    estudanteTemp = {}
    estudanteTemp["nome"] = input("Digite o nome do estudante: ")
    estudanteTemp["email"] = input("Digite o email do estudante: ")
    return estudanteTemp

def mostrarNomesEstudante(listaEstudante):
    for estudante in listaEstudante:
        print(estudante["nome"])


def main():
    listaEstudante = [ ]
    qtdEstudante = int(input("Informe quantos estudantes você deseja salvar na lista: "))
    ordemAlfabetica = (input("Deseja ordernar os usuarios por ordem alfabetica ?"))

    contador = 0
    while(contador < qtdEstudante):
        estudanteTemp = criarEstudante()
        listaEstudante.append(estudanteTemp)
        contador = contador + 1
    if (ordemAlfabetica) == ("sim" or "Sim"):
        mostrarNomesEstudante(listaEstudante.sort()) 
    else:
        mostrarNomesEstudante(listaEstudante)


if (__name__) == ("__main__"):
 main()
