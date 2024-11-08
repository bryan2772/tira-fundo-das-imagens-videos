# Importando as bibliotecas necessárias
import cv2
import numpy as np
import os

# Diretórios de entrada e saída
input_dir = 'ImagensPDI/'  # Diretório das imagens de entrada
output_dir = 'resultados/'  # Diretório para salvar as imagens processadas

# Função para remover fundo
def remover_fundo(imagem):
    # Passo 1: Converter a imagem para escala de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Passo 2: Aplicar suavização para reduzir ruído
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Passo 3: Aplicar limiarização para segmentação
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Passo 4: Refinamento com operações morfológicas
    kernel = np.ones((3, 3), np.uint8)
    morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Passo 5: Identificar contornos e criar máscara
    contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)
    
    # Passo 6: Aplicar a máscara para remover o fundo
    resultado = cv2.bitwise_and(imagem, imagem, mask=mask)
    
    return resultado

# Função principal para processar imagens no diretório
def processar_imagens():
    # Verificar se o diretório de saída existe, se não, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Processar cada imagem no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Carregar a imagem
            img_path = os.path.join(input_dir, filename)
            imagem = cv2.imread(img_path)
            
            # Remover o fundo
            imagem_processada = remover_fundo(imagem)
            
            # Salvar a imagem resultante no diretório de saída
            output_path = os.path.join(output_dir, f'processada_{filename}')
            cv2.imwrite(output_path, imagem_processada)
            
            print(f'Imagem {filename} processada e salva em {output_path}')

# Executando o código
if __name__ == "__main__":
    processar_imagens()
