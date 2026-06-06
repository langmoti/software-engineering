#############################################################################
# Unveraenderliche Dataclasses
# A unchangable dataclass defines a __hash__ method that makes it unique -> ie. permits use as dict key
# 
# After instanciation no changes of variables possible.

# Example unchangable/frozen dataclass:
from dataclasses import dataclass, field

@dataclass(frozen=True)
class FrozenPoint:
  x: float = field(default=0)
  y: float = field(default=0)

# Change triggers new object/instance with new values:
from dataclasses import dataclass, field, replace

fp = FrozenPoint()
fp = replace(x=1, fp)
# fp.x is now 1 and previous object was overwritten by a new object.
# If not using fp =, the old object would still be referenced by fp, so two FrozenPoint instances would exist now.
#############################################################################

#############################################################################
# Properties
# @property decorator permits to use methods like attributs
# class_instance.method() becomes class_instance.method 
# () triggers then even an error
#
# This way, attribute/properties can be computed when called (ie. depending on other values)
#
# Write protected attributes:
# Property decorator gets the value but prohibts overwriting of it, so a self._variable can be read by instance.variable but not written
# 
# Example:
# ...
# __init__(self, radius):
#    self._radius = radius
#
# @property
# def radius(self):
#   return self._radius
# ...
#
# Setter:
# Once a property has been defined, a decorator named @property_name.setter is possible, creating a method below named again like the property.
# (Only with property decorator can two methods have the same name! This is an exception of the rule!)
# property_name is the name of the property, so from aforementioned example its @radius.setter.
# Using the setter decorator, the property can be overwritten, however as method many checks etc. can be performed beforhand.
#
# Setter Example:
# @radius.setter
# def radius(self, new_radius):
#    ... perform checks ... ie. not negative 
#    self._radius = new_radius
#    return
#############################################################################

#############################################################################
# Dataclass have a __post_init__() -> if defined, the auto generated method calls the __post_init__(self, ...).
# InitVar[T] as typ that is forwarded to __post_init__(self, ...) and used there
# field with init=False is set in __post_init__(self, ...)
# InitVar[float] -> the attribute becomes a float when __post_init(self, ...) gets called.
# Means also the attribute with InitVar[float] is not stored as self.var in generated __init__
# One can still print self.var when used with InitVar[float], but it will show the default values like "class template".
# So it never changes to another value.
# 
# Example:
# class ...:
#   x: InitVar[float] = 0.0
#   y: int = field(init=False)
#
#   def __post_init__(self, x):
#     self.y = x
#     ...
# x will always be 0.0, y will change in every instance of the class.
#############################################################################

if __name__ == '__main__':
  print('This file only contains notes and no code to be really run and shown.')
