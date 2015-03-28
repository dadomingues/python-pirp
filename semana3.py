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

# exercício de reescrita do affine

# melhor solução (performance) por yugo4k a partir de barbara_reis
def gg_affine4(f, T):
  import numpy as np
  H, W = domain = f.shape
  n = H * W
  y1,x1 = np.indices(domain)

  yx1 = np.array([y1.ravel(),
                  x1.ravel(),
                  np.ones(n)])
  yx_float = np.dot(np.linalg.inv(T), yx1)
  yy = np.rint(yx_float[0]).astype(int)
  xx = np.rint(yx_float[1]).astype(int)

  g = np.zeros(n, dtype=np.uint8)
  validIdxs = (0 <= yy) & (yy < H) & (0 <= xx) & (xx < W)
  g[validIdxs] = f[yy[validIdxs], xx[validIdxs]]

  return g.reshape(domain)

list_gg_affine.append(gg_affine4)

