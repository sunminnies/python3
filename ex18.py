# 다국어 인사말 프로그램
def salutation():
    msg = 'Where are you from? 1.한국, 2.USA, 3.Japan '
    nation = input(msg)

    if nation == '1': print('안녕')
    elif nation == '2': print('Hello')
    elif nation == '3': print('こんにちは')

salutation()


# 풀이
def sayHello(nation):
    if nation == '1':
        print('안녕하세요')
    elif nation == '2':
        print('Hello')
    elif nation == '3':
        print('こんにちは')
    elif nation == '4':
        print('你好')


nation = input('1.한국 2.미국 3.일본 4.중국 \n당신의 국적은? ')
sayHello(nation)

