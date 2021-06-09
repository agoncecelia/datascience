def check_palindrome(arg):
  reversed = ""
  for i in arg:
    reversed = i + reversed
  if reversed.lower() == arg.lower():
    return True
  return False

print(check_palindrome("Talat"))
