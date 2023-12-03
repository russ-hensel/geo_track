# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

def to_metric( a_num ):
    """
    may be extended up or down
    Returns
         tuple: ( a_new_num, prefix )

    """
    if   a_num > 1.0e12:
        return a_num /1.0e12, "tera"

    elif a_num > 1.0e9:
        return a_num /1.0e9, "giga"

    elif a_num > 1.0e6:
        return a_num /1.0e6, "mega"

    elif a_num > 1.0e3:
        return a_num /1.0e3, "kilo"

    elif a_num > 1.0:
        return a_num,  ""

    elif a_num > 1.e-3:
        return a_num/1.e-3,  "milli"

    elif a_num > 1.e-6:
        return a_num/1.e-6,  "micro"

    elif a_num > 1.e-9:
        return a_num/1.e-9,  "nano"

    elif a_num > 1.e-12:
        return a_num/1.e-12,  "pico"

    else:
        return a_num,  ""

def to_metric_str( a_num, digits_past_dp = 3 ):
    """
    read the code

        digits_past_dp   -- not implemented yet

    Returns
         str

    """
    a_num, prefix  = to_metric( a_num )
    a_num          = float( a_num )
    a_str          = f"{a_num:.4} {prefix}"

    return a_str


# =================================================

if __name__ == "__main__":

    v = 2345.678901

    print( to_metric_str( v ))

    print( to_metric_str( 22 ))

    print( to_metric_str( 22000000 ))