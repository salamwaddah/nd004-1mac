def locate_first(string, target):
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            return index
        else:
            index += 1

    return -1


# Here are a couple function calls to test with.

# This one should return 1
print(locate_first('cookbook', 'ook'))

# This one should return -1
print(locate_first('all your bass are belong to us', 'base'))
