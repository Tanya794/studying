import random

while True:
  s = input("Enter the start of the range: ")
  if not s.isdigit():
    print("Please enter a valid number.")
    continue  
  else:
    break

while True:
  f = input("Enter the end of the range: ")
  if not f.isdigit() or f < s:
    print("Please enter a valid number.")
    continue
  else:
    break

s = int(s)
f = int(f)

random_number = random.randint(s, f)
t = 1

while True:
  n = input("Guess a number: ")
  if not n.isdigit():
    print("Please enter a valid number.")
    continue
  else:
    
 
    n = int(n)
  if random_number != n:
    t += 1
    continue
  else:
    if t == 1:
      print(f"You guessed the number in {t} attempt")
      break
    else:
      print(f"You guessed the number in {t} attempts")
      break
