def check_kaprekar_const(number):
    if len(str(number)) != 4 or len(set(str(number))) < 2:
        return "Please enter a four-digit number with at least two different digits."

    iterations = 0
    kaprekar_constant = 6174

    while number != kaprekar_constant:
        
        number_string = str(number)

        while len(number_string) < 4:
            number_string = '0' + number_string

        # Create largest and smallest numbers by sorting digits
        largest_num = int(''.join(sorted(number_string, reverse=True)))
        smallest_num = int(''.join(sorted(number_string)))

        number = largest_num - smallest_num
        iterations += 1
        
        print(f"No. Iteration {iterations}: {largest_num}-{smallest_num}={number}")

    return f"Kaprekar's constant reached in {iterations} iterations! Bazinga!"

initial_number = 3524    
result = check_kaprekar_const(initial_number)
print(result)
