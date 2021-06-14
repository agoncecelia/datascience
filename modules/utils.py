def return_average(list):
    sum = 0
    for el in list:
        sum += el.get_average()
    return sum / len(list)