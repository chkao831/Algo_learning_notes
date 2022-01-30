class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        start = -1
        min_len = len(s1)+1
        
        i, j = 0, 0
        while(i < len(s1)):
            # aligning beginning
            if(s1[i] == s2[j]): # start is found
                j += 1 
                if(j == len(s2)): # end is found
                    end = i + 1 # mark the end
                    j -= 1 # start turning back
                    while(j >= 0): 
                        if(s1[i] == s2[j]):
                            j -= 1 # once matched an element, turn further back
                        i -= 1
                    # now, i is pointing to one-char front of s1 and j is negative
                    i += 1 # to point to the start of s1
                    j += 1 # to point to the start of s2
                    if(end - i < min_len):
                        min_len = end - i
                        start = i
            # iterate through s1              
            i += 1
        
        returned_str = ""
        if(start != -1): 
            returned_str = s1[start: start+min_len]
            
        return returned_str
