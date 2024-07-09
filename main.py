#https://docs.python.org/3/library/doctest.html
#https://docs.python.org/3/library/unittest.html

from calculator import sum

# print(sum(10,20))
# print(sum(-10,20))
# print(sum(-10.5,20.5))

try:
    print(sum('15',5))
except TypeError as error:
    print('Invalid Parameters')
    print(error)