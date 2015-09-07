#data = ['a','b','c',['abcd','efg']]
#print(data[0])
#print(data[-1])
#print(data[-1][1])
##
#b=[1,2,3]
#c=['Life','is','too','short']
#f = b+c
#print(b+c)          # b와 c의 리스트를 결합
#print(f)            # f에 새로운 리스트 저장
#print(b*3)          # b의 print를 세 번
##
#b[0] = 'green'
#print(b)
#b[1] = ['green01','green02']        # b[1]에 리스트 자체가 들어감
#print(b)
#b[1:2] = ['green1','green2']        # b[1]이상 b[2]미만에 들어감
#print(b)


####################### 리스트 변경
print('----리스트 변경----')
id = ['green','red','blue']
print(id)
# password 삽입
id.insert(1,'1234')
id.insert(3,'4321')
id.insert(5,'2222')
print(id)
# 부가 정보를 리스트로 삽입
id.insert(2,['kim','seoul'])
id.insert(5,['lee','yeosu'])
id.insert(8,['park','seoul'])
print(id)
# 멤버 엑세스
print('----멤버 엑세스----')
guest = ['d','c','b','a','h','e','j','q']
score = [12,423,42,546,87,44,77,44,75,23,65,97]

# for문을 사용하여 멤버 엑세스
for steps in guest:         # guest의 인덱스0~3의 원소 하나 하나를 steps에
    print(steps)
for steps in range(4):      # steps라는 변수에 0~3 인덱스 대입
    print(guest[steps])
for steps in range(3):
    print(id[steps])
print('----sort----')
guest.sort()
print(guest)
guest.reverse()
print(guest)
print('----top5----')
score.sort()
score.reverse()         # 리스트의 내용을 순서만 거꾸로
print(score[:5])        # 5번 인덱스 미만까지 출력
# is instance
print('----is instance----')
for steps in id:
    if isinstance(steps,list):      # steps라는 object가 list이냐?
        for step in steps:          # list이면 다시 for문
            print(step)
    else:                           # list가 아니면 그냥 출력
        print(steps)

# 리스트 요소 엑세스
print('----extend와 append----')
score.extend([60,50])       # extend는 리스트만 인자로 받아 리스트의 각 원소를 추가
print(score)
score.append([60,50])       # [60,50] 자체가 원소로 추가됨
print(score)
score.append(10)
print(score)

# tuple
print('----tuple----')
t1 = ()
t2 = (1)
t3 = (1,)
t4 = (1,2,3)
t5 = 1,2,3
t6 = ('a','b',('ab','cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)