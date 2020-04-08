# This class actually calculates the integral using Simpson's Rule. It gets the interval range and determines
# what values of x the function has to be calculated for and calculates them using the expression tree.

# Given the bounds of integration and number of rectangles this function returns all of the values Simpson's
# Rule needs to calculate and the interval value
def get_intervals(lower_bound, upper_bound, num_of_rec):
    interval_gaps = (upper_bound - lower_bound)/num_of_rec
    values = []
    for i in range(num_of_rec + 1):
        res = lower_bound + (i * interval_gaps)
        values.append(res)
    return values, interval_gaps

# In Simpson's Rule this function does the calculating for the function as various x-values and takes into account
# the 4, 2, 4 pattern of Simpson's Rule
def function_calculate(function, values):
    total = 0
    for i in range(len(values)):
        if i == 0:
            val = function.evaluate(values[0])
            total += val
        elif i == len(values) - 1:
            val = function.evaluate(values[-1])
            total += val
        elif i % 2 == 1:
            val = 4 * function.evaluate(values[i])
            total += val
        elif i % 2 == 0:
            val = 2 * function.evaluate(values[i])
            total += val
    return total

# This function takes in a function (a string in infix form) to integrate on with given bounds and the desired
# number of rectangles to use for approximating
def solve(function, lower_bound, upper_bound, num_of_rec):
    values, delta_x = get_intervals(lower_bound, upper_bound, num_of_rec)
    function_tot = function_calculate(function, values)
    front = delta_x/3
    result = front * function_tot
    return result
