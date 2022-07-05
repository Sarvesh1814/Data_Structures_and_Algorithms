def insertion_sort(elements):
    for i in range(1,len(elements)):
        pointerA = elements[i]
        j=i-1
        while j >=0 and pointerA < elements[j]:
            elements[j+1] = elements[j]
            j=j-1
        elements[j+1] = pointerA
    return elements

def insert_elements():
    global ll
    ll = []
    count = 0
    while True:
        i = int(input("Enter element: "))
        ll.append(i)
        insertion_sort(ll)
        find_median(ll,count)
        count+=1

def find_median(elements,count):
    if count== 0:
        print("median of",elements,": ",elements[0])    
    if count%2==1:
        a= int((count/2)+0.5)
        b= int(count//2)
        print("median of",elements,": ",(((elements[b]+elements[a])/2)))
        
    elif count%2==0 and count>0:
        a=int(count/2)
        print("median of",elements,": ",elements[a])    
    

insert_elements()