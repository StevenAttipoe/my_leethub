class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
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


