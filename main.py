################################################################################
# servo basics
#
# Created: 2015-07-30 16:19:43.367107
#
################################################################################

import servo
import streams

s=streams.serial()

# create a servo motor attaching it to the pin D11. Specification of the PWM feature using the Viper pin mapping signatire is required. 
# min max are left to defaults 500-2500. they need to be properly set to the servo specifications
# control signal period is left to default 20ms
MyServo=servo.Servo(D11.PWM)
  
    
while True:
    print("Servo ON")
    MyServo.attach()
    sleep(3000)
    
    print("Servo controlled in pulse width")
    for i in range (500,2500,10):
        MyServo.moveToPulseWidth(i)
        print(MyServo.getCurrentPulseWidth())
        # Very important: servo default control signal period is 20ms, don't update the controlling PWM at faster frequency!
        sleep (100) 
    
    print("Servo controlled in degrees")
    for i in range(0,180,1):
        # Very important: degree accuracy depends by the min max pulse width setup. Refer to the servo specifications for proper configuration
        MyServo.moveToDegree(i)
        print(MyServo.getCurrentDegree())
        sleep(100)
    
    print("servo OFF")
    MyServo.detach()
    sleep(3000)