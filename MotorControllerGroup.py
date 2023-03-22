from Motor import Motor

class MotorControllerGroup:
    def __init__(self, list_of_motors:list[Motor]):
        self.motors=list_of_motors

    def setspeed(self, speed):
        for motor in self.motors:
            motor.set_speed(speed)

    def speedup(self):
        for motor in self.motors:
            motor.speed_up()

    def slowdown(self):
        for motor in self.motors:
            motor.slow_down()

    def addmotor(self, motor:Motor):
        self.motors.append(motor)