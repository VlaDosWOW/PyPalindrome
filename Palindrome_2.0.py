print("Hello. It's program that checks if some words or numbers are palindrome.\n\
Palindrome is a word, number, phrase, or other\n\
sequence of characters which reads the same backward as forward")
def Palindrome(STR):
    STR = STR.translate({ord(i): None for i in ',;.?-: '})
    STR = STR.lower()
    print(STR)
    halfOfLenSTR = len(STR) // 2 # creating var for half of length
    if len(STR) % 2 != 0: # if lenth of string is odd STRber
        firstHalfWithoudMid = STR[:halfOfLenSTR] 
        '''    ^
        slicing first half without middle symbol because
        we don't need it for palindrome checking
        '''
        secondHalfWithoudMid = STR[halfOfLenSTR+1:] 
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
    firstHalf = STR[:halfOfLenSTR] # slicing second half
    secondHalf = STR[halfOfLenSTR:] # slicing second half
    reversed2ndHalf = secondHalf[::-1] 
    '''    ^
    reversing 2nd half for comparison with 1st
    '''
    return firstHalf == reversed2ndHalf 
    '''    ^
    if they are same, it is palindrome
    '''

while True:
    answer = input('Print something: ')
    if Palindrome(answer):
        print("'" + answer + '\' is palindrome\n')
    else:
        print("'" + answer + '\' is not palindrome\n')