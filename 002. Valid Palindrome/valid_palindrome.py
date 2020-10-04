# O(1)
def is_valid_char(char: str):
    ascii_val = ord(char)
    return 65 <= ascii_val <= 90 # or (97 <= ascii_val <= 122) don't need to check for lower case


# O(n) time
# O(2n) -> O(n) space
def valid_palindrome(string: str) -> bool:
    clean = "" # O(n) space
    reverse = "" # O(n) space

    #preparing valid string with only characters and upper case characters
    for char in string: # O(n) time
        char = char.upper()
        if is_valid_char(char): # O(1)
            clean += char
            reverse = char + reverse

    return clean==reverse