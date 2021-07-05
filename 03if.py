# if문
# num = int(input('숫자를 하나 입력하세요 '))
# if num > 10:
#     print('num은 10보다 크다')

# 속도위반 경고
# speed = int(input('속도를 입력하세요 '))
# # if speed > 50:
# #     print('속도위반!')
#
# if speed > 50: print('속도위반!')

# 합격/불합격 출력: if ~ else
# score = int(input('점수를 입력하세요 '))
#
# if score >= 80:
#     print('합격입니다')
# else:
#     print('아쉽습니다. 다시 도전해주세요!')

# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능
# if score >= 80:
#     pass
# else:
#     pass

# fan 가동
# temp = int(input('기계 온도를 입력하세요 '))
# if temp >= 40:
#     print('팬 가동')
# else:
#     print('팬 중지')

# 입력받은 정수를 3으로 나누어 소수점 첫째자리가 0.5 이상인 경우 반올림해서 출력
# 그렇지 않은 경우 그대로 출력하는 프로그램
# num = int(input('정수를 하나 입력하세요 '))
# result = num / 3
# if (result - int(result) >= 0.5):
#     result = int(result) + 1  # 소수 이하자리 버린 후 올림
# else:
#     result = int(result)  # 소수 이하자리만 버림
#
# print(f'결과: {result}')

# 마일리지 사용
# mileage = int(input('마일리지를 입력하세요 '))
# if mileage >= 1000:
#     print('마일리지 사용가능')
# else:
#     print('마일리지 사용불가')

# 성적처리
# jumsu = int(input('점수를 입력하세요 '))
#
# if 60 <= jumsu < 70:
#     print('양')
# elif 70 <= jumsu < 80:
#     print('미')
# elif 80 <= jumsu < 90:
#     print('우')
# elif 90<= jumsu <= 100:
#     print('수')
# else:
#     print('가')

# 자동주문 시스템
intro = 'Good Morning. Nice to meet you.\nWhere are you from?\n' \
         'Please select a number\n1.대한민국 2.USA 3.中國'
# print(intro)

nation = input(intro)
if nation == '1':
    # print('주문하시겠어요?')
    intro = '주문하시겠어요?'
elif nation == '2':
    # print('Would you like to order?')
    intro = 'Would you like to order?'
elif nation == '3':
    # print('你想訂購嗎?')
    intro = '你想訂購嗎?'
else:
    # print('Would you like to order?')
    intro = 'Would you like to order?'
print(intro)

# # 자동 주문 시스템 만들기
# print('Good morning. Nice to meet you.\n'
#       'Where are you from?\n'
#       'Please select a number\n'
#       '1. 대한민국 2. USA 3. 中國')
# nation = input('')
#
# if nation == '1':
#     intro = '주문 하시겠어요?'
# elif nation == '3':
#     intro = '您要点菜吗?'
# else:
#     intro = 'Would you like to order?'
#
# print(intro)

# 재난지원금 수령액 조회
family = int(input('가족수를 입력하세요 '))
if family == 1:
    # print('400,000원')
    money = 400_000
elif family == 2:
    # print('600,000원')
    money = 600_000
elif family == 3:
    # print('800,000원')
    money = 800_000
else:
    # print('1,000,000원')
    money = 1_000_000

print(f'{money:,}원 지원')

# BMI 지수
# BMI = weight / (height * height)
# bmi = int(input('BMI 지수를 입력하세요 '))
# if bmi <= 90:
#     print('저체중')
# elif 90 < bmi <= 110:
#     print('정상체중')
# elif 110 < bmi <=120:
#     print('과체중')
# elif 120 < bmi <= 140:
#     print('비만')
# else:
#     print('고도비만')

weight = int(input('몸무게: '))
height = int(input('신장: '))
height = height / 100

bmi = weight / (height * height)

if bmi > 30: print('고도비만')
elif bmi > 25: print('비만')
elif bmi > 23: print('과체중')
elif bmi > 18.5: print('정상체중')
else: print('저체중')

# 버스전용차로 단속 프로그램
print('1.월~금 2.토요일 3.공휴일')
day = input('요일을 선택하세요 ')

if day == '1':
    print('버스 전용차로 단속 중입니다')
    print('1.버스 2.승용차')
    car = input('차종을 선택하세요 ')
    if car == '1':
        print('버스입니다')
    else: print('버스 전용차로 위반!')
else: print('토요일 및 공휴일은 단속하지 않습니다.')

# 출생연도에 따른 공적마스크 구매
endBirthYear = int(input('출생연도 끝자리 입력 '))
age = int(input('만나이 입력 '))

day = ''

if age < 65:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일 구매 가능합니다')
        # day = '월'
    elif endBirthYear == 2 or endBirthYear == 7:
        print('화요일 구매 가능합니다')
    elif endBirthYear == 3 or endBirthYear == 8:
        print('수요일 구매 가능합니다')
    elif endBirthYear == 4 or endBirthYear == 9:
        print('목요일 구매 가능합니다')
    else: print('금요일 구매 가능합니다')
    # print(f'{day}요일 구매 가능합니다.')
else: print('언제든지 구매 가능합니다')