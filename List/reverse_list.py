# Define a function named 'reverse' that takes a list as its parameter.
def reverse(list):

    length = len(list)

    n = length

    new_list = [None]*length

    for val in list:
        n = n - 1
        new_list[n] = val 



record = reverse([1,2,3,4,5,6])

print(record)