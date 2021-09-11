import math
import re

# def cal_value_N():
# 164*(1+20%)^n=100000

# (100000 / 164)
# 1.2

# print(math.log(100000 / 164, 1.2))


rex = re.compile(r'\d+')
str = 'Grandma -  111'
mo = rex.search(str)
print(mo.group())


# phoneNumRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Call me at 02-8888-1688 by today.')
# print(mo.group())
