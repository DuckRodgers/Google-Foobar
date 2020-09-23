def solution(entry):
    answer = []
    while (entry >= 1 and entry <= 1000000):
      for lilnum in range(entry,1-1,-1):
        if lilnum**2 > entry:
            pass
        else:
            answer.append(lilnum)
            entry = entry - lilnum**2
      while entry>0:
        answer.append(1)
        entry -= 1
