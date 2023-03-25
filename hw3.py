discount_rate = 0;
def set_rate(rate) :
    global discount_rate
    discount_rate = rate/100;

def get_fixed_price(sale_price) :
    fixed_price = sale_price / (1-discount_rate)
    return fixed_price;




rate = int(input('할인율은?'));
set_rate(rate);

A_sale_price = int(input('A상품의 할인된 가격은?'));
B_sale_price = int(input('B상품의 할인된 가격은?'));

print('A 상품의 정가는', get_fixed_price(A_sale_price), '원');
print('B 상품의 정가는', get_fixed_price(B_sale_price), '원');