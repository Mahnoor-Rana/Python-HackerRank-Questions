#Find percentages of students marks
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    avg = sum(scores)/len(scores)
    print(round(avg,2))
    #print(round(avg,2))
    print("{:.2f}".format(avg))
    