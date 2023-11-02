def sum_of_squares(number):
    """Given a number n, return the sum of the squares of the first n natural numbers"""
    return sum([i**2 for i in range(number + 1)])


def square_of_sums(number):
    """Given a number n, return the square of the sum of the first n natural numbers"""
    return sum([i for i in range(number + 1)]) ** 2
