# 로또 당첨 게임

import random as r


# def readLotto():    # 사용자에게 로또 입력받음
#     magic = []
#     for i in range(6):
#         val = input(f'1 ~ 45 사이의 정수를 하나 입력하세요 ({i+1}/6): ')
#         magic.append(int(val))
#     return magic
#
#
# def makeLotto():    # 컴퓨터가 로또 생성함
#     magic = []
#     for i in range(6):
#         magic.append(r.randint(1, 45))
#     return magic


def readLotto():    # 사용자에게 로또 입력받음
    magic = []
    i = 0
    while len(magic) < 6:
        val = int(input(f'1 ~ 45 사이의 정수를 하나 입력하세요 ({i+1}/6): '))
        if magic.count(val) == 0:   # 입력한 정수가 magic 리스트에 존재하는지 검사
            magic.append(val)
            i += 1

    return magic


def makeLotto():    # 컴퓨터가 로또 생성함
    magic = []
    while len(magic) < 6:
        val = r.randint(1, 45)
        if magic.count(val) == 0:
            magic.append(val)
    return magic


def lotto645():
    magic = readLotto()
    lotto = makeLotto()
    wins = []

    for v in magic:
        if lotto.count(v) != 0:
            wins.append(v)

    print('금주 로또번호', magic)
    print('나의 로또번호', lotto)
    print('일치하는 숫자', wins)

# a = [1,2,3]
# b = [3,4,5]
# b.count(a[2])