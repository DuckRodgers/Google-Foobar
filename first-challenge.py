def solution(entry):
    answer = []
    while (entry >= 1 and entry <= 1000000):
      sol = int(entry**0.5)
      answer.append(sol)
      entry -= sol**2
    new_answer = [var**2 for var in answer]
    print(*new_answer,sep=",")
