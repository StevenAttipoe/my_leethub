class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:x[1])
        maxUnits = 0

        while truckSize > 0 and boxTypes:
            boxCount, unitCount = boxTypes.pop()
            boxCount = min(boxCount, truckSize)
            truckSize -= boxCount
            maxUnits += unitCount * boxCount

        return maxUnits

    def maximumUnits1(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for boxCount, unitCount in boxTypes:
            heapq.heappush(heap, [-unitCount, boxCount])

        maxUnits = 0
        while truckSize > 0 and heap:
            unitCount, boxCount  = heapq.heappop(heap)
            boxCount = min(boxCount, truckSize)
            truckSize -= boxCount
            maxUnits += -unitCount * boxCount

        return maxUnits


    def maximumUnits2(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:-x[1])
        maxUnits = 0
        curBoxes = 0

        for boxes, units in boxTypes:
            if curBoxes >= truckSize:
                break

            if boxes + curBoxes >= truckSize:
                boxesLeft = truckSize - curBoxes
                maxUnits += units * boxesLeft
                curBoxes += boxesLeft
            else:
                maxUnits += units * boxes 
                curBoxes += boxes

        return maxUnits


