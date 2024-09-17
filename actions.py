
class Action:
    """
    Class that governs an action in general
    """
    # pass


class EscapeAction(Action):
    """
    Click of the esc button
    """
    # pass


class MovementAction(Action):
    """
    Class that tracks the player movement
    """
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
