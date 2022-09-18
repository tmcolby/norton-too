#!/usr/bin/env python3
import qwiic_i2c
import qwiic_button
import time
import sys
import subprocess

class ButtonPanel(object):
    def __init__(self, *i2c_address):
        self.buttons=list()
        for address in i2c_address:
            self.buttons.append(qwiic_button.QwiicButton(address))
         
        for button in self.buttons:
            if not button.begin():
                print(f"Problem initializing button {button}")

LED_MAX = 255
LED_MIN = 7
def run2():
    print("Button service started.")
    bp = ButtonPanel(0x6d, 0x6e, 0x6f)
    while True:
        for index, button in enumerate(bp.buttons, 1):
            try:
                if button.is_button_pressed():
                    for _ in range(3):
                        button.LED_on(LED_MAX)
                        time.sleep(0.05)
                        button.LED_on(LED_MIN)
                        time.sleep(0.05)
                    if not button.is_button_pressed():
                        """ this is a click """
                        # execute the task on a short click of the button
                        print(f"CLICK event: button {index}")
                        subprocess.run(f"./button_{index}_click.sh", shell=True)
                        # time.sleep(1)  # no spamming the button
                    else:
                        """ this is long press """
                        button.LED_on(LED_MAX)
                        print(f"LONG PRESS event: button {index}")
                        # execute task on the release of the button
                        subprocess.run(f"./button_{index}_long_press.sh", shell=True)
                        while button.is_button_pressed():
                            time.sleep(0.02)
                        button.LED_on(LED_MIN)
            except Exception as e:
                print(e)

        time.sleep(0.02)

def run():
    print("Button service started.")

    my_button1 = qwiic_button.QwiicButton(0x6d)
    my_button2 = qwiic_button.QwiicButton(0x6e)
    my_button3 = qwiic_button.QwiicButton(0x6f)

    if my_button1.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button2.begin() == False:
        print("\nThe Qwiic Button 2 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    if my_button3.begin() == False:
        print("\nThe Qwiic Button 3 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    print("\nAll buttons ready!")

    while True:
        # Check if button 1 is pressed
        if my_button1.is_button_pressed() == True:
            print("\nButton 1 [0x6d] is pressed!")
            subprocess.run('./kiosk.sh', shell=True)
            while my_button1.is_button_pressed(): 
                time.sleep(0.1)
        
        # Check if button2 is pressed
        if my_button2.is_button_pressed() == True:
            print("\nButton 2 [0x6e] is pressed!")
            while my_button2.is_button_pressed(): 
                time.sleep(0.1)

        # Check if button3 is pressed
        if my_button3.is_button_pressed() == True:
            print("\nButton 3 [0x6f] is pressed!")
            subprocess.run('./toggle-keyboard.sh', shell=True)
            while my_button3.is_button_pressed(): 
                time.sleep(0.1)
        
        time.sleep(0.03)

if __name__ == '__main__':
    try:
        #run()
        run2()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nButton service exited.")
        sys.exit(0)
