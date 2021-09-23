def  gnome_sort(liste):
    if len(liste) <= 1:
        return liste
        
    i = 1
    
    while i < len(liste):
        if liste[i-1] <= liste[i]:
            # eğer listenin n elemanı n-1 . elemanından büyükse bir adım ilerle
            i += 1
        else:
            # eğer listenin n elemanı n-1 . elemanından büyük değilse yerlerini değiştir
            liste[i-1], liste[i] = liste[i],liste[i-1]
            #yer değiştirme işleminden sonra bir adım geriye git
            i -= 1
            if (i == 0):
                i = 1


liste = [7,9,1,8,3]
gnome_sort(liste)
print(liste)

