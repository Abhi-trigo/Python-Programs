price=int(input())
qty=int(input())
amount=price*qty
if amount>10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    if amount>5000:
       print ("5% discount applicable")
       discount=amount*0.05
       amount=amount-discount
    else:
        if amount>2000:
            print ("2% discount applicable")
            discount=amount*0.02
            amount=amount-discount
        else:
           if amount>1000:
                print ("1% discount applicable")
                discount=amount*0.01
                amount=amount-discount
           else:
              print("No discount applicable")
print ("amount payable:",amount)
