class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = None
        self.isPeeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.isPeeked:
            self.current = self.iterator.next()
            self.isPeeked = True

        return self.current
            

    def next(self):
        if self.isPeeked:
            self.isPeeked = False
        else:
            self.current = self.iterator.next()

        return self.current
        

    def hasNext(self):
        return self.isPeeked or self.iterator.hasNext()

class PeekingIterator2: # Won't work if None is part of elements
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.current
        

    def next(self):
        value = self.current
        self.current = self.iterator.next() if self.iterator.hasNext() else None
        return value
        

    def hasNext(self):
        return self.current != None

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
