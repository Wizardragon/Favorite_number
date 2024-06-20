import sys
sys.path.insert(1, './tools')
import math_tools
import math
from numba import njit

last_number_1 = 1
social_numbers_list = []
prime_numbers_list = []
happy_numbers_list = []
perfect_numbers_list = []
friend_numbers_list = []
social_numbers_list = []
already_founded_numbers = []

def verificator_happy_number (last_number): 

  num = last_number

  list_temp = list(str(num))                      
  count  = 0

  while count < 8 :
    count += 1
    sum_of_powers = 0

    for element in list_temp:                
      num_temp = int(element)**2               
      sum_of_powers += num_temp    

    if sum_of_powers == 1:
      happy_numbers_list.append(num)                
      break

    #elif count == 8 :                                     
    #  break

    else :
      list_temp = list(str(sum_of_powers))
      continue     
  
    pass

def verificator_prime_number(last_number):

  number = last_number
  prime = math_tools.prime_checker(number)
  if prime:
    prime_numbers_list.append(number)
    prime_number = number
    calculator_perfect_number(prime_number)
    return prime_number

  """else:
    social_temp = []
    current_number = number
    counter = 0
    while  counter < 5:
      counter = counter + 1
      list_temp = []
      social_num = sum(math_tools.get_divisors(number))
      
      if social_num in social_temp:
        if len(social_temp) == 1:
          social_temp = social_temp[0]
          perfect_numbers.append(social_temp)
          break

        for element in social_temp:
          perfect = math_tools.perfect_checker(element)
          if perfect:
            return False
        a = False
        counter = 0
        while a == False:
          length =len(list_temp)
          if counter < 0:
            social_temp = list_temp
          list_temp =[]
          counter += 1
          print(social_temp)
          for element in social_temp:
            x = sum(math_tools.get_divisors(element))
            if x  not in list_temp:
              list_temp.append(x)
          if len(list_temp) == length:
            a = True                
          else:
            a = False

        period = len(list_temp)
        list_temp.sort()  
        list_temp.append(period)      
        social_numbers.append(list_temp)
        
        break
      social_temp.append(social_num)
      #print (social_temp)
      number = social_num"""
      
def calculator_perfect_number(prime_number):
  index = 2
  while index < (prime_number):
    my_value_should_be_two = (prime_number+1)**(1/index)
    if my_value_should_be_two.is_integer() and my_value_should_be_two == 2.0:     
      perfect_number = (2**(index - 1)) * prime_number
      perfect_numbers_list.append(perfect_number)
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
@njit
def main ():

  prime_number = 0
  for last_number in range(last_number_1 , last_number_1 + 500):
    
    verificator_happy_number(last_number)
    
    
    verificator_prime_number(last_number)


    social_numbers_seeker(last_number)


    if prime_number != 0:
      calculator_perfect_number(prime_number)


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
