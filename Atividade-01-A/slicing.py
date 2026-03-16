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
plt.title("mask")
plt.axis("off") #deixa so imagem
plt.show() #imprime tela


    #degrade

#imagem 200 × 200, desta vez contendo um degrade horizontal, indo do lado preto (0) na esquerda ate branco (255) na direita.

y,x = 200,200
degrade = np.linspace(0,255,x,dtype=np.uint8) #0,255 para sair de preto e ir a branco passa x pq é horizontal

img_gray = np.tile(degrade, (y, 1))
img_2 = np.stack([img_gray]*3, axis=2)

plt.imshow(img_2) 
plt.title("Degrade")
plt.axis("off") #deixa so imagem
plt.show() 


    #Merging

#Utilize a funcao ̃np.where (ou multiplicacao de matrizes divididas por 255) para combinar as duas imagens. A regra e: onde a Imagem 1.a for branca (255), mostre odegrade (Imagem 1.b). Onde for preta, mantenha o fundo preto (0). Exiba a interseccao visual final.

degrade = np.linspace(0,255,x,dtype=np.float32) #mudando pra float32 pra testar degrade mais suave
whiteGray= np.tile(degrade, (y, 1))
img_rgb = np.stack([whiteGray]*3, axis=2).astype(np.uint8)

mask = (img[:,:,0] > 200) & (img[:,:,1] > 200) & (img[:,:,2] > 200)
mask_rgb = np.stack([mask]*3, axis=2)

img_3 = img.copy()

img_3[mask_rgb] = img_rgb[mask_rgb]

plt.imshow(img_3) 

plt.title("Mesclagem")
plt.axis("off")
plt.show() 