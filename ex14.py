# 출석부 관리 시스템
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']

# 1. 가나다 순으로 정렬
students.sort()
print(students)

# 2. 박찬호 전학
students.remove('박찬호')
print(students)
print(len(students))

# 3. 앞에서 학생 3명 선발
print(students[:3])

# 4. 새로운 학생 전학: 이병규
students.insert(5, '이병규')
students.append('이병규')

# 5. 학생 순서를 역순으로
students.reverse()

# 6. 정우람 학생이 정잘남으로 개명
students[1] = '정잘남'