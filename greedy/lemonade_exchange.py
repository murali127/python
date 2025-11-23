def lemonadeChange(bills):
    five = 0
    ten = 0

    for b in bills:
        if b == 5:
            five += 1

        elif b == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1

        else:  # b == 20
            # Try to give 10 + 5 first
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True

bills = list(map(int, input().split()))
print(lemonadeChange(bills))
