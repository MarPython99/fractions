"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `decimal` returning float value of the fraction.
"""
from math import gcd


class Fraction:
    """
    Fraction class.
    """

    def __init__(self, nom, denom):
        if denom == 0:
            raise ValueError
        d = gcd(nom, denom)
        self.nom = nom // d
        self.denom = denom // d
        if self.denom < 0:
            self.denom = self.denom*-1
            self.nom = self.nom * -1

    def __str__(self):
        return f"{self.nom}/{self.denom}"

    def __repr__(self):
        return f"Fraction({self.nom}, {self.denom})"

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom

    def __add__(self, other):
        y = self.denom*other.denom
        x = self.nom*other.denom + other.nom*self.denom
        return Fraction(x, y)

    def decimal(self):
        return self.nom/self.denom

    def __truediv__(self, other):
        x = self.nom*other.denom
        y = self.denom*other.nom
        return Fraction(x, y)

    def __mul__(self, other):
        x = self.nom*other.nom
        y = self.denom*other.denom
        return Fraction(x, y)

    def __sub__(self, other):
        y = self.denom*other.denom
        x = self.nom*other.denom - other.nom*self.denom
        return Fraction(x, y)
