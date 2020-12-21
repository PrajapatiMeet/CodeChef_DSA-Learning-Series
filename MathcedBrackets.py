n = int(input())
pattern = [int(x) for x in input().split()]

balance = 0
pos = 0
balance_pos = 1
max_depth = 0
depth_pos= 0
max_seq = 0
seq_pos = 0
seq = 0

for i in pattern:
    if i == 1:
        balance += 1
    else:
        balance -= 1

    pos += 1
    seq += 1

    if balance > max_depth:
        max_depth = balance
        depth_pos = pos
    
    if balance == 0:
        if seq > max_seq:
            max_seq = seq
            seq_pos = balance_pos
        balance_pos = pos + 1
        seq = 0

print(max_depth, depth_pos, max_seq, seq_pos)
