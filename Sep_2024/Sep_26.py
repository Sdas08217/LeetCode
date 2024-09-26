# My Calendar I
class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.bookings:
            if max(start, s) < min(end, e):
                return False
        self.bookings.append((start, end))
        return True

  # Example usage of MyCalendar
myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # Output: True, event is booked
print(myCalendar.book(15, 25))  # Output: False, overlap with previous event
print(myCalendar.book(20, 30))  # Output: True, no overlap
