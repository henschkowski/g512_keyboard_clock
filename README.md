
## About

This program runs as a Unix daemon and display the current time with
the LEDs on a Logitech (G512) keyboard:

* Function Keys: Hours
* Number keys: Minutes (Tens)
* Number blockkeys: Minutes (Ones)
* "P" and "A" keys: PM or AM


## Installation

* Install https://github.com/MatMoul/g810-led and put it on the PATH
* Configure a default profile for the LEDs in `/etc/g810-led/profile`,
  for example from
  https://github.com/MatMoul/g810-led/blob/master/sample_profiles/colors
* Run ` nohup python g512_keyboard_clock.py & ` 


