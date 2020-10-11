# O(n) time
# O(1) space
def correct_capitalization(string: str) -> bool:
    if string=="":
        return True
    first_char = 'upper' if string[0].isupper() else 'lower'
    upper_chars = 0
    lower_chars = 0
    for char in string:
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1

    #checking for all upper
    if upper_chars == len(string): 
        return True
    #checking for all lower
    elif lower_chars == len(string): 
        return True
    #checking for first char to be upper and others to be lower
    elif first_char == 'upper' and lower_chars == len(string)-1:
        return True
    else:
        return False
