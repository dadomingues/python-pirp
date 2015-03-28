# coding: latin-1

# Exercícios da semana 3




# window e level
 
def TWL(L,W):
    import numpy as np
    Pmin = max(0,L-W//2)
    Pmax = min(255,L+W//2)
    T = np.zeros(256, np.uint8)
    T[Pmin:Pmax+1] = np.floor(np.linspace(0, 255, num=(Pmax - Pmin + 1)))
    T[Pmax:] = 255
    return T
 
def WL(f,L,W):
    import numpy as np
    T = TWL(L,W)
    return T[f]

# usando as funções em um outro script

from tutorial_contraste_iterativo_2 import WL, TWL
W = 30
L = 15
Tw = TWL(L,W)
adshow(ia.iaplot(Tw,ylabel='Output intensity',xlabel='Input intensity'),'Transformada de intensidade W=%d L=%d' % (W,L)



