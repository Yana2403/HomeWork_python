class array56:
    #Дан целочисленный массив A размера N (≤ 15). Переписать в новый 
    #целочисленный массив B все элементы с порядковыми номерами, кратными трем (3, 6, . . .), 
    #и вывести размер полученного массива B и его содержимое. Условный оператор не использовать.
    @classmethod
    def get_ex_method(self):
        N = 0
        while N <= 0 or N > 15:
          N = int(input("Введите N(<=15): "))

        A = []
        for i in range(N):
            A.append(int(input("Введите " + str(i + 1) + " int: ")))

        B = []
        x = 2
        while x < len(A):
             B.append(A[x])
             x += 3
        print("Размер В = " + str(len(B)))
        for i in range(len(B)):
               print(B[i])

          

