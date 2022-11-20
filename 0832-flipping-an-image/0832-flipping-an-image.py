class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if not image:
            return []
        
        ROW, COL = len(image), len(image[0])
        
        for r in range(ROW):
            i, j = 0 , COL - 1
            while i <= j:
                image[r][i], image[r][j] = image[r][j]^1, image[r][i]^1 
                i += 1
                j -= 1
        return image
        