

def bubble_sort(liste): 
  
    # Traverse through all array elements 
    for i in range(len(liste)): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, len(liste)-i-1): # neden -1 yapıyoruz anlamadım????
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if liste[j] > liste[j+1] : 
                liste[j], liste[j+1] = liste[j+1], liste[j] 




"""def bubble_sort2(liste):

    for i in range(len(liste)):

        for j in range(len(liste)-i):
            if liste[i] > liste[i+1]:
                liste[i],liste[i+1] = liste[i+1],liste[i]

"""
liste = [7,3,5,8,2,9,4,15,6]
bubble_sort(liste)
print(liste)
    

 
