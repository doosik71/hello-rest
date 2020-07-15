"""파이썬 샘플 코드."""

import os


def square(a):
    """제곱값(:math:`a^2`)을 반환한다.

    :param a: 입력값.

    :returns: a * a
    """
    return a*a

assert 4 == square(2)