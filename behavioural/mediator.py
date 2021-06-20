"""Reduces complex dependencies between objects by restricting communication to
a mediator object.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseMediator(ABC):
    @abstractmethod
    def notify(self, sender: Any, event: str):
        raise NotImplementedError


class Component:
    def __init__(self, mediator: BaseMediator):
        self.mediator = mediator


class Button(Component):
    def submit(self):
        print(f"Submitting with {self.__class__}")
        self.mediator.notify(self, "Submit")


class SometimesVisibleButton(Button):
    def __init__(self, mediator: BaseMediator):
        super().__init__(mediator)
        self.is_visible = False

    def toggle_visibility(self):
        self.is_visible = not self.is_visible
        print(f"Button is_visible is now {self.is_visible}")


class TickBox(Component):
    def __init__(self, mediator: BaseMediator):
        super().__init__(mediator)
        self.ticked = False

    def toggle(self):
        print("Box has been toggled")
        self.ticked = not self.ticked
        self.mediator.notify(self, str(self.ticked))


class AreYouSureWindow(Component):
    def __init__(self, mediator: BaseMediator):
        super().__init__(mediator)
        self.is_visible = False

    def make_visibile(self):
        self.is_visible = True
        print(f"A window checking if you are sure is now visible")


class SomeDialog(BaseMediator):
    def __init__(self):
        self.always_visible_button = Button(self)
        self.sometimes_visible_button = SometimesVisibleButton(self)
        self.tick_box = TickBox(self)
        self.are_you_sure_window = AreYouSureWindow(self)

    def notify(self, sender: Any, event: str):
        if sender is self.tick_box:
            self.sometimes_visible_button.toggle_visibility()
        if sender in {self.always_visible_button, self.sometimes_visible_button}:
            self.are_you_sure_window.make_visibile()


if __name__ == "__main__":
    dialog = SomeDialog()

    # click on the toggle
    dialog.tick_box.toggle()

    # submit with the button
    assert dialog.sometimes_visible_button.is_visible
    dialog.sometimes_visible_button.submit()