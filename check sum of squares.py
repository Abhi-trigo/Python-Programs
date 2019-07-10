from math import *
def sumofsquares(m):
    j=1
    if(m<=1):
        return False
    else:
        temp=j**2
        while(1):
            a=m-temp
            temp1=sqrt(a)# caculate square root of a
            temp1=int(temp1)# type casting float value to int
            temp1=temp1**2
            if(temp+temp1==m):
                return True
                break
            j=j+1
            temp=j**2
            if(temp>m):
                return False
                break
        
a=sumofsquares(41)
print(a)
