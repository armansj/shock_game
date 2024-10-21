from machine import Pin
import time
import random

led_pins = [0, 1]
shock_pin = Pin(2, Pin.OUT)
button_pin = Pin(3, Pin.IN, Pin.PULL_UP)
buzzer_pin = Pin(4, Pin.OUT)

leds = [Pin(pin, Pin.OUT) for pin in led_pins]
shock = shock_pin

def activate_shock():
    print("Shock activated!")
    shock.value(1)
    time.sleep(1)
    shock.value(0)
    print("Shock delivered!")

def play_game():
    while True:
        if button_pin.value() == 0:
            print("Starting the game...")
            # Turn off all LEDs
            for led in leds:
                led.value(0)

            chosen_player_index = random.randint(0, len(leds) - 1)
            print(f"Player {chosen_player_index + 1} is chosen!")

            leds[chosen_player_index].value(1)

            buzzer_pin.value(1)
            time.sleep(1)
            buzzer_pin.value(0)

            input("Press Enter when the chosen player puts their hand on the shock module...")

            activate_shock()

            leds[chosen_player_index].value(0)

try:
    play_game()
except KeyboardInterrupt:
    print("Exiting game.")
