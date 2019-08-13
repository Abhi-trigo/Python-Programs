def count(step):
    x=y=0
    move=0
    l=[]
    while(step!=0):
        temp=step%4
        move+=10
        if(temp==0):
            x+=move
        elif(temp==1):
            y+=move
        elif(temp==2):
            x-=move
        else:
            y-=move
        step-=1
    l.append(x)
    l.append(y)
    return l
step=int(input())
value=count(step)
print(value[0],value[1])