num1 = 10
num2 = 20
num3 = num1 + num2  # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2  # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2  # 정수 + 실수 = 실수

# 매출액 구하기
# jan = int(input('1월 매출을 입력하세요 '))
# feb = int(input('2월 매출을 입력하세요 '))
# mar = int(input('3월 매출을 입력하세요 '))
# tot = jan + feb + mar
#
# print('1월매출 : {0}'.format(jan))
# print('2월매출 : {0}'.format(feb))
# print('3월매출 : {0}'.format(mar))
# print('1분기 전체 매출 : {0}'.format(tot))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
float(num3)
int(num3)

# 수익 구하기
# buy = int(input('매입액 : '))
# sell = int(input('매출액 : '))
# profit = sell - buy
#
# print('1분기 매출 : {0}'.format(sell))
# print('1분기 매입 : {0}'.format(buy))
# print('수익 : {0}'.format(profit))

# 방 너비 구하기
# width = int(input('가로 : '))
# height = int(input('세로 : '))
# size = width * height
# print('넓이 : {0}㎠'.format(size))

str1 = 'Hello World! '
str1 * 3
2 * str1 * 3
str1 * -2

# BMI 구하기
# weight = int(input('몸무게(kg) : '))
# height = int(input('키(m) : '))
# height = height / 100
# BMI = weight / (height * height)
# print('BMI : {0:.2f}'.format(BMI))
# print(f'BMI : {BMI:.2f}')  # f-string : py3.6부터 지원

# print 출력 속도 : .format > % > f-string

# 동전 개수 알아보기
# coin = int(input('동전 개수는 : '))
# isEven = coin % 2
# print(f'동전의 홀짝여부(0:짝 / 1:홀) {isEven}')

10 / 3
10 // 3

# 빵 나눠주기
# bread = int(input('총 빵의 개수 : '))
# diver = int(input('나눠줄 빵 개수 : '))
#
# stud = bread // diver
# mod = bread % diver
#
# print(f'{bread}개의 빵은 {diver}개씩 {stud}명의 학생에게 나눠줄 수 있고')
# print(f'{mod}개의 빵이 남음')

2**3
2**30

# 복리계산
money = 5_000_000
duration = 5
interest = 0.05

takes = money + (money * interest)  # 1년차
# takes = takes + (takes * interest)  # 2년차
takes += takes * interest
# takes = takes + (takes * interest)  # 3년차
takes += takes * interest
# takes = takes + (takes * interest)  # 4년차
takes += takes * interest
# takes = takes + (takes * interest)  # 5년차
takes += takes * interest

# 놀이기구 탑승
# height = int(input('키를 입력하세요: '))
# isRide = height >= 120
# print(f'탑승가능여부 : {isRide} (True : 탑승가능)')

# 범퍼카 탑승
# height = int(input('키를 입력하세요: '))
# isRide = 120 <= height < 170
# print(f'탑승가능여부 : {isRide} (True : 탑승가능)')

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15)  # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15)  # True and False
# (num1 < 5) and xyz  # py3.8만 지원

# 삼항 연산자
# 참일때 값 if 조건식 else 거짓일때 값
num = 11
'짝수' if (num % 2 == 0) else '홀수'

# 적자/흑자 판단하기
income = int(input('수입을 입력하세요: '))
expense = int(input('지출을 입력하세요'))
'흑자' if (income > expense) else '적자'

# 윤년여부 알아보기
# 4로 나누어 떨어지고 100으로 나누어 떨어지지 않음 혹은 400으로 나누어 떨어짐
year = int(input('년도를 입력하세요: '))
isLeap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
'윤년' if (isLeap) else '평년'


# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op
op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3)  # 정수 몫(//)
op.truediv(10, 3)  # 실수 몫(/)
op.mod(10, 3)
op.pow(2, 30)  # 지수연산

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.lt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급재난지원금
income = int(input('월소득: '))
grant = int(input('다른 지원금 수급 여부(1:받고있다, 2:안받고있다): '))
# x = op.le(income, 4000000)
# y = op.eq(grant, 2)
# '수급대상자' if (op.and_(x, y)) else '비대상자'
isTarget = op.and_(op.le(income, 4_000_000), op.eq(grant, 2))
result = '수급대상자' if (isTarget) else '비대상자'
print(result)
