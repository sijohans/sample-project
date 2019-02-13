"""
Test module for learning python packaging.
"""


def my_sum(arg):
    """
    Sums the arguments and returns the sum.
    """
    total = 0
    for val in arg:
        total += val
    return total


class MySum(object):
    # pylint: disable=too-few-public-methods
    """
    MySum class
    """
    @staticmethod
    def my_sum(arg):
        """
        Sums the arguments and returns the sum.
        """
        return my_sum(arg)
