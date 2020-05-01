class matrix:
    #matrix28
    #Найти минимальный среди максимальных элементов ее столбцов
    @classmethod
    def get_ex_method(self): 
         from random import randint

         M=int(input( print("Enter M"))) #столбы      
         N=int(input(print("Enter N"))) #строки
        
         matrix_create= [[randint (10, 40) for j in range(M)] for i in range(N)]
         print(matrix_create)
     
         for i in range(1, M, 1):
             max=matrix_create[0][i]
             for j in range(1,N, 1):
                 if matrix_create[0][i]>max:
                     max=matrix_create[j][i]
             if i==1:
                 minmax=max
             elif max<minmax:
                 minmax=max
         print(minmax)
