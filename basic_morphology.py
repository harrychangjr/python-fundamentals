#converting numbers from one base to another

def decimal_to_binary(number):
    return str(bin(number)[2:])

def make_decimal_to_n_ary_converter(n):
    def converter(x):
        if x==0 or x==1:   
            return str(x)
        i = x
        b=('A','B','C','D','E','F')
        output = ""
        while i > 0:
            a = i % n         
            if a < 10:
                output = str(i % n) + output
            else:
                d = a - 10
                output = b[d] + output
            i = i // n
        return output
    return converter
 

def hexadecimal_to_decimal(hex_number):
    return int(hex_number,16)
    
def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent
    def hexadecimal_to_decimal(hex_number):
        # return the decimal number that hex_number represents
        hex_str = hex_number
        output = 0
        while hex_str!='':
            output = output + int(digit_decoder(hex_str[0]))*n**(len(hex_str)-1)
            hex_str = hex_str[1:]
        return output
    return hexadecimal_to_decimal

def digit_decoder(x):
    lookup=['A','B','C','D','E','F']
    if x in lookup:
        return str(lookup.index(x)+10)
    else:
        return x
        
def make_p_ary_to_q_ary_converter(p, q):
    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q
    return compose(make_decimal_to_n_ary_converter(q),make_n_ary_to_decimal_converter(p))

def compose(f, g):
    return lambda x: f(g(x))
    

