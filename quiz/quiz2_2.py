'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.
테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))
<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.
'''

import datetime
year = int(input('연도를 입력하시오 : '))
month = int(input('월을 입력하시오 : '))
day = int(input('일을 입력하시오 : '))

def printDayOfWeek(myYear, myMonth, myDay):
    weekday = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return weekday[datetime.datetime(myYear, myMonth, myDay).weekday()]
print(f'{year}년 {month}월 {day}일은 {printDayOfWeek(year, month, day)} 입니다.')