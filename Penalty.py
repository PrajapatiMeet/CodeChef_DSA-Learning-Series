for i in range(int(input())):
    n = int(input())
    a = b = 0
    possible_a = possible_b = n
    shot = 1
    s = input()
    for x in s:
        if (possible_a < b or possible_b < a):
            print(shot - 1)
            break
        x = int(x)
        
        if (shot % 2 == 0):
            if x == 0:
                possible_b -= 1
            else:
                b += 1
        
        else:
            if x == 0:
                possible_a -= 1
            else:
                a += 1
        
        if shot == len(s):
            print(shot)
        shot += 1    
        

            
