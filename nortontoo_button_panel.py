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


def run2():
    print("\nButton service started.")
    bp = ButtonPanel(0x6d, 0x6e, 0x6f)
    while True:
        for index, button in enumerate(bp.buttons, 1):
            try:
                if button.is_button_pressed():
                    subprocess.run(f"./button_{index}_task.sh", shell=True)
                    for _ in range(3):
                        button.LED_on(255)
                        time.sleep(0.05)
                        button.LED_on(7)
                        time.sleep(0.05)
                    while button.is_button_pressed():
                        time.sleep(0.02)
            except Exception as e:
                print(e)

        time.sleep(0.02)

def run():
    print("\nButton service started.")

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
