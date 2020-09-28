def solution(n, b):
    if (b >= 2 and b<= 10):
        k = len(str(n))
        if (k >= 2 and k <= 9):
            
            def convert_10(num,base):
                if base==10:
                    return num
                else:
                    num = str(num)
                    leng = [x for x in num]
                    i = 0
                    j = 0
                    for l in leng:
                        i += int(l)*base**((len(leng)-1)-j)
                        j+=1
                    return i
                      
            def convert_base(num,base):
                res = []
                if base==10:
                    return num
                else:
                    while num > 0:
                        i = num%base
                        res.append(str(i))
                        num = int(num/base)
                    res = res[::-1]
                    sol = "".join(res)
                    sol = int(sol)
                    return sol
                    
                    
            final = []
            while True:
                sol = str(n)
                x = list(sol)
                y = list(sol)
                x.sort(reverse=True)
                y.sort()
                x = int("".join(x))
                y = int("".join(y))
                x = convert_10(x,b)
                y = convert_10(y,b)
                z = x-y
                n = convert_base(z,b)
                quick = str(n)
                list_n = [x for x in quick]
                while len(list_n) != k:
                    list_n.insert(0,'0')
                    n = "".join(list_n)
                if n not in final:
                    final.append(n)
                else:
                    hire_me = len(final) - final.index(n)
                    return hire_me
                    break
