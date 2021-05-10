import math # i am using the square root from math lib, assuming we dont have to implement that
class Complex:


    def __init__(self, real, imag):
        """ Constructs a new complex number

        Args:
            real (number): The real part of the number
            imag (number): The imaginary part of the number
        """
        self.real = real # the real number
        self.imag = imag # the imaginary number (whitout the i part)



    # Assignment 3.3

    # i was unsure if i should assign the new values to self, or return a new complex number
    # so i decided instead of using self.real, self.imag im using r and i and returning a new complex number instead of returning self.

    # assigning to self example:
    #def __add__(self, other):
    #    self.real += other.real
    #    self.imag += other.imag
    #    return self

    def conjugate(self):
        """Returns a Conjugates version of the complex number"""
        i = self.imag * -1 # flipping the sign of the imaginary part (making the real part "mirrored" on its axis)
        return Complex(self.real, i)

    def modulus(self):
        """Returns the modulus/length of the complex number"""
        m = math.sqrt((self.real ** 2) + (self.imag ** 2)) # getting the length of the complex number, square (real^2 + imaginary^2)
        return m

    def __add__(self, other):
        """
        Adds this complex number with another
            Returns:
                the result of the addition
        """
        r = self.real + other.real # adding real and imaginary parts of each number together
        i = self.imag + other.imag
        return Complex(r,i)

    def __sub__(self, other):
        """
        Subtract this complex number with another
            Returns:
                the result of the subtraction
        """
        r = self.real - other.real # subtracting real and imaginary parts of each number together
        i = self.imag - other.imag
        return Complex(r,i)

    def __mul__(self, other):
        """
        Multiplys this complex number
            Returns:
                the result of the multiplication
        """
        # (a,b) * (c,d) = (a*c + a*d + b*c + b*d)
        # a and c consist only of real numbers, b*d becomes (b*d)i^2 and we know that i^2 = -1, so we can replace i^2 with -1 and get a real number
        r = (self.real * other.real) + ((self.imag * other.imag) * -1)
        # a * d and b * c, stays imaginary.
        i = (self.real * other.imag) + (self.imag * other.real)
        return Complex(r,i)

    def __eq__(self, other):
        """ Compares this complex number to another
            Returns:
                True: if they are equal
                False: if they are not equal
        """
        if ( self.real == other.real and self.imag == other.imag ): # compare the real and imaginary parts of each complex number, return true if they are equal
            return True
        else:
            return False


    # Assignment 3.4
    def __radd__(self, other):
        """
        Adds this complex number with another
            Returns:
                the result of the addition
        """
        if not isinstance(other, Complex) and not isinstance(other, complex): # if its not a complex number im assuming its a normal real number
            other = Complex(other, 0)   # turning it into a complex number with only the real part
        return self + other

    def __rsub__(self, other):
        """
        Subtract this complex number with another
            Returns:
                the result of the subtraction
        """

        if not isinstance(other, Complex) and not isinstance(other, complex): # if its not a complex number im assuming its a normal real number
            other = Complex(other, 0) # turning it into a complex number with only the real part
        if isinstance(other, complex):
            other = Complex(other.real, other.imag)

        return other - self # subtracting is not communative
    def __rmul__(self, other):
        """
        Multiplys this complex number
            Returns:
                the result of the multiplication
        """
        return self * other


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass

