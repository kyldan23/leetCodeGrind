class Solution:
    """
    Plan: 
    1. Sort all the intervals by the first element first, since order is not guaranteed 
    2. By default, have the first interval stored in the result list 
    3. Iterate over rest of intervals, except first 
        a. If current starting is within the most recent interval in result: 
            - Set the ending to the greater of the two 
        b. Else: #Current interval is not within the previous interavl 
            - Append current interval to result list 
    
    Complexity: 
        Time: O(NlogN) - sort by first element, since order is NOT guaranteed 
        Space: O(N) - result array could potentially contain all the original intervals 
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) 
        result = [intervals[0]]
        for start, end in intervals[1:]:
            previous = result[-1]
            if start >= previous[0] and start <= previous[1]: 
                previous[1] = max(end, previous[1])
            else: 
                result.append([start, end])
        return result 