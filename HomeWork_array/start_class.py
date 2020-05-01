import ex1,ex2,ex3,ex4,ex5, matrix, array56
class start_class:
     @classmethod
     def get_start(self):
                print('''Введите число для запуска программы: 
                1 -array56; 
                2- matrix; 
                3- задача 1; 
                4- задача 2; 
                5- задача 3;
                6-задача 4;
                7-задача 5.''')
                n=int(input())
                if n == 1:
                     play=array56
                     play.array56.get_ex_method()
                elif n==2:
                       play=matrix
                       play.matrix.get_ex_method()
                elif n==3:
                    play= ex1
                    play.ex1.get_ex_method()
                elif n==4:
                    play=ex2
                    play.ex2.get_ex_method()
                elif n==5:
                    play=ex3
                    play.ex3.get_ex_method()
                elif n==6:
                    play=ex4
                    play.ex4.get_ex_method()
                elif n==7:
                    play=ex5
                    play.ex5.get_ex_method()


  



