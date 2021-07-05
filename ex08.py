# 차량 2부제
carNumber = int(input('차량번호 4자리를 입력하세요 '))
# date = int(input('오늘 날짜를 입력하세요 '))
from datetime import datetime as dt
dt.now()
date = dt.today().day

# if date % 2 == 0:
#     print('오늘 입차: 번호가 짝수인 차량')
#     if carNumber % 2 == 0:
#         print('귀하의 차량은 입차 가능합니다')
#     else: print('귀하의 차량은 입차 불가합니다')
# else:
#     print('오늘 입차: 번호가 홀수인 차량')
#     if carNumber % 2 != 0:
#         print('귀하의 차량은 입차 가능합니다')
#     else: print('귀하의 차량은 입차 불가합니다')

evenOrOdd = '짝수'
if date % 2 != 0: evenOrOdd = '홀수'
print(f'오늘 입차: 번호가 {evenOrOdd}인 차량')

passOrNot = '입차 불가'
# if carNumber % 2 == 0 and date % 2 == 0:  # 검사 2번 시행
if carNumber % 2 == 0 and evenOrOdd == '짝수':
    passOrNot = '입차가능'
print(f'귀하의 차량은 {passOrNot}합니다')
