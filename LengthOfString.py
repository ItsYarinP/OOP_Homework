def length_of_string(string_to_check: str):
    if string_to_check == '':
        return 0
    return 1 + length_of_string(string_to_check[1:])


if __name__ == '__main__':
    string = "booooooo"
    result = length_of_string(string)
    print(result)
