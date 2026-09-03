import turtle as t

#사용자 답변 받는 변수
answer = ''

#헬로월드 출력
print("hi world")

#원하는 기능 입력받음
answer = input("원하는 기능을 입력하세요. (터틀 / 나이계산기):   ")


if answer == "터틀":
    #새 터틀 객체 생성
    goodTurtle = t.Turtle()

    #사각형 그리기
    for i in range(4):
        goodTurtle.forward(100)
        goodTurtle.right(90)

    t.done()

else:
    #입력받은 기능이 없을 경우
    print("그런건 없음 ㄲㅈ")

print("끝")