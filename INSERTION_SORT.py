def insertion_sort(liste):

    for i in range(len(liste)):

        n = liste[i]
        j = i-1
        while j>=0 and n < liste[j]:
            liste[j+1] = liste[j]
            j-=1
        liste[j+1] = n 
            

      
               
               







def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 


liste = [7,3,5,8,2,9,4,15,6]
insertion_sort(liste)
print(liste)



