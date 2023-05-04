def buy(shopping_bag):
    while True:
        item = input('상품명? ')
        if item == '':
            return False
        amount = int(input('수량은? '))
        shopping_bag[item] = amount

        print(f'장바구니에 {item}가(이) {amount}개 담겼습니다.\n')

def show(dict):
    print(f'\n>>> 장바구니 보기: {dict}')

def find(dict):
    key = input('장바구니에서 확인하고자 하는 상품은? ')
    if key in dict:
        print(f'{key}는 {dict[key]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {key}는 없습니다.')
    
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)