

def surpriseList(x):
    y = 0

    while (y < x):

        list = []
        list[y] = y
        y += 1 

    return list

a = int(input())
print(surpriseList(a))
