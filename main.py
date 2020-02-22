# ========================================== 
# 1. using a for loop iterate over a string  
# 2. using a for loop iterate over a list    
# 3. using a for loop iterate over a dictionary
# 3a. using a for loop to iterate over dictionary, only print keys (hint: use keys() method)
# 3b. using a for loop to iterate over dictionary, only print values (hint: use values() method)
# 3c. using a for loop to iterate over dictionary, print both keys and values (hint: use items() method)
# 4. using a for loop to iterate over a dictionary's key and values at same time: 
#    hint - use two variable in for loop and use items() method
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

# 3a. useing a for loop to iterate over a dictionary, only print keys (hint: use keys() method)
# this will provide the similar result to above example 3.
for dictionary_value in some_dictionary.keys():
  print(dictionary_value)
print('--------------******--------------\n')

# 3b. using a for  loop to iterate over dictionary, only print values (hint: use values() method)
for dictionary_value in some_dictionary.values():
  print(dictionary_value)
print('--------------******--------------\n')


#  3c. using a for loop to iterate over dictionary, print both keys and values (hint: use items() method)
for dictionary_value in some_dictionary.items():
  print(dictionary_value)
print('--------------******--------------\n')

# 4. using a for loop to iterate over a dictionary's key and values at same time: 
# hint - use two variable in for loop and use items() method
for key_s_value, value_s_value in some_dictionary.items(): 
  print(key_s_value, value_s_value)