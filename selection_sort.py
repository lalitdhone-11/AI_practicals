a=[7,5,4,9,2,10,3]
def selection_sort(a):
    for i in range(len(a)-1):
        min_idx=i
        for j in range(i,len(a)):
            if a[min_idx]>a[j]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
          
print("unsorted list:",a)
selection_sort(a)
print("sorted list:",a)