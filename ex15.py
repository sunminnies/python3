# 혈액 보관 시스템
# A = []
# B = []
# AB = []
# O = []
#
# for i in range(10):
#     msg = '헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. \nA, B, AB, O : '
#     bloodtype = input(msg)
#     if bloodtype == 'A' or bloodtype == 'a': A.append(bloodtype)
#     elif bloodtype == 'B' or bloodtype == 'b': B.append(bloodtype)
#     elif bloodtype == 'AB' or bloodtype == 'ab': AB.append(bloodtype)
#     elif bloodtype == 'O' or bloodtype == 'o': O.append(bloodtype)
#
# print('---------------------')
# print('혈액형 : 개수')
# print('---------------------')
# print(f'A형: {len(A)}')
# print(f'B형: {len(B)}')
# print(f'AB형: {len(AB)}')
# print(f'O형: {len(O)}')
# print('---------------------')

bloods = []
for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. \nA, B, AB, O : ')
    bloods.append(blood)

print('-'*30)
print(f'혈액형 수급 현황')
print('-'*30)
print(f'A형: {bloods.count("A")}')
print(f'B형: {bloods.count("B")}')
print(f'AB형: {bloods.count("AB")}')
print(f'O형: {bloods.count("O")}')
print('-'*30)
