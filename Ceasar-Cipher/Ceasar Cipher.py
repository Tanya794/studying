def caesar_cipher(string, offset):
  lst = []
  
 
  for item in string:
    lst.append(ord(item))
  
  for i in range(len(lst)):
    lst[i] = lst[i] - offset
  
  for i in range(len(lst)):
    if lst[i] <= 96:
      lst[i] = 26 + lst[i]

  
  
  letters = ""
  for num in lst:
    letters += chr(num)
  return letters
