def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0, []


    max_sum = arr[0]
    current_sum = arr[0]


    start = 0
    end = 0
    temp_start = 0


    for i in range(1, len(arr)):

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i


    return max_sum, arr[start:end+1]
