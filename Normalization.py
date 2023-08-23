
def NORMALIZATION(max):
    a = []
    for i in range(max):
        try:
            a.append(i/(max-1)*100)
        except ZeroDivisionError:
            a.append(0)
    return a
