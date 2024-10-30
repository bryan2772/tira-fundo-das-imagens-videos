from rembg import remove
from PIL import Image
import os

# Diretórios de entrada e saída
input_dir = 'ImagensPDI/'  # Diretório das imagens de entrada
output_dir = 'resultados/'  # Diretório para salvar as imagens processadas

# Verifica se o diretório de saída existe; se não, cria-o
os.makedirs(output_dir, exist_ok=True)

# Itera sobre todos os arquivos do diretório de entrada
for filename in os.listdir(input_dir):
    # Verifica se o arquivo é uma imagem
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Caminho completo da imagem de entrada e de saída
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Carrega a imagem e remove o fundo
        imagem = Image.open(input_path)
        imagemremovida = remove(imagem)

        # Converte para RGB antes de salvar como JPEG
        imagemremovida = imagemremovida.convert("RGB")
        imagemremovida.save(output_path)

        print(f'Imagem {filename} processada e salva em {output_path}')
