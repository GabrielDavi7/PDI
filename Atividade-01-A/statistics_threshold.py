#3 - calculos estatisticos e limiarizacao (statistics)
    #Media e Gray
import os
import numpy as np
import matplotlib.pyplot as plt

output_folder = "save_replies_image"
os.makedirs(output_folder, exist_ok=True)  
path = "img/q2_a_original.png"
img = plt.imread(path)

    # Media dos canais e converte para cinza
media_canais = np.mean(img, axis=2)
img_gray_uint8 = (media_canais * 255).astype(np.uint8)

plt.imshow(img_gray_uint8, cmap='gray') 
plt.title("Imagem em tons de cinza")
plt.axis("off")
plt.show()

    #Media e plotar histograma
media_total = np.mean(img_gray_uint8)
print("Média total:", media_total)

plt.figure(figsize=(8,5))
plt.hist(img_gray_uint8.flatten(), bins=255, range=(0,255), color='gray')
plt.title(f"Histograma da imagem em tons de cinza: {media_total:.2f}")
plt.xlabel("Intensidade")
plt.ylabel("Número de pixels")
plt.savefig(os.path.join(output_folder, "question_3_HistogramaMedia.png"))
plt.show()
plt.close()  # fecha a figura


    #Limiarizacao Analitica Automatica:

# Criar máscara binária usando a média como threshold
mask = np.zeros_like(img_gray_uint8, dtype=np.uint8)

# Define pixels acima ou igual à média como 255 (branco)
mask[img_gray_uint8 >= media_total] = 255

plt.imshow(mask, cmap='gray')
plt.title(f"Limiarização automática (Threshold = {media_total:.2f})")
plt.axis('off')
plt.show()


#salva imagem

plt.imsave(os.path.join(output_folder, "question_3_MediaGray.png"), img_gray_uint8, cmap='gray')
plt.imsave(os.path.join(output_folder, "question_3_Threshold.png"), mask)