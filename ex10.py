# 전기요금 계산
elec = int(input('전기 사용량을 입력하세요 '))
rate = 0  # 기본요금
price = 0  # 단가

if elec > 400:
    rate = 7300
    price = 280.6
elif elec >= 201:
    rate = 1600
    price = 187.9
elif elec <= 200:
    rate = 910
    price = 99.3

fare = rate + (elec * price)
print(f'사용량 : {elec:.1f} kwh\n'
      f'기본요금 : {rate:,}원\n'
      f'단가 : {price}원\n'
      f'전기요금 : {fare:,}원')
