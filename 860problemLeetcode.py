bills : list[int] = [5,5,5,5,20,20,5,5,5,5]
fives: int = 0
tens: int = 0
result: bool = True
for bill in bills:
    if bill == 5:
        fives += 1
    elif bill == 10:
        tens += 1
        fives -= 1
    else:
        if tens > 0:
            tens -= 1
            fives -= 1
        else:
            fives -= 3
    if fives < 0:
        result = False
print( result )
