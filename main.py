# a = {1, 2, 3, 4, 5}
# b = {2, 4, 5}

# for a in b:
#     if a in b:
#         print(a,'is a subset')
#     else:
#         print(b,"is a set")



def find_subsets(s):
    subsets = [[]]
    for element in s:
        subsets += [current +[element] for current in subsets]
    return subsets
input_set = [1,2,3]
print("all subsets", find_subsets(input_set))