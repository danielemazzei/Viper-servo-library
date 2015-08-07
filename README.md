===================
Viper Servo library
===================

This module contains Viper class definitions for servo motors.
The Servo class provides methods for handling generic servo motors connected to pins endowed with PWM.
It also provides easily accessible attributes for direct control motor position with pulse width or degree.

Every Servo instance implements the following methods:

    * attach: connects the servo motor and sets the default position
    * detach: sets the PWM pulse width of the instanced servo to 0 disconnecting the motor
    * moveToDegree: sets the servo position to the desired angle passed as float
    * moveToPulseWidth: sets the servo position to the desired raw value expressed as pulse width (int) milliseconds
    * getCurrentPulseWidth: returns the current servo position in pulse width (int) milliseconds
    * getCurrentDegree: returns the current position in degrees


    Author: Daniele Mazzei
    Contributor Giacomo Baldi

    License GPL3

    info www.viperize.it