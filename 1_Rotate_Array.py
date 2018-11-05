input_as_string = raw_input("Enter the array")

array = [int(x) for x in input_as_string.split()]
dummy_array = array[:] # Slicing the whole 

steps = input("How many places you want to shift: ")

for element in array:
    print 'element in action is: ',element
    index = array.index(element)
    length = len(array)
    if (index + steps + 1) >= length:
        print element, index, index + steps - length
        dummy_array[index + steps - length] = element
        print 'dummy: ', dummy_array
    else:
        print element, index, index + steps
        dummy_array[index + steps] = element
        print 'dummy: ', dummy_array

print dummy_array
