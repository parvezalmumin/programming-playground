# Assigning  a default value to parameter, which is used when no argument is passed
def call(a, b = 3):
  print( a * b)
  return a * b
call(2)

# Here, no-default value comes first, and default value comes second .
# def call(a = 3, b):
#   print( a * b)
#   return a * b
# call(2)
# Ths code will give error