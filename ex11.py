############################################
# FILE: ex11.py
# WRITER: OREN SULTAN, orens, 201557972
# EXERCISE: intro2cs ex11 2015-2016
# DESCRIPTION: implementations of functions which returns math functions
############################################


import math

EPSILON = 1e-5
DELTA = 1e-3
SEGMENTS = 100

X_INDEX = 0
Y_INDEX = 0
START_RANGE = -10
END_RANGE = 10


def plot_func(graph, f, x0, x1, num_of_segments=SEGMENTS, c='black'):
    """
    :param graph:
    :param f:
    :param x0:
    :param x1:
    :param num_of_segments:
    :param c:
    :return:    plot f between x0 and x1 using num_of_segments straight lines.
    use the plot_line function in the graph object.
    f will be plotted to the screen with color c.
    """

    width = (x1 - x0) / num_of_segments
    # initialization for points of first line
    first_point = (x0, f(x0))
    second_point = ((x0 + width), (f(x0 + width)))
    # run as number of segments
    for i in range(num_of_segments):
        # draw the line from first_point to second_point
        graph.plot_line(first_point, second_point, c)

        first_point = second_point
        next_point = first_point[X_INDEX] + width
        second_point = (next_point, (f(next_point)))


def const_function(c):
    """
    :param c:
    :return:
    return the mathematical function f such that f(x) = c
    """

    # return a function f(x) = c
    return lambda x: c


def identity():
    """return the mathematical function f such that f(x) = x
    >>>identity()(3)
    3
    """
    # return a function f(x) = x
    return lambda x: x


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    >>> sinF()(math.pi/2)
    1.0
    """
    # return a function f(x) = sin(x)
    return lambda x: math.sin(x)


def sum_functions(g, h):
    """
    :param g:
    :param h:
    :return: f s.t. f(x) = g(x)+h(x)
    """
    # return sum of functions g(x) + h(x)
    return lambda x: g(x) + h(x)


def sub_functions(g, h):
    """
    :param g:
    :param h:
    :return: f s.t. f(x) = g(x)-h(x)
    """
    # return sub of functions g(x) - h(x)
    return lambda x: g(x) - h(x)


def mul_functions(g, h):
    """
    :param g:
    :param h:
    :return: f s.t. f(x) = g(x)*h(x)
    """
    # return multiplication of functions g(x)*h(x)
    return lambda x: g(x) * h(x)


def div_functions(g, h):
    """
    :param g:
    :param h:
    :return: f s.t. f(x) = g(x)/h(x)
    """
    # return division of functions g(x)/h(x)
    return lambda x: g(x) / h(x)

    # The function solve assumes that f is continuous.
    # solve return None in case of no solution


def solve(f, x0=-10000, x1=10000, epsilon=EPSILON):
    """
    :param f:
    :param x0:
    :param x1:
    :param epsilon:
    :return: the solution to f in the range between x0 and x1
    """

    # base case (stop condition)
    if f(x0) * f(x1) > 0:
        return None
    if f(x0) * f(x1) == 0:
        if f(x0) == 0:
            return x0
        else:
            return x1
    else:
        # binary search concept x= middle of x0, x1
        x = (x0 + x1) / 2
        if abs(f(x)) < epsilon:
            return x
        # if true so f(x) is negative or f(x0) is negative
        # and it's good because according to intermediate value theorem
        # must be c which f(c) = 0 for c between f(x0) and f(x)
        # else both of them are positive
        if f(x0) * f(x) < 0:
            return solve(f, x0, x, epsilon)
        return solve(f, x, x1, epsilon)


def inverse_help_function(g, input, epsilon):
    """
    :param g:
    :param input:
    :param epsilon:
    :return:
    """

    # define start range x0 - x1
    x0 = START_RANGE
    x1 = END_RANGE

    # when one of g(x0) - input or g(x1) - input is negative
    # finish the while and call solve function
    while (g(x0) - input) * (g(x1) - input) > 0:
        x0 *= 2
        x1 *= 2
    # call solve function
    return solve(lambda x: g(x) - input, x0, x1, epsilon)

# inverse assumes that g is continuous and monotonic.


def inverse(g, epsilon=EPSILON):
    """
    :param g:
    :param epsilon:
    :return: f s.t. f(g(x)) = x
    """
    return lambda x: inverse_help_function(g, x, epsilon)


def compose(g, h):
    """
    :param g:
    :param h:
    :return: the f which is the compose of g and h
    """
    # return compose function of g on h
    return lambda x: g(h(x))


def derivative(g, delta=DELTA):
    """
    :param g:
    :param delta:
    :return: f s.t. f(x) = g'(x)
    """
    # return derivative of function g (=g'(x)) by the formula
    # g'(x) = (g(x + DELTA) - g(x)) / DELTA
    return lambda x: (g(x + delta) - g(x)) / delta


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    :param f:
    :param x0:
    :param x1:
    :param num_of_segments:
    :return: return a float - the definite_integral of f between x0 and x1
    """

    segment_length = (x1 - x0) / num_of_segments
    x1 = x0 + segment_length
    sum_of_di = 0
    # run as number of segments
    for i in range(num_of_segments):
        # add to sum the area of segment
        sum_of_di += f((x0 + x1) / 2) * (x1 - x0)
        # move one segment right
        x0 = x1
        x1 += segment_length
    return sum_of_di


def integral_function_help(f, delta, x):
    """
    :param f:
    :param delta:
    :param x:
    :return: the correct calc according to x value
    using definite_integral function
    """

    if x < 0:
        return -1 * definite_integral(f, x, 0, math.ceil(abs(x) / delta))
    elif x == 0:
        return 0
    else:
        return definite_integral(f, 0, x, math.ceil(abs(x) / delta))


def integral_function(f, delta=0.01):
    """ return F such that F'(x) = f(x)
    :param f:
    :param delta:
    :return:
    """
    return lambda x: integral_function_help(f, delta, x)


def ex11_func_list():
    """return a list of functions as a solution to q.12"""

    # create vars for sin and derivative functions
    sin = sin_function()
    cos = derivative(sin)

    # initalize the returned list
    func_list = list()

    func_list.append(const_function(4))
    func_list.append(sum_functions(sin, const_function(4)))
    func_list.append(compose(sin, sum_functions(identity(),
                                                const_function(4))))
    func_list.append(div_functions(mul_functions(sin,
                                                 mul_functions(identity(),
                                                                identity())),
                                   const_function(100)))
    func_list.append(div_functions(sin, sum_functions(cos,
                                                      const_function(2))))
    func_list.append(integral_function(
        sub_functions(sum_functions(mul_functions(identity(), identity()),
                                    identity()),
                      const_function(3))))
    func_list.append(mul_functions(const_function(5),
                                   sub_functions(compose(sin, cos), cos)))
    func_list.append(inverse(mul_functions(mul_functions(identity(),
                                                         identity()),
                                           identity())))
    return func_list

# function that genrate the figure in the ex description
def example_func(x):
    return (x/5)**3

if __name__ == "__main__":
    import tkinter as tk
    from ex11helper import Graph
    master = tk.Tk()
    graph = Graph(master, -100, -100, 100, 100)
    # un-tag the line below after implementation of plot_func
    plot_func(graph,example_func,-100,100,SEGMENTS,'red')

    ex11_func_list()
    master.mainloop()