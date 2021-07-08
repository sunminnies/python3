# 회원가입 프로그램

members = {}
flag = True

menu = '-'*20
menu += '\n 회원가입 프로그램  \n'
menu += '-'*20
menu += '\n 1. 회원가입 \n'
menu += ' 2. 프로그램 종료 \n'
menu += '-'*20

while flag:
    print(menu)
    choice = input('작업을 선택하세요 : ')

    if choice == '1':   # 회원가입 절차 수행
        userid = input('아이디는? ')
        passwd = input('비밀번호는? ')
        members[userid] = passwd

    elif choice == '2': # 가입한 회원들을 출력한 후 종료
        print('프로그램을 종료합니다.')
        print('가입한 회원들은 다음과 같습니다.')
        for u, p in members.items():
            print(f'{u} : {p}')
        flag = False
