2. 다음 코드 실행 시 출력 결과를 작성하세요.

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

---

# 답변

B
C
B
C
B
C
A