# 3.4 Numeric types: Floating-point
* Floating-point number is a real number, like 98.6, or 0.0001, or -666.667. The term "floating-point" refers to the decimal point being able to appear anywhere ("float") in the number. Thus float is a data type for floating-point numbers.

* FLoating-point literal is writtent with the fractional part even if that fraction is 0, as in 1.0, 0.0, or 99.0

* Scientific notation is useful for representing floating-point numbers that are much greater than or much less than 0, such as 6.02x1023. A floating-point literal using scientific notation is written using an e preceding the power-of-10 exponent, as in 6.02e23 to represent 6.02x1023. The e stands for exponent. Likewise, 0.001 is 1x10-3, so it can be written as 1.0e-3. 
	* The e-3 shifts the decimal point three places to the left
* Type 540,000,000 as a floating-point literal using scientific notation with a single digit before and after the decimal point.
	* 5.4e8 - Remember by adding a decimal between 5 and 4 then times it by 10^8. Decimal point is eight places from 4 on.

# Overflow
Float-type objects have a limited range of values that can be represented. For a standard 32-bit installation of Python, the maximum floating-point value is approximately 1.8E308, and the minimum foating-point value is 2.3E-308. Assigning a floating-point value outside of this range generates an OverflowError. Overflow occures when a value is too large to be stored in the memory allocated by the interpreter.