
class EasingBase:
    limit = (-1, 1)

    def __init__(self, start=0, end=1, duration=1):
        self.start = start
        self.end = end
        self.duration = duration

    @classmethod
    def func(cls, t):
        raise NotImplementedError

    def ease(self, alpha):
        """
        Interpolate between start and end given an alpha from 0 to duration
        :param alpha: 0 to duration
        :return: respective value between start and end
        """
        t = self.limit[0] * (1 - alpha) + self.limit[1] * alpha
        t /=self.duration
        a = self.func(t)
        return self.end * a + self.start * (1 - a)


"""
Quadratic easing functions
"""


class QuadEaseInOut(EasingBase):
    limit = (-1, 1)

    def func(self, t):
        if t < 0:
            return (t + 1) ** 2 / (self.limit[1] - self.limit[0])
        return -(t - 1) ** 2 / (self.limit[1] - self.limit[0]) + 1


class QuadEaseIn(QuadEaseInOut):
    limit = (-1, 0)


class QuadEaseOut(QuadEaseInOut):
    limit = (0, 1)
