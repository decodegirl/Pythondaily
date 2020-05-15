#bruteforce solution

def longestPalindrome( s):
    longest = ""
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j] == s[i:j][::-1]:
                if len(longest) < len(s[i:j]):
                    longest = s[i:j]
                
    return longest


print(longestPalindrome('bababbcccccccccccd'))




#optimal solution

def longest_palindrome(s):
    if not s:
        return ''
    
    longest = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(longest):
            #update the res
            longest = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(longest):
            longest = tmp
    return longest



#helper function
def helper(s,l,r):
    while l >= 0 and  r < len(s) and s[l] == s[r]:
        l -= 1 #decrement the left
        r += 1 #increment the right

    return s[l+1:r]


print(longest_palindrome('bababbcccccccccccd'))