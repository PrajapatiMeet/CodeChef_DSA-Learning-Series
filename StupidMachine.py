for i in range(int(input())):
    n = int(input())
    boxes = [int(x) for x in input().split()]
    tokens = boxes[0]
    min = boxes[0]
    for j in range(1, n):
        if boxes[j] < min:
            tokens += boxes[j]
            min = boxes[j]
        else:
            tokens += min
    print(tokens)