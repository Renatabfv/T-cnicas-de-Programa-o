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
    for Estudante in listaEstudante:
        print(Estudante["nome"])

def main():
    listaEstudante = []
    qtdEstudante = int(input("Informe quantos estudantes você deseja salvar na lista: "))
    contador = 0

    while(contador < qtdEstudante):
        estudanteTemp = criarEstudante()
        listaEstudante.append(estudanteTemp)
        contador = contador + 1
    
    mostrarNomesEstudante(listaEstudante)

if(__name__ == "__main__"):
    
