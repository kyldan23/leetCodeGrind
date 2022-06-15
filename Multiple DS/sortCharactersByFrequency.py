from collections import defaultdict
import heapq
class Solution:
    """ Understand 
    Questions: 
    1. Empty string = not possible given constraints of len(s) 
    2. Tie break between multiple characters that have the same frequency - does not matter
    3. Does capitalized/uncapitalized matter for the same letter? Yes, capitalized and 
    uncapitalized are treated as two separate characters. 
    4. Is there only letters? No, there can be digits in the string as well
    
    Test Case (Own): 
    Input: "hello"
    Output: "llheo" or "lleho" or "llohe" - basically any order of the characters after the l's
    
    Test case (Own): 
    Input: "helLo"
    Output: "helLo" or any ordering since all characters are unique here 
    
    Test Case (Own): 
    Input: "betae"
    Output: "eebta" - "bta" can be ordered in any way 
    """
    """Match 
    Keep Track of: Frequency of each character that appears - must iterate over the string at least once 
    
    Idea 1: Hashmap (Key: character, Value: Frequency)
        1. Iterate over all the characters, updating their frequency in the hashtable O(N)
        2. Sort the frequencies O(NlogN)
        3. Print out the new string O(N)
        Total Time: O(NlogN), Space: O(N)
    
    Idea 2: Heap? 
        1. Iterate over all the characters, updating their frequency in the hashtable O(N)
        2. Place everything into list in tuple form: [(frequency, character), (character, frequency)] - O(N)
        3. Heapify (max-heap) list - O(N)
        4. Pop out all elements from list and form string - O(N)
        Total Time: O(N) - removes need for sorting 
    """
    
    """Plan 
    1. Iterate over all the characters, updating their frequency in the hashtable 
    2. Place everything into list in tuple form: [(frequency, character), (character, frequency)]
    3. Heapify (max-heap) list
    4. Result = []
    4. Pop all elements from the max-heap 
        a. For each element popped, append that many elements to the list
    """
    """ Evaluate
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def frequencySort(self, s: str) -> str:
        #Input: "hello"
        dict_freq = defaultdict(int)
        for character in s: #{"h": 1 }
            dict_freq[character] += 1 
        
        list_freq = [] #[(-1, 'h'), (-2, 'l')]
        for character in dict_freq: 
            list_freq.append((-dict_freq[character], character))
        heapq.heapify(list_freq)
        
        result = [] 
        while list_freq:  
            curr = heapq.heappop(list_freq)  
            for _ in range(-curr[0]):  
                result.append(curr[1])
                """ Appending to the end of string could result in O(N^2) due to new string creation each time. Note result was originally an empty string. 
                result = result + curr[1]"""
        return "".join(result)
            
        