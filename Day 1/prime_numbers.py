
#Generating prime numbers 

def gen_primenos(num):

    my_nums = []
    if num in (0, 1):
        return "Zero or One cannot be prime numbers."

    if num < 2:
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
