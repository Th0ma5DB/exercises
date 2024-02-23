# Write your code here
def median(ns):
    list = sorted(ns)
    middle = len(list) // 2

    if len(list) % 2 == 0:
        return (list[middle - 1] + list[middle]) / 2
    else:
        return list[middle]