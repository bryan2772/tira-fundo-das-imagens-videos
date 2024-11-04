# Projeto de Remoção de Fundo em Imagens e Vídeos

## Autores: Ryan Alves e Victoria Moraes

## Descrição do Projeto
Este projeto aplica e compara diversas técnicas de segmentação para remoção automática de fundo em imagens e vídeos, destacando objetos de interesse. Foram implementadas cinco abordagens principais: YOLO, rembg, GrabCut, limiarização adaptativa e limiarização simples. Os métodos foram testados em diferentes condições, incluindo a remoção de fundo em tempo real com YOLO, que apresentou o melhor desempenho.

## Objetivos Específicos
1. Implementar diferentes métodos de segmentação para remover fundos de imagens e vídeos.
2. Comparar a eficácia de cada método em termos de precisão e qualidade visual.
3. Apresentar os resultados obtidos, destacando as vantagens e limitações de cada técnica.

## Explicação de Cada Código

### 1. **Código com YOLO para Remoção de Fundo em Tempo Real**
   - **Descrição**: Utiliza o modelo YOLO para segmentação em tempo real, detectando e isolando objetos enquanto o vídeo é capturado.
   - **Processo**: Cada quadro de vídeo é analisado em tempo real, com YOLO identificando objetos e aplicando uma máscara que remove o fundo.
   - **Vantagens**: Alta precisão e capacidade de segmentação dinâmica em vídeos ao vivo.
   - **Limitações**: Exige mais recursos computacionais, especialmente em dispositivos de menor capacidade.

### 2. **Código com rembg**
   - **Descrição**: O `rembg` usa redes neurais para segmentação, projetado para separar o primeiro plano do fundo em imagens estáticas.
   - **Processo**: As imagens são enviadas ao `rembg`, que retorna uma versão da imagem sem o fundo.
   - **Vantagens**: Boa precisão e rápido em imagens estáticas com fundos uniformes.
   - **Limitações**: Pode ter dificuldade em imagens com baixo contraste entre o objeto e o fundo.

### 3. **Código com GrabCut**
   - **Descrição**: GrabCut usa um modelo de cores para segmentação, ideal para isolar objetos com contornos bem definidos.
   - **Processo**: Após uma máscara preliminar, o algoritmo refina a segmentação com iterações para isolar o objeto de interesse.
   - **Vantagens**: Boa qualidade de segmentação com ajustes manuais mínimos.
   - **Limitações**: Pode requerer ajuste inicial para definir o objeto de interesse.

### 4. **Código com Limiarização Adaptativa**
   - **Descrição**: Técnica que aplica limiares locais para segmentação, ideal para lidar com iluminação variada.
   - **Processo**: Cada imagem é convertida para tons de cinza, e limiares adaptativos são aplicados para separar o objeto do fundo.
   - **Vantagens**: Simples e rápido, adequado para imagens com contrastes médios.
   - **Limitações**: Menor precisão para objetos complexos ou detalhes finos.

### 5. **Código com Limiarização Simples**
   - **Descrição**: Técnica básica que usa um único limiar para separar o objeto do fundo em imagens de alto contraste.
   - **Processo**: Aplicação direta de um valor de limiar em escala de cinza para obter uma máscara binária.
   - **Vantagens**: Rápido e direto, bom para objetos com contrastes definidos.
   - **Limitações**: Eficácia limitada em imagens com baixa diferença entre objeto e fundo.

## Comparação dos Resultados
Após testes, o método com YOLO em tempo real apresentou o melhor desempenho em precisão e adaptabilidade a diferentes cenários. O `rembg` foi eficaz para imagens estáticas com planos de fundo simples, enquanto o GrabCut forneceu segmentações precisas com ajustes mínimos. As técnicas de limiarização apresentaram resultados mais limitados e são recomendadas para casos com contraste elevado entre objeto e fundo.

### Conclusão
A técnica com YOLO é ideal para aplicações que exigem alta precisão e segmentação em tempo real. `rembg` e GrabCut representam alternativas eficazes para imagens estáticas. As técnicas de limiarização são opções rápidas para cenários com contraste bem definido.

## Ferramentas Necessárias
- **Python 3.8.18**
- **OpenCV** para processamento de imagem e vídeo.
- **NumPy** para operações com arrays.
- **YOLO** e **rembg** para segmentação baseada em IA.

## Como Executar o Código
1. Certifique-se de que Python e as bibliotecas necessárias estão instaladas.
2. Execute os scripts:
   - `main.ipynb`: Script de remoção de fundo em imagens e vídeos.
   - `grab2.py`: Script com a técnica GrabCut.
   - `rembgtest.py`: Script que utiliza a biblioteca rembg.
   - `removefundovideo.py`: Script para remoção de fundo em vídeos usando YOLO em tempo real.
3. Revise os resultados para verificar a eficácia de cada método.

## Estrutura de Arquivos
- `ImagensPDI/`: Contém as imagens de entrada para processamento.
- `resultado/`: Diretório para as imagens e vídeos processados com fundo removido.
- `main.ipynb`: Script principal para análise de imagens e vídeos.
- `grab2.py`: Script específico para remoção de fundo com GrabCut.
- `rembgtest.py`: Script específico para remoção de fundo com `rembg`.
- `removefundovideo.py`: Script específico para remoção de fundo em tempo real com YOLO.
