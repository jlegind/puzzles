

romnums = {'i': 1, 'v': 5, 'x': 10, 'l':50, 'c': 100, 'd':500, 'm': 1000}


def roman_To_Digits(romanNumeral):
    return_list = []

    roman_list = list(romanNumeral)
    digi_list = [romnums[j] for j in roman_list]

    return digi_list


# len_rom = len(roman_digits)
# stop_value = len_rom


def roman_calc(roman_digits):
    # roman digits must be a list of integers like those converted from roman_to_Digits()
    # Calculates the int value of a roman numeral.
    len_rom = len(roman_digits)
    r_list = []
    for i, j in enumerate(roman_digits):
        print(f"i:{i} AND j:{j}")
        print(f"The plus one:: value {roman_digits[int(i)]}, the position being:= {i}")
        if i+1 == len_rom:
            print('Returning ----- end of list reached')
            r_list.append(j)
            return r_list
        if j < roman_digits[i+1]:
            # Testing the rule that a numeral preceding a smaller numeral must be negated.
            print("WE are in minus -!-!", 'we are appending', -j)
            r_list.append(-j)
        else:
            print('In regular ELSE condition')
            r_list.append(j)

roman_input = 'xxiv'
roman_numbers = roman_To_Digits(roman_input)
print(f"ORIGINAL numbers: {roman_numbers}")
res = roman_calc(roman_numbers)
print(res)
print(f"Final tally= {sum(res)}")