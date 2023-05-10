import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    lista = []
    while(not enforcou and not acertou):

        chute = input("Qual letra ?  ")
        chute = chute.strip().upper()       #tira os espacos que vem do input

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, voce errou! Faltam {} tentativas".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")

    print("Fim do jogo.")

def imprime_mensagem_abertura():

    print("*********************************")
    print("***Bem vindo no jogo da forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    with open("palavras.txt") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()