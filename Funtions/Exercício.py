from audioop import reverse
from math import prod, factorial


list1 = [-5, 4, 23, -42, 0, 23, 78, -78, -34]
list2 = [12, 25, -7, 6, 25, 23 -43, -250]
list3 = [2, 3]
number = 5
txt = "Reverter uma string"

def Max_number(args):
  print(max(args))
  
def Sum_Numbers(args):
  print(sum(args))

def Mult_Numbers(args):
  print(prod(args))

def Inverter(args):
  print(args[::-1])

def Factorial_Number(args):
  print(factorial(args))



def Pascal_Tree():
  n = 8

  for i in range(n): 
      for j in range(n-i+1): 
          print(end=" ") 
    
      for j in range(i+1): 
          print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ") 
      print()

def Pascal_Tree2():
  n = 8
    
  for i in range(1, n+1): 
      for j in range(0, n-i+1): 
          print(' ', end='') 
    
      
      C = 1
      for j in range(1, i+1): 
          print(' ', C, sep='', end='') 
          C = C * (i - j) // j 
      print()


Max_number(list1)
Sum_Numbers(list1)
Mult_Numbers(list3)
Inverter(txt)
Factorial_Number(number)
Pascal_Tree()
Pascal_Tree2()
