"""TSL2561 adapter for Mozilla WebThings Gateway."""

from gateway_addon import Device
import socket
import threading
import time

from .TSL2561_property import TSL2561Property


_DEFAULT_THRESHOLD = 50
_POLL_INTERVAL = 2
_MINIMUM_POWER_SAVE_TIME = 1


class TSL2561Device(Device):
    """TSL2561 device type."""

    def __init__(self, adapter, _id, dev_dict):
        """
        Initialize the object.

        adapter -- the Adapter managing this device
        _id -- ID of this device
        dev_dict -- the device object to initialize from
        """
        Device.__init__(self, adapter, _id)
        self.sensor = dev_dict['sensor']
        self._type = ['OnOffSwitch', 'Light Sensor']

        if not self.name:
            self.name = self.description

        self.update_properties()

        self.properties['on'] = TSL2561Property(
            self,
            'on',
            {
                '@type': 'OnOffProperty',
                'label': 'On/Off',
                'type': 'boolean',
            },
            self.is_on())

        self.properties['on'] = TSL2561Property(
            self,
            'on',
            {
                '@type': 'ThresholdProperty',
                'label': 'Threshold in Lux',
                'type': 'number',
            },
            _DEFAULT_THRESHOLD)

        t = threading.Thread(target=self.poll)
        t.daemon = True
        t.start()

    def poll(self):
        """Poll the device for changes."""
        while True:
            time.sleep(_POLL_INTERVAL)
            self.update_properties()

            for prop in self.properties.values():
                prop.update()

    def update_properties(self):
        """Update the cached properties."""
        try:
            self.sensor_properties = {
                'lux': self.sensor.lux or 0}
        except socket.error:  # TODO update to appropriate IO error
            pass

    def is_on(self):
        """Determine whether or not the light is on."""
        return self.sensor_properties['lux'] > self.threshold()

    def threshold(self):
        return self.properties['threshold'].value
