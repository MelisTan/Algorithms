

  
def oddevenSort(liste):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(liste) - 1, 2):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                sorted = False
        for i in range(1, len(liste) - 1, 2):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                sorted = False
    return liste

liste = [5,7,8,6,3,1,4,2]
oddevenSort(liste)
print(liste)
