def oddeven(n):
    digit=0
    oddsum=0
    evensum=0
    while(n!=0):
        digit=n%10
        if(digit%2==0):
            evensum=evensum+digit
        else:
            oddsum=oddsum+digit
        n=n//10
    if((evensum%4==0 and evensum!=0) or (oddsum%3==0 and oddsum!=0)):
        return True
    else:
        return False
test=int(input())
for i in range(test):
    inp=int(input())
    ans=oddeven(inp)
    print(ans)
