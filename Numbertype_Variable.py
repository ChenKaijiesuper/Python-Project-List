# Number type & Variable

# Character String
from cmath import pi
from telnetlib import PRAGMA_HEARTBEAT


print('I\'m ok.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')

# Boolean value
print(3 > 2)
print(3 > 5)
print(5 > 3 & 3 > 1)
print(5 > 3 or 3 > 1)
print(not True)
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值 None
print(None)

# Variable
a = 2
t_007 = 'T007'
Answer = True
a = 1.23
a = 'a'

# b = 'ABC' a = 'XYZ'
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# Constant
print(pi)

# Division method
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)

print(r'''Hello,
Lisa!''')