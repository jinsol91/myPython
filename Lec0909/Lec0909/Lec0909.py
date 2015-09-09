## 기본 예제
a = {'name':'pey', 'phone':'01199992222','birth':'1119'}
b = a.keys()
print(b)

b = list(a.keys())      # list로 출력
print(b)
b = list(a.values())    # a의 모든 value 액세스
print(b)
b = a.items()
print(b)

print(a['name'])

c = {1:'c'}
c[2] = 'b'

## 영화 평점 문제
star = {'홍길동':{'베테랑':5.0,'암살':4.5},
        '이순신':{'베테랑':2.4,'암살':5.0},
        '장영실':{'베테랑':3.3,'암살':4.2}}
print(star['홍길동'])          # 홍길동이 평점 준 데이터들 출력
print(star['홍길동']['암살'])    # 홍길동이 암살을 몇 점 주었나 출력
#print(star['세종'])          # 없는 키 접근은 오류 발생
print(star.get('세종'))       # get으로 없는 키 접근은 None 출력

## 제어문(if-else)
#answer = input("Would you like express shipping?:\n")
#if (answer.upper() == "YES"):           # yes든, YES든 무조건 대문자로 바꿔주는 upper() 함수
#    print("That will be an extra $10")
#if (answer.upper() == "NO"):pass        # 아무것도 안할거면 pass구문 사용

## 제어문(for)
a = [(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)
print("")
mark = [20,30,40,50,60]
for i in range(len(mark)):      # mark list의 길이를 return하는 len()
    print(mark[i])
# 구구단
for i in range(2,10):
    print("     <%d단>"%i)
    for j in range(1,10):
        print("%2d * %2d = %2d"%(i,j,i*j))  # 문자열과 숫자를 함께 출력하는 %
    print("")

## 그리기 라이브러리 turtle
import turtle
turtle.color("blue")
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#     turtle.forward(50)
#     turtle.right(90)
#nSides = 5      # 면의 갯수
#for steps in range(nSides):
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for moresteps in range(nSides):
#        turtle.forward(50)
#        turtle.right(360/nSides)

## while
# 메뉴 만들기 예제
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:"""    # 여러줄 문자열 처리하는 """(세 개)

print(prompt)