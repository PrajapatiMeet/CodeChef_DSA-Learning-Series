for i in range(int(input())):
    max_profit = 0
    for j in range(int(input())):
        stores, people, prize = [int(x) for x in input().split()]
        profit = int((people / (stores + 1))) * prize
        if (profit > max_profit):
            max_profit = profit
    print(max_profit)
