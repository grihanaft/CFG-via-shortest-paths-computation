class Semiring(object):

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError
