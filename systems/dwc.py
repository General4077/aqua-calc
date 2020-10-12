"""
Define the DWC system
"""

from ._base import System

class DWC(System):
    """
    Deep Water Culture system
    """

    def __init__(self, *, height: float = 0, width: float = 0, length: float = 0):
        self.height = height
        self.width = width
        self.length = length


    @property
    def surface_area(self) -> float:
        return 2 * (
            (self.length * self.width) +\
            (self.length * self.height) +\
            (self.width * self.height)
        )

    def __str__(self):
        return f"Surface Area: {self.surface_area}ft\u0032"
