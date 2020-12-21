for i in range(int(input())):
    n, k = map(int, input().split())
    cakes = [int(x) for x in input().split()]
    
    types = [0] * k
    max_length = 0
    i = 0
   
    for j in range(n):
        types[cakes[j] - 1] += 1
        
        if not 0 in types:
            while not 0 in types:
                types[cakes[i] - 1] -= 1
                i += 1
        
        if (j-i+1) > max_length:
            max_length = j - i + 1
        
    print(max_length)