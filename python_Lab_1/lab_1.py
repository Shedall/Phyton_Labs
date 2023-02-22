print('Helow world')

arr = list(range(20))
arr_anser = list()
for i in arr:
    if (i % 2 == 0) and (i != 0):
        arr_anser += [i]
print(arr_anser)