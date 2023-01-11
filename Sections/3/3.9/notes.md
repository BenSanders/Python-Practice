# The math module

While basic math operations like + or * are sufficient for some computations, programmers sometimes wish to perform more advanced math operations such as computing a square root. Python comes with a standard math module to support such advanced math operations. A module is Python code located in another file. The programmer can import the module for use in their own file, or in an interactive interpreter. The programmer first imports the module to the top of a file.



sqrt() is known as a function. A function is a list of statements that can be executed simply by referring to the function's name. The statements for sqrt() are within the math module itself and are not relevant to the programmer. The programmer provides a value to the function (like num above). The function executes its statements and returns the computed value. Thus, sqrt(num) above will evaluate to 7.0.

The process of invoking a function is referred to as a function call. The item passed to a function is referred to as an argument. Some functions have multiple arguments, such as the function pow(b, e), which returns be. The statement `ten_generation_ancestors = 1024 * num_people` could be replaced by `ten_generation_ancestors = math.pow(2, 10) * num_people` to be more clear.

Some commonly used math functions https://docs.python.org/3.7/library/math.html


 Correct

The math.fabs() function takes -8.6 as an input value, and produces that value's absolute value. 

The math.pow() function takes two arguments, 3.0 and 2.0, as input values. math.pow(3.0, 2.0) raises 3.0 to power 2.0.

