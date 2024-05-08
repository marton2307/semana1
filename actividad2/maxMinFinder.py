def find_max_min(array):
    if len(array) == 0:
        return None, None 

    minimum = maximum = array[0]  
    
    for element in array:
        if element < minimum:
            minimum = element  
        elif element > maximum:
            maximum = element  
    return maximum, minimum

array = [3, 1, 9, 7, 5, 9]
max1, min1 = find_max_min(array)
print("Array - Max =", max1, ", Min =", min1)

