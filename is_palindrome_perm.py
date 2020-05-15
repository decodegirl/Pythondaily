# QUESTION
#GIVEN A STRING WRITE A FUNCTION TO DETERMINE WHETHER IT IS A PERMUTATION OF A PALINDROME
# a palindrome is a word which is written the same forwards and backwards
#example 'madam' 'racecar' 'kayak' are palindromes
# a permutation is an arrangement of letters.'pot' and 'top'

#'ayakk'  KAYAK  M A D A M R A C E C A R
# hashtables

def is_palindrome_permutation(str):
    #delete whitespaces
    str = str.replace(' ','')
    #convert to lower case/similar cases
    str = str.lower()

    char_set = {}
    for i in str:
        if i in char_set:
            char_set[i] += 1
        else:
            char_set[i] = 1

    odd_counter = 0
    for k,v in char_set.items():
        if v % 2 != 0 and odd_counter == 0:
            odd_counter += 1

        elif v% 2 != 0 and odd_counter != 0:
            return False
    return True



print(is_palindrome_permutation('ayakkc'))









