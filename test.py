shop = [2,3,4,4,5,6,1,2,2,2,1,8,2]
def most(n, shop):
    price = 0
    smth = 0
    WTNF = 0
    for i in range(n):
        if shop[i] % 2 == 0:
            price += shop[i]
        elif shop[i] % 2 != 0:
            smth = price
            price = 0
        if WTNF < price:
            WTNF = price
    if WTNF < price:
        WTNF = sum
    print (WTNF)
most(13, shop)
