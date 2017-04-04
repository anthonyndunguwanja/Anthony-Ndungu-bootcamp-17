
#Generating prime numbers 

def gen_primenos(num):
    '''This is a function to output prime numbers using asymptotic analysis from 0 to n'''

    my_nums = []
    if num in (0, 1):
         '''Testing zero or one is not a prime number'''
        return "Zero or One cannot be prime numbers."

    if num < 2:
        '''Testing that a number less than two is not a prime mumber'''
        return "Prime numbers cannot be less than two."

    if type(num) != int:
        return "Only integers are allowed."

    for x in range(2, num + 1):
        if x > 1:
            for y in range(2, x):
                if (x % y) == 0:
                    break
            else:
                my_nums.append(x)
    return my_nums
