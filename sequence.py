def remove_duplicates(sequence):
    sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = []
    [result.append(x) for x in sequence if x not in result]
    print(result)


