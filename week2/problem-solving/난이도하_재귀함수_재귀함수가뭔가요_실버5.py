# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478


def intro():
    print ("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def question_line(n=0):
    return "____"*n + '"재귀함수가 뭔가요?"'

def story_line1(n=0):
    return "____"*n + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'

def story_line2(n=0):
    return "____"*n + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'

def story_line3(n=0):
    return "____"*n + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

def real_answer(n=0):
    return "____"*n + '"재귀함수는 자기 자신을 호출하는 함수라네"'

def answer_line(n=0):
    return "____"*n + '라고 답변하였지.'

def whole_structure(depth):
    intro()
    i = 0
    j = depth

    while i <= depth:
        print(question_line(i))
        if i < depth:
            print(story_line1(i))
            print(story_line2(i))
            print(story_line3(i))
        if i == depth:
            print(real_answer(i))
        i += 1
    while j >= 0:
        print(answer_line(j))
        j -= 1

N = int(input())
whole_structure(N)


'''
    question_line(0)
    story_line1(0)
    story_line2(0)
    story_line3(0)

    question_line(1)
    story_line1(1)
    story_line2(1)
    story_line3(1)

    question_line(2)
    story_line1(2)
    story_line2(2)
    story_line3(2)

    question_line(3)
    story_line1(3)
    story_line2(3)
    story_line3(3)

    question_line(4)    

    real_answer(4)

    answer_line(4)
    answer_line(3)
    answer_line(2)
    answer_line(1)
    answer_line(0)
    '''


## gpt 코칭 후 수정한 코드

'''
def intro():
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def recursive_dialog(current, target):
    indent = "____" * current

    print(indent + '"재귀함수가 뭔가요?"')

    if current == target:
        print(indent + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(indent + "라고 답변하였지.")
        return

    print(indent + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(indent + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(indent + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    recursive_dialog(current + 1, target)

    print(indent + "라고 답변하였지.")

N = int(input())
intro()
recursive_dialog(0, N)

'''