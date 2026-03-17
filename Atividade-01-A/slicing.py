#1 - fatiamento (slicing)
    #mascara
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#Gere uma imagem de 200 × 200 pixels com o fundo totalmente preto (valor 0)
img_1a = np.zeros((200,200,3), dtype=np.uint8)

#ex: matriz[50:150, 50:150] e quadrado branco valor = 255
img_1a[50:150, 50:150] = [255,255,255]

#mostrar imagem
plt.imshow(img_1a) 
plt.title("mask")
plt.axis("off") #deixa so imagem
plt.show() #imprime tela


     #degrade

#imagem 200 × 200, desta vez contendo um degrade horizontal, indo do lado preto (0) na esquerda ate branco (255) na direita.

y,x = 200,200
degrade = np.linspace(0,255,x,dtype=np.uint8) #0,255 para sair de preto e ir a branco passa x pq é horizontal

img_gray = np.tile(degrade, (y, 1))
img_1b = np.stack([img_gray]*3, axis=2)

plt.imshow(img_1b) 
plt.title("Degrade")
plt.axis("off") #deixa so imagem
plt.show() 


    #Merging

#Utilize a funcao np.where(ou multiplicacao de matrizes divididas por 255) para combinar as duas imagens. 
# A regra e: onde a Imagem 1a for branca (255), mostre odegrade (Imagem 1.b). Onde for preta, mantenha o fundo preto (0). Exiba a interseccao visual final.
img_1c = np.where(img_1a == 255, img_1b, 0).astype(np.uint8)

plt.imshow(img_1c) 
plt.title("Mesclagem")
plt.axis("off")
plt.show()

#salva imagem
output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  

plt.imsave(os.path.join(output_folder, "question_1_Maks_IMG.png"), img_1a)
plt.imsave(os.path.join(output_folder, "question_1_Degrade_IMG.png"), img_1b)
plt.imsave(os.path.join(output_folder, "question_1_Merging_IMG.png"), img_1c)

