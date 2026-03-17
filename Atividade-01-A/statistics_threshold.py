#3 - calculos estatisticos e limiarizacao (statistics)
    #Media e Gray
import os
import numpy as np
import matplotlib.pyplot as plt

path = "img/q2_a_original.png"
img= plt.imread(path)

#media dos canais
media_canais = np.mean(img, axis=2)#como pedido
print("Média dos Canais:", media_canais)

#conversão
img_gray_uint8 = (media_canais * 255).astype(np.uint8)#converte para uint8
plt.imshow(img_gray_uint8, cmap='gray') 
plt.title("colormap cinza.")
plt.axis("off") #deixa so imagem
plt.show()



output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  

plt.imsave(os.path.join(output_folder, "question_3_MediaGray.png"), img_gray_uint8)