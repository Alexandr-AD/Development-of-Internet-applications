class fig_colour:

    def __init__(self):
        self.colour = None

    @property
    def get_colour(self):
        return self.colour

    @get_colour.setter
    def set_colour(self, col):
        self.colour = col