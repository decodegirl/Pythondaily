#ARRAYS AND STRINGS
#QUESTION 1
#Implement an algorithm to determine whether a string has all unique characters.

#What if you cannot use additional data structures?

#solution1 inbuilt python sets

def is_unique(str):
    #delete whitespaces
    str = str.replace(' ','')
    #convert to similar case
    str = str.lower()
    #check length of str
    if len(str) > 256:
        return False

    else:
        return len(str) == len(set(str))


#print(is_unique('celin is comiNg'))

#solution2 hashtables

def is_unique(str):
    #delete whitespaces
    str = str.replace(' ','')
    #convert to similar case
    str = str.lower()
    #check length of str
    if len(str) > 256:
        return False

    else:
        char_set = {}
        for i in str:
            if i in char_set:
                return False
            else:
                char_set[i] = True
        return True

#print(is_unique('celin'))

#solution3

def is_unique(str):
    #delete whitespaces
    str = str.replace(' ','')
    #convert to similar case
    str = str.lower()
    #check length of str
    if len(str) > 256:
        return False

    else:
        for i in range(len(str)):
            for j in range(i+1, len(str)):
                if str[i] == str[j]:
                    return False
        return True

print(is_unique('He Ran'))