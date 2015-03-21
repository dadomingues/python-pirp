# coding: latin-1

# Exercícios da semana 2

# rampa

def rr_indices(lado):
    # solução 1:
    # cria um matriz de altura e largura "lado" preenchendo-a
    # com seu indice de coluna (usando np.indices)
    import numpy as np
    lixo, rampa = np.indices( (lado, lado) )
    return rampa
 
def rr_resize(lado):
    # solução 2:
    # cria uma rampa unidimensional e aumenta sua altura
    import numpy as np
    return np.resize(np.arange(lado), (lado,lado))

# x

def x_indices1(N):
    # apos preencher a matriz com zeros ela é varrida;
    # onde os índices r e c forem iguais ou (N-1)-c
    # altera o valor para TRUE.
    import numpy as np
    r, c = np.indices((N, N))
    f = (r==c) | (r==N-1-c)
    return f

def x_indices2(N):
    # cria um vetor com indices e traça as duas
    # linhas correndo a matriz com ajuda do vetor
    import numpy as np
    i = np.arange(N)
    f = np.zeros((N,N), dtype=bool)
    f[i,i] = True
    f[i,-i-1] = True
    return f
    
def x_idespelho(N):
    # cria uma matriz em que tudo é falso com a
    # exceção da posição onde os ídices são iguais;
    # depois realiza adição com seu próprio espelho.
    f = np.identity(N,'bool')
    return f | f[:,::-1]

# crop

def crop_vh(f):
    # verifica se as linhas que possuem algum valor maior que zero
    # verifica se as coluns que possuem algum valor maior que zero
    # gera uma saída com o pedaço em que existe valores maiores que zero.
    import numpy as np
    maxR = f.max(1)
    (iR,) = maxR.nonzero()
    f = f[iR[0]:iR[-1]+1] # crop na altura / linhas
    maxC = f.max(0)
    (iC,) = maxC.nonzero()
    return  f[:, iC[0]:iC[-1]+1] # crop na largura / colunas
    
def crop_limites(f):
    # busca os pontos X e Y iniciais e finais
    # da área a ser cortada e retorna o conteúdo.
    r = f.max(1)  # projeção horizontal
    c = f.max(0)  # projeção vertical
    ri = r.nonzero()[0]  # índices de pixels com valores não zeros
    ci = c.nonzero()[0]
    rmin = ri[0]         # primeiro índice de pixel com valor não zero
    rmax = ri[-1] + 1    # último índice de pixel com valor não zero
    cmin = ci[0]
    cmax = ci[-1] + 1
    return f[rmin:rmax, cmin:cmax]
    
def crop_indices(f):
    # pouco eficiente
    rc = f.nonzero()
    rmin = rc[0].min()
    rmax = rc[0].max()+1
    cmin = rc[1].min()
    cmax = rc[1].max()+1
    return f[rmin:rmax, cmin:cmax]
