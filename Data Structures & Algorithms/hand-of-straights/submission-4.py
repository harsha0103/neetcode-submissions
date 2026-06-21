from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = Counter(hand)
        min_arr = []
        for key in d:
            heapq.heappush(min_arr, (key, d[key]))

        prev = -1
        res = []
        
        while min_arr:
            # Flush group before starting a new one
            if len(res) == groupSize:
                while res:
                    new, new_count = res.pop()
                    if new_count > 0:
                        heapq.heappush(min_arr, (new, new_count))
                prev = -1

            curr, count = heapq.heappop(min_arr)
            if res and curr - prev != 1:
                return False
            res.append((curr, count - 1))
            prev = curr

        # Final group flush
        if len(res) != 0 and len(res) != groupSize:
            return False
        return True
