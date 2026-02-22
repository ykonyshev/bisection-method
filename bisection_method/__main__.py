import math
from typing import Final
from bisection_method import Intervals, SameSignsError, bisection_method
from generate_latex import generate_latex


SAME_SIGNS_MESSAGE: Final[str] = """The provided function and interval don't meet the definition of the Bolzano's theorem,
the values f(a) and f(b) don't have different signs, therefore, it's not guaranteed
that there is a zero.
Please try again.
"""


def print_table(data: Intervals) -> None:
    print(f"{"n":>2} | {"a_n":^6} | {"m_n":^6} | {"b_n":^6} | {"b_n - a_n":^9}")
    for n, a, m, b, abs_err in data:
        print(f"{n:>2} | {a:^6.4f} | {m:^6.4f} | {b:^6.4f} | {abs_err:^9.5f}")


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

        while True:
            try:
                func_expr = input("Input an expression that defines a continuous function\n>>> ")

                def f(x: float) -> float:
                    return eval(func_expr, locals={"x": x, **math.__dict__})

                try:
                    f(a)
                    f(b)
                except ZeroDivisionError, ValueError:
                    print("The provided function is not defined at `a` or `b`.")
                    continue
                except Exception:
                    print("The evaluation of the function for `f(a)` and/or `f(b)` cause an error.\n\
                            Most likely the expression defining the function is invalid, please try again.")
                    continue
            except KeyboardInterrupt:
                return

            break

        
        while True:
            try:
                eps = float(
                    input("Input the approximation precision (epsilon) as a floating point number\n>>> ")
                )

                if eps < 0:
                    raise ValueError("Epsilon must not be negative")
            except ValueError:
                print("Invalid value for epsilon, must be a positive number.")
                continue
            except KeyboardInterrupt:
                return

            break

        try:
            x_0, intervals = bisection_method(a, b, f, eps)
        except SameSignsError:
            print(SAME_SIGNS_MESSAGE)
            continue

        print_table(intervals)

        break

    x_precision = math.floor(abs(math.log10(eps))) if eps > 0 else 0

    print(f"x_0 = {x_0:.{x_precision}f}±{eps} = {x_0:.10f}")
    f_x_0 = f(x_0)
    f_x_precision = abs(math.floor(math.log10(abs(f_x_0) % 1))) + 4 if abs(f_x_0) > 0 else 0
    print(f"f(x_0) = 0±{abs(f(x_0)):.{f_x_precision}f} = {f_x_0:.10f}")

    generate_latex(intervals, f)


if __name__ == "__main__":
    main()
