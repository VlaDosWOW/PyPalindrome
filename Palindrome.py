nums = [str(i*1) for i in range(1, 1000000)]
'''^
creating list with numbers 
from 1 to 1000000 (for test)
'''

#creating function for checking palindrome
def Palindrome(num):
    halfOfLenNum = len(num) // 2 # creating var for half of length
    if len(num) % 2 != 0: # if lenth of string is odd number
        firstHalfWithoudMid = num[:halfOfLenNum] 
        '''    ^
        slicing first half without middle symbol because
        we don't need it for palindrome checking
        '''
        secondHalfWithoudMid = num[halfOfLenNum+1:] 
        '''    ^
        slicing second half without middle symbol because
        we don't need it for palindrome checking
        '''
        reversed2ndHalf = secondHalfWithoudMid[::-1] # reversing 2nd half for comparison
        '''    ^
        reversing 2nd half for comparison with 1st
        '''
        return firstHalfWithoudMid == reversed2ndHalf
        '''    ^
        if they are same, it is palindrome and return is ending function
        '''
    firstHalf = num[:halfOfLenNum] # slicing second half
    secondHalf = num[halfOfLenNum:] # slicing second half
    reversed2ndHalf = secondHalf[::-1] 
    '''    ^
    reversing 2nd half for comparison with 1st
    '''
    return firstHalf == reversed2ndHalf 
    '''       ^
    if they are same, it is palindrome
    '''
list = []
# function that prints number if it is a palindrome
for num in nums:
    if Palindrome(str(num)):
        list.append(num)