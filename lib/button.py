from machine import Pin
from time import ticks_ms

class Button:
    def __init__(self, pin):
        self.last_press = 0
        self.last_long_press = 0
        self.long_press_achieved = False
        self.last_state = 1
        self.current_state = 1
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
    
    def pressed(self):
        response = 0
        self.current_state = self.pin.value()

        # Key down event
        if self.current_state == 0 and self.last_state == 1:
            self.last_press = ticks_ms()
            self.last_state = self.current_state
            self.long_press_achieved = False

        # Key held down (long press buildup)
        if not self.long_press_achieved:
            if self.current_state == 0 and self.last_state == 0:
                if (ticks_ms() - self.last_press) > 500:

                    # Make sure it's been some time since the last long press, too
                    if (ticks_ms() - self.last_long_press > 100):
                        self.last_long_press = ticks_ms()
                        self.long_press_achieved = True
                        response = 2

        # Key up event
        if self.current_state == 1 and self.last_state == 0:

            # Debounce
            if (ticks_ms() - self.last_press) > 10:

                # Make sure it's not a long press
                if (ticks_ms() - self.last_press) < 500:
                    response = 1
        
        self.last_state = self.current_state
        return response