import math

class RpnCalculator:


    def __init__(self):
        self.history = []

    ## Calculator methods
    def push(self, value):
        """
        Adds a value to the calculators stack
        """
        self.history.append(value)

    def result(self):
        """
        Returns the last pushed value from the stack without removing it. If no result is available, method should return 0.
        """
        # most pythonic way to get last in last is -1
        return self.history[-1]

    def stack(self):
        """
        Returns a list of values representing the current internal stack
        """
        return self.history

    def pop(self):
        """
        Removes the last pushed value from the calculators stack
        """
        return self.history.pop()

    def clear(self):
        """
        Cleans the internal state of our calculator
        """
        self.history.clear()

    ##  Math Methods
    def add(self):
        """
        Adds the two latest values pushed. Push 2, Push 3 (add) -> 5
        """
        a = self.pop()
        b = self.pop()
        c= a+b
        self.push(c)

    def sub(self):
        """    
        Subtracts the latest value pushed from the second last value pushed. Push 5, Push 3, (sub) -> 2
        """
        a = self.pop()
        b = self.pop()
        c= b-a
        self.push(c)

    def mul(self):
        """
        Multiplies the two latest values pushed. Push 2, Push 3, (mul) -> 6
        """
        a = self.pop()
        b = self.pop()
        c= a*b
        self.push(c)

    def div(self):
        """
        Divides the the second last value pushed by the last value pushed. Push 5, Push 2, (div) -> 2.5
        """
        a = self.pop()
        b = self.pop()
        c= b/a
        self.push(c)

    def sqrt(self):
        """
        Calculates the square root of the last value pushed. Push 9, (sqrt) -> 3
        """
        a = self.pop()
        c= math.sqrt(a)
        self.push(c)
