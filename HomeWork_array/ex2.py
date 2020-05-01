class ex2(object):
    @classmethod
    #приводит к тому, что в правом верхнем углу массива оказывается минимальный
#элемент
    def get_ex_method(self):
        from random import random
        N=int(input(print("Введите число N:")))
        a = []
        for i in range(N): #создание матрицы
            z = []
            for j in range(N):
                  n = int(random() * 50) - 25
                  z.append(n)
                  print("%4d" % n, end='')
            print()
            a.append(z)
        print()
        min=a[i][j]
        b=0
        z=0
        for i in range(N): #поиск минимального значения
            for j in range(N):
                if (a[i][j]<min):
                    min=a[i][j]
                    b=i
                    z=j
        print("Минимальное значение: ",min, " строка: ",b+1, " столбец: ",z+1)
        for j in range(N): #обмен строк
            buff=a[b][j]
            a[b][j]=a[0][j]
            a[0][j]=buff
        for i in range(N): #обмен столбцов
            buff=a[i][z]
            a[i][z]=a[i][N-1]
            a[i][N-1]=buff
        for i in range(N): #вывод результата
            for j in range(N):
                print("%4d"%a[i][j], end='')
            print()

