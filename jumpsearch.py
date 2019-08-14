def jump(m,l,ele):
    l.sort()
    pos=0
    while(pos!=len(l)):
        if(l[pos]==ele):
            return pos
        elif(l[pos]<ele):
            pos=pos+m
        else:
            temp=pos-m
            for i in range(temp,pos):
                if(l[i]==ele):
                    return i


n=int(input("Enter the size of array "))
l=[]
for i in range(n):
    x=int(input("Enter the element: "))
    l.append(x)
m=int(n**0.5)
ele=int(input("Enter the element to be searched "))
pos=jump(m,l,ele)
print(pos)