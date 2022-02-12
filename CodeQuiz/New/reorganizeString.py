from collections import Counter
from heapq import heappush, heappop
from re import S
from this import s

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        max_freq = Counter(S).most_common(1)[0][1]
        if 2*max_freq -1 > len(S):
            return ""
        else:
            heap = []
            for k,v in Counter(S).items():
                heappush(heap, (v*-1, k))
            result = []
            while heap:
                v,k = heappop(heap)
                if not result or k != result[-1]: # can add the top most element
                    result.append(k)
                    if v != -1:
                        heappush(heap,(v+1,k))
                else:                             # cannot add the top most element
                    v1,k1 = heappop(heap)
                    result.append(k1)
                    heappush(heap, (v,k))
                    if v1 != -1:
                        heappush(heap, (v1+1,k1))
            return "".join(result)

    def myfunc(self,s):
        s_counter = Counter(s)
        ref = []
        for key in s_counter.keys():
            ref.append((key, s_counter[key]))
        
        ref = sorted(ref, key=lambda y:y[1])
        black_queue = [ref.pop()]
        white_queue = ref
        res = ""
        while white_queue and black_queue:
            b, bc = black_queue.pop()
            w, wc = white_queue.pop()
            if bc > wc:
                res+= (b+w)*wc
                black_queue.append((b,bc-wc))
            elif bc < wc:
                res += (w+b)*bc
                black_queue.append((w,wc-bc))
            elif wc == bc:
                res += (w+b)*bc
                if not white_queue:
                     break
                else:
                    black_queue.append(white_queue.pop())
        
        if black_queue:
            if black_queue[0][1] == 1:
                res += black_queue[0][0]
            else:
                return ""
        return res

s = "aaaabddbccee"
mySolution = Solution()
mySolution.reorganizeString(s)