'''
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        alphabet = ["" for _ in range(27)] # _, A, B, C etc.
        for i in range(1, 27):
            alphabet[i] = chr(97+i-1) #alphabet[1] = A, alphabet[26] = Z 
        '''
        decode("226", 0 , "", alphabet) -> 3
            decode("226", 1 , "B", alphabet) -> 2
                decode("226", 2 , "BB", alphabet)
                    decode("226", 3 , "BBF", alphabet) -> 1
                decode("226", 3 , "BZ", alphabet) -> 1
            decode("226", 2 , "V", alphabet)
                decode("226", 3 , "VF", alphabet) -> 1
        '''

        def decode(s: str, i: int, soln: str, alphabet: list , m: dict):
            if i in m:
                # the current known number of ways 
                return m[i]

            if i == len(s):
                #print(soln)
                return 1

            numWays = 0
            if i < len(s)-1:
                # two characters curr and next
                if 9 < int(s[i:i+2]) < 27:
                    numWays += decode(s, i+2, soln + alphabet[int(s[i:i+2])], alphabet, m)

            if  0 < int(s[i]) < 10:
                numWays += decode(s, i+1, soln + alphabet[int(s[i])], alphabet, m)

            m[i] = numWays

            return numWays

        return decode(s, 0, "", alphabet, {})

#print(decode("226", 0, "", alphabet))
