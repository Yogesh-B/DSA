# https://www.geeksforgeeks.org/problems/three-way-partitioning/1?page=1
# Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.

# Note: The generated output is true if you modify the given array successfully. Otherwise false.

# Geeky Challenge: Solve this problem in O(n) time complexity.

# Examples:

# Input: arr[] = [1, 2, 3, 3, 4], a = 1, b = 2
# Output: true
# Explanation: One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be true.

# Input: arr[] = [1, 4, 3, 6, 2, 1], a = 1, b = 3
# Output: true
# Explanation: One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be true.

# Constraints:
# 1 <= arr.size()<= 106
# 1 <= array[i], a, b <= 109

def three_way_partitioning(arr, a, b):
    pass
    #here we need to write some good code.



def main():
    arr = list(map(int, input("Enter the array(numbers separated by space): ").split(" ")))
    a, b = map(int, input("Enter the range(a and b separated by space): ").split(" "))
    
    three_way_partitioning(arr, a, b)
    print(arr)


if __name__ == "__main__":
    main()