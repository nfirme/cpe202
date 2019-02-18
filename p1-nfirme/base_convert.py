def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""

    result = ''
    quo = num // b
    rem = num % b

    result = result + str(dict.get(rem))

    if b > 16 or b < 1:
        raise ValueError('Base must be between 2 and 16')
    else:
        if quo == 0:
            return result
        return convert(quo, b) + result

dict = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F',
}