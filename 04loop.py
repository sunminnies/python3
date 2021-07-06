# 반복문
# 1 ~ 10까지 정수 출력
for i in range(1, 10+1):
    print(i)

# 2 ~ 10사이 짝수 출력
for i in range(2, 10, 2):
    # print(i)
    print(i, end=' ')

for i in range(1, 10):
    if i % 2 == 0: print(i)

# 메일발송
num = int(input('메일 발송할 횟수를 입력하세요 '))
for i in range(1, num+1):
    print('메일발송')

# 1 ~ 10사이 정수 중 3의 배수에 '3의 배수!' 출력
for i in range(1, 11):
    print(f'num = {i}')
    if i % 3 == 0:
        print('3의 배수!')  # 3의 배수 밑에 출력

for i in range(1, 11):
    if i % 3 == 0:
        print('3의 배수!')
    else: print(f'num = {i}')  # 3의 배수 자리에 출력

# 구구단 5단 출력하기
dan = int(input('단을 입력하세요 '))
for i in range(1, 10):
    print(f'{dan} x {i} = {dan * i}')

# 1 ~ 10까지 정수 합 출력하기
sum = 0
for i in range(1, 10+1):
    sum += i
print(sum)

# 1 ~ 100까지 정수 중에서 3과 7의 공배수와 최소공배수 구하기
for i in range(1, 100+1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

min = 100
for i in range(100, 1, -1):
    if i % 3 == 0 and i % 7 == 0:
        if min >= i: min = i
        print(i, end=',')
print(f'최소공배수 {min}')

for i in range(-10, 1):
    print(i, end=',')

# 1 ~ 10까지 출력
for i in range(10):
    print(i+1)

# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end=',')

# 50보다 작은 7의 배수
for i in range(1, 51):
    if i % 7 == 0: print(i, end=',')

# 1 ~ 10까지 출력
num = 1
while num < 10+1:
    print(num)
    num += 1

# 1 ~ 30까지의 정수 중 홀수와 짝수를 구분하여 출력하기
num = 1
while num <= 30:
    if num % 2 == 0: print(f'짝수 : {num}')
    else: print(f'홀수 : {num}')
    num += 1

# 구구단 3단 출력하기
i = 1
dan = 3
while i < 9+1:
    print(f'{dan} x {i} = {dan * i}')
    i += 1

# 0 ~ 100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
num = 1
min = 100
while num < 100+1:
    if num % 3 == 0 and num % 8 == 0:
        print(f'공배수 : {num}')
        if min > num: min = num
    num += 1
print(f'최소공배수 : {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1: 진행, 2: 종료'))
    if code == 1: print('게임 진행')
    else:
        flag = False
        print('게임 종료')

# 1 ~ 50까지 정수 중 3의 배수 더하기
sum = 0
for i in range(1, 50+1):
    if i % 3 == 0:
        sum += i
print(sum)

sum = 0
for i in range(1, 50+1):
    if i % 3 != 0: continue
    sum += i
print(sum)

# 1 ~ 100까지 모든 정수 더하기
# 단, 정수의 합이 500이 넘었을 때의 정수는 무엇인가?
sum = 0
for i in range(1, 100+1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# 1 ~ 10까지 정수의 총합을 구하고 반복이 끝나는 경우 완료 메세지 출력
sum = 0
for i in range(10):  # 0 ~ 9
    sum += (i + 1)
else:
    print(f'총합 계산 끝! : {sum}')

# 삼각형 넓이 구하기
# 단, 너비가 150을 넘으면 프로그램을 종료하고 이때의 가로/세로 길이 출력
width = 2
height = 3
area = 0
while area <= 150:
    area = (width * height) / 2
    print(area, width, height)
    width += 2
    height += 3

# 1 ~ 100까지 정수 중 5와 7의 배수를 제외한 나머지 정수 출력
for i in range(100+1):
    if i % 5 == 0 or i % 7 == 0: continue
    print(i, end=' ')

# 구구단 출력
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j:2d} x {i:2d} = {j * i:2d} \t', end=' ')
    print()
