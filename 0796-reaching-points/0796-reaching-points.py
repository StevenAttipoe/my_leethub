class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if sx == tx:
                return (ty - sy) % sx == 0 
            if sy == ty:
                return (tx - sx) % sy == 0
            
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        return False

    def reachingPoints1(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False

        if sx == tx:
            return (ty - sy) % sx == 0 
        if sy == ty:
            return (tx - sx) % sy == 0

        if tx > ty:
            return self.reachingPoints(sx, sy, tx % ty, ty)
        else:
            return self.reachingPoints(sx, sy, tx, ty % tx)
        
        return False

    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            
            if tx > ty:
                tx -= ty
            else:
                ty -= tx

        return False

    # find y
    # x, xn +y = ty

    # find x
    # x + yn = tx

    # n = (ty - y) % x == 0

    # n = (tx - x) % y == 0
            

        