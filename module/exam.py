# 시험 통과 여부

def exampass(kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3

    isPass = '불합격'
    isAll60 = avg >= 60
    is40 = kor < 40 or eng < 40 or mat < 40

    if isAll60 and not is40:
        isPass = '합격'

    # 파이썬에서는 함수의 리턴값으로 2개 이상 지정 가능
    return tot, avg, isPass
