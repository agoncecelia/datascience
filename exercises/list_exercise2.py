a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Forma 1
def find_unique(a, b):
  c = []
  for i in a:
    for x in b:
      if x == i and x not in c:
        c.append(x)
  return c

# Forma 2
a = set(a)
b = set(b)
c = a.intersection(b)
print(c)


list1 = [1, 1, 2, 3, 1, 144, 13, 21, 34, 55, 89]
list2 = [1, 8, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unique_list = find_unique(list1, list2)
print(unique_list)
print(find_unique(a, b))
