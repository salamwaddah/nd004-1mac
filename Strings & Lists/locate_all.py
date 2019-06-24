def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches


# Here are a couple function calls to test with.
print(locate_all('cookbook', 'ook'))
# [1, 5]
print(locate_all('yesyesyes', 'yes'))
# [0, 3, 6]
print(locate_all('the upside down', 'barb'))
# []
