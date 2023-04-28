class Solution():
    def isPalindrome(self, x):
        
        if x < 0 or (x%10 == 0 and x != 0 ):
            return False 
        r = 0
        while(x > r) :
            r = r * 10 + x % 10 
            x //= 10 
        if(x == r or x == r//10):
            return True
        return False
        
