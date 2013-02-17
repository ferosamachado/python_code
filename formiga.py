#Função:        Jogo do labirinto
#               Acha o caminho do labirinto, iniciando pelo E->entrada até o S->saída.
#Autor:         Felipe Rosa
#Professor:     Fernando Massanori


def fumiga():
    
    labirinto = '''
    +-------------+-----+
    | | | |       |     |
    | | | | +---+ | +++S|
    E |   | | | | | ++--+
    | | | | | | | |     |
    | | | | |   | +---+ +
    |   | | | |         |   
    | | | | | | +-+ +---+
    | | |   | |   | |   |
    | | | | | | +-+ +-+ |
    | | | | | | |       |
    +-----------+-------+
    '''
    y, x,c = 0, 0, 0
    inicio = []
    for linha in labirinto.splitlines():
        inicio.append(list(linha))
    for i in inicio:
        if 'E' in i:
            x = i.index('E')
            y = c
        c = c + 1
    teste(y,x,inicio)    

def teste(y,x,inicio):
    if inicio[y][x+1]=='S' or inicio[y][x-1]=='S' or inicio[y+1][x]=='S' or inicio[y-1][x]=='S':
        print('Assou!!')
        inicio[y][x]='^'
        for i in inicio:
            w = ''.join(i)
            print(w)
    else:
        quadrante(y,x,inicio)

def quadrante(y,x,inicio):
    if inicio[y-1][x]==' ':
       inicio[y][x]='o'
       y = y-1
       teste(y,x,inicio)
    elif inicio[y+1][x]==' ':
        inicio[y][x]='o'
        y = y+1
        teste(y,x,inicio)
    elif inicio[y][x+1]==' ':
        inicio[y][x]='o'
        x = x+1
        teste(y,x,inicio)
    elif inicio[y][x-1]==' ':
        inicio[y][x]='o'
        x = x-1
        teste(y,x,inicio)
    else:
        inicio[y][x]='.'
        bola(y,x,inicio)

def bola(y,x,inicio):
    if inicio[y-1][x]=='o':
       inicio[y-1][x]='.'
       if inicio[y-2][x]==' ' or inicio[y-2][x]=='o':
            inicio[y-1][x]='o'
       y = y-1
       teste(y,x,inicio)
    elif inicio[y][x+1]=='o':
        inicio[y][x+1]='.'
        if inicio[y][x+2]==' ' or inicio[y][x+2]=='o':
            inicio[y][x+1]='o'
        x = x+1
        teste(y,x,inicio)
    elif inicio[y+1][x]=='o':
        inicio[y+1][x]='.'
        if inicio[y+2][x]==' ' or inicio[y+2][x]=='o':
            inicio[y+1][x]='o'
        y = y+1
        teste(y,x,inicio)
    elif inicio[y][x-1]=='o':
        inicio[y][x-1]='.'
        if inicio[y][x-2]==' ' or inicio[y][x-2]=='o':
            inicio[y][x-1]='o'
        x = x-1
        teste(y,x,inicio)
    else:
        print('Death to all defiers!')

fumiga()
