#Função: Lista do google develop day
#Autor: Felipe Rosa e Raphael Ramos
#Professor: Fernando Massanori 


#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


# D. Dada uma lista de n??meros retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
  return list (set(nums))

# E. Cripto desafio!!
# Dada uma frase, voc?? deve retirar todas as letras repetidas das palavras
# e sortear as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto, depois tente sortear
# as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  lista = []
  lista2 = frase.split()
  b = ''
  h = 0
  for x in lista2:
    a = list(set(x))
    a.sort()
    a = ''.join(a)
    lista.append(a)
  return " ".join(lista)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('remove_iguais')
  test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
  test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
  test(remove_iguais([]), [])

  print ()
  print ('cripto')
  test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
  test(cripto('Batatinha quando nasce esparrama pelo chao'),
       'Bahint adnoqu acens aemprs elop acho')

if __name__ == '__main__':
  main()
