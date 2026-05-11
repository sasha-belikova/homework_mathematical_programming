def addbin(x, y):                                     # starting the funktion
    result_add = int(x, 2) + int(y, 2)                # converting two binary numbers into decimal numbers and adding them
    result_add_binar = bin(result_add)                # converting the previous result back into a binary number
    print('The addition of two binary numbers', x, 'and', y, 'is', result_add_binar)




def multbin(a, b):                               # the same logic as for addition
    result_multi = int(a, 2) * int(b, 2)
    result_multi_binar = bin(result_multi)
    print('The multiplication of two binary numbers', a, 'and', b, 'is', result_multi_binar)



def floatbin(n):
    point_place = n.find('.')                            # found the position of the point
    fraction_length = len(n) - point_place - 1           # amount of digits after the point
    n = n.replace('.', '')                               # changed the binary number with a point into a normal binary number
    n_without_point = int(n, 2)                          # converted the binary number as a normal one
    real_number = n_without_point / 2**fraction_length   # divided by 2 to the power of the amount of digits after the point, 
                                                             # so the fractional part is counted as 2^-1, 2^-2, and so on
    print('Conversion from binary fraction', n, 'to a real number is', real_number)



def fractionsbin(k):
    from fractions import Fraction                       # importing a Fraction from module fractions
    point_place = k.find('.')                            # the structure is pretty the same to the floatbin
    fraction_length = len(k) - point_place - 1           
    k = k.replace('.', '')                               
    k_without_point = int(k, 2)                          
    fraction_number = Fraction(k_without_point, 2**fraction_length)
    print('Conversion from binary fraction', k, 'to Fraction is', fraction_number)