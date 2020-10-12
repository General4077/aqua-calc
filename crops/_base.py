"""
Define the crop type
"""

class Crop:
    """
    The base class for all crops
    """

    root_area = None

    def __str__(self):
        return f'Root Area: {self.root_area} ft\u0032/ft\u0032'
        