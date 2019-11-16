import numpy as np
import cv2 as cv

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Camera Indisponível")
    exit()

while True:
    _, quadro = camera.read()

    quadro_suavizado = cv.GaussianBlur(quadro,(5,5),0)
    #quadro_preto_e_branco = cv.cvtColor(quadro, cv.COLOR_BGR2GRAY)

    cv.imshow('imagem_suavizada', quadro_suavizado)
    cv.imshow('imagem', quadro)
    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()