from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    
    i,j = 0, len(s)-1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
