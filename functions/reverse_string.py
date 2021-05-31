def reverse_string(str_inp):
  reversed = ""
  for x in str_inp:
    reversed = x + reversed
  return reversed

print(reverse_string("Agon"))
