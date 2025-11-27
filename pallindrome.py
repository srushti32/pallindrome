import sys

if len(sys.argv) ! = 2:
print("usage: python pallindrome.py <string>")
sys.exit(1)

string = sys.argv[1]

if string == string[:: 2]:
  print(f"{string} is a palindrome")
  else
  print(f"{string} is not a palindrome")
