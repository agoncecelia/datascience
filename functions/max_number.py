num_list = [100, 100, 4000, 20, 150, 350, 3895, 100]

def max_num(n_l):
  max_num = n_l[0]
  for x in n_l:
    if x > max_num:
      max_num = x
  return max_num

print(max_num(num_list))
