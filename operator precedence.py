1. a = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 50
'''
Copy code
2 + 3 * 4 ** 2
= 2 + 3 * 16
= 50
'''



2. b = (2 + 3) * 4 ** 2  # 5 * 16 = 80
'''
(2 + 3) * 4 ** 2
= 5 * 16
= 80

'''



c = 10 % 3 + 2 / 5  # 1 + 0.4 = 1.4
'''
10 % 3 + 2 / 5
= 1 + 0.4
= 1.4

'''
d = 10 / 3 // 2  # 1
'''
10 / 3 // 2
= 3.33... // 2
= 1
'''


e = 0b1010 & 0b1100  # 0b1000 = 8
f = 0b1010 ^ 0b1100  # 0b0110 = 6
g = 0b1010 | 0b1100  # 0b1110 = 14



h = 3 == 3.0  # True
i = not 3 == 3.0  # False


j = True or False and not True  # True

'''
The logical NOT (not) operator is evaluated first, then the logical AND (and) operator is evaluated, and finally the logical OR (or) operator is evaluated
'''

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
