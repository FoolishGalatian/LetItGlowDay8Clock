This code is an extension of "The PiHut Let it Glow Maker Advent Cabin" project for Day 8 (https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-8-rainbow-ring).

It is code that uses a 12-LED addressable RGB Ring to make a rudiementary clock. The clock uses 3 LED's on the ring to represent the hour (green), minute (red), and second (blue) hands on a clock. Since there are only 12 lights on the ring, the second hand updates every 5 seconds and the minute hand updates every 5 minutes, so I would not use it to make your next event, or you might be late. 

BECAUSE THIS IS BUILT TO RUN ON A RASPBERRY PI PICO WITH NO BATTERY, YOU WILL NEED TO SYNC THE REAL TIME CLOCK ON THE PICO BEFORE RUNNING THE PROGRAM (This can be done via Thonny or Visual Studio Code - MicroPico Device Controller Extension)

https://forums.raspberrypi.com/viewtopic.php?t=349334
