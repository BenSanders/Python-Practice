# 3.15 Musical note frequencies


''' Type your code here. '''
import math

r = float(input())

value1 = r * pow(2, 1/12)
value2 = r * pow(2, 2/12)
value3 = r * pow(2, 3/12)
value4 = r * pow(2, 4/12)

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(r, value1, value2, value3,value4))
#print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(r, value1, value2, value3, value4))