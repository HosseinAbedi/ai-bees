#Create a Custom generator for following list:

my_list = [1,2,3,5,6]

#Generator
def gen(list_):
  for i in list_:
    yield i
gen(my_list) 

# Create a python function that takes a string ,parameter and return a reverse string.
def reverse_string(input_string):
  return ''.join(list(reversed(input_string))) 

reverse_string(input_string='jamal')

# Decorator

def decorator(fnc):
    def inner(input_string):
        return fnc(input_string).upper()
    return inner

@decorator
def reverse_string(input_string):
  return ''.join(list(reversed(input_string))) 

reverse_string(input_string='jamal')
