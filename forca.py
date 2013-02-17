#           Função:         Jogo da forca em python. Sistema baixa uma lista de palavras em pt-br e sorteia uma.
#                           Necessario conexao web na primeira execução.
#           Autor:          Felipe Rosa
#           Professor:      Fernando Massanori


print('Round Forca! Esteja pronto!')
def Busca():
    import urllib.request
    page = urllib.request.urlopen ('http://www.ime.usp.br/~pf/algoritmos/dicios/br')
    palavra = page.read().decode ("iso8859").split()
    Randomiza (palavra)

def Randomiza(palavra):
    import random
    global coco
    global secreta
    secreta = random.choice (palavra)
    global certas
    global erradas
    certas = ' '
    erradas = ' '
    totalc = ' '
    coco = ' '
    print("ESTE É O JOGO DA FORCA!")
    print("É simples! Chute letras até acertar a palavra. Mas cuidado: você só tem seis chances!")
    desenha_situação(secreta,certas,erradas,totalc,coco,palavra)

def desenha_situação(secreta,certas,erradas,totalc,coco,palavra):
    global forca
    forca = [
         """
             +----------+
             |          |
             |          |
                        |
                        |
                        |
                        |
                        |
            ==============""",
         """
            +----------+
            |          |
            O          |
                       |
                       |
                       |
                       |
                       |
           ==============""", 
         """
           +----------+
           |          |
           O          |
           |          |
                      |
                      |
                      |
                      |
          ==============""", 
         """
           +----------+
           |          |
           O          |
          /|          |
                      |
                      |
                      |
                      |
          ==============""", 
         """
           +----------+
           |          |
           O          |
          /|\         |
                      |
                      |
                      |
                      |
          ==============""", 
         """
           +----------+
           |          |
           O          |
          /|\         |
          /           |
                      |
                      |
                      |
          ==============""", 
         """
           +----------+
           |          |
           O          |
          /|\         |
          / \         |
                      |
                      |
                      |
          =============="""]
    
    print (forca[len(erradas)-1])
    for x in secreta:
        print ('_', end = ' ')
    chute (secreta,certas,erradas,totalc,coco,palavra)
                
def chute(secreta,certas,erradas,totalc,coco,palavra):
    global letra
    letra = str (input ('\nFale a letra: '))    
    if letra in coco:
        print ("Você já colocou esta letra, tente novamente")
        return chute(secreta,certas,erradas,totalc,coco,palavra)
    else:
        if len(letra) > 1:
            print('Somente uma letra, por favor...')
            return chute(secreta,certas,erradas,totalc,coco,palavra)
        else:
            if letra.isalpha():
                coloca_letra (secreta,certas,erradas,letra,totalc,coco,palavra)
            else:
                print('E quero SOMENTE letras!')
                chute(secreta,certas,erradas,totalc,coco,palavra)

def coloca_letra (secreta,certas,erradas,letra,totalc,coco,palavra):
    cont = 0
    while cont<6:
        if letra in secreta:
            certas = certas + letra
            print (forca[len(erradas)-1])
            positron = 0
            while positron < len(secreta):                
                if letra == secreta[positron]:
                    totalc = totalc + letra
                positron = positron + 1                
            print("\n\nAs letras certas são: ", totalc)

        else:
            erradas = erradas + letra
            cont = cont + 1                
            if len(erradas) < 8:
                print (forca[len(erradas)-1])
            else:
                print ("K.O.! Winner is... Computer!")
                print('Oh! a palavra é essa... ', secreta, ', Blu,Blu!')
                de_novo(palavra)        
        for x in secreta:
            if x in certas:
                print (x, end = ' ')
            else:
                print ('_', end = ' ')
        coco = certas + erradas
        print ('\nAs letras já colocadas são: ', coco)
        if len(totalc) == len(secreta)+1:
            venceu(palavra)
        else:
            chute(secreta,certas,erradas,totalc,coco,palavra)
    de_novo(palavra)

def de_novo(palavra):
    resurrection = input ("Quer jogar mais uma vez? s ou n ")
    while resurrection != 's' and resurrection != 'n':
        print ("Hey apple!É só s e n!")
        resurrection = input ("Quer jogar mais uma vez? s ou n: ")
    if resurrection == 's':
        print ("Então vamos rodar esse trem!")
        Randomiza(palavra)
    elif resurrection == 'n':
        print ("Não quer jogar, não joga meu!")
        fim_de_jogo()

def venceu(palavra):
    print("K.O.! Winner is... Player!")
    de_novo(palavra)

def fim_de_jogo():
    import os
    print ("Acabou!")
    os._exit(0)
    
Busca()
