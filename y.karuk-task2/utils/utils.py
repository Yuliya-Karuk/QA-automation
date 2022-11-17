import re

class Utils:
    def find_digit_from_string(searching_string):
        list_with_number = re.findall('[0-9]+', searching_string)
        number_string = list_with_number[0]
        for i in list_with_number[1:]:
            number_string = number_string + i
        number_int = int(number_string)
        return number_int


    def find_number_from_string(searching_string):
        list_with_number = re.findall('[0-9.]+', searching_string)
        number_string = list_with_number[0]
        for i in list_with_number[1:]:
            number_string = number_string + i
        number_float = float(number_string)
        return number_float