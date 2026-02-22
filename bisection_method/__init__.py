from collections.abc import Callable

type Zero = float
type Intervals = list[tuple[int, float, float, float, float]]


class SameSignsError(Exception):
    """
    Error raised when the function has values ofmatching signs for both
    bounds on the interval.
    """


def bisection_method(
    a: float, b: float, f: Callable[[float], float], eps: float
) -> tuple[Zero, Intervals]:
    """
    Implementation of the bisection bisection method
    after https://en.wikipedia.org/wiki/Bisection_method
    """

    # The bisection method and the underlying Bolzano's theorem is defined for
    # f(a) and f(b) with different signs.
    if f(a) * f(b) > 0:
        raise SameSignsError

    # Keeping track of the intervals
    intervals: Intervals = []

    m = 0
    i = 0
    while b - a >= eps:
        # Computing the middle point and the value at that point for the
        # function
        m = (a + b) / 2
        f_m = f(m)

        intervals.append((i, a, m, b, b - a))

        # We have found the precise zero, can return early
        if f_m == 0:
            return m, intervals

        f_a = f(a)
        # If the values on the left end of the interval and the middle have the
        # same sign, i.e. +, + or -, -, then we change the left bound to be the
        # middle, as the zero is between the middle and the right bound.
        # Otherwise, we cahnge the right bound to the middle, as the zero is
        # between the left bound and the middle.
        if f_a * f_m > 0:
            a = m
        else:
            b = m

        i += 1

    # Also including the interval when `b - a < eps`
    m = (a + b) / 2
    intervals.append((i, a, m, b, b - a))

    return m, intervals
