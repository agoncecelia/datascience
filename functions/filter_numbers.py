num_list = [1, 3, 100, 30, 25, 33, 18, 19]

def count_even_odd(num_list):
  even_count = 0
  odd_count = 0
  for num in num_list:
    if num % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return even_count, odd_count

print(count_even_odd(num_list))

# Return list of even and list of odd numbers

def filter_numbers(num_list):
  odd, even = [], []
  for num in num_list:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return even, odd

def advanced_filter(num_list):
  odd, even = [], []
  odd_count, even_count = 0, 0
  for num in num_list:
    if num % 2 == 0:
      even.append(num)
      even_count += 1
    else:
      odd.append(num)
      odd_count += 1

  data = {
    "even": {
      "count": even_count,
      "list": even
    },
    "odd": {
      "count": odd_count,
      "list": odd
    }
  }
  return data

print(advanced_filter(num_list))
