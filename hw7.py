shopping_bag = {}
while True:
    item = input('상품명? ')
    if item == '':
        break
    amount = input('수량은? ')
    shopping_bag[item] = amount

    print(f'장바구니에 {item}가(이) {amount}개 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')