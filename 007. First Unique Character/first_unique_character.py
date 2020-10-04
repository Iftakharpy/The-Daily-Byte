# O(n) time
# O(n+m) space 
# here n is the number of unique characters and m is the number of characters that only appears once
def first_unique_character(string: str) -> int:
    cache = {} # to keep track of seen characters
    first_seen = {} #to store indexes of unique charaters

    # O(n)
    for index,char in enumerate(string):
        if cache.get(char):
            # if the charater is seen previously then remove it from the first_seen map
            if first_seen.get(char) != None: 
                first_seen.pop(char)
        else:
            cache[char] = True
            first_seen[char] = index
    
    if first_seen:
        return first_seen[next(iter(first_seen))] # return first item in the first_seen map
    return -1


# def first_unique_character(string: str) -> str:
#     pos = len(string)
#     for i in range(ord('a'), ord('z') + 1):
#         if chr(i) in string and chr(i) not in string[string.index(chr(i)) + 1:]:
#             pos = min(pos, string.index(chr(i)))
#     return -1 if pos == len(string) else pos
