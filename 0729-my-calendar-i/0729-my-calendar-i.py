from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()
        
    def book(self, start: int, end: int) -> bool:
        indexToInsert = self.calendar.bisect_right((start, end))
        
        if ((indexToInsert > 0 and self.calendar[indexToInsert - 1][1] > start) or 
            (indexToInsert < len(self.calendar) and self.calendar[indexToInsert][0] < end)):
                return False

        self.calendar.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)