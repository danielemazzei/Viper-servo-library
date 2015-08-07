"""
.. module:: servo 

This module contains class definitions for servo motors.
The Servo class provides methods for handling generic servo motors connected to pins endowed with PWM.
It also provides easily accessible attributes for direct control motor position with pulse width or degree.

Every Servo instance implements the following methods:

    * attach: connects the servo motor and sets the default position
    * detach: sets the PWM pulse width of the instanced servo to 0 disconnecting the motor
    * moveToDegree: sets the servo position to the desired angle passed as float
    * moveToPulseWidth: sets the servo position to the desired raw value expressed as pulse width (int) milliseconds
    * getCurrentPulseWidth: returns the current servo position in pulse width (int) milliseconds
    * getCurrentDegree: returns the current position in degrees

"""


import pwm

class Servo():
    
    """
==================
Servo class
==================

.. class:: AnalogSensor(pin,min_width=500,max_width=2500,default_width=1500,period=20000)

    This is the class for handling a servo motor. 
    * pin: is where the servo motor signal wire is connected. The pin requires PWM functionality and have to be passed using the DX.PWM Viper signature
    * min_width and max_width: are the min and max values of the PWM pulse width (milliseconds). They have to be tuned according to servo capabilities. Defaults are set to the widest used range.
    * default_width: is the position where the servo motor is moved when it is attached. It is expressed in milliseconds and the default is set to 1500 corresponding to 90° if the min max width range is sets as default.
    * period: is the period of the PWM used for controlling the servo expressed in milliseconds. Default is 20ms that is the widest used standard. 
    
    After initialization the servo motor object is created and the controlling PWM set to 0 leaving the servo digitally disconnected
    """


    def __init__(self,pin,min_width=500,max_width=2500,default_width=1500,period=20000):
        
        self.pin=pin
        self.minWidth=min_width
        self.maxWidth=max_width
        self.defaultPosition=default_width
        self.currentPosition=default_width
        self.period=period
        pwm.write(self.pin,self.period,0,MICROS)
        
    def map_range(self,x, in_min, in_max, out_min, out_max):
        if x < in_min:
            x = in_min    
        elif x > in_max: 
            x = in_max
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min    

        """
.. method:: attach()
    Writes the default_width to the servo associated PWM enabling the motor and moving it to the default position. 
        """

    def attach(self):
        pwm.write(self.pin,self.period,self.defaultPosition,MICROS)

        """
.. method:: detach()
    Writes 0 on the servo associated PWM disabling the motor. 
        """        
            
    def detach(self):
        pwm.write(self.pin,self.period,0,MICROS)

        """
.. method:: moveToDegree(degree)
    Moves the servo motor to the desired position expressed as degrees (float). 
        """        
        
    def moveToDegree(self,degree):
        
        width=int(self.map_range(degree,0,180,self.minWidth,self.maxWidth))
        
        if width != self.currentPosition:            
            self.currentPosition=width
            pwm.write(self.pin, self.period,self.currentPosition,MICROS)
    
        """
.. method:: moveToPulseWidth(width)
    Moves the servo motor to the desired position expressed as pulse width (int) milliseconds. The input have to be included in the min max set range. 
        """        

    def moveToPulseWidth(self,width):
        
        if width< self.minWidth:
            width=self.minWidth
        elif width > self.maxWidth:
            width=self.maxWidth
        
        if width != self.currentPosition:            
            self.currentPosition=int(width)
            pwm.write(self.pin, self.period,self.currentPosition,MICROS)

        """
.. method:: getCurrentPulseWidth()
    Returns the servo motor position as pulse width (ms). 
        """                    
        
    def getCurrentPulseWidth(self):
        return self.currentPosition

        """
.. method:: getCurrentDegree()
    Returns the servo motor position as degrees. 
        """                    

    def getCurrentDegree(self):
        degree=self.map_range(self.currentPosition,self.minWidth,self.maxWidth,0,180)
        return degree
     
        
    