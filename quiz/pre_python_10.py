"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))