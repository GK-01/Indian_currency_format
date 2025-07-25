# Convert number into a comma separated Indian currency format.

def format_currency(amount):
    integer_part, decimal_part = amount.split('.')

    if len(integer_part) <= 3:
        formatted_integer = integer_part
    else:
        last_three = integer_part[-3:]
        other_digits = integer_part[:-3]
        res = ""
        while other_digits:
            res = "," + other_digits[-2:] + res
            other_digits = other_digits[:-2]
        formatted_integer = res[1:] + "," + last_three
    
    return formatted_integer + '.' + decimal_part

money=str(input("Enter the amount: "))
print(f"Formatted according to Indian Currency: {format_currency(money)}")