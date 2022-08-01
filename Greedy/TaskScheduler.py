import heapq
from collections import Counter, deque
class Solution:
    """ 
    Understand: 
    1. Are the tasks always grouped already by letter? 
    2. Is n less than the number of tasks? 
        Given: 
        -Input is limited to uppercase letters: A-Z (26 possible letters)
    Plan:
    Data Structures: 
    1. Hashmap with frequency of each letter task 
    2. Heap with all tasks that are able to be performed at the current time (no idle time)
    3. Queue with a tuple for each element (frequency, time until it can be added back to the heap)
    
    1. Get the count of each letter in "tasks"
    2. Heapify the list of counts into max-heap 
    3. Start time at 1 
    4. while heap or queue is not empty: #still more tasks to complete 
        -Pop element (frequency) from heap 
        -Reduce its value by 1 ("completing current task")
        -Add the frequency to the queue, along with the time it can be added back into the heap
        -If queue is not emepty, check the front element: 
            - If front element's time is equal to current time, add back to heap 
        -Increment the time 
    
    Evaluate: 
        Time: O(N)
            1. Count frequency of each task into dictionary: O(N)
            2. Adding to heap is O(log26) = O(1) since at most 26 elements, based on the number of letters in the alphabet, doesn't grow with input.  
        Space: O(1) - size of dictionary, queue, and heap are all capped at 26 elements, doesn't grow with input size. 
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        maxHeapCounts = [-count for count in taskCounts.values()]
        heapq.heapify(maxHeapCounts) #maxheap formed by minheap of negative values 
        
        time = 0 
        queue = deque() #tuple (count, nextTime)
        
        while maxHeapCounts or queue: #still more tasks to complete
            time += 1 
            
            if maxHeapCounts: 
                count = 1 + heapq.heappop(maxHeapCounts) #adding 1 since the counts are negative in the heap 
                if count < 0: 
                    queue.append((count, time + n)) # time + n is when the task can be added back to heap 
            if queue and (queue[0][1] == time): #check if first element in queue is ready to be added back 
                count = queue.popleft()[0] #only need the count from the tuple 
                heapq.heappush(maxHeapCounts, count)
        return time 
            
            
        
        
        
        
        