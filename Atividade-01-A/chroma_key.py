#4 - Chroma Key
    #isolamento

import os
import numpy as np
import matplotlib.pyplot as plt

path = "img/q2_a_original.png"
img = plt.imread(path)

ceu_rgb = np.array([135, 206, 235]) / 255.0
tolerancia = 0.05 # 5% de tolerancia  no valor acima quanto maior mais pixels longe do valor atual de rgb informado ele vai pegar
 
mask_ceu = (np.abs(img[:,:,0] - ceu_rgb[0]) <= tolerancia) & (np.abs(img[:,:,1] - ceu_rgb[1]) <= tolerancia) & (np.abs(img[:,:,2] - ceu_rgb[2]) <= tolerancia)

plt.imshow(mask_ceu, cmap='gray')
plt.title("Máscara do Céu Azul")
plt.axis("off")
plt.show()


output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  
print("Imagens salvas na pasta:", output_folder)
plt.imsave(os.path.join(output_folder, "question_4_FatiamentoCeu.png"), mask_ceu)