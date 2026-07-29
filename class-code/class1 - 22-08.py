# -*- coding: utf-8 -*-
"""
@author: Edvonaldo Horácio (edvonaldo.santos@ifal.edu.br)

@description: Carregando imagem usando OpenCV

"""
import cv2 as cv

# Load the input image
img_clr = cv.imread('../imagens/baboon.jpg', cv.IMREAD_COLOR)
cv.imshow('Baboon Colorido', img_clr)
cv.waitKey(0)

img_gray = cv.imread('../imagens/baboon.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Baboon em Grayscale', img_gray)
cv.waitKey(0)

cv.destroyAllWindows()