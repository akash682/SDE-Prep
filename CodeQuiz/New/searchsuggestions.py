import heapq
class Solution:
    def suggestedProducts(self, products, searchWord):
        ans = []
        
        #create a heap of words
        #this is automatically sorted by lexicographical order
        hp = []
        for x in products:
            heapq.heappush(hp, x)
        
        #loop over every character of searchWord
        for i, char in enumerate(searchWord):
            #if empty heap, nothing to be done
            if not hp:
                ans.append([])
                continue
            #buffer contains at most 3 elements
            buffer = []
            while hp and len(buffer) < 3:
                this = heapq.heappop(hp)
                if len(this) >= i + 1 and this[:i+1] == searchWord[:i+1]:
                    buffer.append(this)
            #add the elements back to heap
            for x in buffer:
                heapq.heappush(hp, x)
            #suggestions at current character
            ans.append(buffer)
        
        return ans

mySolution = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
mySolution.suggestedProducts(products, searchWord)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # BruteForce Approach
        res = []
        for j in range(len(searchWord)):
            tmp = []
            for i in range(len(products)):
                if products[i][:j+1] == searchWord[:j+1]:
                    tmp.append(products[i])
            y = sorted(tmp)
            if len(tmp) >= 3:
                res.append(y[:3])
            else:
                res.append(y)
        
        return res
