#Class: there is a motor class that you can make objects of, there are multiple motor objects,
# each one has properties, one of the properties is a CAM ID, which is an indicator of which
# signals it should listen to, and each motor has methods that allows you to run the motors independently

#Class: Xbox controller is a class, a property of an xbox controller object could be some identifyer like what port you've plugged it into.

#In python you need to indent, there are no curly braces.

#A dunder init __init__ initializes the object by taking in the arguments from the main function, then __init__ initializes an object using
# the arguments as the in-class variables.

# class My_Class:
#     def __init__(self, args, more_args):
#         self.property= args
#     def my_cool_method(self, args, more_args):
#         #my code
#         pass #keyword that means that the method does nothing.

#then in main:

# my_object=My_Class() # makes an object of My_Class type
# my_object.my_cool_method() # This makes that object do its cool method which actually does nothing so it sucks

#TO IMPORT CLASSES:
# from ctre.motors import REVMotor #this imputs the revmotor class from ctre.motors library.
# my_motor=REVMotor()
# my_motor.set_speed(1)
from Motor import Motor

if __name__ == "__main__":
    x=Motor()
    print(x.speed)
    x.speed_up()
    print(x.speed)
    x.slow_down()
    x.slow_down()
    print(x.speed)

