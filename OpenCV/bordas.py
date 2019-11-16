import numpy as np
import cv2 as cv

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Camera Indisponível")
    exit()

while True:
    _, quadro = camera.read()

    quadro_suavizado = cv.GaussianBlur(quadro,(5,5),0)

    quadro_preto_e_branco_suavizado = cv.cvtColor(quadro_suavizado, cv.COLOR_BGR2GRAY)
    quadro_preto_e_branco = cv.cvtColor(quadro, cv.COLOR_BGR2GRAY)

    bordas =  cv.Canny(quadro_preto_e_branco,100,200)
    bordas_com_suavizacao =  cv.Canny(quadro_preto_e_branco_suavizado,100,200)


    cv.imshow('imagem_suavizada', bordas_com_suavizacao)
    cv.imshow('imagem', bordas)
    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()