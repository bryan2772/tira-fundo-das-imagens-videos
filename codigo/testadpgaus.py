# %%
# Importando as bibliotecas necessárias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread("../ImagensPDI/stockvault-bulb128619.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb, cmap='gray')
plt.axis("off")
plt.show()

# %%
# Converter para escala de cinza
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.show()

# %%
# Aplicar a limiarização adaptativa para obter uma máscara inicial
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 3)
plt.imshow(thresh, cmap='gray')
plt.axis("off")
plt.show()

# %%
# Inverter a máscara para que o objeto fique branco e o fundo preto
mask = cv2.bitwise_not(thresh)
plt.imshow(mask, cmap='gray')
plt.axis("off")
plt.show()

# %%
# Remover pequenos ruídos e suavizar a máscara com operações de morfologia
kernel = np.ones((5,5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
mask = cv2.GaussianBlur(mask, (7, 7), 0)

# %%
# Identificar contornos e criar uma máscara refinada
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask_refined = np.zeros_like(mask)
cv2.drawContours(mask_refined, contours, -1, (255), thickness=cv2.FILLED)
plt.imshow(mask_refined, cmap='gray')
plt.axis("off")
plt.show()

# %%
# Converter a máscara refinada para 3 canais para aplicá-la na imagem colorida
mask_rgb = cv2.cvtColor(mask_refined, cv2.COLOR_GRAY2RGB)

# Aplicar a máscara refinada na imagem original para manter apenas o objeto
foreground = cv2.bitwise_and(rgb, mask_rgb)

# Definir o fundo como branco ou preto
background = np.full_like(rgb, 255)  # Fundo branco
final_image = np.where(mask_rgb == 0, background, foreground)

# Exibe a imagem original e a imagem segmentada
plt.subplot(1, 2, 1)
plt.title("Imagem Original")
plt.imshow(rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Imagem Segmentada (Fundo Removido)")
plt.imshow(final_image)
plt.axis("off")

plt.show()
