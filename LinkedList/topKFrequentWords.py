import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """ Step 1: Understand - Create test cases, especially edge cases relating to the inputs
        Edge Cases: 
            1. What if k is greater than the number of unique words in the list? 
            2. What if k is negative? 
        """
        """Step 2: Broad Strategy (Guides Data Structure Selection)
        1. Count associated with each word (Mapping Hashtable: word => count)
        2. Grab the k most frequent words 
        """
        """Step 3: Consider Data Structure Runtimes (Matching Stage)
        Runtime Using Heap: 
        *Constructing the heap (heapify): O(N)
        *Grabbing k elements from heap: k elements * O(logN) = O(k*logN), where k < N(number of elements)
        
        Runtime Using Hashmap: 
        *Adding all elements to the hashmap: O(N)
        *Sorting the elements by occurences: O(N*logN) - fastest time for sorting
        
        Conclusion: If k is very small, Heap offers the best runtime, without sorting. 
        """
        """Step 4: Pseudo-code
        word_to_count = calculate_count(words) #Function returns a dictionary (word=> count)
        word_count_heap = heapify(word_to_count) #creates a heap of tuples with each containing the word and its count 
        result = [] #contains k most frequent words 
        for i in range(k): 
            result.append(word_count_heap.pop())
        return result
        """ 
        """Step 5: Verification / Analysis 
        1. Run through test cases 
        2. Time Complexity: O(N) for dictionary creation + O(N) to convert dict to list + O(N) to heapify list  + O(k*logN) pop k elements from heap = O(N) + O(k*logN)
        3. Space complexity: O(N) for dictionary creation + O(N) to convert dict to list + O(1) no storage to heapify + O(k) store k elments in result => O(N)
        """
        
        #Create dictionary of (word:count):
        word_to_count = self.calculate_count(words) #{word:count}
        
        #Convert dictionary to list of tuples: [(count1, word1), (count2, word2)]
        word_count_pairs = []
        for word,count in word_to_count.items():
            word_count_pairs.append((-count, word)) #Python's heap is implmented as minheap only
        
        #Heapify list of (count, word) pairs 
        heapq.heapify(word_count_pairs)
        
        #Pop k elements from heap
        result = [] 
        for i in range(k):  
            result.append(heapq.heappop(word_count_pairs)[1]) #extract only the word from the tuple
        return result
        
        
    def calculate_count(self, words): 
        result_dict = {}
        for word in words:  
            if word in result_dict: 
                result_dict[word] += 1
            else: 
                result_dict[word] = 1
        return result_dict