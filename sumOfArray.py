def sum_of_array(int_array: [int]):
    if len(int_array) == 0:
        return 0
    else:
        return int_array[0] + sum_of_array(int_array[1:])


if __name__ == '__main__':
    array_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_of_array(array_of_numbers)
    print(result)
