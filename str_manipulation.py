'''this file is for functions on string manipulation'''


def remove_vowel(string_):
    '''this should remove vowel letters either in upper/lower type. but i need to need how to shrink the code more.
    i used the translate() function which allowed me replace each character in the string using the given translation table. i used the ord() function to get the unicode code point of the character and ‘None’ as a replacement to remove it from the result string. However here i used the iterator to do for multiple xter'''
    string_ = string_.translate({ord(i): None for i in 'AaEeIiOoUu'})
    return string_


def rem_vowel(_string):
    _vowel = ["a", "e", "i", "o", "u"]
    for i in _vowel:
        _string = _string.replace(i, "")
        return _string


def word_count(_string):
    '''i will be using the split() function to split
    the word... check the split() function, it is a
    string function'''
    _count = len(_string.split())
    return _count
