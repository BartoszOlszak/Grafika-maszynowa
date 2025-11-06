from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


im = Image.open('obraz.png')
print("tryb obraz.png:", im.mode)


def statystyki(im1):
    s = stat.Stat(im1)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


def rysuj_histogram_rgb(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


def rysuj_histogram_l(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:])
    plt.show()

# zadanie 1a

#rysuj_histogram_rgb(im)

r, g, b = im.split()

#rysuj_histogram_l(r)
#rysuj_histogram_l(g)
#rysuj_histogram_l(b)

#zadanie 1b

hist = im.histogram()
a = 155
print("kanał r ", hist[a])
print("kanał g ", hist[a+256])
print("kanał b ", hist[a+2*256])

# zadanie 1c

def zlicz_piksele(obraz, kolor):


