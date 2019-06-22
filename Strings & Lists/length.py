# Add your code here.
def total_length(l):
    total = 0
    for i in l:
        total = total + len(i)
    return total


# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
print(total_length(["", '', "", '']))
