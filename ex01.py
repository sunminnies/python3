# 예제1: 비밀번호 메일 발송
print('회원정보를 입력해주세요')
email = input('이메일을 입력하세요')
name = input('이름을 입력하세요')
userid = input('아이디를 입력하세요')
passwd = input('비밀번호를 입력하세요')

print('--------------------------------------------')
print('To.' + email)
print('> 아이디 및 비밀번호 확인')
print(name + ' 고객님 안녕하세요')
print(name + ' 고객님의 아이디와 비밀번호는 아래와 같습니다')
print('아이디: ' + userid)
print('비밀번호: ' + passwd)

# print 출력시 변수와 문자열 사이에 , 사용 : 공백이 하나 더 추가
print('=============================================')
print('To.', email)
print('> 아이디 및 비밀번호 확인')
print(name, ' 고객님 안녕하세요')
print(name, ' 고객님의 아이디와 비밀번호는 아래와 같습니다')
print('아이디: ', userid)
print('비밀번호: ', passwd)

# format 함수 사용 : 문자열 템플릿으로 출력 : py3
print('=============================================')
print('To. {0}'.format(email))
print('> 아이디 및 비밀번호 확인')
print('{0} 고객님 안녕하세요'.format(name))
print('{0} 고객님의 아이디와 비밀번호는 아래와 같습니다'.format(name))
print('아이디: {0}'.format(userid))
print('비밀번호: {0}'.format(passwd))

# format 문자열 사용 : py2
print('=============================================')
print('To. %s' % email)
print('> 아이디 및 비밀번호 확인')
print('%s 고객님 안녕하세요' % name)
print('%s 고객님의 아이디와 비밀번호는 아래와 같습니다' % name)
print('아이디: %s' % userid)
print('비밀번호: %s' % passwd)
