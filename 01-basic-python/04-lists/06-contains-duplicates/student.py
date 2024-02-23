# Write your code here
def contains_duplicates(xs):
    for i in range(len(xs)):
        for x in range(i + 1, len(xs)):
            if xs[i] == xs[x]:
                return True
    return False