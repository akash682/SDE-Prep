class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        reference = "123456789"
        
        low_digits = len(str(low))
        high_digits = len(str(high))
        
        res = []
        
        for window in range(low_digits, high_digits+1):
            for win_pos in range(10 - window):
                hikaku = int(reference[win_pos:win_pos+window])
                if low <= hikaku and hikaku <= high:
                    res.append(int(reference[win_pos:win_pos+window]))
        
        return res