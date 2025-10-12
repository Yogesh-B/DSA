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
# arr = [1,5,3,8,4,6,55,22,15,45]  #1 5 3 8 4 6 55 22 15 45
arr = [int(x) for x in input("Enter array elements separated by space:").split()]
# x = 100
x = int(input("Enter target x:"))


########### naiv logic 1 start
# #main logic below
# arr_n = len(arr)
# smallest_sub_len = arr_n
# final_sum = None
# final_index = []
# for i in range(arr_n):
#     tmp_sum = 0
#     for j in range(i,arr_n):
#         tmp_sum += arr[j]
#         if(tmp_sum > x and j-i+1 <= smallest_sub_len):
#             smallest_sub_len = j-i+1
#             final_sum = tmp_sum
#             final_index = [i,j]
#             print(arr[i:j+1], tmp_sum)
# if final_sum is not None:
#     print(f"final answer: {smallest_sub_len}, sum: {final_sum}, sub_array:{arr[final_index[0]:final_index[1]+1]}")
# else:
#     print("Not found")
########### naiv logic 1 end


# sliding window o(n)
arr_sum = 0
final_sum = 0
arr_len = len(arr)
smallest_sub_len = arr_len+1
final_index = [0,0]
start_i = 0
end_i = 0
for end_i in range(arr_len):
    arr_sum += arr[end_i]
    print(f"{arr[start_i:end_i+1]}: {arr_sum}")

    if arr_sum > x:
        print(f"----> : {arr[start_i:end_i+1]}: {arr_sum}")
        tmp_len = end_i - start_i + 1
        smallest_sub_len = min(smallest_sub_len, tmp_len)
        while (arr_sum > x and start_i<end_i):
            arr_sum -= arr[start_i]
            start_i += 1
            if arr_sum > x:
                tmp_len = end_i - start_i + 1
                smallest_sub_len = min(smallest_sub_len,tmp_len)
                final_index = [start_i,end_i]
                final_sum = arr_sum
if smallest_sub_len > arr_len:
    print("Not found")
else: 
    print(f"Length: {smallest_sub_len}, Sum: {final_sum}, Sub Array: {arr[final_index[0]:final_index[1]+1]}")
