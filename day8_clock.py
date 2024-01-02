# Imports
from machine import Pin
from neopixel import NeoPixel
import time
import math


def get_hms_leds(chour_led=0, cmin_led=0, csec_led=0):
    #function to get the LED indexes to light up on the ring based on the current time

    #get te local time and add 1 because it is zero indexed
    chour = time.localtime()[3] + 1
    cmin = time.localtime()[4]
    csec = time.localtime()[5]

    #print the hours, mins, secs
    print('    actual: ', chour, ' ', cmin, ' ', csec)

    #calculate the hour LED
    if chour < 6:
        #set LED to hour + 6 LEDs
        chour_led = chour + 6
    elif chour >= 6 and chour < 12:
        #subtract 6 LEDs
        chour_led = chour - 6
    elif chour >= 12 and chour < 18:
        #subtract 12 hours, but add 6 LEDs
        chour_led = chour - 12 + 6
    else:
        #chour is 18 to 24
        #subtract 12 hours and 6 LEDs
        chour_led = chour - 12 - 6

    #calculate the minute LED
    if cmin < 30:
        #set LED to min + 6 LEDs
        cmin_led = cmin/5 + 6
    else:
        #subtract 6 LEDs
        cmin_led = cmin/5 - 6
    
    #round down to the nearest 5 minutes
    cmin_led = math.floor(cmin_led)

    #calculate the second LED
    if csec < 30:
        #set LED to min + 6 LEDs
        csec_led = csec/5 + 6
    else:
        #subtract 6 LEDs
        csec_led = csec/5 - 6

    #round down to the nearest 5 seconds
    csec_led = math.floor(csec_led)

    #calculated LED to light up
    print('calculated: ', chour_led, ' ', cmin_led, ' ', csec_led)

    #return the new led numbers to the function call
    return chour_led, cmin_led, csec_led


def main():
    #Main Routine
    # Define the strip pin number (2) and number of LEDs (12)
    ring = NeoPixel(Pin(2), 12)

    # Define some RGB color variables
    hr_color = 0,10,0 #green
    min_color = 10,0,0 #red
    sec_color = 0,0,10 #blue

    # Initialize variables
    hr_led, min_led, sec_led = 0, 0, 0

    # Turn off all LEDs before starting rest of program
    ring.fill((0,0,0))
    ring.write()
    time.sleep(1)

    #run in perpetuity
    while True:
        # reset the previous LEDs to clear
        ring[hr_led] = ((0,0,0))
        ring[min_led] = ((0,0,0))
        ring[sec_led] = ((0,0,0))

        #get the new LEDs to light up  with the new time
        hr_led, min_led, sec_led = get_hms_leds(hr_led, min_led, sec_led)

        #light up the new LEDs
        ring[hr_led] = ((hr_color))
        ring[min_led] = ((min_color))
        ring[sec_led] = ((sec_color))
        ring.write()

        #update every 5 seconds because we have a ring with 12 lights (60/12 = 5)
        # Show the LED for this long
        time.sleep(5)


if __name__ == '__main__':
    main()
