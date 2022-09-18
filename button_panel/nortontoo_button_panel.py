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
def run():
    print("Button service started.")
    bp = ButtonPanel(0x6d, 0x6e, 0x6f)
    while True:
        # process each button forever
        for index, button in enumerate(bp.buttons, 1):
            try:
                if button.is_button_pressed():
                    # if pressed, flicker the button led
                    for _ in range(3):
                        button.LED_on(LED_MAX)
                        time.sleep(0.05)
                        button.LED_on(LED_MIN)
                        time.sleep(0.05)

                    if not button.is_button_pressed():
                        # event is a short "click"
                        print(f"CLICK event: button {index}")
                        subprocess.run(f"./button_{index}_click.sh", shell=True)
                        # time.sleep(1)  # no spamming the button
                    else:
                        # else, even is a  "long press"
                        print(f"LONG PRESS event: button {index}")
                        button.LED_on(LED_MAX)
                        subprocess.run(f"./button_{index}_long_press.sh", shell=True)
                        while button.is_button_pressed():
                            # wait until button is released
                            time.sleep(0.02)
                        button.LED_on(LED_MIN)
            except Exception as e:
                print(e)

        time.sleep(0.02)

if __name__ == '__main__':
    try:
        run()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nButton service exited.")
        sys.exit(0)
