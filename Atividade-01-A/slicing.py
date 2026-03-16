#1 - fatiamento (slicing)
    #mascara

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt #mostra imagem

#Gere uma imagem de 200 × 200 pixels com o fundo totalmente preto (valor 0)
img = np.zeros((200,200,3), dtype=np.uint8)

#ex: matriz[50:150, 50:150] e quadrado branco valor = 255
img[50:150, 50:150] = [255,255,255]

#mostrar imagem
plt.imshow(img) 
plt.axis("off") #deixa so imagem
plt.show() #imprime tela


    #degrade

#imagem 200 × 200, desta vez contendo um degrade horizontal, indo do lado preto (0) na esquerda ate branco (255) na direita.

y,x = 200,200
degrade = np.linspace(0,255,x,dtype=np.uint8) #0,255 para sair de preto e ir a branco passa x pq é horizontal

img_gray = np.tile(degrade, (y, 1))
img_2 = np.stack([img_gray]*3, axis=2)

plt.imshow(img_2) 
plt.axis("off") #deixa so imagem
plt.show() 
