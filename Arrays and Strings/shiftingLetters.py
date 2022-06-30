class Solution:
    """ Understand
    1. Can there be more elements in shifts array than the length of s? Don't worry about
    Input: String "s", List "shifts"
    Output: String 
    """
    """ Plan 
    - Use ASCII to get a number associated with each letter
    1. Get the sum of all values in shifts
    2. Iterate over the values in shifts 
        a. Evaluate the next shift value and current shifted letter at the same time 
    3. Return shifts list 
    """
    """ Evaluate
    Time: O(N)
    Space: O(1) - reusing the original shifts array in the input, not using any extra data structure 
    """
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        for i in range(len(shifts)):
            total, shifts[i] = total - shifts[i], chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))
        return "".join(shifts)