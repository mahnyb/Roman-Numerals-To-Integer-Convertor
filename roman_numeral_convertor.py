def roman_to_int(roman):

    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    result = 0

    for i in range(len(roman)):

        value = roman_dict[roman[i]]

        if (i + 1) < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            result -= value
        else:
            result += value
    
    return result

roman_numeral_input = input("\nEnter the Roman Numerals that you want to convert: ")

int_equivalent = roman_to_int(roman_numeral_input)

if int_equivalent is not None:
    print("\nThe Integer Equivalent of your entered number is: ", int_equivalent)

