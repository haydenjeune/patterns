"""
Provides a simplified interface to a library, framework, or other
complex set of classes
"""


class Some:
    def do_a_thing(self):
        pass


class Complex:
    def the_very_first_thing(self):
        pass


class ThingDoer:
    def the_thing(self, thing: Some):
        pass


class Facade:
    # clients just call do, the facade deals with teh complexity of the thingdoer
    def do(self):
        a = Some()
        b = Complex()
        b.the_very_first_thing()
        c = ThingDoer()
        c.the_thing(a)