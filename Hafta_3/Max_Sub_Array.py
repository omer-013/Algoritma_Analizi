def max_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    best_subarray = []


    for i in range(n):
        for j in range(i, n):  
            current_sum = sum(arr[i:j+1]) 
            if current_sum > max_sum: 
                max_sum = current_sum
                best_subarray = arr[i:j+1] 

    return max_sum, best_subarray
