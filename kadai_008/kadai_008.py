import random
var = random.randint(1, 10)
print(var)
if var %3 == 0:
  print("Fizz")
elif var %5 == 0:
  print("Bazz")
elif var %3 == 0 and var %5 == 0:
  print("FizzBuzz")
else:
  print("and条件が成り立ちませんでした")
