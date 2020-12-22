def find_warmhole(x, warmholes, forArrival=False):
    i, mid = 0, 0
    j = len(warmholes) - 1
      
    while i <= j:
        mid = int((i + j) / 2)
        if x == warmholes[mid]:
            return warmholes[mid]
        if x < warmholes[mid]:
            j = mid - 1
        if x > warmholes[mid]:
            i = mid + 1
    
    if forArrival:
        return warmholes[mid] if x > warmholes[mid] else warmholes[mid-1]
    else:
        return warmholes[mid] if x < warmholes[mid] else warmholes[mid+1]

n, x, y = map(int, input().split())
contests = []
for i in range(n):
    contests.append([int(j) for j in input().split()])
v = [int(j) for j in input().split()]
w = [int(j) for j in input().split()]
v.sort()
w.sort()
min_time = 10**9

for contest in contests:
    if contest[0] >= v[0] and contest[1] <= w[-1]:
        v_warmhole = find_warmhole(contest[0], v, True)
        w_warmhole = find_warmhole(contest[1], w)
        if (w_warmhole - v_warmhole + 1) < min_time:
            min_time = w_warmhole - v_warmhole + 1

print(min_time)