# O(n+m) time complexity
# O(n) space complexity
# here O(n) -> O(1) because
# we are storing 26 characters in the hash map. 
# "string and target which only consist of lowercase letters" - according to the problem statement
def spot_the_difference(string: str, target: str) -> str:
    lookup_table = {}
    # O(n)
    for ch in target:
        if lookup_table.get(ch):
            lookup_table[ch] += 1
        else:
            lookup_table[ch] = 1
    # O(m)
    for ch in string:
        lookup_table[ch] -= 1
        if lookup_table.get(ch) == 0:
            lookup_table.pop(ch)
    
    if lookup_table:
        return next(iter(lookup_table))
    return ""