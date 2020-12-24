n = int(input())
points = []
for i in range(n):
    points.append([int(x) for x in input().split()])
points.sort()

left = []
stack = []
for point in points:
    while len(stack) > 0 and stack[-1][1] >= point[1]:
        stack.pop()
    if len(stack) == 0:
        left.append(0)
    else:
        left.append(stack[-1][0])
    stack.append(point)

right = [0] * n 
stack = []
for i in reversed(range(n)):
    while len(stack) > 0 and stack[-1][1] >= points[i][1]:
        stack.pop()
    if len(stack) == 0:
        right[i] = 100000
    else:
        right[i] = stack[-1][0]
    stack.append(points[i])

max_area = 0
for i in range(n):
    area = (right[i] - left[i]) * points[i][1]
    if area > max_area:
        max_area = area
    
    if i == 0 and (points[i][0] * 500) > max_area:
        max_area = points[i][0] * 500
    elif i == n-1 and ((100000 - points[i][0]) * 500) > max_area:
        max_area = (100000 - points[i][0]) * 500
    else:
        if (points[i][0] - points[i-1][0]) * 500 > max_area:
            max_area = (points[i][0] - points[i-1][0]) * 500           

print(max_area)