# My Calendar II
class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start, end):
        # Check if the new booking overlaps with any double booking
        for s, e in self.overlaps:
            if start < e and end > s:  # There is an overlap with a double booking
                return False
        
        # Check for overlaps with the single bookings to update the double bookings
        for s, e in self.booked:
            if start < e and end > s:  # There is an overlap
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.overlaps.append((overlap_start, overlap_end))
        
        # If no triple booking, add the new booking to the single bookings
        self.booked.append((start, end))
        return True
#Example usage
# Instantiate the MyCalendarTwo object
myCalendarTwo = MyCalendarTwo()

# Book some events and print the result
print(myCalendarTwo.book(10, 20))  # Expected output: True, as the event can be booked
print(myCalendarTwo.book(50, 60))  # Expected output: True, as the event can be booked
print(myCalendarTwo.book(10, 40))  # Expected output: True, as this causes only a double booking
print(myCalendarTwo.book(5, 15))   # Expected output: False, as this would cause a triple booking
print(myCalendarTwo.book(5, 10))   # Expected output: True, no triple booking
print(myCalendarTwo.book(25, 55))  # Expected output: True, overlaps but no triple booking
