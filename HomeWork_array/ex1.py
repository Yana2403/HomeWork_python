class ex1(object):
    @classmethod
    #определяет, верно ли, что никакой из положительных элементов не превосходит по
    #модулю любой из отрицательных элементов, расположенных в массиве правее него (числа
    #– вещественные)
    
    def get_ex_method(self):
        import math
        a = [] # заводим пустой список
        n = int(input(print("Введите число элементов"))) # считываем количество элемент в списке
        for i in range(n):
              a.append(int(input(print("Введите элемент")))) # добавляем элемент в список
        print(a)


        def check(i):
            
            if a[i] >=0 and a[i]<abs(a[i+1]):
                return check(i+1)
            elif a[i]<0:
                 return check(i+1)
            else:
                return 1

        check(0)
        
            

