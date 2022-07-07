"""Using Figure 2.2 illustrate the operation of insertion-sort on the array A = [31,41,59,26,41]"""

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]


        while list_a[i-1] > value_to_sort and i >0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1
        

    


    print(list_a)

insertion_sort(list_a = [31,41,59,26,41])

            
            # list_a = [ 31, 41, 59, 26, 41 ]
