from typing import List


# O(n)
def is_all_same(iterator: List[str]) -> bool:
    prev = iterator[0]
    for cur in range(1,len(iterator)):
        if prev == iterator[cur]:
            pass
        else:
            return False
    return True

# O(n*m)
def longest_common_prefix(array: List[str]) -> str:
    prefix = []
    for chars in zip(*array):
        if is_all_same(chars):
            prefix.append(chars[0])
        else:
            break
    return "".join(prefix)


# #answer from disscussion didn't understand how the min and max is working here
# # O(n)
# def longest_common_prefix(m):
#     if not m: return ''
#             #since list of string will be sorted and retrieved min max by alphebetic order
#     s1 = min(m)
#     s2 = max(m)

#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i] #stop until hit the split index
#     return s1