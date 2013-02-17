#Função: COnversor de numerais para números romanos.
#Autor: Felipe Rosa
#Professor: Fernando Massanori

#Inicia as variáveis, pois aparecem a primeira vez no laço
num = 0
roman = ""
num2 = 0
#pega a entrada, caso ela seja verdadeira
while num <= 0 or num > 1000000:
    num = int(input("Entre com o número para converter em algarismos romanos: " ))
    if num <= 0 or num > 1000000:
        print("Número inválido!")

num2 = num
#substitui 1000000 por ~M
while num >= 1000000:
    roman = roman + "~M"
    num = num - 1000000
    
#substitui 500000 por ~D
while num >= 500000:
    roman = roman + "~D"
    num = num - 500000
    
#substitui 100000 por ~C
while num >= 100000:
    roman = roman + "~C"
    num = num - 100000

#substitui 50000 por ~L
while num >= 50000:
    roman = roman + "~L"
    num = num - 50000

#substitui 10000 por ~X
while num >= 10000:
    roman = roman + "~X"
    num = num - 10000

#substitui 5000 por ~V
while num >= 5000:
    roman = roman + "~V"
    num = num - 5000

#substitui 1000 por M
while num >= 1000:
    roman = roman + "M"
    num = num - 1000

#substitui 500 por D
while num >= 500:
    roman = roman + "D"
    num = num - 500

#substitui 100 por C
while num >= 100:
    roman = roman + "C"
    num = num - 100

#substitui 50 por L
while num >= 50:
    roman = roman + "L"
    num = num - 50

#substitui 10 por X
while num >= 10:
    roman = roman + "X"
    num = num - 10

#substitui 5 por V
while num >= 5:
    roman = roman + "V"
    num = num - 5

#substitui 1 por I
while num >= 1:
    roman = roman + "I"
    num = num - 1

#casos que podem acontecer e possuem simbologia especial
roman = roman.replace( '~D~C~C~C~C', '~C~M' )
roman = roman.replace( '~C~C~C~C', '~C~D' )
roman = roman.replace( '~X~X~X~X', '~X~C' )
roman = roman.replace( '~X~X~X~X', '~X~L' )
roman = roman.replace( '~VMMMM', '~I~X' )
roman = roman.replace( 'MMMM', '~I~V' )
roman = roman.replace( 'DCCCC', 'CM' )
roman = roman.replace( "CCCC", "CD" )
roman = roman.replace( "LXXXX", "XC" )
roman = roman.replace( "XXXX", "XL" )
roman = roman.replace( "VIIII", "IX" )
roman = roman.replace( "IIII", "IV" )

#imprime o romanultado em algarismos romanos
print("Este número %d corresponde a %s em algarismos romanos." %(num2,roman))
