from game.casting.actor import Actor


class Artifact(Actor):
    """The points that the user will gain or lose if they have intersected a rock or a diamond.

    The artifact's responsibility is to keep track of the of the points that the user will gain or lose, when he intersect something on the screen

    Attributes:
        _points (int): A negative or positive point.
    """

    def __init__(self):
        """Constructs a new Artifact. It inherits from Actor its methods and attributes."""
        super().__init__()
        self._points = 0

    def get_points(self):
        """Returns a negative or positive point.

        Returns:
            integer: A negative or positive point.
        """
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1

        return self._points
