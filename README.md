
## About

This program runs as a Unix daemon and display the current time with
the LEDs on a Logitech (G512) keyboard:

* Function Keys: Hours
* Number keys: Minutes (Tens)
* Number blockkeys: Minutes (Ones)
* "P" and "A" keys: PM or AM


## Installation

### Base steps

* Install https://github.com/MatMoul/g810-led and put it on the PATH
* Create / configure a default profile for the LEDs in `/etc/g810-led/profile`,
  for example from
  https://github.com/MatMoul/g810-led/blob/master/sample_profiles/colors
* To try: Run ` nohup python3 g512_keyboard_clock.py & ` 


### Installation as a systemd service
* `sudo cp g512-keyboard.service /etc/systemd/system`
* `sudo systemctl daemon-reload`
* `sudo systemctl enable g512-keyboard`
* `sudo systemctl start g512-keyboard`


