print('Helow world')


arr = list(range(20))
arr_anser = list()
for i in arr:
    if (i % 2 == 0) and (i != 0):
        arr_anser += [i]
print(arr_anser)


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

while(True):
    try:
        print ("please,enter a number_1")
        numb_1 = input()
        numb_1 = float(numb_1)
        print ("please,enter a number_2")
        numb_2 = input()
        numb_2 = float(numb_2)
        break
    except  ValueError:
        print("incorrect data entered,please try again")

print ("please,enter a operator")
while(True):
    operat = input()
    if (operat == "+") or (operat == "-") or (operat == "*") or (operat == "/"):
        print("anser = ",miniCalculatir(numb_1,numb_2,operat))
        break
    else:
        print("The operator was entered incorrectly, please try again")