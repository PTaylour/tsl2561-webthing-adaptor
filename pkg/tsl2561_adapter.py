"""TSL2561 adapter for Mozilla WebThings Gateway."""

from gateway_addon import Adapter
from .tsl2561 import get_devices
from .tsl2561_device import TSL2561Device

_TIMEOUT = 3


class TSL2561Adapter(Adapter):
    """Adapter for TSL2561 smart bulbs."""

    def __init__(self, verbose=False):
        """
        Initialize the object.

        verbose -- whether or not to enable verbose logging
        """
        self.name = self.__class__.__name__
        Adapter.__init__(self,
                         'tsl2561-adapter',
                         'tsl2561-adapter',
                         verbose=verbose)

        self.pairing = False
        self.start_pairing(_TIMEOUT)

    def start_pairing(self, timeout):
        """
        Start the pairing process.

        timeout -- Timeout in seconds at which to quit pairing
        """
        if self.pairing:
            return

        self.pairing = True
        for dev in get_devices():
            _id = dev['_id']
            if _id not in self.devices:
                device = TSL2561Device(self, _id, dev)
                self.handle_device_added(device)

        self.pairing = False

    def cancel_pairing(self):
        """Cancel the pairing process."""
        self.pairing = False
