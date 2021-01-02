def bonAppetit(bill, k, b):
    bill.pop(k)
    charged = sum(bill)/2
    if b - charged == 0:
        print ('Bon Apetite')
    else:
        print (b - charged)
    

bonAppetit([3,10,2,9], 1, 7)