num_list = [10,20,100,3,5,7,123,12,15]
lista_numer_2 = [101,203,101,6,5,7,123,12,15]

def filter_list(arg1):
  odd, even = [], []
  for num in arg1:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return {"odd": odd, "even": even}

lista1 = filter_list(num_list)
lista2 = filter_list(lista_numer_2)

print(lista1)
print(lista2)


def sum(a, b, c):
  return a + b + c

print(sum(1,2,3))
print(sum(0,0,0))
