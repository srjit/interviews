
# Given a roman numeral, convert it to an integer.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999]


_roman_dict = {'I': 1,
 'V': 5,
 'X' : 10,
 'L': 50,
 'C' : 100,
 'D' : 500,
 'M' : 1000
 }


# 2578

# MMDLXXVIII


# 2578/1000 = 2000
# 578/100 = 500
# 78/10 = 70
# 8










