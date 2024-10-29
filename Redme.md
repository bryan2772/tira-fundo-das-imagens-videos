
# Projeto de Remoção de Fundo em Imagens

## Descrição do Projeto
Este projeto visa desenvolver um algoritmo capaz de remover o fundo de imagens automaticamente, aplicando técnicas de processamento em escala de cinza para facilitar a segmentação. O objetivo é criar um método robusto que possa identificar o fundo e removê-lo, deixando apenas os objetos de interesse na imagem. Os resultados serão apresentados em uma sessão de teste marcada para o dia 04/11.

## Objetivos Específicos
1. Converter as imagens originais para escala de cinza.
2. Aplicar uma técnica de segmentação que identifique o primeiro plano e o fundo.
3. Ajustar o contraste e brilho para aprimorar a separação entre objeto e fundo.
4. Remover o fundo das imagens selecionadas.
5. Demonstrar os resultados obtidos.

## Passo a Passo do Algoritmo

1. **Carregar as Imagens**: Utilizar uma biblioteca como OpenCV ou PIL para carregar as imagens originais.

2. **Converter para Escala de Cinza**:
    - Transformar cada imagem em tons de cinza para simplificar o processamento.

3. **Aplicar Filtro de Suavização (Opcional)**:
    - Aplicar um filtro de suavização, como o GaussianBlur, para reduzir o ruído que possa dificultar a segmentação.

4. **Segmentação do Objeto de Interesse**:
    - Utilizar técnicas como limiarização (thresholding) para distinguir o objeto do fundo, ajustando os valores para captar o contraste desejado.
    - Alternativamente, o algoritmo Canny pode ser usado para detectar bordas e identificar contornos.

5. **Refinamento com Morfologia (Opcional)**:
    - Aplicar operações morfológicas (dilatação ou erosão) para melhorar o contorno do objeto e assegurar que o fundo seja bem isolado.

6. **Remover o Fundo**:
    - Com base na máscara criada, remover ou reduzir a visibilidade do fundo, mantendo apenas o objeto de interesse na imagem final.

7. **Salvar e Exibir os Resultados**:
    - Salvar as imagens com o fundo removido e exibi-las para verificação.

## Ferramentas Necessárias
- **Python 3.x**
- **Biblioteca OpenCV** para manipulação e processamento de imagens.
- **Biblioteca NumPy** para manipulação de matrizes e operações matemáticas.

## Como Executar o Código
1. Certifique-se de que Python e as bibliotecas necessárias estão instaladas.
2. Execute o código principal (ex: `remocao_fundo.py`), que executará as etapas do algoritmo descrito.
3. Revise as imagens resultantes para verificar a remoção de fundo.

## Estrutura de Arquivos
- `imagens/`: Contém as imagens de entrada para o processamento.
- `resultados/`: Diretório onde serão salvas as imagens processadas com o fundo removido.
- `remocao_fundo.py`: Script principal contendo o código para remoção de fundo.

