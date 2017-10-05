def map(key, value):
    intermediate = []
    for columnIndex in range(0, len(value)):
        intermediate.append({columnIndex: {key: value[columnIndex]}})
        # The goal is to put the columnIndex as the new key because it will become the new row index
        # We put the key in the dictionnary to help the shuffle&sort to sort
    print(intermediate)
    return intermediate


map(0, [1, 2, 3, 4])
map(1, [5, 6, 7, 8])
map(2, [9, 0, 1, 2])

# We suppose that the shuffle and sort put all the infos in the good order
def reduce(new_key, new_value):
    transposevalues = []
    for columnIndex in new_value:
        transposevalues.append(new_value[columnIndex])
    print({new_key: transposevalues})
    return {new_key: transposevalues}
    # We return a list with all the values and their key


reduce(0, {0: 1, 1: 5, 2: 9})
reduce(1, {0: 2, 1: 6, 2: 0})
reduce(2, {0: 3, 1: 7, 2: 1})
reduce(3, {0: 4, 1: 8, 2: 2})
