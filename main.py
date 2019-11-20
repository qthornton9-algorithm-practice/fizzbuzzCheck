def fizzBuzz():
  for i in range(1,101):
    print(i)
    if i % 3 == 0 and i % 5 ==0:
      print(f"{i}: fizz buzz")
    elif i % 3 == 0:
      print(f"{i}: fizz")
    elif i % 5 == 0:
      print(f"{i}: buzz")
fizzBuzz()