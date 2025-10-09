from PIL import Image
import numpy as np

# zadanie1

inicjaly = Image.open("inicjaly.bmp")

#zadanie2

print("---------- informacje o obrazie")
print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)

#zadanie3

dane_inicjaly = np.asarray(inicjaly) #wczytanie tablicy true/false
dane_inicjaly1 = dane_inicjaly.astype(np.uint8)  #to zmienia na tablice 0/1
print(dane_inicjaly1)
t1_text = open('t1.txt', 'w')
for rows in dane_inicjaly1:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')
t1_text.close()

#zadanie4

print("pixel 50 30:", dane_inicjaly[30][50]) # tutaj na odwrot bo z tablicy piew wczytujemy wysokosc
print("pixel 90 40:", dane_inicjaly[40][90])
print("pixel 0 99:", dane_inicjaly[0][99])

#zadanie5

