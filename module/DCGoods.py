# 구매상품 할인율 계산
# 1개 - 5%
# 2개 - 10%
# 3개 - 20%
# 4개이상 - 30%

def checkDiscount(goods):
    rate = 0.3
    sum = 0
    if len(goods) == 1:
        rate = 0.05
    elif len(goods) == 2:
        rate = 0.1
    elif len(goods) == 3:
        rate = 0.2

    for i in range(len(goods)):
        sum += goods[i]

    fare = sum - (sum * rate)

    print(f'할인율: {rate}\n총구매금액: {sum}\n할인적용금액: {fare}')


def discountGoods():
    goods = []
    flag = True

    while flag:
        choice = input('상품을 구매하시겠습니까? 1.구매, 2.종료 ')
        if choice == '1':
            price = int(input('구매 금액을 입력하세요 '))
            goods.append(price)

        elif choice == '2':
            flag = False
            checkDiscount(goods)

        else:
            print('잘못 입력하셨습니다.')
