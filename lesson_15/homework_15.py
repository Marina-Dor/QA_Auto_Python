class Diamond:
    def __init__(self, side_a, angle_a):
        self._side_a = None
        self._angle_b = None
        self._angle_a = None
        self.setattr('side_a', side_a)
        self.setattr('angle_a', angle_a)

    def setattr(self, attribute, value):
        if attribute == 'side_a':
            if value <= 0:
                raise ValueError("Side length should be more than 0.")
            self._side_a = value
        elif attribute == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("The angle must be in the range from 0 to 180 degrees.")
            self._angle_a = value
            self._angle_b = 180 - value
        else:
            raise AttributeError(f"Unknown attribute '{attribute}'")

    @property
    def side_a(self):
        return self._side_a

    @property
    def angle_a(self):
        return self._angle_a

    @property
    def angle_b(self):
        return self._angle_b

    def __repr__(self):
        return f"Diamond: side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b}"


diamond_test_cases = [
    {"side_a": 5, "angle_a": 60},     # Valid
    {"side_a": 5, "angle_a": 180},    # Invalid: angle is 180
    {"side_a": 5, "angle_a": 0},      # Invalid: angle is 0
    {"side_a": 5, "angle_a": 200},    # Invalid: angle is more 180
    {"side_a": 0, "angle_a": 60},     # Invalid: side is 0
]

for i, case in enumerate(diamond_test_cases, start=1):
    try:
        diamond = Diamond(case["side_a"], case["angle_a"])
        print(f"Test case {i}: Diamond created successfully - {diamond}")
    except ValueError as e:
        print(f"Test case {i}: Error - {e}")
    except AttributeError as e:
        print(f"Test case {i}: Error - {e}")
