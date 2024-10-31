from ultralytics import YOLO
import cv2
import numpy as np

# Inicialize o objeto de captura de vídeo
cap = cv2.VideoCapture(0)

# Carrega o modelo YOLO
model = YOLO("yolov8x-seg.pt")

while True:
    success, img = cap.read()
    if success:
        # Realiza a segmentação e detecção com YOLO no quadro original
        results = model.track(img, persist=True)

        # Cria uma máscara vazia para armazenar as detecções
        combined_mask = np.zeros(img.shape[:2], dtype=np.uint8)

        for result in results:
            if result.masks is not None:  # Verifica se a segmentação de máscara está presente
                for cls, conf, mask in zip(result.boxes.cls, result.boxes.conf, result.masks.data):
                    # Converte a máscara de tensor para um array NumPy
                    mask_np = mask.cpu().numpy()  # Converte de tensor para NumPy

                    # Adiciona a máscara para qualquer classe detectada com confiança > 0.63
                    if conf > 0.63:
                        combined_mask = cv2.bitwise_or(combined_mask, mask_np.astype(np.uint8) * 255)

        # Converte a imagem original para escala de cinza
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("Imagem convertida para escala de cinza.")

        # Exibe a imagem em escala de cinza
        cv2.imshow("Imagem em Escala de Cinza", gray_img)

        # Aplica a máscara para remover o fundo do quadro original colorido
        masked_img = cv2.bitwise_and(img, img, mask=combined_mask)

        # Exibe a imagem segmentada
        cv2.imshow("Segmented Objects", masked_img)


    # Detecta se a tecla 'q' foi pressionada para fechar
    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Tecla pressionada")
        break

cap.release()
cv2.destroyAllWindows()
