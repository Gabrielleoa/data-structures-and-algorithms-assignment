def remove_duplicates(sequence):
    sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = []
    [result.append(x) for x in sequence if x not in result]
    print(result)


#    result = []
#    for n in sequence:
#       if n not in result:
#          if n not in result:
#             result.append(n)
# sequence = 2, 3, 2, 4, 5, 3, 6, 7, 5
# result = remove_duplicates(sequence)
# print(result)
          