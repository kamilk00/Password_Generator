import random

numbers = '1234567890'
symbols = '!@#$%&()_-+={}[]|\:;?.>,<'
upper_case = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
lower_case = 'qwertyuioplkjhgfdsazxcvbnm'

all_of_signs = numbers + symbols + upper_case + lower_case

while 1:
    
    limit = input("Lower limit is: ")
    try:
        ll = int(limit)
    except:
        print("ERROR! That's not integer!")
        break

    if ll <= 0:
        print("ERROR! Lower limit is too low!")
        break

    limit = input("Upper limit is: ")
    try:
        ul = int(limit)
    except:
        print("ERROR! That's not integer!")

    if ul < ll:
        print("ERROR! Lower limit is too low!")
        break

    length = random.randint(ll, ul)
    password = "".join(random.sample(all_of_signs, length))
    print("Your password: \n" + password)

    break