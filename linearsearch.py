dearr=[4,5,87,98,6]

def unorderedsearch(dearr,data):
    n=len(dearr)
    for i in range(n):
        if dearr[i]==data:
            return("item found")
    


print(unorderedsearch(dearr,5)) 
    
    
    
def orderedSearch(dearr,data):
    n=len(dearr)
    for i in  range(n):
        if dearr[i]==data:
            return ("item found")
        elif dearr[i]>data:
            return("item not  in list")
    return("Your data is bigger the content of the array")
    
    
    
    
    
    
    
    
    
    
    
    