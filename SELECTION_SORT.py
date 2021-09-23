


def selection_sort(liste):

    for i in range(len(liste)):

        minimum = i
        for j in range(i+1,len(liste)):

            if liste[j] < liste[minimum]:   
                minimum = j
        print(liste)
            
        liste[minimum] ,liste[i] =  liste[i], liste[minimum]


liste = [4,8,6,2,1,9,3]

selection_sort(liste)
print(liste)


