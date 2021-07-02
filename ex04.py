# 예제4 수온 계산기
depth = int(input('수심을 입력하세요: '))
depth = depth // 10
temp = 20
temp -= depth*0.7
print(f'수온은 {temp}')