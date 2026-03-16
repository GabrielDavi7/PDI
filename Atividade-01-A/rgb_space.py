#2 - Brincando com Canais de Cor(RGB Space)
    #Leitura

import matplotlib.pyplot as plt
import numpy as np
import os

path = "img/q2_a_original.png"

img_alfa = plt.imread(path)
print("Shape original:", img_alfa.shape)
plt.imshow(img_alfa) 
plt.title("Com Alfa")
plt.axis("off")
plt.show()

if img_alfa.shape[-1] == 4: #tirando alfa
    img_NoAlfa = img_alfa[:, :, :3] #tira do alfa
else:
    img_NoAlfa = img_alfa

print("Shape final (RGB):", img_NoAlfa.shape)

plt.imshow(img_NoAlfa) 
plt.title("Sem Alfa")
plt.axis("off")
plt.show()

    #Invert RGB com fatiamento

img_invert = img_NoAlfa.copy()#copia imagem

img_invert[:, :, [0, 2]] = img_invert [:,:,[2,0]] #troca o vermelho pelo azul se fosse trocar vende teriamos que pegar o valor 1

plt.imshow(img_invert)
plt.title("R e B Invert (fatiamento)")
plt.axis("off")
plt.show()


    #Big Red copia foto original(com alfa)

img_red_filter = img_alfa.copy()
img_red_filter[:, :, [1,2]] = 0 #zera verde e azul

plt.imshow(img_red_filter)
plt.title("Filter Red")
plt.axis("off")
plt.show()


#Salva imagens
output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  

plt.imsave(os.path.join(output_folder, "question_2_Alfa.png"), img_alfa)
plt.imsave(os.path.join(output_folder, "question_2_NoAlfa.png"), img_NoAlfa)
plt.imsave(os.path.join(output_folder, "question_2_InvertRGB.png"), img_invert)
plt.imsave(os.path.join(output_folder, "question_2_RedFilter.png"), img_red_filter)

print("Imagens salvas na pasta:", output_folder)