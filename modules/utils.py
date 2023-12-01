import re

def string_to_number(input_string, reverse_search = False):
    if len(input_string) == 1 and input_string.isdigit():
        return str(input_string)

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    if not reverse_search:
        search_string = input_string
    else:
        search_string = reversed(input_string)
    
    current = ''
    for c in list(search_string):
        if not reverse_search:
            current += c
        else:
            current = c + current

        for n in numbers:
            if n in current:
                return str(numbers.index(n)+1)

    return None

def decode_coodinate(input_string):
    if len(input_string) == 1:
        return int(input_string)

    possible_digits = re.split(r'([1-9])', input_string)

    final_coordinate = ''
    
    # find the first digit
    for digit in possible_digits:
        current = string_to_number(digit)
        if current != None:
            final_coordinate += current
            break
            
    # find the second digit
    for digit in reversed(possible_digits):
        current = string_to_number(digit, reverse_search=True)
        if current != None:
            final_coordinate += current
            break
    # print ("input string %s resulted on %s" % (input_string, final_coordinate))

    return int(final_coordinate) 

def extract_calibration_value(input_string):
    return decode_coodinate(input_string)