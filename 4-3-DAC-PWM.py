import RPi.GPIO as GPIO

aux = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.OUT)
p = GPIO.PWM(aux, 1000)
p.start(0)

try:
    while True:
        inputStr = input("Enter a value betweeen 0 and 100 ('q' to exit) >")

        if inputStr.isdigit():
            value = float(inputStr)
            if value>100 or value<0:
                print("The value is invalid, try again")
                continue    
            p.ChangeDutyCycle(value)    
        elif inputStr == 'q':
            break
        else:
            print("Enter a positive float")
            continue    
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exeptions")
finally:
    p.stop()
    GPIO.cleanup(aux)
    print("GPIO cleanup completed")