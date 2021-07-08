# 계산기 프로그램
def computer():
    num1 = int(input('첫번째 숫자를 입력하세요 '))
    op = input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈 \n연산자를 선택하세요. ')
    num2 = int(input('두번째 숫자를 입력하세요 '))
    compute(op, num1, num2)


def compute(op, num1, num2):
    if op == '1':
        print(f'덧셈 결과: {num1 + num2}')
    elif op == '2':
        print(f'뺄셈 결과: {num1 - num2}')
    elif op == '3':
        print(f'곱셈 결과: {num1 * num2}')
    elif op == '4':
        print(f'나눗셈 결과: {num1 / num2}')
    else:
        print('연산자를 잘못 입력하셨습니다!')


computer()