def miniCalculatir(numb_1,numb_2,operat):
    if (operat == "+"):
        return numb_1 + numb_2
    if (operat == "-"):
        return numb_1 - numb_2
    if (operat == "*"):
        return numb_1 * numb_2
    if (operat == "/"):
        if(numb_2 == 0):
            return "invalid input, divide by zero"
        return numb_1 / numb_2

def helow_world():
    print('Helow world')

def listeven():
    arr = list(range(20))
    arr_anser = list()
    for i in arr:
        if (i % 2 == 0):
            arr_anser += [i]
    print(arr_anser)