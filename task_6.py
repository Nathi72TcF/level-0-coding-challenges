def maximum_number(*arguments):
    number = 0
    *create_list, = arguments 
    duplicates = [i for i in create_list]
    small_numbers = [i for i in create_list for j in duplicates if i < j]
    for i in duplicates:
        if i not in small_numbers:
            number = i
    print(number)
    return number

maximum_number(5, 4, 5)
