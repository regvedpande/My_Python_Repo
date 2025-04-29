class SmartLight:
    def __init__(self, is_on=False):
        self._is_on = is_on  # Encapsulated state

    def turn_on(self):
        """Turns the light on."""
        self._is_on = True
        print("Light is now ON.")

    def turn_off(self):
        """Turns the light off."""
        self._is_on = False
        print("Light is now OFF.")

    def get_status(self):
        """Returns the current status of the light."""
        return "ON" if self._is_on else "OFF"

# Usage:
my_light = SmartLight()
my_light.turn_on()
print(f"The light is: {my_light.get_status()}")
my_light.turn_off()
