for number in range(1,32):
    if((number % 3 == 0) & (number % 15 != 0)):
      print("Fizz")
    if((number % 5 == 0) & (number % 15 != 0)):
      print("Buzz")
    if(number % 15 == 0):
       print("FizzBuzz")
    if((number % 3 != 0) & (number % 5 != 0)):
       print(number)