class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1
        for i in range(int(sqrt(area)), 1, -1):
            if(area%i==0):
                W = i
                break

        L = int(area/W)
        out = [L, W]

        return out