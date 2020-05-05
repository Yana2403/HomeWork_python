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
        for i in range (N):
             for j in range (N):
              A.append(0)    
       # A= [[0 for j in range(N)] for i in range(N)] - с этим работает вроде
                   
             
        for i in range(1,c+1,1):
            for j in range(1,c+1,1):
                 A[i][j]=randint(0,25) #'int' object does not support item assignment
                                  
     
           



             
                 


