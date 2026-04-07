def brutematch(text,pattern):
    n=len(text)
    m=len(pattern)
    for i in range(n-m+1):
        if text[i:m+i]==pattern:
         return 1
    return -1