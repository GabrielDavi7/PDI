#4 - Chroma Key
    #isolamento

import os
import numpy as np
import matplotlib.pyplot as plt

path = "img/q2_a_original.png"
img = plt.imread(path)

if img.shape[-1] == 4: #tirando o alfa
    img = img[:, :, :3]

ceu_rgb = np.array([135, 206, 235]) / 255.0
tolerancia = 0.05 # 5% de tolerancia no valor acima, quanto maior mais pixels longe do valor atual de rgb informado ele vai pegar
 
mask_ceu = (np.abs(img[:,:,0] - ceu_rgb[0]) <= tolerancia) & (np.abs(img[:,:,1] - ceu_rgb[1]) <= tolerancia) & (np.abs(img[:,:,2] - ceu_rgb[2]) <= tolerancia)

plt.imshow(mask_ceu, cmap='gray')
plt.title("Mask do Céu Azul")
plt.axis("off")
plt.show()


    #Novo fundo
    
y, x, canais = img.shape

new_fundo = np.zeros(img.shape, dtype=img.dtype) # Cria a tela preta

# Linha do degradê: começa no Azul Escuro (0.6) e vai até o Preto (0.0) na largura (x)
coluna_degrade = np.linspace(0.0, 0.6, y).reshape(-1, 1)
matriz_degrade = np.tile(coluna_degrade, (1,x))

new_fundo[:, :, 2] = matriz_degrade #aplica degrade somente no rgb azul  

plt.imshow(new_fundo)
plt.title("Novo Fundo (Azul Escuro para Preto)")
plt.axis("off")
plt.show()


output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  
print("Imagens salvas na pasta:", output_folder)
plt.imsave(os.path.join(output_folder, "question_4_FatiamentoCeu.png"), mask_ceu)
plt.imsave(os.path.join(output_folder, "question_4_NovoFundo.png"), new_fundo)

