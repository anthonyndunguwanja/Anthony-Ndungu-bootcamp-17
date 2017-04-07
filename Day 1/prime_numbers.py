#Generating prime numbers 

def prime_number_generator(number):

    my_numbers = []
    if number in (0, 1):
        return "Zero or One cannot be prime numbers."

    if number < 2:
        return "Prime numbers cannot be less than two."

    if type(number) != int:
        return "Only integers are allowed."

    for x in range(2, number + 1):
        if x > 1:
            for y in range(2, x):
                if (x % y) == 0:
                    break
            else:
                my_numbers.append(x)
    return my_numbers



