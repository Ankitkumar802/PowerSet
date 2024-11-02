


def find_subsets(s):
    subsets = [[]]
    for element in range(len(s)):
        for element1 in range(element +1, len(s) + 1):
            subsets.append(s[element:element1])
    return subsets

input_set = input("enter a string")
print("all substring", find_subsets(input_set))