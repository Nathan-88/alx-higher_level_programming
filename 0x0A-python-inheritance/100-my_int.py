#!/usr/bin/python3
"""object int with subclass MyInt"""


class MyInt(int):
    """defined class MyInt"""

    def __eq__(self, other):
        """== operator is inverted to the opposite of what it does"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """!= operator is inverted to the opposite of what it does"""
        return not super().__ne__(other)
