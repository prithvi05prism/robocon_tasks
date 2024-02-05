class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        listing = [[]]
        for i in range(0, numRows):
	        term = 1
	        row=[]
	        for j in range(0, i+1):
		        row.append(term)
		        term = int((term*(i-j)/(1+j)))
	        listing.append(row)

        listing.remove([])
        return listing
        