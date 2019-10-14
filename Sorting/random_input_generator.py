''''''
'''-------------------------------------------------------------------------MERGE SORT---------------------------------------------------------------------------------------'''
def mergeSort(arr):

    if len(arr) == 1:
        return arr

    else:
        left_arr = arr[:int(len(arr)/2)]
        right_arr = arr[int(len(arr)/2):]

        returned_sorted_left_arr = mergeSort(left_arr)
        returned_sorted_right_arr = mergeSort(right_arr)

        return merge(returned_sorted_left_arr, returned_sorted_right_arr)

def merge(left_arr, right_arr):
    merged_arr = []

    while( len(left_arr)> 0 and len(right_arr) > 0):
        if left_arr[0] < right_arr[0]:
            merged_arr.append(left_arr.pop(0))
        else:
            merged_arr.append(right_arr.pop(0))

    while (len(left_arr)>0):
        merged_arr.append(left_arr.pop(0))

    while (len(right_arr)>0):
        merged_arr.append(right_arr.pop(0))

    return merged_arr


'''--------------------------------------------------------------------------Quick Sort------------------------------------------------------------------------------------'''
def partition(arr, start, end):
    left_border = (start - 1)

    #taking the last element as the pivot
    pivot = arr[end]

    for j in range(start, end):

        if arr[j] < pivot:
            left_border = left_border + 1
            arr[left_border], arr[j] = arr[j], arr[left_border]

    arr[left_border + 1], arr[end] = arr[end], arr[left_border + 1]
    return (left_border + 1)


def quickSort(arr):
    start = 0
    end = len(arr)-1
    #do in-place sorting of quick sort, we do not need any auc=xillary array
    helper_quicksort(arr,start,end)
    return arr




def helper_quicksort(arr, start, end):

    if start < end:
        partition_location = partition(arr, start, end)

        #recursively call helper_quicksort() in-place
        helper_quicksort(arr, start, partition_location - 1)
        helper_quicksort(arr, partition_location + 1, end)



import random, time, matplotlib.pyplot as plt

'''----------------------------------merge_sort_unsorted_input------------------------------'''
merge_sort_unsorted_input_times = []
for input_size in range (1,950,1):

    list = [random.randint(0,100000) for i in range(input_size)]
    start_time = time.time()
    mergeSort(list)
    time_taken_for_this_array = time.time() - start_time
    merge_sort_unsorted_input_times.append(time_taken_for_this_array)


plt.plot(merge_sort_unsorted_input_times)

# naming the x axis
plt.xlabel('Input Size')
# naming the y axis
plt.ylabel('Running Time')
# giving a title to my graph
plt.title('Merge Sort - Unsorted Input')
# function to show the plot
plt.show()

'''----------------------------------------------------------------------------------------------------'''
'''----------------------------------merge_sort_sorted_input------------------------------'''
# merge_sort_sorted_input_times = []
# for input_size in range (1,950,1):
#
#     list = [i for i in range(input_size)]
#     start_time = time.time()
#     mergeSort(list)
#     time_taken_for_this_array = time.time() - start_time
#     merge_sort_sorted_input_times.append(time_taken_for_this_array)
#
# plt.plot(merge_sort_sorted_input_times)
# # naming the x axis
# plt.xlabel('Input Size')
# # naming the y axis
# plt.ylabel('Running Time')
# # giving a title to my graph
# plt.title('Merge Sort- Sorted Input')
# # function to show the plot
# plt.show()

'''-----------------------------------------------------------------------------------------------------------------'''
'''----------------------------------quick_sort_unsorted_input------------------------------'''
# quick_sort_unsorted_input_times = []
# for input_size in range (1,5000,1):
#
#     list = [random.randint(0,100000) for i in range(input_size)]
#     start_time = time.time()
#     quickSort(list)
#     time_taken_for_this_array = time.time() - start_time
#     quick_sort_unsorted_input_times.append(time_taken_for_this_array)
#
# plt.plot(quick_sort_unsorted_input_times)
# # naming the x axis
# plt.xlabel('Input Size')
# # naming the y axis
# plt.ylabel('Running Time')
# # giving a title to my graph
# plt.title('Quick Sort- Unsorted Input')
# # function to show the plot
# plt.show()

'''-----------------------------------------------------------------------------------------------------'''
'''----------------------------------quick_sort_sorted_input------------------------------'''
# quick_sort_sorted_input_times = []
# for input_size in range (1,950,1):
#
#     list = [i for i in range(input_size)]
#     start_time = time.time()
#     quickSort(list)
#     time_taken_for_this_array = time.time() - start_time
#     quick_sort_sorted_input_times.append(time_taken_for_this_array)
#
# plt.plot(quick_sort_sorted_input_times)
# # naming the x axis
# plt.xlabel('Input Size')
# # naming the y axis
# plt.ylabel('Running Time')
# # giving a title to my graph
# plt.title('Quick Sort- Sorted Input')
# # function to show the plot
# plt.show()


