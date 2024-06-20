
import math

def get_divisors (number):

  divisors = []

  if number == 1:

      divisors.append(1)
      return divisors
 
  square = int(math.isqrt(number))
  #divisors.append(1)
  step = 2 if number%2 else 1
  for i in range (1,  square + 1, step): 
      if number % i == 0:

        divisors.append(i)

        if i != 1 :
          divisors.append(number//i)
  divisors = list(set(divisors))
  divisors.sort()
  return divisors  




def prime_checker (number):
  if number == 1:
    return False
  elif number == 2:
    return True
  elif number % 2 == 0:
    return False
  square = math.isqrt(number)
  for i in range(3, square + 1,2):     
    if number % i == 0:
      return False
  return True


def perfect_checker (number):
  divisors = []

  if number == 1:

      divisors.append(1)
      return False
 
  square = int(math.isqrt(number))
  step = 2 if number%2 else 1
  for i in range (1,  square + 1, step): 
      if number % i == 0:

        divisors.append(i)

        if i != 1 and i:
          divisors.append(number//i)
  divisors = list(set(divisors))
  if sum(divisors) == number:
    return True 
  else:
    return False