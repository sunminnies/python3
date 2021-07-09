# 파일 다루기


# 입력한 성적데이터를 파일에 저장
fname = 'c:/Java/sungjuk.dat'

name = input('이름은? ')
kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))

f = open(fname, 'w')    # 지정한 파일을 쓰기모드로 열기
# data = 'Hello, World!'
data = f'{name} {kor} {eng} {mat}'  # 파일에 기록할 내용을 문자열로 작성

f.write(data)
f.close()

# 기록한 성적데이터를 파일로부터 읽어오기
f = open(fname, 'r')
data = f.read()
print(data)
f.close()

# 일정관리 메모 저장
def saveMemo(memo):
    fname = 'c:/Java/myMemo.txt'

    f = open(fname, 'a')    # 'w'는 기존 메모를 지우고 새로 작성,  'a'는 기존 메모에 추가(append)
    f.write(memo + "\n")
    f.close()

def memoMain():
    memo = input('메모를 입력하세요. ')
    saveMemo(memo)

memoMain()

# py3 방식으로 파일 다루기
# 기존 파일 입출력 코드에서 불편한 점은 파일 작업 후에는 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도됨
with open(fname, 'w') as f:
    f.write('blah blah blah')

# 파일에서 데이터 읽어오기
fname = 'c:/Java/EMPLOYEES'
with open(fname) as f:
    data = f.read()     # 모든 데이터를 한번에 다 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline()     # 데이터를 한줄 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline()     # 모든 데이터를 라인 단위로 읽어옴
    print(data)     # 읽어온 결과는 list 형식

# EMPLOYEES에서 사번, 이름, 입사일, 급여를 출력하세요
with open(fname) as f:
    f.readline()    # 첫줄은 읽기만 하고 처리하지 않음
    while True:
        line = f.readline()
        if not line: break  # 읽을 데이터가 없는 경우 작업 중단
        data = line.split(',')  # 문자열을 ,로 분리해서 리스트로 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

# 타이타닉 데이터셋을 이용해서 승객이름name, 성별sex, 나이age, 승선위치embarked, 사망여부survived 추출해서 출력하세요
# 단, survived가 0이면 '사망', 1이면 '생존'이라고 출력함
# embarked가 S이면 'Southhampthon', C이면 'Cherbourg', Q이면 'Queenstown'이라고 출력함

fname = 'c:/Java/titanic3b.csv'
with open(fname) as f:
    f.readline()
    while True:
        line = f.readline()
        if not line: break
        data = line.split(',')

        # name = data[2]
        sex = data[2]
        age = data[3]

        embarked = data[9]
        if embarked == 'S': embarked = 'Southhampton'
        elif embarked == 'C': embarked = 'Cherbourg'
        elif embarked == 'Q': embarked = 'Queenstown'
        else: emb = 'none'

        survived = data[1]
        if survived == '0': survived = '사망'
        elif survived == '1': survived = '생존'

        if age == '': age = '0'

        titanic = f'{sex} {age} {embarked} {survived}'
        print(titanic)

