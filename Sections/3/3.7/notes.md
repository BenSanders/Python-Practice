# Division: Integer rounding
The division operator / performs division and returns a floating-point number. Ex:

* 20 / 10 is 2.0
* 50 / 50 is 1.0
* 5 / 10 is 0.5

The floored division operator `//` can be used to round down the result of a floating-point division to the closest whole number value. The resulting value is an integer type if both operands are integers; if either operand is a float, then a float is returned.

* 20 // 10 is 2.
* 50 // 50 is 1.
* 5 // 10 is 0. (5/10 is 0 and the remainder 5 is thrown away).
* 5.0 // 2 is 2.0

Another example:
5.0 // 2 is 2.0 because floored division rounds the result of the floating point division down to the closest whole number, represented in floating point. So 2.5 is rounded down to 2.0.

Think of it as 5 / 2.0 = 2.5 then round to the nearest whole number down to 2.0.

# Modulo (%)

The basic arithmetic operators include not just (+, -, *, /) but also %. The modulo operator evalutes the remainder of the division of two integer operands. Ex. 23 % 10 is 3


* 24 % 10 is 4. Reason: 24 / 10 is 2 with remainder 4.
* 50 % 50 is 0. Reason: 50 / 50 is 1 with remainder 0.
* 1 % 2 is 1. Reason: 1 / 2 is 0 with remainder 1.

Ask course instructor question about 3.7.1 challenge activity