from re import L


def Binary_search_recursive(list_numbers,find_number,start,end):
   
    if start<=end:
        Mid_index = (start+end)//2
        if list_numbers[Mid_index]== find_number:
            return Mid_index+1
        if find_number>list_numbers[Mid_index]:
            start=Mid_index+1
            return Binary_search_recursive(list_numbers,find_number,start,end)
        if find_number< list_numbers[Mid_index]:
            end=Mid_index-1
            return Binary_search_recursive(list_numbers,find_number,start,end)
    return None

def Binary_search(list_numbers,find_numbers):
    start=0
    end= len(list_numbers)-1
    while start<=end:
        Mid_index= (start+end)//2
        if list_numbers[Mid_index]== find_numbers:
            return Mid_index+1
        if list_numbers[Mid_index]< find_numbers:
            start= Mid_index+1
        else:
            end= Mid_index-1
    return None

def Binary_search_AllOccurances(list_numbers,find_numbers):
    l=[]
    index = Binary_search(list_numbers,find_numbers)
    i=index-1
    while i >=0:
        if list_numbers[i]== find_numbers:
            l.append(i+1)
            i=i-1
        else:
            break
    while index<= len(list_numbers):
        if list_numbers[index]== find_numbers:
            l.append(index+1)
            index=index+1
        else: 
            break
    if l is None:
        return None
    else:
        l.sort()
        return l


if __name__ == "__main__":
    ll= [25,42,42,42,42,42,32,30,85]
    ll.sort()
    print("The given list: ",ll)
    print("The given number acc to Recursive Binary Search is on index",Binary_search_recursive(ll,find_number=42,start=0,end=len(ll)))
    print("The given number acc to Binary Search is on index",Binary_search(ll,42))
    print("The given number acc to Binary Search all ouccrance is on indices",Binary_search_AllOccurances(ll,42))