import numpy as np

from crypto import give_advise


def test_give_advise():
    result = give_advise([1, 1, 2])
    np.testing.assert_equal(result, "sell")

    result = give_advise([1, 1, 0])
    np.testing.assert_equal(result, "buy")

    result = give_advise([1, 1, 1])
    np.testing.assert_equal(result, "do nothing")


def failing_test():
    np.testing.assert_equal(True, False)
