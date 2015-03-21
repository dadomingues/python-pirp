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
