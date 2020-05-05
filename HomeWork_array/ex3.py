class ex3(object):
    @classmethod
    #заменяет в исходном массиве A каждый элемент суммой его 1-окружения (11.2)
    def get_ex_method(self):
        import random
        from random import randint
        N=int(input(print("Введите число N:")))
        A =[]
        c=N
        N+=2   
        A= [[0 for j in range(N)] for i in range(N)] #формирования массива с рамкой из 0
                   
             
        for i in range(1,c+1,1): #заполнение массива NxN(входные данные)
            for j in range(1,c+1,1):
                 A[i][j]=randint(0,5) 
        print("Исходный массив:")
        for i in range(1,c+1,1): #вывод начального массива
            for j in range(1,c+1,1):
                 print(A[i][j], end=' ')
            print()
        Z=[[],[]]
        Z= [[0 for j in range(c)] for i in range(c)] #Формирование нового массива
        n=0 #сумма чисел 1 окружения
        for i in range(1,c+1,1): #сложение чисел 1 окружения
            for j in range(1,c+1,1):
                n=A[i][j-1]+A[i-1][j]+A[i+1][j]+A[i][j+1]
                Z[i-1][j-1]=n
        print("Результат:")
        for i in range(len(Z)): #вывод получившегося массива
            for j in range(len(Z[i])):
                print(Z[i][j], end=' ')
            print()


                                  
     
           



             
                 


