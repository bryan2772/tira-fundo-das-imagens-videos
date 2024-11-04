from rembg import remove
import os
from PIL import Image

# Caminhos dos diretórios de entrada e saída
input_dir = '/mnt/nvme1n1p2/doc/Faculdade-BCC/BCC-8º periodo/jesga/trabalho1/ImagensPDI'
output_dir = '/mnt/nvme1n1p2/doc/Faculdade-BCC/BCC-8º periodo/jesga/trabalho1/results/'

# Certifica-se de que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Itera sobre todos os arquivos no diretório de entrada
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    
    # Verifica se o arquivo é uma imagem
    if filename.endswith((".png", ".jpg", ".jpeg")):
        # Abre a imagem
        imagem = Image.open(file_path)
        
        # Remove o fundo da imagem
        imagemremovida = remove(imagem)
        
        # Converte para RGB antes de salvar como JPEG
        imagemremovida = imagemremovida.convert("RGB")
        
        # Define o caminho completo para salvar a imagem processada
        output_path = os.path.join(output_dir, filename)
        
        # Salva a imagem sem o fundo
        imagemremovida.save(output_path)

print("Processamento concluído!")
