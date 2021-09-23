def  stupid_sort(liste):
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
            #yer değiştirme işleminden sonra başa dön
            i = 1
            

liste = [7,9,1,8,3]
stupid_sort(liste)
print(liste)
