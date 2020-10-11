# O(n) assuming paring binary nums to int takes O(n) time
# and formatting int to binary number as string takes O(n) time
# O(n) space for storing converted binary number as string
def add_binary(binary_x: str, binary_y: str) -> str:
    x = int(binary_x,2)
    y = int(binary_y,2)
    return "{:b}".format(x+y) # no extra step needed
    # return bin(x+y)[2:] #extra step needed to return only binary num
