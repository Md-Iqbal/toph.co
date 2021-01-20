def encrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

  return cipher

s = int(input())
text = input()
print(encrypt(text, s))