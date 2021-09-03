## Leet Code, ex. 2: "Roman to Integer"

# Convert a roman numeral to an integer

class Solution(object):
    def romanToInt(self, s):
        dic = {
               "I":1,
               "V":5,
               "X":10,
               "L":50,
               "C":100,
               "D":500,
               "M":1000,
        }
        
        previous = 0
        current = 0
        total = 0
        
        for i in range(len(s)):
            current = dic[s[i]]
            if current > previous:
                # -2*previous: previous number is added, so subtracted twice to nullify addition                    
                total = total + current -2 * previous 
            else:
                total += current
            previous = current
            
        return total