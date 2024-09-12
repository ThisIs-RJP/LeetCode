#!/usr/bin/env python3

def lemonadeChange(bills):
    five = 0
    ten = 0

    if bills[0] != 5:
        return False

    for bill in bills:
        if bill == 5:
            five += 1
        
        elif bill == 10:
            ten += 1
            if five > 0:
                five -= 1
            else:
                return False
        
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True
            

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,5,10,20]))
