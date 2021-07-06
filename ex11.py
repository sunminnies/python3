# 369 게임 만들기
# 1 ~ 99까지 1씩 증가하면서 3, 6, 9가 들어갈때마다 숫자와 함께 '짝!'을 출력하는 프로그램
# for i in range(1, 100):
#     clap = ''
#     if i % 3 == 0 or i % 6 == 0 or i % 9 == 0:
#         clap = '짝!'
#     print(f'{i} {clap}')

for i in range(1, 100):
    clap = ''
    if i < 10:  # 숫자가 한자리라면
        if i % 3 == 0:
            clap = '짝!'
    else:   # 숫자가 두자리라면
        num1 = i // 10  # 첫째 숫자 추출
        num2 = i % 10   # 나머지 숫자 추출

        if num1 % 3 == 0:   # 첫째 숫자가 3의 배수라면
                clap += '짝!'

        if num2 % 3 == 0 and num2 != 0: # 둘째 숫자가 3의 배수이고 0이 아니라면
                clap += '짝!'
    print(f'{i} {clap}')
print()

# 문자열로 출력
for i in range(1, 100):
    print(i, end=' ')
    for j in str(i):
        if int(j) % 3 == 0 and int(j) != 0:
            print("짝!", end=' ')
    print()

# 미국판 369 게임 buzz : https://www.wikihow.com/Play-Buzz
