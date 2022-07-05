def insertion_sort(elements):
    for i in range(1,len(elements)):
        pointerA = elements[i]
        j=i-1
        while j >=0 and pointerA < elements[j]:
            elements[j+1] = elements[j]
            j=j-1
        elements[j+1] = pointerA
    return elements

tests = [[2, 1, 5, 7, 2, 0, 5]]

for i in tests:
    print("Unsorted Array ", i)
    print("Sorted Array ",insertion_sort(i))