### Homework
# write T(n) = ? and Complexity Big-O = ?
def task1(arr):
    for i in arr:
        print(i)
    for j in arr:
        print(j)
# T(n) = n + n = 2n
# Big-O = O(n)

def task2(arr):
    for i in arr:
        for j in arr:
            print(i, j)

    for k in arr:
        print(k)
# T(n) = n^2 + n = n^2
# Big-O = O(n^2)
#Первый блок имеет два цикла: внешний и внутренний. Внутренний цикл вложен во внешний, поэтому количество итераций равно n⋅n=n^2

def task3(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)
    for x in arr:
        for y in arr:
            print(x, y)

# T(n) = n^3 + n^2
# Big-O = O(n^3)
# Первый блок имеет три цикла: i, j, k. Поэтому количество итераций равно n⋅n⋅n=n^3




