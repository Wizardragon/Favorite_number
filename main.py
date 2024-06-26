import numba
from numba import njit
from numba.typed import List


last_number_1 = 1
social_numbers_list = List()
prime_numbers_list = List()
happy_numbers_list = List()
perfect_numbers_list = List()
friend_numbers_list = List()
social_numbers_list = List()
already_founded_numbers = List()

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
  return divisors  



@njit
def prime_checker (number,divisors):
  if number == 1:
    return False
  if len(divisors) == 1:
    return number
  else:  
    False

@njit
def number_to_digit_list(number):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits

@njit
def verificator_happy_number(number): 
  list_temp = number_to_digit_list(number)                      
  count  = 0
  while count < 8 :
    count += 1
    sum_of_powers = 0

    for element in list_temp:                
      num_temp = (element)**2               
      sum_of_powers += num_temp    

    if sum_of_powers == 1:
      happy_numbers_list.append(number)
      break               

    else :
      list_temp = number_to_digit_list(sum_of_powers)
      continue
  return 0

@njit
def verificator_prime_number(number,divisors):

  prime = prime_checker(number,divisors)
  if prime:
    prime_numbers_list.append(number)
    prime_number = number
    calculator_perfect_number(prime_number)


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
 
def social_numbers_seeker(last_number):
  number = last_number
  number_test = last_number
  counter = -1
  temporal_list = []
  
  while counter < 30:
    
    counter += 1
    next_number = sum(math_tools.get_divisors(number)) 
    if next_number in already_founded_numbers:
      break
    if next_number == number:
      break
    if next_number in temporal_list:      
      if counter == 2:
        friend_numbers_list.append(temporal_list)
        for element in temporal_list:
          already_founded_numbers.append(element)
        break
      else:
        if number_test not in temporal_list:
          break
        for element in temporal_list:
          already_founded_numbers.append(element)   
        temporal_list.append(counter)
        social_numbers_list.append(temporal_list) 
        break
    temporal_list.append(next_number)
    number=next_number    

def main ():
  social_numbers_list = List()
  prime_numbers_list = List()
  happy_numbers_list = List()
  perfect_numbers_list = List()
  friend_numbers_list = List()
  social_numbers_list = List()
  already_founded_numbers = List()


  for last_number in range(last_number_1 , last_number_1 + 500):
    
    verificator_happy_number(last_number)
    
    
    verificator_prime_number(last_number)


    social_numbers_seeker(last_number)



  with open ("./happy_numbers.txt", "a") as f:
    for element in happy_numbers_list:
      f.write(str(element) + ",")
  """with open ("./social_numbers.txt", "a") as f:
    for element in social_numbers:
      f.write(str(element) + ",")"""
  with open ("./prime_numbers.txt", "a") as f:
    for element in prime_numbers_list:
      f.write(str(element) + ",")
  with open ("./perfect_numbers.txt", "a") as f:
    for element in perfect_numbers_list:
      f.write(str(element) + ",")


if __name__ == '__main__':
  main()
  print(f'estos son los número perfectos {perfect_numbers_list}')
  print(f'estos son los número primos {prime_numbers_list}')
  print(f'estos son los número felices {happy_numbers_list}')
  print(f'estos son los número amigos {friend_numbers_list}')
  print(f'estos son los número sociales {social_numbers_list}')
