def sum_list(arg1):
  sum = 0
  for num in arg1:
    sum = sum + num
  return sum

def filter_list(arg1):
  odd, even = [], []
  for num in arg1:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return {"odd": odd, "even": even}

# Create a function that accepts a list
# Filters odd from even
# Returns a dictionary like below:
# Note: You can use above function for next exercise
#{
#  "odd": {
#    "sum": 100,
#    "list": [1,3,5...]
#  },
#  "even": {
#    "sum": 100,
#    "list": [2,4,6...]
#  }
#}
lista1 = [1,2,3,4,5,6,7,8]
def advanced_filter_sum(arg1):
  filtered_lists = filter_list(arg1)
  odd_sum = sum_list(filtered_lists["odd"])
  even_sum = sum_list(filtered_lists["even"])
  return {
    "odd": {
      "sum": odd_sum,
      "list": filtered_lists["odd"]
    },
    "even": {
      "sum": even_sum,
      "list": filtered_lists["even"]
    }
  }

print(advanced_filter_sum(lista1))
