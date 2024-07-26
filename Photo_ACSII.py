import os
from PIL import Image
import numpy as np
import time




def Img_Convert(path):
    try:
        img_gray_scale_matrix = np.array(Image.open(path).convert("L").resize((96,54)))
        file = open("resultado_Impreso","a")
        file.write("\n")
        for i in img_gray_scale_matrix:
            for j in i:
                if j<51:
                    file.write("*")
                    print("*", end = "")
                elif j>=51 and j<102:
                    file.write("+")
                    print("+", end = "")
                elif j >=102 and j<153:
                    file.write("-")
                    print("-", end = "" )
                elif j>=153 and j < 204:
                    file.write(".")
                    print(".",end="")
                else:
                    file.write(" ")
                    print(" ",end="")
            print("")
            file.write("\n")


        file.close()



    except IsADirectoryError:
        print("Esta no es una direccion valida")


def main():

    opc = 0

    while opc != 2:

        print("======================================================")
        print("=                                                    =")
        print("=  1-Transofrmar Imagen (preferible en blanco/negro) =")
        print("=                                                    =")
        print("======================================================")
        print("=                                                    =")
        print("=  2-Salir                                           =")
        print("=                                                    =")
        print("======================================================")
        print("=                                                    =")
        print("=                   .:Created by:                    =")
        print("=                         BlitzKriegCod:.            =")
        print("=                                                    =")
        print("======================================================")
        print("\n")
        print("Inserte una opcion: ",end="")



        opc = int(input())

        match opc:
            case 1:
                print("\n")
                print("Inserte la direccion de la imagen /algun_lugar/img.ext:",end = "")
                Img_Convert(input())
            case _:
                for i in "Wey son dos opciones o uno o 2":
                    time.sleep(0.1)
                    print(i,end = '')
                _=os.system("clear")


if __name__ == "__main__":
    main()


