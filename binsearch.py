myarr=[12,13,17,19,24,34,45,47,48,50,54,58,60,61]

def binarysearch(myarray,target):
    low=0
    high=len(myarray)-1
    
    while low<=high:
        mid=(high+low)//2
        
        if  myarray[mid]==target:
            return (f"item {myarray[mid]} was found ")
        elif myarray[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ("item not found")
print(binarysearch(myarr,13))