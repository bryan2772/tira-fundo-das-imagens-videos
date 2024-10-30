from rembg import remove
from PIL import Image
import os

# Diretórios de entrada e saída
input_dir = 'ImagensPDI/'  # Diretório das imagens de entrada
output_dir = 'resultados/'  # Diretório para salvar as imagens processadas

imagem = Image.open(input_dir)
imagemremovida = remove(imagem)

# Converte para RGB antes de salvar como JPEG
imagemremovida = imagemremovida.convert("RGB")
imagemremovida.save(output_dir)