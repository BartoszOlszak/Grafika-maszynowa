from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

#zadanie 6

def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        return "obrazy nie są identyczne, bo obrazy mają inny tryb"
    if obraz1.size != obraz2.size:
        return "obrazy nie są identyczne, bo obrazy mają inny rozmiar"
    obraz1_np = np.array(obraz1)
    obraz2_np = np.array(obraz2)

    w, h = obraz1.size # juz sprawdzone czy rozmiary sa identyczne

    for i in range(w):
        for j in range(h):
            if not np.array_equal(obraz1_np[j][i], obraz2_np[j][i]):
                return "obrazy nie są identyczne, bo obrazy mają inne piksele"

    return "obrazy sa identyczne"

beksinki1 = Image.open('beksinski1.png')
beksinki2 = Image.open('beksinski2.png')
beksinki3 = Image.open('beksinski3.png')

#print(ocen_czy_identyczne(beksinki1, beksinki2))
#print(ocen_czy_identyczne(beksinki1, beksinki3))
#print(ocen_czy_identyczne(beksinki2, beksinki3))
#print(ocen_czy_identyczne(beksinki1, beksinki1))
#print(ocen_czy_identyczne(beksinki2, beksinki2))
#print(ocen_czy_identyczne(beksinki3, beksinki3))













