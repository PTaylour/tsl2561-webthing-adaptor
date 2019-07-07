"""TSL2561 adapter for Mozilla WebThings Gateway."""

from gateway_addon import Property


class TSL2561Property(Property):
    """Property type for Eufy smart switches/plugs."""

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        device -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)
        self.set_cached_value(value)

    def set_value(self, value):
        """
        Set the current value of the property.
        value -- the value to set
        """
        if self.name == 'threshold':
            self.set_value(value)

    def update(self):
        """Update the current value, if necessary."""
        if self.name != 'on':
            return

        value = self.device.is_on()
        if value != self.value:
            self.set_value(value)
