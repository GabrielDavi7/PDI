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