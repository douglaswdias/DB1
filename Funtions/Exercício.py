from audioop import reverse
from math import prod


list1 = [-5, 4, 23, -42, 0, 23, 78, -78, -34]
list2 = [12, 25, -7, 6, 25, 23 -43, -250]
list3 = [2, 3]
txt = "Reverter uma string"

def Max_number(args):
  print(max(args))
  
def Sum_Numbers(args):
  print(sum(args))

def Mult_Numbers(args):
  print(prod(args))

def Inverter(args):
  print(args[::-1])




Max_number(list1)
Sum_Numbers(list1)
Mult_Numbers(list3)
Inverter(txt)
