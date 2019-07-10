def Flames(temp1,temp2):
    temp1=list(temp1.lower())
    temp2=list(temp2.lower())
    temp=temp1[:]
    i=0
    #print("temp1",temp1)
    #print("temp2",temp2)
    while(1):
        x=temp[i]
        if(x in temp2):#TO check for the character in another list
            temp2.remove(x)# removing the element from second list
            temp1.remove(x)# removing the element from first list
            i=i+1
        else:
            i=i+1
        if(i==len(temp)):
            break
    count=len(temp1)+len(temp2)# to get the total element in the list 
    #print("temp1",temp1)
    #print("temp2",temp2)
    return count
        

def calculate(value):
    ''' the logic is
     the score%6 will give me the index in the list for 6 value the modulas will give me 0
     so I put the element sister at 0'''
    if(value>0):
        flames=['SISTER','FRIEND','LOVER','AFFECTION','MARRIAGE','ENEMY']
        temp=value%6 
        return(flames[temp])
    else:
        print("Error in genrating the relation ")

First=input("Enter the First name: ")
second=input("Enter the Second name: ")
temp=min(len(First),len(second))
if(temp==len(First)):
    score=Flames(First,second)
else:
    score=Flames(second,First)
result=calculate(score)
print("The score generated is: ",score)
print("The generated relation is: ",result)
