from rembg import remove
from PIL import Image
import os
import matplotlib.pyplot as plt

# Diretórios de entrada e saída
input_dir = 'ImagensPDI/'  # Diretório das imagens de entrada
output_dir = 'resultados/'  # Diretório para salvar as imagens processadas

# Verifica se o diretório de saída existe; se não, cria-o
os.makedirs(output_dir, exist_ok=True)

# Itera sobre todos os arquivos do diretório de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Carrega a imagem e converte para escala de cinza
        imagem = Image.open(input_path).convert("L")
        plt.imshow(imagem, cmap='gray')
        plt.title(f"Imagem em Cinza: {filename}")
        plt.axis('off')
        plt.show()

        # Remove o fundo
        imagemremovida = remove(imagem)
        plt.imshow(imagemremovida)
        plt.title(f"Imagem sem Fundo: {filename}")
        plt.axis('off')
        plt.show()

        # Converte para RGB e exibe colorida
        imagemremovida_rgb = imagemremovida.convert("RGB")
        plt.imshow(imagemremovida_rgb)
        plt.title(f"Imagem Colorida Final: {filename}")
        plt.axis('off')
        plt.show()

        # Salva a imagem final sem fundo em RGB
        imagemremovida_rgb.save(output_path)
        print(f'Imagem {filename} processada e salva em {output_path}')
