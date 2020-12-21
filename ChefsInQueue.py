n, k = map(int, input().split())
chefs = [int(x) for x in input().split()]
fearfulness = 1
stack = []
stack.append([chefs[-1], 0])

for i in reversed(range(n-1)):
    j = 0
    while len(stack) > 0 and chefs[i] <= stack[-1][0]:
        j += (stack[-1][1] + 1)
        stack.pop()

    if len(stack) != 0:
        fearfulness = (fearfulness * (j + 2)) % 1000000007    
    
    stack.append([chefs[i], j])

print(fearfulness)