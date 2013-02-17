#Função: fibonacci e fatorial recursivo.
#Autor: Felipe Rosa
#Professor: Fernando Massanori

def fib(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
        print(a)
def fat(n):
    f = 1
    c = 1
    while c<=n:
        f = f * c
        c +=1
    return f

def fat2(n):
    f = 1
    while n >0:
        f = f * n
        n -=1
    return f

def fat3(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * fat3(n-1))