def precedence(x):
    if x == '^':
        return 3
    elif x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    else:
        return 0

for i in range(int(input())):
    n = int(input())
    infix = input().strip()
    postfix = ''
    stack = []
    operator = ['+', '-', '*', '/', '^']
    
    for j in infix:
        if j == '(':
            stack.append(j)
        
        elif j == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        
        elif j in operator:
            while stack and precedence(j) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(j)
        
        else:
            postfix += j
    
    while stack:
        postfix += stack.pop()
    
    print(postfix)