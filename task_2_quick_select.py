def quick_select(array, k):
    # base case - array with one element
    if len(array) <= 1:
        return array[0]

    # choose pivot
    pivot = array[len(array) // 2]

    # devide array into three parts
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # search for k-th min element
    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return quick_select(right, k - len(left) - len(middle))


if __name__ == "__main__":
    numbers = [
        11,
        82,
        32,
        43,
        25,
        16,
        7,
        81,
        39,
        104,
        19,
        22,
        92,
        63,
        55,
        106,
        17,
        77,
        90,
        15,
    ]
    k = 5  # Find the 5th smallest element
    res = quick_select(numbers, k)
    print(f"The {k}-th minimum element is: {res}")
