def main():
    coins = [5, 10, 25]
    amnt_due(coins)


def amnt_due(coins):
    due = 50
    while due <= 50:
        if due <= 0:
            due = abs(due)
            print(f"Change Owed: {due}")
            return
        else:
            print(f"Amount Due: {due}")
            insert_coin = int(input("Insert Coin: "))
            if insert_coin in coins:
                due -= insert_coin
            else:
                due
    return due

main()
