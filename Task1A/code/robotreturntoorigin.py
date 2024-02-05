class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countx = 0
        county = 0

        for i in moves:
            if(i == 'U'): county = county +1
            if(i == 'R'): countx = countx +1
            if(i == 'L'): countx = countx -1
            if(i == 'D'): county = county -1

        if(countx == 0 and county == 0):
            return True
        
        return False