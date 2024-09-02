#!/usr/bin/env python3

# coins = list(reversed(sorted([2, 5, 1])))
# amount = 11

# coins = [2]
# amount = 3

# coins = [1]
# amount = 0

coins = [186,419,83,408]
amount = 6249

coins = list(reversed(sorted(coins)))


def coin_change(c, amt):

    print("Here is the list ", end=" ")
    print(c)

    if not c:
        return [-1, -1, -1]
    
    elif c:
        num = c[0]
        print("RAHAAAAAAAAAAAAAA " + str(num))

        if amt // num > 0:
            # print([(num, amt // num), c.pop(0), (amt - (num * (amt // num)))], end="\n\n")
            c.pop(0)
            return [(num, amt // num), c, (amt - (num * (amt // num)))]
        else:
            return None
    


output = []
originalAmount = amount

while coins != []:

    out = coin_change(coins, amount)
    if out:
        coins = out[1]
        amount = out[2]

        output.append(out[0])

        if coins == -1:
            break
    else:
        coins.pop(0)

if -1 not in output:
    resultNum = 0
    total = 0

    for num in output:
        resultNum = resultNum + num[1]

        total = total + (num[0] * num[1])

    print("Here is the total and amount", total, originalAmount)

    if output == []:
        print(-1)
    elif total == originalAmount:
        print(resultNum)
    else:
        print(-1)
        
else:
    print(-1)