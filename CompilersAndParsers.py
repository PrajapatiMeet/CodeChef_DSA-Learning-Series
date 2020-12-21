for i in range(int(input())):
    string = input()
    balance = 0
    length = 0
    valid_str = 0
    
    for j in string:
        if j == '<':
            balance += 1
        else:
            balance -= 1
        
        if balance < 0:
            break
        
        length += 1
        if balance == 0:
            valid_str = length

    print(valid_str)

            