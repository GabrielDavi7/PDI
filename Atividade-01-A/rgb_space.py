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

output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  

plt.imsave(os.path.join(output_folder, "question_2_Alfa.png"), img_alfa)
plt.imsave(os.path.join(output_folder, "question_2_NoAlfa.png"), img_NoAlfa)


print("Imagens salvas na pasta:", output_folder)