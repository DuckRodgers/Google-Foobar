def solution(m,f):
    if int(m) < 10e50 and int(f) < 10e50:
        if int(m) > 0 and int(f) > 0:
            m_int = int(m)
            f_int = int(f)
            count = 0
            while True:
                if f_int == 1 and m_int == 1:
                    print(int(count))
                    break
                elif f_int > m_int:
                    if f_int%m_int == 0 and m_int != 1:
                        print('impossible')
                        break
                    elif f_int%m_int == 0 and m_int == 1:
                        if f_int%2 == 0:
                            count += f_int/2
                            f_int/= 2
                        else:
                            count += f_int - 1
                            print(int(count))
                            break
                    else:
                        count += int(f_int/m_int)
                        f_int -= int(f_int/m_int)*m_int
                elif m_int > f_int:
                    if m_int == 1 and f_int == 1:
                        print(int(count))
                        break
                    elif m_int%f_int == 0 and f_int != 1:
                        print('impossible')
                        break
                    elif m_int%f_int == 0 and f_int == 1:
                        if m_int%2 == 0:
                            count += m_int/2
                            m_int/= 2
                        else:
                            count += m_int - 1
                            print(int(count))
                            break
                    else:
                        count += int(m_int/f_int)
                        m_int -= int(m_int/f_int)*f_int
                else:
                    print('impossible')
                    break
