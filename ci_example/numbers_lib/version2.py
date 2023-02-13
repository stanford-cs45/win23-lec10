"""
Super cool library for getting numbers of a specified amount.

Work in progress. Currently only supports ten.
"""

import random

def get_ten():
    """
    CHANGELOG v2.0: Add some randomness to make the developer experience
                    more interesting
    """
    # 1 in 100 chance of returning 9, heh heh >:)
    if random.randrange(0, 100) == 0:
        return 9
    return 10
