import numba
import timeit

@numba.njit
def number_to_digit_list(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits
@numba.njit
      
def verificator_happy_number_numba (num): 
  list_temp = number_to_digit_list(num)                      
  count  = 0
  while count < 8 :
    count += 1
    sum_of_powers = 0

    for element in list_temp:                
      num_temp = (element)**2               
      sum_of_powers += num_temp    

    if sum_of_powers == 1:
      return num               

    else :
      list_temp = number_to_digit_list(sum_of_powers)
      continue
  return 0
@numba.njit
def main_numba(last_number): 
  happy_number_list_numba=[]
  for i in range(1,last_number + 1):
    happy_number = verificator_happy_number_numba(i)
    if happy_number != 0:
      happy_number_list_numba.append(happy_number)
    else:
      continue  
  





def verificator_happy_number (last_number):
  happy_number_list = [] 
  for num in range(1,last_number + 1):

    list_temp = list(str(num))                      
    count  = 0

    while count < 8 :
      count += 1
      sum_of_powers = 0

      for element in list_temp:                
        num_temp = int(element)**2               
        sum_of_powers += num_temp    

      if sum_of_powers == 1:
        happy_number_list.append(num)                
        break

      else :
        list_temp = list(str(sum_of_powers))
        continue     
    
      pass
  return happy_number_list    

if __name__ == '__main__':
  last_number = int(input("pls, insert a number --> "))
  execution_time = timeit.timeit("main_numba(last_number)", globals=globals(), number=10)
  print(f"El tiempo promedio de numba es {execution_time/10}")

  execution_time = timeit.timeit("verificator_happy_number(last_number)", globals=globals(), number=10)
  print(f"El tiempo promedio de python es {execution_time/10}")
