from collections.abc import Callable
import math
from typing import Final

type Zero = float
type AbsoluteError = float


def bisection_method(
    a: float, b: float, f: Callable[[float], float], eps: float
) -> Zero | None:
    """
    Implementation of the bisection bisection method
    after https://en.wikipedia.org/wiki/Bisection_method
    """

    # The bisection method and the underlying Bolzano's theorem is defined for
    # f(a) and f(b) with different signs.
    if f(a) * f(b) > 0:
        return None

    m = (a + b) / 2
    f_m = f(m)

    # https://x-engineer.org/bisection-method/#:~:text=the%20number%20n%20of%20iterations%20we%20need%20to%20perform%20is
    # We want to achive the absolute error for `x_0` of `eps`,
    # we compute the number of iterations after which the length
    # of the interval [a, b] will be less than or equal to `eps`
    n = math.ceil(math.log2((b - a) / eps))
    for _ in range(n):
        f_m = f(m)

        # We have found the precise zero, can return early
        if f_m == 0:
            return m

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

        m = (a + b) / 2

    return m


SAME_SIGNS_MESSAGE: Final[str] = """The provided function and interval don't meet the definition of the Bolzano's theorem,
the values f(a) and f(b) don't have different signs, therefore, it's not guaranteed
that there is a zero.
Please try again.
"""


def main() -> None:
    while True:
        while True:
            try:
                a, b = map(
                    lambda v: float(str.strip(v)),
                    input("Input the interval bounds, comma-separated\n>>> ").split(","),
                )
            except ValueError:
                print("Could not parse the interval bounds, please try again.")
                continue
            except KeyboardInterrupt:
                return

            break

        try:
            func_expr = input("Input an expression that defines the function\n>>> ")
            eps = float(
                input("Input the approximation precision as a floating point number\n>>> ")
            )
        except KeyboardInterrupt:
            return

        def f(x: float) -> float:
            return eval(func_expr, locals={"x": x, **math.__dict__})

        x_0 = bisection_method(a, b, f, eps)
        if x_0 is None:
            print(SAME_SIGNS_MESSAGE)
            continue

        break

    x_precision = math.floor(abs(math.log10(eps)))

    print(f"x_0 = {x_0:.{x_precision}f}±{eps} = {x_0:.20f}")
    f_x_0 = f(x_0)
    f_x_precision = abs(math.floor(math.log10(abs(f_x_0))))
    print(f"f(x_0) = 0±{abs(f(x_0)):.{f_x_precision}f} = {f_x_0:.20f}")


if __name__ == "__main__":
    main()
