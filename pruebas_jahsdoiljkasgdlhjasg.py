import numba
from numba import njit
perfect_numbers_list=[]
from numba.typed import List

"""
num= 100000
list_temp = list(str(num))
print(list_temp)
list_temp=[int(element)for element in list_temp]
print (type(list_temp[2]))
print(list_temp)
"""
"""
@njit
def porte():
  num =10
  square =int(((num**0.5)))
  print(square)
  square_2 = 3/square
  return square_2
square_2=porte()
print(square_2)

number = 37

@njit

def get_divisors (number):

  divisors = List()
  if number == 1:

      divisors.append(1)
      return divisors
 
  square = square =int(((number**0.5)))
  step = 2 if number%2 else 1
  for i in range (1,  square + 1, step): 
      if number % i == 0:

        divisors.append(i)

        if i != 1 :
          divisors.append(number//i)
  #divisors = list(set(divisors))
  #divisors.sort()
  return divisors
#print(type(get_divisors))
number = int(input("number pls -->  "))  



@njit
def prime_checker (number,divisors):
  if number == 1:
    return False
  if len(divisors) == 1:
    return True 
  else:  
    return False

divisors= get_divisors(number)
print (type(divisors))
print(prime_checker(number,divisors))

"""
"""
@njit
def calculator_perfect_number(prime_number):
  index = 2
  while index < (prime_number):
    my_value_should_be_two = (prime_number+1)**(1/index)
    if  my_value_should_be_two == 2:     
      perfect_number = (2**(index - 1)) * prime_number
      return perfect_number
      break
    else:
      index +=1
      continue
print(calculator_perfect_number(8191))
print(int(2))
print(int(2.3))
print(int(2.9))
print (2==2.0)
"""

prime_number = int(input("number --> "))
def calculator_perfect_number(prime_number):
    index = 2
    while index < prime_number:
        if (prime_number + 1) == 2 ** index:
            perfect_number = (2 ** (index - 1)) * prime_number
            return perfect_number
        index += 1
    return 0
r = calculator_perfect_number(prime_number)
print(r)