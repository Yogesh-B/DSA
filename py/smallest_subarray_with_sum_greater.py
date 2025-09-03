#Smallest subarray with sum greater than x
#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

#Examples:

#Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
#Output: 3
#Explanation: Minimum length subarray is [4, 45, 6]
#Input: x = 100, arr[] = [1, 10, 5, 2, 7]
#Output: 0
#Explanation: No subarray exist

##note: subarray means consecutive elements



#brute force method
#input array and target x
arr = [1,5,3,8,4,6,55,22,15,45]
x = 100
smallest_sub_len = 0
#main logic below
arr_n = len(arr)
for i in range(len(arr)):
    # we need two indices... one goes left, one goes right from the current index
    n = i
    m = i
    tmp_sum = 0
    tmp_arr = arr[n:m]
    while(n>0 or m < arr_n-1):
        if n>0:
            n-=1
            tmp_arr = arr[n:m+1]
            print(tmp_arr)
        if m<arr_n-1:
            m+=1
            tmp_arr = arr[n:m+1]
            print(tmp_arr)
        print(arr)
        #WIP

#idea 1 sort array nlog => then there could be a possibility for better comolexity
