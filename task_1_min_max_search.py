def min_max_search(array, first_index, last_index):
    # base case - array with one element
    if first_index == last_index:
        return array[first_index], array[first_index]
    
    # base case - array with two elements
    if last_index == first_index+1:
        if array[first_index] < array[last_index]:
            return array[first_index], array[last_index]
        else:
            return array[last_index], array[first_index]
        
    # devide array into two parts and recursively call min_max_search
    middle_index = (first_index + last_index) // 2
    min_left, max_left = min_max_search(array, first_index, middle_index)
    min_right, max_right = min_max_search(array, middle_index+1, last_index)

    return min(min_left, min_right), max(max_left, max_right)

if __name__ == '__main__':
    numbers = [11, 82, 32, 43, 25, 16, 7, 81, 39, 104, 19, 22, 92, 63, 55, 106, 17, 77, 90, 15]
    res=min_max_search(numbers, 0, len(numbers)-1)
    print(res) # (7, 106)




