# ========================================== 
# 1. using a for loop iterate over a string  
# 2. using a for loop iterate over a list    
# 3. using a for loop iterate over a dictionary
# 3a. useing a for loop wiht dictionary, only print keys (hint: use keys() method)
# ========================================== 

# 1. using a for loop iterate over a string
some_string = 'Lorem ipsum dolor sit amet'
for specific_string_value in some_string:
  print(specific_string_value)
print('--------------******--------------\n')

# 2. using a for loop iterate over a list 
some_list = ['kiwi', 'mango', 'apple', 'watermelon', 'papaya']
for specific_list_value in some_list: 
  print(specific_list_value)
print('--------------******--------------\n')

# 3. using a for loop iterate over a dictionary 
some_dictionary = {
  'username': 'Kevin',
  'password': 12345, 
  'location': 'Cali'
}
for dictionary_value in some_dictionary: 
  print(dictionary_value)
print('--------------******--------------\n')

# 3a. useing a for loop wiht dictionary, only print keys (hint: use keys() method)
# this will provide the similar result to above example 3.
for dictionary_value in some_dictionary.keys():
  print(dictionary_value)
print('--------------******--------------\n')
