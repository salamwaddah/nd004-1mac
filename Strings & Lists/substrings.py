# Write your code here
def is_substring(needle, haystack):
    for index in range(len(haystack)):
        if (haystack[index:index + len(needle)] == needle):
            return True
    return False


# Below are some calls you can use to test it

# This one should return False
print(is_substring('bad', 'abracadabra'))

# This one should return True
print(is_substring('dab', 'abracadabra'))
