# coding: latin-1

# Exercícios da semana 4

def tp(f, t):
  # recebe imagem e o deslocamento linha/coluna por parâmetro
  # baseado no tutorial de translação periódica
  import numpy as np
  import ia636
  H,W = f.shape
  dh,dw = t
  dhi = (-dh + H) % H # mapeamento inverso igual feito em iaffine (inversa de T)
  dwi = (-dw + W) % W # mapeamento inverso
  f2 = np.vstack((f,f))
  f4 = np.hstack((f2,f2))
  return f4[dhi:dhi+H,dwi:dwi+W]

def tp_indices(f, t):
  # recebe imagem e o deslocamento linha/coluna por parâmetro
  # baseado no iaptrans, por índices
  # somente para matrizes 2D
  import numpy as np
  g = np.empty_like(f)
  H,W = f.shape
  rr,cc = t
  row,col = np.indices(f.shape)
  g[:] = f[(row-rr)%H, (col-cc)%W]
  return g

def tp_fatiamento(f, t):
  # recebe imagem e o deslocamento linha/coluna por parâmetro
  # fatiando a imagem em regiões e reposicionando-as
  import numpy as np
  H,W = f.shape
  dh,dw = t
  g = np.empty_like(f)
  g[0:dh,0:dw] = f[-dh :    , -dw :   ]  # f1
  g[0:dh,dw:W] = f[-dh :    , 0   :-dw]  # f2
  g[dh:H,0:dw] = f[0   :-dh , -dw :   ]  # f3
  g[dh:H,dw:W] = f[0   :-dh , 0   :-dw]  #f4
  return g
