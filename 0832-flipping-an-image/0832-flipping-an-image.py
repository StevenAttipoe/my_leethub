class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if not image:
            return []
        
        ROW, COL = len(image), len(image[0])
        flippedImage = []
        
        for i in range(ROW):
            flippedRow = []
            for j in range(COL - 1, -1, -1):
                if image[i][j] == 0:
                    flippedRow.append(1)
                else:
                    flippedRow.append(0)
            flippedImage.append(flippedRow)
            
        return flippedImage
        