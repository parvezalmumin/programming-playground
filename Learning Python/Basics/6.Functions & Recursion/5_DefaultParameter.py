# Assigning  a default value to parameter, which is used when no argument is passed
def call(a = 2, b = 3):
  print( a * b)
  return a * b
call()