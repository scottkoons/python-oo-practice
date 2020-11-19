"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Create a new generator, starting at start. Both start & next are set to the initial start argument"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Show the default information"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Generate a new serial number using next"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""
        self.next = self.start
