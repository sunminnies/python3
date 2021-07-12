from EMP import EMP
from datetime import datetime


class EMPService:
    # 객체 생성 없이 바로 사용 가능한 static method로 선언
    @staticmethod
    def readEmp():  # 사원번호, 이름, 성, 이메일, 전화번호, 입사일 입력
        empno = input('사원번호는? ')
        fname = input('이름은? ')
        lname = input('성은? ')
        email = input('이메일은? ')
        phone = input('전화번호는? ')
        hdate = input('입사일은? ')
        return EMP(empno, fname, lname, email, phone, hdate)

    @staticmethod
    def computeDuty(emp):  # 입사일 기준 근무일 계산
        hdate = emp.hdate.split('-')

        # year = EMP.hdate.substring(4)
        # month = EMP.hdate.substring(6,7)
        # day = EMP.hdate.substring(9,10)

        now = datetime.now()
        hire = datetime(int(hdate[0]), int(hdate[1]), int(hdate[2]))
        days = now - hire  # 근무일수
        print(str(days).split(' ')[0], '일')



