from PIL import Image

def zlicz_piksele(obraz, kolor):
    # Rozpakuj kolor na składowe RGB
    r, g, b = kolor
    licznik = 0
    
    # Przechodzimy po wszystkich pikselach w obrazie
    for y in range(obraz.height):
        for x in range(obraz.width):
            # Pobieramy kolor piksela (r, g, b)
            pixel = obraz.getpixel((x, y))
            # Sprawdzamy, czy pixel ma taki sam kolor jak szukany
            if pixel == (r, g, b):
                licznik += 1
    
    return licznik

# Przykładowe użycie
obraz = Image.open('obraz.jpg')
kolor = (155, 155, 155)
liczba_pikseli = zlicz_piksele(obraz, kolor)
print(f"Liczba pikseli o kolorze {kolor}: {liczba_pikseli}")
