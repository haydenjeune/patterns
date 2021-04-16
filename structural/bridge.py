"""
Bridge lets you split a large class or set of closely related classes into two
separate hierarchies - abstraction and implementation - which can be developed
independently of each other.
"""

from typing import Protocol


class Device(Protocol):
    def is_enabled(self):
        raise NotImplementedError()

    def enable(self):
        raise NotImplementedError()

    def disable(self):
        raise NotImplementedError()

    def get_volume(self) -> int:
        raise NotImplementedError()

    def set_volume(self, percent: int):
        raise NotImplementedError()


class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.disable() if self.device.is_enabled() else self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 1)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 1)


class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)


class PanasonicUltraVision3000TV:
    def is_enabled(self):
        # some integration code specific to this model of TV
        print("This TV can never truly be turned off!")
        return False

    def enable(self):
        # some integration code specific to this model of TV
        print("Trying to enable")
        return

    def disable(self):
        # some integration code specific to this model of TV
        print("Trying to disable")
        return

    def get_volume(self) -> int:
        # some integration code specific to this model of TV
        print("The volume is always set to 11 on this tv!")
        return 11

    def set_volume(self, percent: int):
        # some integration code specific to this model of TV
        print("Trying to set the volume")
        return


if __name__ == "__main__":
    tv = PanasonicUltraVision3000TV()
    remote = AdvancedRemote(device=tv)

    remote.toggle_power()
    remote.mute()
    remote.volume_up()
    remote.volume_down()
