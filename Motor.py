class Motor:
    def __init__(self):
        self.speed = 0.5

    def set_speed(self, newspeed):
        self.speed = newspeed

    def speed_up(self):
        self.speed *= 2

    def slow_down(self):
        self.speed *= 0.5