# O(n) time where len(S) is the time complixity
# O(n) space where len(J) is space complexity
def jewels_and_stones(J: str, S: str) -> int:
    cache = {dis:True for dis in J}
    total = 0
    for jw in S:
        if cache.get(jw):
            total+=1
    return total
