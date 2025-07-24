due = 50
#change = 0

while due>0:
    coins = int(input('Insert Coin: '))
    if coins in [10,5,25]:
        due-=coins
    print(f'Change Owed: {abs(due)}') if due<=0 else print(f'Amount due: {due}')
    