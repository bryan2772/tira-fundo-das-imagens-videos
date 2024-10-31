# -*- coding: cp1252 -*-
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

import cv2
import numpy as np

class GrabCutGUI(Frame):
    def __init__(self, master=None):
        # Invoca o construtor da classe pai Frame
        Frame.__init__(self, master)

        # Inicializar a interface gráfica
        self.iniciaUI()

    def iniciaUI(self):
        # Preparando a janela
        self.master.title("Janela da Imagem Segmentada")
        self.pack()

        # Computa ações de mouse
        self.computaAcoesDoMouse()

        # Carregando a imagem do disco
        self.imagem = self.carregaImagemASerExibida()

        # Criar um canvas que receberá a imagem
        self.canvas = Canvas(self.master, width=self.imagem.width(), height=self.imagem.height(), cursor="cross")

        # Desenhar a imagem no canvas
        self.canvas.create_image(0, 0, anchor=NW, image=self.imagem)
        self.canvas.image = self.imagem  # Previne que a imagem seja removida pelo garbage collector

        # Posiciona todos os elementos no canvas
        self.canvas.pack()

    def computaAcoesDoMouse(self):
        self.startX = None
        self.startY = None
        self.rect = None
        self.rectangleReady = None
        
        self.master.bind("<ButtonPress-1>", self.callbackBotaoPressionado)
        self.master.bind("<B1-Motion>", self.callbackBotaoPressionadoEmMovimento)
        self.master.bind("<ButtonRelease-1>", self.callbackBotaoSolto)

    def callbackBotaoSolto(self, event):
        if self.rectangleReady:
            # Criar uma nova janela
            windowGrabcut = Toplevel(self.master)
            windowGrabcut.wm_title("Segmentation")
            windowGrabcut.minsize(width=self.imagem.width(), height=self.imagem.height())

            # Criar canvas para essa nova janela
            canvasGrabcut = Canvas(windowGrabcut, width=self.imagem.width(), height=self.imagem.height())
            canvasGrabcut.pack()

            # Aplicar GrabCut na imagem
            mask = np.zeros(self.imagemOpenCV.shape[:2], np.uint8)
            rectGcut = (int(self.startX), int(self.startY), int(event.x - self.startX), int(event.y - self.startY))
            fundoModel = np.zeros((1, 65), np.float64)
            objModel = np.zeros((1, 65), np.float64)

            # Invocar GrabCut
            cv2.grabCut(self.imagemOpenCV, mask, rectGcut, fundoModel, objModel, 5, cv2.GC_INIT_WITH_RECT)

            # Preparando imagem final
            maskFinal = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            imgFinal = self.imagemOpenCV * maskFinal[:, :, np.newaxis]
            for x in range(self.imagemOpenCV.shape[1]):
                for y in range(self.imagemOpenCV.shape[0]):
                    if maskFinal[y][x] == 0:
                        imgFinal[y][x][:] = 255 

            # Converter de volta do OpenCV para Tkinter
            imgFinal = cv2.cvtColor(imgFinal, cv2.COLOR_BGR2RGB)
            imgFinal = Image.fromarray(imgFinal)
            imgFinal = ImageTk.PhotoImage(imgFinal)

            # Inserir a imagem segmentada no canvas
            canvasGrabcut.create_image(0, 0, anchor=NW, image=imgFinal)
            canvasGrabcut.image = imgFinal          

    def callbackBotaoPressionadoEmMovimento(self, event):
        # Novas posições de x e y
        currentX = self.canvas.canvasx(event.x)
        currentY = self.canvas.canvasy(event.y)

        # Atualiza o retângulo a ser desenhado
        self.canvas.coords(self.rect, self.startX, self.startY, currentX, currentY)

        # Verifica se existe retângulo desenhado
        self.rectangleReady = True

    def callbackBotaoPressionado(self, event):
        # Convertendo o x do frame para o x do canvas e copiando isso em startX
        self.startX = self.canvas.canvasx(event.x)
        self.startY = self.canvas.canvasy(event.y)

        if not self.rect:
            self.rect = self.canvas.create_rectangle(0, 0, 0, 0, outline="blue")

    def carregaImagemASerExibida(self):
        caminhoDaImagem = filedialog.askopenfilename()

        # Se a imagem existir, entra no if
        if caminhoDaImagem:
            self.imagemOpenCV = cv2.imread(caminhoDaImagem)

            # Redimensiona a imagem para caber na tela
            max_width = self.master.winfo_screenwidth() - 100
            max_height = self.master.winfo_screenheight() - 100

            h, w = self.imagemOpenCV.shape[:2]
            scaling_factor = min(max_width / w, max_height / h)
            new_size = (int(w * scaling_factor), int(h * scaling_factor))

            self.imagemOpenCV = cv2.resize(self.imagemOpenCV, new_size)

            # Converte de OpenCV para PhotoImage
            image = cv2.cvtColor(self.imagemOpenCV, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            return image

def main():
    # Inicializa o Tkinter
    root = Tk()

    # Cria a aplicação
    appcut = GrabCutGUI(master=root)

    # Cria o loop do programa
    appcut.mainloop()

if __name__ == "__main__":
    main()
