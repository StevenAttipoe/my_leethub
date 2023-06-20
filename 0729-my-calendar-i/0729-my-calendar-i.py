class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        for bookedStart, bookedEnd in self.calendar:
            if bookedStart < end and start < bookedEnd:
                return False
        self.calendar.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)